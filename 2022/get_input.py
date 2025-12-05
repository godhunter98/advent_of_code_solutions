import requests
from pathlib import Path
from dotenv import load_dotenv
import os

root = Path(__file__).resolve().parent.parent
load_dotenv(root / '.env')

def fetch_input(year: int, day: int) -> str:
    if 0<day<=25 and 2014<year:
        session = os.environ["session_cookie"]
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        resp = requests.get(url, headers={"Cookie": f"session={session}"})
        resp.raise_for_status()
        return resp.text.strip()
    else:
        raise ValueError("Please Enter Day value between 0 and 26, Year later than 2015!")
