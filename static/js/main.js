// let url = 'http://127.0.0.1:5000/predict';
let url = 'https://snowfallpredicter.azurewebsites.net/predict'

let apiKey = "e43f7d5b3cc56c04e4ae9d3d593f7940";
let openweatherUrl = "https://api.openweathermap.org/data/2.5/forecast?q=Pithoragarh&cnt=1&appid=" + apiKey;

$.ajax({
    type: 'post',
    dataType: 'json',
    url: openweatherUrl,
    success: function(data) {
        console.log(data);
        let nextPredictionTime = document.getElementById("nextPredictionTime");

        predictionTime = new Date(data.list[0].dt * 1000);
        nextPredictionTime.innerText = predictionTime;

        let nightHours = (data.city.sunset - data.city.sunrise) / 3600;

        let rain = (data.list[0].rain !== undefined) ? data.list[0].rain["3h"] : 0;

        let weatherData = {
            "maxtempC": data.list[0].main.temp_max,
            "FeelsLikeC": data.list[0].main.feels_like,
            "cloudcover": data.list[0].clouds.all,
            "humidity": data.list[0].main.humidity,
            "precipMM": rain,
            "visibility": data.list[0].visibility,
            "winddirDegree": data.list[0].wind.deg,
            "windspeedKmph": data.list[0].wind.speed,
            "nightHours": nightHours
        }

        predict(weatherData);
    },
    error: function(xhr, status, error) {
        alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
    }
});

function predict(postData) {
    $.ajax({
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify(postData),
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {


            let prediction = document.getElementById("prediction");
            if (data.prediction === 0) {
                prediction.innerText = "No snowfall";
            } else {
                prediction.innerText = "Snowfall";
            }
        },
        error: function(xhr, status, error) {
            alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
        }
    });
}