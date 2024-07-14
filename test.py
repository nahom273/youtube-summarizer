import whisper
import os
# Initialize the Whisper model
whisper_model = whisper.load_model("base")

# Path to the local audio file
audio_file_path = "CB323_Regular.mp3"

# Check if the file exists
if os.path.exists(audio_file_path):
    print(f"Audio file found: {audio_file_path}")
else:
    print(f"Audio file not found: {audio_file_path}")
    exit()

# Transcribe the audio file using Whisper
try:
    result = whisper_model.transcribe(audio_file_path)
    print("Transcription result:")
    print(result['text'])
except Exception as e:
    print(f"Error transcribing audio: {e}")
