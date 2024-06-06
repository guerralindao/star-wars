
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
data_object = get_data_config(data_from_config, file_name) # Get data config

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
        
        """
        Documentation:
            1. Scrape data
            2. Read data
            3. Parsing data
            
            9. Clean work folders
        """

        # Start scrape and elaborate responses
        response = getting_data_from_website() # Get response_id

        # Check if the response is not None
        if response is not None:
            # Setting json responses path
            path_to_json_files = f"{CURRENT_DIRECTORY}/lobster/"

            # Get all JSON file names as a list
            json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

            # Loop every json file
            for json_file_name in json_file_names:
                # Debug: Print file name
                # print(f"File name: {json_file_name}")
                parsing_data_from_response(json_file_name) # Elaborate response_id
                clean("lobster", json_file_name) # Cleaner
        
    else:
        # Website running disable 
        print(f"{file_name} (disabled)") # Script disabled


##############################
# Other functions
##############################

""" Payload response """
def payload_response(response_id):
    # Open and read response json format
    # I'm not declare file extension because it will be pass from directory list 
    with open(f'{CURRENT_DIRECTORY}/lobster/{response_id}', 'r') as file:
        data = json.load(file)
    # Return response data
    return data


""" Check empty in json object """
def is_empty_json(json_obj):
    # return true if length is 0. 
    if json_obj is None:
        return True
    return len(json_obj) == 0


""" Get data from website """
def getting_data_from_website():

    # Initializing variables
    data = None
    page_number = 1
    response_name = f"response_{TRASMISSIONE}"
    
    # Change request from IT to ENG
    # my_request = f"{WEBSITE_URL_API}/cards?locale=it&pagination[page]={page_number}&pagination[pageSize]={WEBSITE_ELEMENTS_NUMBER}"
    my_request = f"{WEBSITE_URL_API}/cards?pagination[page]={page_number}&pagination[pageSize]={WEBSITE_ELEMENTS_NUMBER}"

    # Send the request
    response = requests.get(my_request)

    # Check response: 200 = good, 404 = bad
    if response.status_code == 200:

        # Print feedback
        print(f"{TRASMISSIONE}: Response status code 200")

        # parse json data
        data = json.loads(response.content.decode('utf-8'))

        # Get section from JSON
        data_meta_page = data["meta"]["pagination"]["page"]
        data_meta_size = data["meta"]["pagination"]["pageSize"]
        data_meta_pages = data["meta"]["pagination"]["pageCount"] # Reminder: Number of page availables
        data_meta_total = data["meta"]["pagination"]["total"] # Reminder: Number of cards

        # Loop until page_number reach totale pages from response
        while page_number <= data_meta_pages:

            # Create response id
            # Create dynamic request with page number
            response_id = f"{response_name}_P{page_number}"
            my_request = f"{WEBSITE_URL_API}/cards?locale=it&pagination[page]={page_number}&pagination[pageSize]={WEBSITE_ELEMENTS_NUMBER}"

            # Send the request with page number updated
            response = requests.get(my_request)

            # Get json data
            data = json.loads(response.content.decode('utf-8'))

            # Save response on file.json
            with open(f'lobster/{response_id}.json', 'w') as file:
                json.dump(data, file)

            # Print feedback
            print(f"{TRASMISSIONE}: Get response [{response_id}.json] page[{page_number}]")

            # Increment page_number by 1
            page_number = page_number + 1

    else:
        # Print feedback
        print(f"{TRASMISSIONE}: Not found response. Request failed")
        return None # None

    # Return response id for the next steps
    return response


