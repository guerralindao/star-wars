#!/app/starwars/.venv/bin/python3

# Import OS library
import os
import datetime

# Time
timestamp = datetime.datetime.now() # Extract timestamp
timestamp = datetime.date.strftime(timestamp, '%d/%m/%Y T%H:%M:%S') # Setting time

# Declare variables
lobster = "lobster" # Lobster directory : there are temporally files and backups
assets = "assets" # Assets directory : there are images, parsed files and backups
subdir_backups = "backups" # Backups directory
subdir_images = "images" # Images directory

# Make MAIN directories to setup project
os.system(f"mkdir -p {lobster}")
os.system(f"mkdir -p {assets}")

# Make BACKUPS directories
os.system(f"mkdir -p {lobster}/{subdir_backups}")
os.system(f"mkdir -p {assets}/{subdir_backups}")

# Make IMAGES directory
os.system(f"mkdir -p {assets}/{subdir_images}")

# Finish
print(f"{timestamp}: Setup finished")
