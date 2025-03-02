import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the relative path to the JSON file
demons_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Demons.json")


# Load demons from Demons.json
try:
    with open(demons_path, "r") as file:
        demons_data = json.load(file)["demons"]
except FileNotFoundError:
    logging.error(f"Error: Could not find {demons_path}")
    demons_data = {}
except json.JSONDecodeError:
    logging.error("Error: Invalid JSON format in Demons.json")
    demons_data = {}