""" Reading JSON data and parsing """ 
def parsing_data_from_response(response_id):
    
    # Payload response
    list_data = []
    data = payload_response(response_id)

    # Variables
    elements_key = 0
    elements_json = len(data["data"]) # Get all cards on JSON

    # Loop for get data from every card
    while elements_key < elements_json:

        # Print feedback
        print(f"{TRASMISSIONE}: File {response_id} element {elements_key} ...")
        
        dataset = data["data"][elements_key]["attributes"]
        number_subelement = 0

        # Difference on cards (campo: artFrontHorizontal)
        #   BASE = False
        #   EROE = True
        #   TRUPPA = False
        #   EVENTO = False 
        data_attributes_artFrontHorizontal = dataset["artFrontHorizontal"]
        data_attributes_artBackHorizontal = dataset["artBackHorizontal"]
        
        ######################
        # Get data from JSON #
        ######################

        """ Attributes """
        data_attributes_title = dataset["title"] if dataset["title"] is not None else "ND"
        data_attributes_subtitle = dataset["subtitle"] if dataset["subtitle"] is not None else "ND"
        data_attributes_cardnumber = dataset["cardNumber"] if dataset["cardNumber"] is not None else "ND"
        data_attributes_artist = dataset["artist"] if dataset["artist"] is not None else "ND"
        data_attributes_cost = dataset["cost"] if dataset["cost"] is not None else "ND"
        data_attributes_life = dataset["hp"] if dataset["hp"] is not None else "ND"
        data_attributes_power = dataset["power"] if dataset["power"] is not None else "ND"
        data_attributes_text = dataset["text"] if dataset["text"] is not None else "ND"
        # More informations about card
        data_attributes_uid = dataset["cardUid"] if dataset["cardUid"] is not None else "ND"
        data_attributes_epicaction = dataset["epicAction"] if dataset["epicAction"] is not None else "ND"

        # Get Front image 
        data_image_front = dataset["artFront"]["data"]["attributes"]["url"]
        
        # Get Back image
        data_image_back = ""
        if data_attributes_artBackHorizontal is not None:
            data_image_back = dataset["artBack"]["data"]["attributes"]["url"]
        
        #######################
        # Set empty variables #
        #######################
        
        data_type_name = None
        data_type_description = None
        data_type_value = None

        data_rarity_name = None
        data_rarity_character = None

        data_expansion_name = None
        data_expansion_description = None
        data_expansion_code = None

        """ 
        ************************************* 
        *   Aspects (it would be a loop) 
        ************************************* 
        """ 
        # Empty boxes
        box_data_aspects_name = ""
        box_data_aspects_description = ""
        box_data_aspects_color = ""
        if is_empty_json(dataset["aspects"]["data"]) is False:
            
            # Initialize variables
            my_index = 0
            max_index = len(dataset["aspects"]["data"]) if len(dataset["aspects"]["data"]) is not None else None # Get len data
            
            # Start loop
            while my_index < max_index: 

                # Get informations
                data_aspects_name = dataset["aspects"]["data"][my_index]["attributes"]["name"] if dataset["aspects"]["data"][my_index]["attributes"]["name"] is not None else "ND"
                data_aspects_description = dataset["aspects"]["data"][my_index]["attributes"]["description"] if dataset["aspects"]["data"][my_index]["attributes"]["description"] is not None else "ND"
                data_aspects_color = dataset["aspects"]["data"][my_index]["attributes"]["color"] if dataset["aspects"]["data"][my_index]["attributes"]["color"] is not None else "ND"
                
                # Compile boxes with array informations
                box_data_aspects_name += f"{data_aspects_name}, "
                box_data_aspects_description += f"{data_aspects_description}, "
                box_data_aspects_color += f"{data_aspects_color}, "

                # Continue loop
                my_index = my_index + 1

        """ 
        ************************************* 
        *   Type
        ************************************* 
        """ 
        if is_empty_json(dataset["type"]["data"]) is False:
            data_type_name = dataset["type"]["data"]["attributes"]["name"] if dataset["type"]["data"]["attributes"]["name"] is not None else "ND" 
            data_type_description = dataset["type"]["data"]["attributes"]["description"] if dataset["type"]["data"]["attributes"]["description"] is not None else "ND"
            data_type_value = dataset["type"]["data"]["attributes"]["value"] if dataset["type"]["data"]["attributes"]["value"] is not None else "ND"
        
        """ 
        ************************************* 
        *   Traits (it would be a loop)
        ************************************* 
        """ 
        # Empty boxes
        box_data_traits_name = ""
        box_data_traits_description = ""
        if is_empty_json(dataset["traits"]["data"]) is False:

            # Initialize variables
            my_index = 0
            max_index = len(dataset["traits"]["data"]) if len(dataset["traits"]["data"]) is not None else None # Get len data
            
            # Start loop
            while my_index < max_index: 
                
                # Get informations
                data_traits_name = dataset["traits"]["data"][my_index]["attributes"]["name"] if dataset["traits"]["data"][my_index]["attributes"]["name"] is not None else "ND"
                data_traits_description = dataset["traits"]["data"][my_index]["attributes"]["description"] if dataset["traits"]["data"][my_index]["attributes"]["description"] is not None else "ND"

                # Compile boxes with array informations
                box_data_traits_name += f"{data_traits_name}, "
                box_data_traits_description += f"{data_traits_description}, "

                # Continue loop
                my_index = my_index + 1

        """ 
        ************************************* 
        *   Arenas (it would be a loop)
        ************************************* 
        """ 
        # Empty boxes
        box_data_arenas_name = ""
        box_data_arenas_description = ""
        if is_empty_json(dataset["arenas"]["data"]) is False:

            # Initialize variables
            my_index = 0
            max_index = len(dataset["arenas"]["data"]) if len(dataset["arenas"]["data"]) is not None else None # Get len data
            
            # Start loop
            while my_index < max_index: 
                
                # Get informations
                data_arenas_name = dataset["arenas"]["data"][my_index]["attributes"]["name"] if dataset["arenas"]["data"][my_index]["attributes"]["name"] is not None else "ND"
                data_arenas_description = dataset["arenas"]["data"][my_index]["attributes"]["description"] if dataset["arenas"]["data"][my_index]["attributes"]["description"] is not None else "ND"

                # Compile boxes with array informations
                box_data_arenas_name += f"{data_arenas_name}, "
                box_data_arenas_description += f"{data_arenas_description}, "

                # Continue loop
                my_index = my_index + 1

        """ 
        ************************************* 
        *   Rarity
        ************************************* 
        """ 
        if is_empty_json(dataset["rarity"]["data"]) is False:
            data_rarity_name = dataset["rarity"]["data"]["attributes"]["name"] if dataset["rarity"]["data"]["attributes"]["name"] is not None else "ND"
            data_rarity_character = dataset["rarity"]["data"]["attributes"]["character"] if dataset["rarity"]["data"]["attributes"]["character"] is not None else "ND"

        """ 
        ************************************* 
        *   Expansion
        ************************************* 
        """ 
        if is_empty_json(dataset["expansion"]["data"]) is False:
            data_expansion_name = dataset["expansion"]["data"]["attributes"]["name"] if dataset["expansion"]["data"]["attributes"]["name"] is not None else "ND"
            data_expansion_description = dataset["expansion"]["data"]["attributes"]["description"] if dataset["expansion"]["data"]["attributes"]["description"] is not None else "ND"
            data_expansion_code = dataset["expansion"]["data"]["attributes"]["code"] if dataset["expansion"]["data"]["attributes"]["code"] is not None else "ND"

        # Debug
        # print()
        # print(f">>>> File : {response_id} Elemento : {elements_key}")
        # print(f"Titolo : {data_attributes_title}")
        # print(f"Sub-Titolo : {data_attributes_subtitle}")
        # print(f"Card Id : {data_attributes_cardnumber}")
        # print(f"Artista : {data_attributes_artist}")
        # print(f"Costo : {data_attributes_cost}")
        # print(f"Vita : {data_attributes_life}")
        # print(f"Potenza : {data_attributes_power}")
        # print(f"Testo : {data_attributes_text}")
        # print(f"IMG Fronte : {data_image_front}")
        # print(f"IMG Retro : {data_image_back}")
        # # print(f"Aspetto nome : {data_aspects_name}")
        # # print(f"Aspetto desc : {data_aspects_description}")
        # # print(f"Aspetto color : {data_aspects_color}")
        # print(f"Tipo nome : {data_type_name}")
        # print(f"Tipo desc : {data_type_description}")
        # print(f"Tipo value : {data_type_value}")
        # # print(f"Tratti nome : {data_traits_name}")
        # # print(f"Tratti desc : {data_traits_description}")
        # # print(f"Arena nome : {data_arenas_name}")
        # # print(f"Arena desc : {data_arenas_description}")
        # print(f"Rarità : {data_rarity_name}")
        # print(f"Rarità carattere : {data_rarity_character}")
        # print(f"Espansione nome : {data_expansion_name}")
        # print(f"Espansione desc : {data_expansion_description}")
        # print(f"Espansione codice : {data_expansion_code}")
        # print()

        # Caracthers to cleaner
        to_clean = re.compile("<.*?>")
        
        # Removing html tags, examples: <h1><br />...
        data_attributes_text = re.sub(to_clean, "", data_attributes_text)
        box_data_aspects_description = re.sub(to_clean, "", box_data_aspects_description)
        box_data_traits_description = re.sub(to_clean, "", box_data_traits_description)
        box_data_arenas_description = re.sub(to_clean, "", box_data_arenas_description)
        
        # Removing line breaks
        data_attributes_text = re.sub("\n|\r", " ", data_attributes_text)
        box_data_aspects_description = re.sub("\n|\r", " ", box_data_aspects_description)
        box_data_traits_description = re.sub("\n|\r", " ", box_data_traits_description)
        box_data_arenas_description = re.sub("\n|\r", " ", box_data_arenas_description)

        # Append on my list my information
        list_data.append({
            "trasm": TRASMISSIONE, # Trx timestamp
            "response_id": response_id, # Response name (file_name)
            "elements_key": elements_key, # Number of element
            "title": data_attributes_title, # Title
            "subtitle": data_attributes_subtitle, # Subtitle
            "card_number": data_attributes_cardnumber, # Card number
            "artist": data_attributes_artist, # Artist
            "cost": data_attributes_cost, # Cost
            "hp": data_attributes_life, # Life
            "power": data_attributes_power, # Power
            "text": data_attributes_text, # Text effect
            "image_front": data_image_front, # Image front
            "image_back": data_image_back, # Image back
            "card_uid": data_attributes_uid, # Uid card
            "epic_action": data_attributes_epicaction, # Epic action
            "variants": "XXX",
            "aspect_name": box_data_aspects_name, # [ARRAY]
            "aspect_description": box_data_aspects_description, # [ARRAY]
            "aspect_color": box_data_aspects_color, # [ARRAY]
            "type_name": data_type_name, # Type name 
            "type_description": data_type_description, # Type description
            "type_value": data_type_value, # Type value
            "traits_name": box_data_traits_name, # [ARRAY]
            "traits_description": box_data_traits_description, # [ARRAY]
            "arenas_name": box_data_arenas_name, # [ARRAY]
            "arenas_description": box_data_arenas_description, # [ARRAY]
            "rarity_name": data_rarity_name, # Rarity name
            "rarity_character": data_rarity_character, # Rarity character
            "expansion_name": data_expansion_name, # Expansion name
            "expansion_description": data_expansion_description, # Expansion description
            "expansion_code": data_expansion_code # Expansion code
        })

        ########
        # LOOP #
        ########
        # Increase elements key
        elements_key = elements_key + 1
    
    # print()
    # print(list_data)

    ###########
    # STORAGE #
    ###########
    # Create file storage for save categories
    # Append data because the products are in continuos change
    create_data_storage(list_data, f"{file_name}_cards_{TRASMISSIONE}", "a")

    # Print feedback
    print(f"{TRASMISSIONE}: The data has been parsed")



##############################
# Code execution
##############################
if __name__ == "__main__":
    main()