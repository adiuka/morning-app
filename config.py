from dotenv import load_dotenv
import os


load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
LAT = float(os.getenv("LAT"))
LON = float(os.getenv("LON"))
SPOTIFY_URI = os.getenv("SPOTIFY_URI")
SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_RECEIVER = os.getenv("SMTP_RECEIVER")
