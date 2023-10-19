# Description: Settings for the application
import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_API_TOKEN = os.getenv("DISCORD_API_TOKEN")
