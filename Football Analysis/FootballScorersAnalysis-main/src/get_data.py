import json
import re
from pprint import pprint
from functools import reduce
from typing import Tuple

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet

p_url = re.compile(r'href=\S+')
p_wiki = re.compile(r'/wiki/\S+')
p_national = re.compile(r' national')
p_digit = re.compile(r'\d+')
p_year = re.compile(r'\d{4}')
p_goals = re.compile(r'\d+\sgoals?')
p_assist = re.compile(r'\d+\sassists?')
p_parenthesis = re.compile(r'\(.+\)')
p_height_m = re.compile(r'\d\.\d*.*m')
p_height_cm = re.compile(r'\d*\s?cm')
p_height = re.compile(r'\d\.\d*')
p_birth_date_headline = re.compile(r'Date of birth|Born')
p_national_team = re.compile(r'.?National team.?')
p_date_range = re.compile(r'\d{4}.*')
p_scoring = re.compile(r'Scoring.*')


def get_soup(url: str) -> BeautifulSoup:
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html5lib')


def get_goals_num(soup: BeautifulSoup, achievement_type: str) -> {}:
    """
    :param soup: wiki page soup with a given competition statistics
    :param achievement_type: 'goals' or 'assists'
    :return: dictionary with the goals/assists numbers as keys and lists of html players elements
    """
    pattern = ''
    if achievement_type == 'goals':
        pattern = p_goals
    elif achievement_type == 'assists':
        pattern = p_assist

    goals = {}
    # main_headline = soup.find(text=score_type)
    # print(main_headline)
    # headlines = main_headline.find_all_next(text=pattern)

    # elem_after_lists = soup.find('span',attrs={"class":"toctext"},text='Scoring')
    # headlines = elem_after_lists.find_all_previous(text=pattern)
    # print(elem_after_lists)

    headlines = soup.find_all('b', text=pattern)
    print(headlines)
    if not len(headlines):
        headlines = soup.find_all('dt', text=pattern)
        print(headlines)
    headlines = get_valid_headlines(headlines)
    print(headlines)
    for h in set(headlines):
        next_elem = h.findNext('ul').findAll('li')
        goals[int(p_digit.search(h.text).group())] = next_elem
    return goals


def get_valid_headlines(l: [BeautifulSoup]):
    previous_num = p_digit.search(l[0].text).group()
    correct = 1
    for elem in l[1:]:
        current_num = p_digit.search(elem.text).group()
        if previous_num > current_num:
            correct += 1
        previous_num = current_num
    return l[:correct]


def extract_dict_data(goals_dictionary: {}) -> {}:
    url_dictiionary = {}
    for num, soup_elem in goals_dictionary.items():
        players = [player.find_all('a', href=True) for player in soup_elem]
        players_hrefs = [[href['href'] for href in player] for player in players]
        url_dictiionary[num] = [list(map(get_pure_url, player_urls)) for player_urls in players_hrefs]
    return url_dictiionary


def get_name(soup: BeautifulSoup) -> str:
    name = soup.find('caption', attrs={'class': 'fn'})
    if name is None:
        name = soup.find('h1')
    for s in name.find_all('style'):
        s.decompose()
    for s in name.find_all('span'):
        s.decompose()
    return ''.join([ch for ch in name.text if ch.isalpha() or ch == ' '])


def get_age(soup: BeautifulSoup, tournament_year: int) -> int:
    age_row = soup.find('th', text=p_birth_date_headline)
    birth_date = age_row.find_next_sibling('td').text
    return tournament_year - int(p_year.search(birth_date).group())


def get_height(soup: BeautifulSoup) -> float:
    height_row = soup.find('th', text='Height')
    if not height_row:
        return 0
    height = height_row.find_next_sibling('td').text
    h_meters = p_height_m.search(height)
    if h_meters:
        height_str = h_meters.group()
        height_meters = p_height.search(height_str).group()
        return float(height_meters)
    else:
        h_cm = p_height_cm.search(height)
        height_str = h_cm.group()
        height_cm = p_digit.search(height_str).group()
        return float(height_cm) / 100


