
##############################
# Libraries
##############################
import os # using for system evinronment
import sys # using for system logic
import json # using for use and read json data 
import requests # using for bs4
import pandas as pd # using for create and elaborate data
import re # using for bs4
import datetime # using datetime module
from bs4 import BeautifulSoup # using for scrape websites
from multiprocessing import Process # Multiprocess
from dotenv import load_dotenv # using for environment

# Set current work path
CURRENT_DIRECTORY = os.getcwd() # Set current path

# Load environment variables
# load_dotenv(f"{CURRENT_DIRECTORY}/.env")

##############################
# Parameters
##############################
LOGGING_FORCE = True
LOGGING_MODE = "CSV" # Logging format file
TIMESTAMP = datetime.datetime.now() # Stores current time
TRASMISSIONE = datetime.date.strftime(TIMESTAMP, '%Y%m%dT%H%M%S') # Trasmissione

REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36 Edg/123.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "it-IT,it;q=0.5"
} # Set user agent for parsing anti-robots websites


##############################
# Functions
##############################
# Payload soup
def payload_soup(PAYLOAD_URL):
    response = requests.get(PAYLOAD_URL, headers=REQUEST_HEADERS) # Versione con headers
    response.content  # This will store the HTML content of the webpage    
    soup = BeautifulSoup(response.content, "html.parser")
    # soup = BeautifulSoup(response.content, "lxml")
    # print(soup)
    return soup

# Logging section, at the moment availables: CSV, SHELL 
# Example: create_data_storage(data, name, shop_name)
def create_data_storage(data, name, mode):
    storage_data = data
    storage_name = name
    storage_mode = mode

    # Check data passed on function
    if storage_data is None:
        return
    
    # Check name parameter passed on function 
    if storage_name is None: 
        return
    
    # Check format (see on configuration file)
    if LOGGING_MODE == "CSV":
        df = pd.DataFrame(storage_data)
        df.to_csv(f"parsed/{storage_name}.csv", mode=f"{storage_mode}", index=False, header=False, sep=";", encoding="utf-8")  # Optional: Don't include index column
    else:
        print("Storage not configured. It miss format")

