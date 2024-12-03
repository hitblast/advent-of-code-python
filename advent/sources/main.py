# Imports.
import os
from datetime import datetime


# Function to grab data from the data folder.
def grab_data(*, day: int, year: int | None = None) -> str:
    current_year = year if year else datetime.now().year
    cwd = os.getcwd()
    data_path = os.path.join(cwd, f"advent/sources/data/{current_year}/day{day}.txt")

    with open(data_path) as f:
        data = f.read()

    return data
