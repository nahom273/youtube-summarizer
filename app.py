from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)

# Load summarization pipeline
summarizer = pipeline("summarization")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    video_url = request.form['video_url']
    video_id = extract_video_id(video_url)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    except Exception as e:
        summary = f"An error occurred: {str(e)}"

    return render_template('index.html', summary=summary)


def extract_video_id(url):
    # Extract video ID from URL
    from urllib.parse import urlparse, parse_qs
    query = urlparse(url).query
    video_id = parse_qs(query).get('v')
    return video_id[0] if video_id else url.split('/')[-1]


if __name__ == '__main__':
    app.run(debug=True)
