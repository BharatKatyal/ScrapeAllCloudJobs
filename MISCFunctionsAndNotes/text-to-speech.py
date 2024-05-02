from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
)

speech_file_path = Path(__file__).parent / "speech2.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="My Name is Bharat, I am a creative and innovative developer"
)

response.stream_to_file(speech_file_path)