from file_entry_class import FileDataEntry

# prints out welcome message
def welcome_message(): 
    print("Welcome to the meteorite filtering program\n") # welcome message
    print("This program allows you to filter NASA meteorite data contained in a text file\n")
    print("The data in the text file must be organized in a specific format\n Required format:\n    Each line of the text file describes a single meteorite.")
    print("    For each meteorite line there must be 12 tab separated data points\n \nPlease follow the prompts to filter the data")       
    print("\nI am the developer, Chase\n")
    print("The release date of this program is October 5th 2023\n")

def file_data_prompter(file_entry, input_text, output_text): # runs the input menu and the quitCheck function
    file_entry = input(input_text)
    quitCheck(file_entry, output_text) # checks to see if the program exits or continues
    return file_entry

# checks to see if program quits or continues
def quitCheck(promptInput, output_text):
    if promptInput == ">q" or promptInput == ">Q": 
        print("The program is now exiting Goodbye!")
        exit() # exits program
        #return # exits the program
    else:
        print(output_text + promptInput) # prints read mode

def dataFiltering(file_entry): # chooses year, mass or exit based on user input
    data_filter = input("What attribute would you like to filter the data on\n 1. meteor MASS(g)\n 2. The Year the meteor fell to earth\n 3. QUIT\n")
   
    if data_filter == "3": # exists the program
        print("The program is now exiting Goodbye!")
        exit()
    elif data_filter == "2":
        bounds_prompt(file_entry, "YEAR")
        file_entry.titleholder = "YEAR"
    elif data_filter == "1":
        bounds_prompt(file_entry, "MASS")
        file_entry.titleholder = "MASS"

def bounds_prompt(file_entry, label_text): # prompts for upper and lower bounds of mass or year
    file_entry.lower_bound = file_data_prompter(file_entry.lower_bound, "Enter the LOWER limit (inclusive) for the meteor's " + label_text + " , Enter >Q or >q to quit: \n", "Lower Bound: ")
    file_entry.upper_bound = file_data_prompter(file_entry.lower_bound, "Enter the UPPER limit (inclusive) for the meteor's " + label_text + " , Enter >Q or >q to quit: \n", "Lower Bound: ")
   