import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')  

list_of_files = [
    "requirements.txt",
    "app.py",
    "setup.py"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    if file_path.is_file():
        logging.info(f"'{filepath}' already exists.")
    else:
        logging.info(f"'{filepath}' does not exist. Creating the file.")
        file_path.touch()
        