def get_team_league(soup: BeautifulSoup, year: int) -> (str, str):
    team, team_url = get_team(soup, year)
    league, country = 'No club', 'Unknow'
    if team_url != '-':
        r = requests.get(team_url)
        soup_league = BeautifulSoup(r.content, 'html5lib')
        league, league_url = get_league(soup_league)
        country = get_league_country(league_url)
    return team, f'{league} ({country})'


def get_league_country(league_url: str) -> str:
    try:
        r = requests.get(league_url)
        soup = BeautifulSoup(r.content, 'html5lib')
        country_row = soup.find('th', text='Country')
        country = country_row.find_next_sibling('td').text
        country = p_parenthesis.sub('', country)
        return country.strip()
    except:
        return 'Unknown'


def check_dates(dates_range_str: str, year: int) -> bool:
    last_date = dates_range_str.replace('0000', '').strip()
    if (not last_date[-1].isdigit()) and int(p_digit.search(last_date).group()) < year:
        return True
    dates = re.split(r'\D', dates_range_str)
    if len(dates) == 1 and int(dates[0]) == year:
        return True
    if len(dates) == 2 and int(dates[0]) < year <= int(dates[1]):
        return True
    return False


def check_dates_kuba(year_range: str, year: int) -> bool:
    int_range = [int(x) if x else 9999 for x in re.split(r'\D', year_range)]
    int_range = [x if x != 0 else 9999 for x in int_range]
    int_range = int_range * 2 if len(int_range) == 1 else int_range
    return int_range[0] <= year <= int_range[1]


def cut_initial_chars(name: str) -> str:
    if name.strip() == '':
        return ''
    i = -1
    valid_start = False
    while not valid_start:
        i += 1
        valid_start = name[i].isalnum()
    return name[i:]


def get_team(soup: BeautifulSoup, tournament_year: int) -> (str, str):
    team, team_url = 'No club', '-'
    elems = soup.find_all('th')
    elem_after_teams = [elem for elem in elems if elem and p_national_team.search(elem.text)]
    th_elems = elem_after_teams[0].find_all_previous('th')
    for th in th_elems:
        date_range = th.text.strip()
        if p_date_range.search(date_range) and check_dates(date_range, tournament_year):
            team_elem = th.find_next_sibling('td').find('a')
            team = cut_initial_chars(p_parenthesis.sub('', team_elem['title'])).strip()
            team_url = get_pure_url(team_elem['href'])
            return team, team_url
    return team, team_url


def get_league(soup: BeautifulSoup) -> (str, str):
    league, league_url = 'No club', '-'
    try:
        league_headline = soup.find('table', attrs={'class': 'infobox vcard'}).find('th', text='League')
        league = league_headline.find_next_sibling('td')
        league_url = get_pure_url(league.find('a', href=True)['href'])
        return league.text.strip(), league_url
    except Exception as e:
        print('EXCEPT', e)
        return league.strip(), league_url


def get_nation(soup: BeautifulSoup) -> str:
    nation = soup.find('h1', attrs={'id': 'firstHeading'}).text
    span = p_national.search(nation)
    if span:
        span = span.span()
        return nation[:span[0]]
    return nation.strip()


def get_player_data(url_nation: str, url_player: str, tournament_year: int) -> {}:
    r_nation = requests.get(url_nation)
    soup_nation = BeautifulSoup(r_nation.content, 'html5lib')
    r_player = requests.get(url_player)
    soup_player = BeautifulSoup(r_player.content, 'html5lib')
    soup_player_table = soup_player.find('table', attrs={'class': 'infobox vcard'})
    # soup_player_table = soup_player.find('table')
    name = get_name(soup_player)
    age = get_age(soup_player, tournament_year)
    height = get_height(soup_player)
    team, league = get_team_league(soup_player_table, tournament_year)
    nation = get_nation(soup_nation)
    player_data = {'name': name, 'age': age, 'height': height, 'club': team, 'league': league, 'country': nation}
    return player_data


