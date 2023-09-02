import os

def add_directory(path: str, name: str) -> None:
    print(f"Creating directory for {name}")
    if not os.path.exists(path):
        os.makedirs(path)