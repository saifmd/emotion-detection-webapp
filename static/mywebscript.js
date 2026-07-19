let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const resultBox = document.getElementById("system_response");

    resultBox.innerHTML = "Analyzing...";

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                resultBox.innerHTML = xhttp.responseText;
            } else {
                resultBox.innerHTML = "Unable to analyze the text right now. Please try again.";
            }
        }
    };

    const encodedText = encodeURIComponent(textToAnalyze);
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodedText, true);
    xhttp.send();
};
