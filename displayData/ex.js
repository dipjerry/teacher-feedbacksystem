var data_k = JSON.parse('{{Knowledge_G | safe}}');
var labels_k = JSON.parse('{{Knowledge_L | safe}}');
var data_CnC = JSON.parse('{{Clarity_communication_G | safe}}');
var labels_CnC = JSON.parse('{{Clarity_communication_L | safe}}');
var data_Hs = JSON.parse('{{helpStudent_G | safe}}');
var labels_Hs = JSON.parse('{{helpStudent_L | safe}}');
var data_p = JSON.parse('{{presentation_G | safe}}');
var labels_p = JSON.parse('{{presentation_L | safe}}');
var data_Co = JSON.parse('{{co_opeartive_G | safe}}');
var labels_Co = JSON.parse('{{co_opeartive_L | safe}}');
var data_No = JSON.parse('{{newOutlook_G | safe}}');
var labels_No = JSON.parse('{{newOutlook_L | safe}}');
var data_c = JSON.parse('{{checking_G | safe}}');
var labels_c = JSON.parse('{{checking_L | safe}}');
var data_s = JSON.parse('{{Seminar_G | safe}}');
var labels_s = JSON.parse('{{Seminar_L | safe}}');
var data_i = JSON.parse('{{interaction_G | safe}}');
var labels_i = JSON.parse('{{interaction_L | safe}}');
var data_e = JSON.parse('{{effectiveness_G | safe}}');
var labels_e = JSON.parse('{{effectiveness_L | safe}}');
var data_Mi = JSON.parse('{{motivatesInterest_G | safe}}');
var labels_Mi = JSON.parse('{{motivatesInterest_L | safe}}');




var ctx2 = document.getElementById('myK').getContext('2d');
var myChart = new Chart(ctx2, {
    type: 'horizontalBar',
    data: {
        labels: labels_k,
        datasets: [{
            label: '% of Feedback',
            data: data_k,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for knowledge ends
//graph for clarity and communication start
var ctx3 = document.getElementById('myCnC').getContext('2d');
var myChart = new Chart(ctx3, {
    type: 'horizontalBar',
    data: {
        labels: labels_CnC,
        datasets: [{
            label: '% of Feedback',
            data: data_CnC,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for clarity and communication ends
//graph for helping student start
var ctx4 = document.getElementById('myHs').getContext('2d');
var myChart = new Chart(ctx4, {
    type: 'horizontalBar',
    data: {
        labels: labels_Hs,
        datasets: [{
            label: '% of Feedback',
            data: data_Hs,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for helping student ends
//graph for presentation starts 
var ctx5 = document.getElementById('myP').getContext('2d');
var myChart = new Chart(ctx5, {
    type: 'horizontalBar',
    data: {
        labels: labels_p,
        datasets: [{
            label: '% of Feedback',
            data: data_p,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for presentation ends
//graph for Motivate interest start
var ctx6 = document.getElementById('myMi').getContext('2d');
var myChart = new Chart(ctx6, {
    type: 'horizontalBar',
    data: {
        labels: labels_Mi,
        datasets: [{
            label: '% of Feedback',
            data: data_Mi,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for Motivate interest ends
var ctx7 = document.getElementById('myCo').getContext('2d');
var myChart = new Chart(ctx7, {
    type: 'horizontalBar',
    data: {
        labels: labels_Co,
        datasets: [{
            label: '% of Feedback',
            data: data_Co,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for co Operative ends
//graph for New outlook start
var ctx8 = document.getElementById('myNo').getContext('2d');
var myChart = new Chart(ctx8, {
    type: 'horizontalBar',
    data: {
        labels: labels_No,
        datasets: [{
            label: '% of Feedback',
            data: data_No,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for New outlook ends
//graph for checking starts
var ctx9 = document.getElementById('myC').getContext('2d');
var myChart = new Chart(ctx9, {
    type: 'horizontalBar',
    data: {
        labels: labels_c,
        datasets: [{
            label: '% of Feedback',
            data: data_c,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for checking ends
//graph for seminar start
var ctx10 = document.getElementById('myS').getContext('2d');
var myChart = new Chart(ctx10, {
    type: 'horizontalBar',
    data: {
        labels: labels_s,
        datasets: [{
            label: '% of Feedback',
            data: data_s,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting

});
//graph for seminar ends
//graph for Interection starts
var ctx11 = document.getElementById('myI').getContext('2d');
var myChart = new Chart(ctx11, {
    type: 'horizontalBar',
    data: {
        labels: labels_i,
        datasets: [{
            label: '% of Feedback',
            data: data_i,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for Interection ends
//graph for Interection starts
var ctx12 = document.getElementById('myE').getContext('2d');
var myChart = new Chart(ctx12, {
    type: 'horizontalBar',
    data: {
        labels: labels_e,
        datasets: [{
            label: '% of Feedback',
            data: data_e,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: ['rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: setting
}); //graph for Interection ends