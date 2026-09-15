import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL","https://qae-assignment-tau.vercel.app/?user-id=candidate-wHfCSeDQhVNk")
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
