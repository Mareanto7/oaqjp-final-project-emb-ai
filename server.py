''' Server file to handle HTTP requests '''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analysis")


@app.route("/")
def render_index_page():
    ''' Route handling to serve index.html file '''
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    ''' Route handling to serve get request '''
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        dominant_emotion = None
        emotion_scores = None
        # Return a 400 error response if the input is blank
        return f"400 error: Invalid text! Please try again! Dominant Emotion: \
        {dominant_emotion} Emotion Scores: {emotion_scores}"

    dominant_emotion, emotion_scores = emotion_detector(text_to_analyse )
    return f"For the given statement, the system response is \
    {emotion_scores}. The dominant emotion is: {dominant_emotion}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
