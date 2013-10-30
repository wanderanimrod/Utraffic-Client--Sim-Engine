console.log("Data fetcher loaded!");
dataOut = $("#data");

var fetchData = function() {
    var requestUrl = "http://localhost:5000/get_data/10/";
    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if(request.readyState == 4) {
            console.log(request.responseText);
            var dataJson = JSON.parse(request.responseText);
            plugDataIntoPage(dataJson);
        }
    };

    request.open("GET", requestUrl, true);
    request.send();
};

var plugDataIntoPage = function(dataJson) {
    dataOut.text(dataJson.visualisation)
};

fetchData();