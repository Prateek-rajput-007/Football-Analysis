import get_data
import requests
from bs4 import BeautifulSoup


def check_player_data():
    # EURO 2020 GOALS
    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Hungary_national_football_team',
                                 'https://en.wikipedia.org/wiki/Attila_Fiola', 2021)
    assert p == {'name': 'Attila Fiola', 'age': 31, 'height': 1.82, 'club': 'Fehérvár FC', 'league': 'NB I (Hungary)',
                 'country': 'Hungary'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Croatia_national_football_team',
                                 'https://en.wikipedia.org/wiki/Mario_Pa%C5%A1ali%C4%87', 2021)
    assert p == {'name': 'Mario Pašalić', 'age': 26, 'height': 1.89, 'club': 'Atalanta B.C.',
                 'league': 'Serie A (Italy)', 'country': 'Croatia'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Spain_national_football_team',
                                 'https://en.wikipedia.org/wiki/Ferran_Torres', 2021)
    assert p == {'name': 'Ferran Torres', 'age': 21, 'height': 1.84, 'club': 'Manchester City F.C.',
                 'league': 'Premier League (England)', 'country': 'Spain'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Croatia_national_football_team',
                                 'https://en.wikipedia.org/wiki/Ivan_Peri%C5%A1i%C4%87', 2021)
    assert p == {'name': 'Ivan Perišić', 'age': 32, 'height': 1.86, 'club': 'Inter Milan', 'league': 'Serie A (Italy)',
                 'country': 'Croatia'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Denmark_national_football_team',
                                 'https://en.wikipedia.org/wiki/Joakim_M%C3%A6hle', 2021)
    assert p == {'name': 'Joakim Mæhle', 'age': 24, 'height': 1.86, 'club': 'K.R.C. Genk',
                 'league': 'Belgian First Division A (Belgium)', 'country': 'Denmark'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Federico_Chiesa', 2021)
    assert p == {'name': 'Federico Chiesa', 'age': 24, 'height': 1.75, 'club': 'Juventus F.C.',
                 'league': 'Serie A (Italy)', 'country': 'Italy'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Ciro_Immobile', 2021)
    assert p == {'name': 'Ciro Immobile', 'age': 31, 'height': 1.85, 'club': 'S.S. Lazio', 'league': 'Serie A (Italy)',
                 'country': 'Italy'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Lorenzo_Insigne', 2021)
    assert p == {'name': 'Lorenzo Insigne', 'age': 30, 'height': 1.63, 'club': 'S.S.C. Napoli',
                 'league': 'Serie A (Italy)', 'country': 'Italy'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Manuel_Locatelli', 2021)
    assert p == {'name': 'Manuel Locatelli', 'age': 23, 'height': 1.86, 'club': 'U.S. Sassuolo Calcio',
                 'league': 'Serie A (Italy)', 'country': 'Italy'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Austria_national_football_team',
                                 'https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87', 2021)
    assert p == {'name': 'Marko Arnautović', 'age': 32, 'height': 1.92, 'club': 'Shanghai Port F.C.',
                 'league': 'Chinese Super League (China)', 'country': 'Austria'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Nicol%C3%B2_Barella', 2021)
    assert p == {'name': 'Nicolò Barella', 'age': 24, 'height': 1.72, 'club': 'Inter Milan',
                 'league': 'Serie A (Italy)', 'country': 'Italy'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Leonardo_Bonucci', 2021)
    assert p == {'name': 'Leonardo Bonucci', 'age': 34, 'height': 1.9, 'club': 'Juventus F.C.',
                 'league': 'Serie A (Italy)', 'country': 'Italy'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Switzerland_national_football_team',
                                 'https://en.wikipedia.org/wiki/Breel_Embolo', 2021)
    assert p == {'name': 'Breel Embolo', 'age': 24, 'height': 1.84, 'club': 'Borussia Mönchengladbach',
                 'league': 'Bundesliga (Germany)', 'country': 'Switzerland'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Belgium_national_football_team',
                                 'https://en.wikipedia.org/wiki/Romelu_Lukaku', 2021)
    assert p == {'name': 'Romelu Lukaku', 'age': 28, 'height': 1.9, 'club': 'Inter Milan', 'league': 'Serie A (Italy)',
                 'country': 'Belgium'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Switzerland_national_football_team',
                                 'https://en.wikipedia.org/wiki/Xherdan_Shaqiri', 2021)
    assert p == {'name': 'Xherdan Shaqiri', 'age': 30, 'height': 1.69, 'club': 'Liverpool F.C.',
                 'league': 'Premier League (England)', 'country': 'Switzerland'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Denmark_national_football_team',
                                 'https://en.wikipedia.org/wiki/Kasper_Dolberg', 2021)
    assert p == {'name': 'Kasper Dolberg', 'age': 24, 'height': 1.87, 'club': 'OGC Nice', 'league': 'Ligue 1 (France)',
                 'country': 'Denmark'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/North_Macedonia_national_football_team',
                                 'https://en.wikipedia.org/wiki/Goran_Pandev', 2021)
    assert p == {'name': 'Goran Pandev', 'age': 38, 'height': 1.84, 'club': 'Genoa C.F.C.', 'league': 'Serie A (Italy)',
                 'country': 'North Macedonia'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Belgium_national_football_team',
                                 'https://en.wikipedia.org/wiki/Thomas_Meunier', 2021)
    assert p == {'name': 'Thomas Meunier', 'age': 30, 'height': 1.91, 'club': 'Borussia Dortmund',
                 'league': 'Bundesliga (Germany)', 'country': 'Belgium'}

    p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy_national_football_team',
                                 'https://en.wikipedia.org/wiki/Matteo_Pessina', 2021)
    assert p == {'name': 'Matteo Pessina', 'age': 24, 'height': 1.87, 'club': 'Atalanta B.C.',
                 'league': 'Serie A (Italy)', 'country': 'Italy'}

    # # WORLD CUP 2006
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Ghana', 'https://en.wikipedia.org/wiki/Asamoah_Gyan',
    #                              2006)
    # assert p == {'name': 'Asamoah Gyan', 'age': 21, 'height': 1.86, 'club': 'Modena F.C.',
    #              'league': 'Serie C Group B (Italy)', 'country': 'Ghana', 'goals': 1}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy', 'https://en.wikipedia.org/wiki/Luca_Toni', 2006)
    # assert p == {'name': 'Luca Toni', 'age': 29, 'height': 1.93, 'club': 'ACF Fiorentina', 'league': 'Serie A (Italy)',
    #              'country': 'Italy', 'goals': 2}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Costa_Rica',
    #                              'https://en.wikipedia.org/wiki/R%C3%B3nald_G%C3%B3mez', 2006)
    # assert p == {'name': 'Rónald Gómez', 'age': 31, 'height': 1.88, 'club': 'Deportivo Saprissa',
    #              'league': 'Liga FPD (Costa Rica)', 'country': 'Costa Rica', 'goals': 1}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Croatia', 'https://en.wikipedia.org/wiki/Darijo_Srna',
    #                              2006)
    # assert p == {'name': 'Darijo Srna', 'age': 24, 'height': 1.81, 'club': 'FC Shakhtar Donetsk',
    #              'league': 'Ukrainian Premier League (Ukraine)', 'country': 'Croatia', 'goals': 1}
    #
    # # p = get_data.get_player_data('https://en.wikipedia.org/wiki/England', 'https://en.wikipedia.org/wiki/David_Beckham', 2006)
    # # assert p == {'name': 'Association football career', 'age': 31, 'height': 1.8, 'club': 'Real Madrid CF', 'league': 'La Liga (Spain)', 'country': 'England', 'goals': 1}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Iran',
    #                              'https://en.wikipedia.org/wiki/Sohrab_Bakhtiarizadeh', 2006)
    # assert p == {'name': 'Sohrab Bakhtiarizadeh', 'age': 33, 'height': 1.85, 'club': 'Saba Battery Club',
    #              'league': 'No club (Unknown)', 'country': 'Iran', 'goals': 1}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy',
    #                              'https://en.wikipedia.org/wiki/Alessandro_Del_Piero', 2006)
    # assert p == {'name': 'Alessandro Del Piero', 'age': 32, 'height': 1.74, 'club': 'Juventus F.C.',
    #              'league': 'Serie A (Italy)', 'country': 'Italy', 'goals': 1}
    #
    # # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Italy', 'https://en.wikipedia.org/wiki/Fabio_Grosso', 2006)
    # # assert p == {'name': 'Fabio Grosso', 'age': 29, 'height': 1.9, 'club': 'U.S. Città di Palermo', 'league': 'Serie C Group C (Italy)', 'country': 'Italy', 'goals': 1}
    #
    # # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Ukraine', 'https://en.wikipedia.org/wiki/Andriy_Shevchenko', 2006)
    # # assert p == {'name': 'Association football career', 'age': 30, 'height': 1.83, 'club': 'A.C. Milan', 'league': 'Serie A (Italy)', 'country': 'Ukraine', 'goals': 2}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Australia', 'https://en.wikipedia.org/wiki/Craig_Moore',
    #                              2006)
    # assert p == {'name': 'Craig Moore', 'age': 31, 'height': 1.85, 'club': 'Newcastle United F.C.',
    #              'league': 'Premier League (England)', 'country': 'Australia', 'goals': 1}
    #
    # p = get_data.get_player_data('https://en.wikipedia.org/wiki/Spain', 'https://en.wikipedia.org/wiki/Fernando_Torres',
    #                              2006)
    # assert p == {'name': 'Fernando Torres', 'age': 22, 'height': 1.86, 'club': 'Atlético Madrid',
    #              'league': 'La Liga (Spain)', 'country': 'Spain', 'goals': 3}


def test_player_dictionaty():
    check_player_data()


def create_soup(url):
    r_player = requests.get(url)
    soup_player = BeautifulSoup(r_player.content, 'html5lib')
    return soup_player.find('table', attrs={'class': 'infobox vcard'})


def test_gavranovic_get_senior_career_trs():
    soup_player_table = create_soup('https://en.wikipedia.org/wiki/Mario_Gavranovi%C4%87')

    result = get_data.get_senior_career_trs(soup_player_table)

    assert len(result) == 9
    assert 'Lugano' in result[0].text
    assert '2006' in result[0].text
    assert '2008' in result[0].text
    assert '21' in result[0].text
    assert 'Schalke' in result[3].text
    assert 'Dinamo Zagreb' in result[8].text


def test_harry_kane_get_senior_career_trs():
    soup_player_table = create_soup('https://en.wikipedia.org/wiki/Harry_Kane')

    result = get_data.get_senior_career_trs(soup_player_table)

    assert len(result) == 5
    assert 'Tottenham' in result[0].text
    assert '2009' in result[0].text
    assert '242' in result[0].text
    assert 'Millwall' in result[2].text
    assert 'Leicester' in result[4].text


def test_get_team_kuba():
    helper_get_team_test(get_data.get_team_kuba)


def test_get_team_kaja():
    helper_get_team_test(get_data.get_team)


def helper_get_team_test(get_team_function):
    soup = create_soup('https://en.wikipedia.org/wiki/Harry_Kane')
    team, url = get_team_function(soup, 2020)
    assert url == 'https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C.'
    assert team == 'Tottenham Hotspur F.C.'

    team, url = get_team_function(soup, 2011)
    assert url == 'https://en.wikipedia.org/wiki/Leyton_Orient_F.C.'
    assert team == 'Leyton Orient F.C.'

    team, url = get_team_function(soup, 2012)
    assert url == 'https://en.wikipedia.org/wiki/Millwall_F.C.'
    assert team == 'Millwall F.C.'

    team, url = get_team_function(soup, 2013)
    assert url == 'https://en.wikipedia.org/wiki/Leicester_City_F.C.'
    assert team == 'Leicester City F.C.'

    soup = create_soup('https://en.wikipedia.org/wiki/%C3%81lvaro_Morata')
    team, url = get_team_function(soup, 2020)
    assert url == 'https://en.wikipedia.org/wiki/Atl%C3%A9tico_Madrid'
    assert team == 'Atlético Madrid'

    team, url = get_team_function(soup, 2021)
    assert url == 'https://en.wikipedia.org/wiki/Juventus_F.C.'
    assert team == 'Juventus F.C.'

    soup = create_soup('https://en.wikipedia.org/wiki/Federico_Chiesa')
    team, url = get_team_function(soup, 2021)
    assert url == 'https://en.wikipedia.org/wiki/Juventus_F.C.'
    assert team == 'Juventus F.C.'

    soup = create_soup('https://en.wikipedia.org/wiki/Mario_Gavranovi%C4%87')
    team, url = get_team_function(soup, 2021)
    assert url == 'https://en.wikipedia.org/wiki/GNK_Dinamo_Zagreb'
    assert team == 'GNK Dinamo Zagreb'

    soup = create_soup('https://en.wikipedia.org/wiki/Goran_Pandev')
    team, url = get_team_function(soup, 2021)
    assert url == 'https://en.wikipedia.org/wiki/Genoa_C.F.C.'
    assert team == 'Genoa C.F.C.'

    team, url = get_team_function(soup, 2022)
    assert url == '-'
    assert team == 'No club'

    soup = create_soup('https://en.wikipedia.org/wiki/Martin_Braithwaite')
    team, url = get_team_function(soup, 2021)
    assert url == 'https://en.wikipedia.org/wiki/FC_Barcelona'
    assert team == 'FC Barcelona'

    soup = create_soup('https://en.wikipedia.org/wiki/Kak%C3%A1')
    team, url = get_team_function(soup, 2006)
    assert url == 'https://en.wikipedia.org/wiki/A.C._Milan'
    assert team == 'A.C. Milan'

    soup = create_soup('https://en.wikipedia.org/wiki/Sohrab_Bakhtiarizadeh')
    team, url = get_team_function(soup, 2006)
    assert url == 'https://en.wikipedia.org/wiki/Saba_Battery_Club'
    assert team == 'Saba Battery Club'
