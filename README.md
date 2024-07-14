# YouTube Video Summarizer

A simple web application built with Flask that takes a YouTube video URL, extracts the transcript (if available), and summarizes the content using an AI summarization tool.

## Features

- Paste a YouTube video link to get a summary of the video's content.
- Extracts the transcript of the video if available.
- Summarizes the content using Hugging Face's `transformers` library.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-summarizer.git
   cd youtube-summarizer
Here's the consolidated `README.md` content you can copy and paste:

```markdown
# YouTube Video Summarizer

A simple web application built with Flask that takes a YouTube video URL, extracts the transcript (if available), and summarizes the content using an AI summarization tool.

## Features

- Paste a YouTube video link to get a summary of the video's content.
- Extracts the transcript of the video if available.
- Summarizes the content using Hugging Face's `transformers` library.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-summarizer.git
   cd youtube-summarizer
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Open the web application in your browser.
2. Paste the YouTube video URL into the input field.
3. Click the "Summarize" button.
4. The summary of the video content will be displayed below the form.

## Project Structure

```
youtube_summarizer/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

- `app.py`: The main Flask application file.
- `requirements.txt`: A list of Python dependencies to be installed.
- `templates/index.html`: The HTML template for the web application's interface.
- `static/styles.css`: The CSS file for styling the web application.

## Dependencies

- Flask: A micro web framework for Python.
- youtube-transcript-api: A library to fetch YouTube video transcripts.
- transformers: A library from Hugging Face for natural language processing tasks.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Hugging Face Transformers](https://github.com/huggingface/transformers)
```

### Additional Steps:

1. Create a `requirements.txt` file to list all the dependencies:
   ```bash
   pip freeze > requirements.txt
   ```

2. Push the `README.md` file to GitHub along with your project files:
   ```bash
   git add README.md
   git commit -m "Add README.md"
   git push
   ```

Replace `your-username` with your actual GitHub username in the repository URL. This `README.md` provides an overview of the project, installation instructions, usage guide, project structure, dependencies, and acknowledgments. Adjust the content as needed to better fit your specific project details.
