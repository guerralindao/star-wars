
##############################
# Configuration
##############################
from config import * # Configuration file

##############################
# Libraries / Markets
##############################
from components.starwars import main as starwars # Libreria starwars scraping

##############################
# Code functions
##############################
def main():

    print() # Starting
    print("=====================")
    print("= RUNNING FUNCTIONS =")
    print("=====================")
    print()


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