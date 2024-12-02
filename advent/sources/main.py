# Imports.
import os


# Function to grab data from the data folder.
def grab_data(*, day: int) -> str:
    cwd = os.getcwd()

    data_path = os.path.join(cwd, f"advent/sources/data/day{day}.txt")

    with open(data_path) as f:
        data = f.read()

    return data


# Create a decorator to support the function.
def data_decorator(day: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = grab_data(day=day)
            return func(data, *args, **kwargs)

        return wrapper

    return decorator
