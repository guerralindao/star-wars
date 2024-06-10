
##############################
# Load libraries
##############################
import sys
sys.path.append('/app/starwars') # Setting path
import os
from config import *

# Setting current name file
file_name_full = os.path.basename(__file__) # Get full base name file
file_name = file_name_full[:-3] # Get only file name without extension

# Start to get parameters from configuration file
data_from_config = load_data_config() # Load config file data
data_object = get_data_config(data_from_config, "starwars") # Get data config

# Check if data config is None
if data_object is not None:
    ################################
    # Script parameters 
    ################################
    WEBSITE_URL = data_object["url"] # Url
    WEBSITE_URL_BASE = data_object["url_base"] # Base url
    WEBSITE_URL_API = data_object["url_api"] # API url
    WEBSITE_ELEMENTS_NUMBER = data_object["number_of_elements" ] # Number of elements
    WEBSITE_STATUS = data_object["status" ] # Status


##############################
# Code functions
##############################
def main():
    
    # Last check to be sure if the script is enabled or not
    # if it's enabled I will run the script, otherwise I see message on else 
    if data_object is not None:
        
        # Setting json responses path
        path_to_json_files = f'{CURRENT_DIRECTORY}/assets/'

        # Get all CSV file names as a list
        csv_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.csv')]

        # Checking if list is not empty
        if csv_file_names:
            # Loop every CSV file
            for csv_file_name in csv_file_names:
                result = getting_images(csv_file_name) # Elaborate file
                download_image(result) # Download images (front)
                clean("assets", csv_file_name) # Cleaner
        else:
            print(f"{TRASMISSIONE}: List filename images empty")

    else:
        # Website running disable 
        print(f"{file_name} (disabled)") # Script disabled


##############################
# Other functions
##############################

""" Get images from CSV """
def getting_images(file):

    # Get data from file CSV
    data = pd.read_csv(f"{CURRENT_DIRECTORY}/assets/{file}", header=None, sep=";", encoding="utf-8")

    # Get result from data and convert to list
    result_img_front = data[11].tolist() # Front images [11]
    result_img_back = data[12].tolist() # Back images [12]

    # Removing empty values / "nan" values
    result_img_front = [i for i in result_img_front if str(i) != 'nan']
    result_img_back = [i for i in result_img_back if str(i) != 'nan']

    # Create a single list
    result = result_img_front + result_img_back

    # Return result
    return result


""" Download image from url """
def download_image(result):

    # Initializing variables
    data = None
    counter = 0

    # Loop all informations
    # Download images (i = url image)
    for i in result:
        # Setting name file
        # Implementation: Get last item of splitted string (filename)
        name_image = i.split("/")[-1]
        
        # Print feedback
        print(f"{TRASMISSIONE}: Download image [{name_image}] ...")
        
        # Compile counter images downloaded
        counter = counter + 1

        # Obtain response
        response = requests.get(i)

        # Save response to image
        with open(f"{CURRENT_DIRECTORY}/assets/images/{name_image}", 'wb') as file:
            file.write(response.content)        
        # End loop

    # Print feedback about numbers of images
    print(f"{TRASMISSIONE}: [{counter}] images downloaded")





##############################
# Code execution
##############################
if __name__ == "__main__":
    main()