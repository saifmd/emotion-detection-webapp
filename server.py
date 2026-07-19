'''This is the main flask interface for 
    emotion detector functionality'''

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the range of emotions
        and their score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze', '')
    response = emotion_detector(text_to_analyze, use_hf=True)
    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    score_strings = [f"'{emo}': {response[emo]}" for emo in emotions]
    scores_part = ", ".join(score_strings[:-1]) + f" and {score_strings[-1]}"

    result = (
        f"For the given statement, the system response is {scores_part}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
