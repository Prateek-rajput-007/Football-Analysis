function switch_to(type) {
    Object.keys(all_charts).forEach(id => {
        all_charts[id].destroy();
        all_charts[id] = new Chart(
            document.getElementById(id).getContext("2d"),
            createChart(id, labels[id], datas[id], type)
        );
    });
}

function modify_one_goal(checkbox, title) {
    all_charts[title].data.labels = checkbox.checked ?
        one_goal_labels : no_one_goal_labels;
    all_charts[title].data.datasets[0].data = checkbox.checked ?
        one_goal_datas : no_one_goal_datas;
    labels[title] = all_charts[title].data.labels;
    datas[title] = all_charts[title].data.datasets[0].data;
    all_charts[title].update();
}

function createChart(title, labels, datas, type) {
    let step = 360 / datas.length;
    let colorsHue = datas.map((elem, index) => `hsla(${index * step}, 100%, 50%, 0.25`);
    return {
        type: type,
        data: {
            labels: labels,
            datasets: [{
                data: datas,
                backgroundColor: colorsHue
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: type == "bar" ? false : true,
                    position: "bottom",
                    maxHeight: 200
                },
                title: {
                    display: true,
                    text: title,
                    font: {
                        size: 20
                    }
                }
            }
        }
    };
}

function appendCanvas(title, labels, datas, type = "bar") {
    let canvas = document.createElement('canvas');
    canvas.width = "1500";
    canvas.height = "600";
    canvas.id = title;
    document.getElementById('container').appendChild(canvas);
    let chart = new Chart(canvas, createChart(title, labels, datas, type));
    all_charts[title] = chart;
}

function fill_init(title, label_fill, data_fill) {
    labels[title] = label_fill;
    datas[title] = data_fill;
    appendCanvas(title, labels[title], datas[title]);
}

function start(dataToDraw, score) {
    current_data = dataToDraw.filter(({ goals }) => goals > 1);
    no_one_goal_labels = current_data.map(({ name }) => name);
    no_one_goal_datas = current_data.map(({ goals }) => goals);
    one_goal_labels = dataToDraw.map(({ name }) => name);
    one_goal_datas = dataToDraw.map(({ goals }) => goals);

    all_goals = dataToDraw.reduce((acc, { goals }) => acc + goals, 0);
    document.getElementById("all_goals").innerHTML += all_goals;

    fill_init(score, no_one_goal_labels, no_one_goal_datas);

    current_data = dataToDraw.reduce(
        (acc, { country, goals }) => {
            acc[country] = (acc[country] || 0) + goals;
            return acc;
        }, {}
    );
    fill_init(score + " by country", Object.keys(current_data), Object.values(current_data));

    current_data = dataToDraw.reduce(
        (acc, { club, goals }) => {
            acc[club] = (acc[club] || 0) + goals;
            return acc;
        }, {}
    );
    fill_init(score + " by club", Object.keys(current_data), Object.values(current_data));

    current_data = dataToDraw.reduce(
        (acc, { league, goals }) => {
            acc[league] = (acc[league] || 0) + goals;
            return acc;
        }, {}
    );
    fill_init(score + " by league", Object.keys(current_data), Object.values(current_data));

    current_data = playerData.reduce(
        (acc, { age, goals }) => {
            let step = Math.floor(age / 5);
            let min = step * 5;
            let max = (step + 1) * 5 - 1;
            let key = `${min} - ${max}`;
            acc[key] = (acc[key] || 0) + goals;
            return acc;
        }, {}
    );

    current_data = Object.entries(current_data).sort();
    fill_init(score + " by age", current_data.map(([k, v]) => k), current_data.map(([k, v]) => v));

    current_data = playerData.filter(({ height }) => height != 0);
    current_data = current_data.reduce(
        (acc, { height, goals }) => {
            let step = Math.floor(height * 100 / 5);
            let min = step * 5;
            let max = (step + 1) * 5 - 1;
            let key = `${min} - ${max}`;
            acc[key] = (acc[key] || 0) + goals;
            return acc;
        }, {}
    );

    current_data = Object.entries(current_data).sort();
    fill_init(score + " by height (in cm)", current_data.map(([k, v]) => k), current_data.map(([k, v]) => v));
}

let all_goals;
let all_charts = {};
let labels = {};
let datas = {};

let current_data = [];
let no_one_goal_labels = [];
let no_one_goal_datas = [];
let one_goal_labels = [];
let one_goal_datas = [];


window.onload = function () {
    document.getElementById("bar_radio").checked = true;
    document.getElementById("pie_radio").checked = false;
    document.getElementById("one_goal").checked = false;
}
