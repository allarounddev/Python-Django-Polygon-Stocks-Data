ask_quotes0 = {}

function executeQuery() {
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/get_contents/',
        success: function (data) {
            // do something with the return value here if you like

            south_africa_time = new Date().toLocaleString("en-GB", { timeZone: `Africa/Ceuta` }).split(',')[1];

            data = JSON.parse(data);
            console.log(data.ask_quotes0);
            console.log(data.ask_quotes1);
            console.log(data.ask_quotes2);

            // TSLA
            if (JSON.stringify(data.quotes0) != "{}") {
                $("#quotes_tbody0").empty();
                quotes0 = data.quotes0;
                quotes0 = JSON.parse(quotes0);
                for (var key in quotes0) {
                    console.log(key);
                    console.log(Object.values(quotes0[key]));
                    $("#quotes0 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes0[key])[0] + '</td><td>' + Object.values(quotes0[key])[1] + '</td></tr>');
    
                }
            }
            if (JSON.stringify(data.trades0) != "{}") {
                $("#trades_tbody0").empty();
                trades0 = data.trades0;
                trades0 = JSON.parse(trades0);
                for (var key in trades0) {
                    console.log(key);
                    console.log(Object.values(trades0[key]));
                    $("#trades0 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades0[key])[0] + '</td><td>' + Object.values(trades0[key])[1] + '</td></tr>');
    
                }
            }
            if (JSON.stringify(data.ask_quotes0) != "{}") {
                $("#ask_quotes_tbody0").empty();
                ask_quotes0 = data.ask_quotes0;
                ask_quotes0 = JSON.parse(ask_quotes0);
                for (var key in ask_quotes0) {
                    console.log(key);
                    console.log(Object.values(ask_quotes0[key]));
                    $("#ask_quotes0 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes0[key])[0] + '</td><td>' + Object.values(ask_quotes0[key])[1] + '</td></tr>');
    
                }
            }
            
            //AAPL
            if (JSON.stringify(data.quotes1) != "{}") {
                
                $("#quotes_tbody1").empty();

                quotes1 = data.quotes1;
                quotes1 = JSON.parse(quotes1);
                for (var key in quotes1) {
                    console.log(key);
                    console.log(Object.values(quotes1[key]));
                    $("#quotes1 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes1[key])[0] + '</td><td>' + Object.values(quotes1[key])[1] + '</td></tr>');
    
                }
            }
            if (JSON.stringify(data.trades1) != "{}") {
                $("#trades_tbody1").empty();
                trades1 = data.trades1;
                trades1 = JSON.parse(trades1);
                for (var key in trades1) {
                    console.log(key);
                    console.log(Object.values(trades1[key]));
                    $("#trades1 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades1[key])[0] + '</td><td>' + Object.values(trades1[key])[1] + '</td></tr>');
    
                }
            }
            if (JSON.stringify(data.ask_quotes1) != "{}") {
                $("#ask_quotes_tbody1").empty();
                ask_quotes1 = data.ask_quotes1;
                ask_quotes1 = JSON.parse(ask_quotes1);
                for (var key in ask_quotes1) {
                    console.log(key);
                    console.log(Object.values(ask_quotes1[key]));
                    $("#ask_quotes1 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes1[key])[0] + '</td><td>' + Object.values(ask_quotes1[key])[1] + '</td></tr>');
    
                }

            }

            //AMZN
            if (JSON.stringify(data.quotes2) != "{}") {

                console.log('okokokok');
                $("#quotes_tbody2").empty();
                quotes2 = data.quotes2;
                quotes2 = JSON.parse(quotes2);
                for (var key in quotes2) {
                    console.log(key);
                    console.log(Object.values(quotes2[key]));
                    $("#quotes2 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes2[key])[0] + '</td><td>' + Object.values(quotes2[key])[1] + '</td></tr>');
                    
                }
                
            }
            if (JSON.stringify(data.ask_quotes2) != "{}") {
                $("#ask_quotes_tbody2").empty();
                ask_quotes2 = data.ask_quotes2;
                ask_quotes2 = JSON.parse(ask_quotes2);
                if (JSON.stringify(ask_quotes2) !== "{}") {
                    for (var key in ask_quotes2) {
                        console.log(key);
                        console.log(Object.values(ask_quotes2[key]));
                        $("#ask_quotes2 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes2[key])[0] + '</td><td>' + Object.values(ask_quotes2[key])[1] + '</td></tr>');
                    }
                }
            }
            
            if (JSON.stringify(data.trades2) != "{}") {
                $("#trades_tbody2").empty();
                trades2 = data.trades2;
                trades2 = JSON.parse(trades2);
                for (var key in trades2) {
                    console.log(key);
                    console.log(Object.values(trades2[key]));
                    $("#trades2 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades2[key])[0] + '</td><td>' + Object.values(trades2[key])[1] + '</td></tr>');
    
                }
            }

            //AMD
            if (JSON.stringify(data.quotes3) != "{}") {

                console.log('okokokok');
                $("#quotes_tbody3").empty();
                quotes3 = data.quotes3;
                quotes3 = JSON.parse(quotes3);
                for (var key in quotes3) {
                    console.log(key);
                    console.log(Object.values(quotes3[key]));
                    $("#quotes3 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes3[key])[0] + '</td><td>' + Object.values(quotes3[key])[1] + '</td></tr>');
                    
                }
                
            }
            if (JSON.stringify(data.ask_quotes3) != "{}") {
                $("#ask_quotes_tbody3").empty();
                ask_quotes3 = data.ask_quotes3;
                ask_quotes3 = JSON.parse(ask_quotes3);
                if (JSON.stringify(ask_quotes3) !== "{}") {
                    for (var key in ask_quotes3) {
                        console.log(key);
                        console.log(Object.values(ask_quotes3[key]));
                        $("#ask_quotes3 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes3[key])[0] + '</td><td>' + Object.values(ask_quotes3[key])[1] + '</td></tr>');
                    }
                }
            }
            
            if (JSON.stringify(data.trades3) != "{}") {
                $("#trades_tbody3").empty();
                trades3 = data.trades3;
                trades3 = JSON.parse(trades3);
                for (var key in trades3) {
                    console.log(key);
                    console.log(Object.values(trades3[key]));
                    $("#trades3 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades3[key])[0] + '</td><td>' + Object.values(trades3[key])[1] + '</td></tr>');
    
                }
            }
            //GOOGL
            if (JSON.stringify(data.quotes4) != "{}") {

                console.log('okokokok');
                $("#quotes_tbody4").empty();
                quotes4 = data.quotes4;
                quotes4 = JSON.parse(quotes4);
                for (var key in quotes4) {
                    console.log(key);
                    console.log(Object.values(quotes4[key]));
                    $("#quotes4 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes4[key])[0] + '</td><td>' + Object.values(quotes4[key])[1] + '</td></tr>');
                    
                }
                
            }
            if (JSON.stringify(data.ask_quotes4) != "{}") {
                $("#ask_quotes_tbody4").empty();
                ask_quotes4 = data.ask_quotes4;
                ask_quotes4 = JSON.parse(ask_quotes4);
                if (JSON.stringify(ask_quotes4) !== "{}") {
                    for (var key in ask_quotes4) {
                        console.log(key);
                        console.log(Object.values(ask_quotes4[key]));
                        $("#ask_quotes4 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes4[key])[0] + '</td><td>' + Object.values(ask_quotes4[key])[1] + '</td></tr>');
                    }
                }
            }
            
            if (JSON.stringify(data.trades4) != "{}") {
                $("#trades_tbody4").empty();
                trades4 = data.trades4;
                trades4 = JSON.parse(trades4);
                for (var key in trades4) {
                    console.log(key);
                    console.log(Object.values(trades4[key]));
                    $("#trades4 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades4[key])[0] + '</td><td>' + Object.values(trades4[key])[1] + '</td></tr>');
    
                }
            }
            //META
            if (JSON.stringify(data.quotes5) != "{}") {

                console.log('okokokok');
                $("#quotes_tbody5").empty();
                quotes5 = data.quotes5;
                quotes5 = JSON.parse(quotes5);
                for (var key in quotes5) {
                    console.log(key);
                    console.log(Object.values(quotes5[key]));
                    $("#quotes5 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes5[key])[0] + '</td><td>' + Object.values(quotes5[key])[1] + '</td></tr>');
                    
                }
                
            }
            if (JSON.stringify(data.ask_quotes5) != "{}") {
                $("#ask_quotes_tbody5").empty();
                ask_quotes5 = data.ask_quotes5;
                ask_quotes5 = JSON.parse(ask_quotes5);
                if (JSON.stringify(ask_quotes5) !== "{}") {
                    for (var key in ask_quotes5) {
                        console.log(key);
                        console.log(Object.values(ask_quotes5[key]));
                        $("#ask_quotes5 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes5[key])[0] + '</td><td>' + Object.values(ask_quotes5[key])[1] + '</td></tr>');
                    }
                }
            }
            
            if (JSON.stringify(data.trades5) != "{}") {
                $("#trades_tbody5").empty();
                trades5 = data.trades5;
                trades5 = JSON.parse(trades5);
                for (var key in trades5) {
                    console.log(key);
                    console.log(Object.values(trades5[key]));
                    $("#trades5 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades5[key])[0] + '</td><td>' + Object.values(trades5[key])[1] + '</td></tr>');
    
                }
            }
            //GOOG
            if (JSON.stringify(data.quotes6) != "{}") {

                console.log('okokokok');
                $("#quotes_tbody6").empty();
                quotes6 = data.quotes6;
                quotes6 = JSON.parse(quotes6);
                for (var key in quotes6) {
                    console.log(key);
                    console.log(Object.values(quotes6[key]));
                    $("#quotes6 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(quotes6[key])[0] + '</td><td>' + Object.values(quotes6[key])[1] + '</td></tr>');
                    
                }
                
            }
            if (JSON.stringify(data.ask_quotes6) != "{}") {
                $("#ask_quotes_tbody6").empty();
                ask_quotes6 = data.ask_quotes6;
                ask_quotes6 = JSON.parse(ask_quotes6);
                if (JSON.stringify(ask_quotes6) !== "{}") {
                    for (var key in ask_quotes6) {
                        console.log(key);
                        console.log(Object.values(ask_quotes6[key]));
                        $("#ask_quotes6 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(ask_quotes6[key])[0] + '</td><td>' + Object.values(ask_quotes6[key])[1] + '</td></tr>');
                    }
                }
            }
            
            if (JSON.stringify(data.trades6) != "{}") {
                $("#trades_tbody6").empty();
                trades6 = data.trades6;
                trades6 = JSON.parse(trades6);
                for (var key in trades6) {
                    console.log(key);
                    console.log(Object.values(trades6[key]));
                    $("#trades6 tbody").append('<tr> <td>' + south_africa_time + '</td> <td>' + key + '</td> <td>' + Object.values(trades6[key])[0] + '</td><td>' + Object.values(trades6[key])[1] + '</td></tr>');
    
                }
            }

        }
    });
    updateCall();
}

function updateCall() {
    if (JSON.stringify(ask_quotes0) === "{}") {
        setTimeout(function () { executeQuery() }, 1000);
    } else {
        setTimeout(function () { executeQuery() }, 1000);
    }
}

$(document).ready(function () {

    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/get_data/',
        success: function (data) {
            console.log('asdf');
        },
        error: function (error_data) {
            console.log(error_data)
        }
    })

    executeQuery();
});