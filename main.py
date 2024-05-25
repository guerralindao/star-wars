
##############################
# Configuration
##############################
from config import * # Configuration file

##############################
# Libraries
##############################
from components.starwars import main as starwars # Library starwars scraping
from components.images_download import main as _download # Library download images
from components.images_compare import main as _compare # Library comparing images
from system.telegram_sendmessage import main as _alert # Library alert administrator [SYSTEM]

##############################
# Code functions
##############################
def main():

    print() # Start
    print("===========================")
    print("= START RUNNING FUNCTIONS =")
    print("===========================")
    
    starwars() # Start scrape data from website
    _download() # Start downloading images from website
    _alert() # Start send notification to administrator

    print() # Finish
    print("============================")
    print("= FINISH RUNNING FUNCTIONS =")
    print("============================")

##############################
# Code execution
##############################
if __name__ == "__main__":
    # Handle optional parameter
    function = sys.argv[1] if len(sys.argv) > 1 else None 

    # Check if the parameter is not None
    if function is None:
        # Not provided a function
        main()
    else:
        try:
            # Check if the function exists
            # It could happened if I forgot to declare library
            # Try to get the function from parameter and execute that
            call = getattr(sys.modules[__name__], function)
            print(f"Executing {function}() function...")
            call()
        except Exception as e: 
            print(f"{TIMESTAMP}: {e}") # Print error message