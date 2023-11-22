import requests
import datetime
from pathlib import Path

current_directory = Path(__file__).parent


def image_downloader(image_url: str | None):
    if image_url is None:
        raise ValueError("No image URL returned from API.")
    response = requests.get(image_url)
    if response.status_code != 200:
        raise ValueError("Could not download image from URL.")
    # Get current time in format YYYY-MM-DD-HH-MM-SS-MS
    current_time: str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    with open(f"{current_directory}/{current_time}.png", "wb") as file:
        file.write(response.content)