def get_pure_url(url: str) -> str:
    html_base = 'https://en.wikipedia.org'
    main = p_wiki.search(url).group()
    if main[-1] == '"':
        main = main[:-1]
    return html_base + main


def get_goal_scorers(goals_dictionary, tournament_year: int) -> {int: [{}]}:
    players_data = []
    for goals_num, players in goals_dictionary.items():
        for player in players:
            print(player)
            nation_url = player[0]
            player_url = player[1]
            player_dict = get_player_data(nation_url, player_url, tournament_year)
            player_dict['goals'] = goals_num
            print(player_dict)
            players_data.append(player_dict)
    players_data = sorted(players_data, key=lambda x: x['goals'], reverse=True)
    return players_data


def get_assistants(assists_dictionary, tournament_year: int) -> ({str: {str}}):
    assistants_data = []
    for assists_num, assistants in assists_dictionary:
        for assistant in assistants:
            nation_url = assistant[0]
            assistant_url = assistant[1]
            assistant_dict = get_player_data(nation_url, assistant_url, tournament_year)
            assistant_dict['assists'] = assists_num
            print(assistant_dict)
            assistants_data.append(assistant_dict)
    return assistants_data


def save_json(filename: str, players_dictionary: {}):
    with open(filename, 'w') as players_file:
        data = json.dumps(players_dictionary)
        players_file.write('playerData = ')
        players_file.write(data)


def get_senior_career_trs(soup: BeautifulSoup) -> ResultSet:
    trs = soup.findAll('tr')
    take_after = lambda acc, elem: (acc[0] + [elem], True) if acc[1] else (
        acc[0], "Years" in elem.text and "Team" in elem.text)
    (head_removed, temp) = reduce(take_after, trs, ([], False))
    take_while = lambda acc, elem: (acc[0] + [elem], True) if "National team" not in elem.text and acc[1] else (
        acc[0], False)
    (tail_removed, temp) = reduce(take_while, head_removed, ([], True))
    return tail_removed


def get_team_kuba(soup: BeautifulSoup, tournament_year: int) -> Tuple[str, str]:
    result = [(x[0], x[1], x[3]) for x in map(parse_player_tr, get_senior_career_trs(soup)) if
              check_dates_kuba(x[2], tournament_year)]
    if len(result) > 1:
        result = [x for x in result if x[2]]
    if len(result) == 0: return '', ''
    team, url, on_loan = result[0]
    return team, get_pure_url(url)


def parse_player_tr(tr: BeautifulSoup):
    print(tr)
    return tr.find('a')['title'], tr.find('a')['href'], tr.find('th').text, '(loan)' in tr.text


if __name__ == '__main__':
    stats_url = 'https://en.wikipedia.org/wiki/UEFA_Euro_2020_statistics'
    # stats_url = 'https://en.wikipedia.org/wiki/2006_FIFA_World_Cup_statistics'
    # stats_url = 'https://en.wikipedia.org/wiki/UEFA_Euro_2012_statistics'
    # stats_url = 'https://en.wikipedia.org/wiki/2021_Copa_Am%C3%A9rica_statistics'
    # stats_url = 'https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_statistics'

    soup = get_soup(stats_url)

    d = get_goals_num(soup, 'goals')
    goals_dict = extract_dict_data(d)
    goal_scorers = get_goal_scorers(goals_dict, 2021)
    save_json('../js/data_2021.js', goal_scorers)

    # d_a = get_goals_num(soup, 'assists')
    # goals_dict = extract_dict_data(d_a)
    # goal_scorers = get_goal_scorers(goals_dict, 2021)
    # save_json('../js/data_assists_2021.js', goal_scorers)

    # TODO
    # - posortowac dane w kolkach
    # - dopasowac do serie a i innych lig
    # - dodac pozycje
    # - dodac wysokosc i grubosc
    # - make 'Euro 2020 statistics' page header looking nicer
    # - add unicode flag
    # - fix colors in 'on-goal-scorers'
    # - add menu at the top of the page
