import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/database/__init__.py",
    f"{project_name}/database/mongodb.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/generic.py",
    f"{project_name}/kafka_config/__init__.py",
    f"{project_name}/kafka_consumer/__init__.py",
    f"{project_name}/kafka_consumer/json_consumer.py",
    f"{project_name}/kafka_logger/__init__.py",
    f"{project_name}/kafka_producer/__init__.py",
    f"{project_name}/kafka_producer/json_producer.py",
    ".env",
    "setup.py",
    "requirements.txt",
    "sample_data/kafka-sensor-topic/",
    "consumer_main.py",
    "producer_main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created")