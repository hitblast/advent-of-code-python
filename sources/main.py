# Imports.
import os
from datetime import datetime


# Function to grab data from the data folder.
def grab_data(*, day: int, year: int | None = None) -> str:
    current_year = year if year else datetime.now().year
    cwd = os.getcwd()
    data_path = os.path.join(cwd, f"sources/data/{current_year}/day{day}.txt")

    with open(data_path) as f:
        data = f.read()

    return data


# Create a decorator to support the function.
def data_decorator(day: int, year: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = grab_data(day=day, year=year)
            return func(data, *args, **kwargs)

        return wrapper

    return decorator
