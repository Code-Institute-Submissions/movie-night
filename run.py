import requests
from bs4 import BeautifulSoup
import os
import time


"""

This Python script scrapes movie titles from a webpage "Best Movies of the Year 2023" webpage
and filters the list to give the 50 best movies out of a list of more then 150 
and saves the downloaded HTML content. 

The code uses some of the already exisitng and highly common coding lines such as:
1. requests.get(web_address) ----> This uses the highly common requests library and its get() method.
2. BeautifulSoup(html_doc,"html.parser") ----> Another highly common class called 'Beautiful soup'.
3. with open() ----> Uses commonly used with and open function for automatic closing of file and uses 'mode' argument
   of the function to either read or write the named file. 

It offers the user choices to:
1. Use an existing .html file containing the desired webpage content (for in case,if user ran the script twice).
2. Create a new .html file by downloading the webpage content from the provided URL.
3. Exit anytime after getting prompt for creating a new file.

The script utilizes the `requests` library to fetch the webpage content,
`BeautifulSoup` to parse the HTML, and error handling mechanisms to catch potential exceptions
during file operations and network requests.

**Key functionalities:**

- Prompts the user to choose between using an existing .html file(if available) or downloading a new one.
- Handles user input for file selection or creation.
- Downloads the webpage content using the `requests` library and saves it to a file.
- Parses the downloaded HTML content using `BeautifulSoup`.
- Extracts movie titles from HTML elements with the class "article_movie_title".
- Prints the extracted movie titles.
"""


"""
HELPER FUNCTIONS : [get_new_file_name() and get_file_path()]
"""
def get_new_file_name():
    """
    Prompts the user for a new filename or exiting the program 
    and if the user wish to continue, it ensures
    the file name given by user has the .html extension,if not
    it adds the .html extension.
    """
    while True:
        save_location = input("Enter the desired filename or exit the program (type 'exit'): \n")
        if save_location.lower()=='exit':
            exit()
        elif not save_location.endswith(".html"):
            save_location += ".html"
        return save_location


def get_file_path():
    """
    Saves the exisiting html files into an empty list. 
    Runs when there are, html files present in the program directory which is the gitpod's workspace path. 
    if html files are already available, it gives user possibility to perform operations on them, 
    such as using the existing file by giving a number related to the movie or creating a new one.
    """
    base_path = "/workspace/movie-night"
    html_files = []
    for filename in os.listdir(base_path):
        if filename.endswith(".html"):
            html_files.append(filename)

    if html_files:
        print("PLEASE BE RESPECTFUL,DO NOT SCRAP AGAIN IF A SAVED FILE ALREADY EXIST!\n")
        time.sleep(1)
        print("Loading....")
        time.sleep(2)
        view_existing_files = input("One or more existing (.html)files are found. Do you wish to see them ('y/n'): \n ")
        if view_existing_files.lower() != 'n':
            print("Existing HTML files in the current directory are:\n")
            for index, existing_file in enumerate(html_files):
                print(f"{index+1}. {existing_file}")
            user_choice = input("\nUse existing file (enter number) or create new (enter 'n'): \n ")
            if user_choice.lower() != 'n':
                try:
                    chosen_index = int(user_choice) - 1   #since user_choice is index+1, so -1 gives the right indexing
                    if 0 <= chosen_index < len(html_files):
                        return os.path.join(base_path, html_files[chosen_index])
                    else:
                        print("Invalid choice. Please select a valid existing file number.")
                        return get_file_path()
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    return get_file_path()
            else:
                get_new_file_name()
        else:
            get_new_file_name()
    else:
        get_new_file_name()

    return os.path.join(base_path, save_location)  # Return path for new file


"""
CORE FUNCTIONS : [scrapMyWeb() and extract_movie_titles()]
"""
def scrapMyWeb(web_address):
    """
    Use the file path and the file (either newly created or exisiting),
    to write the content of the webpage in it.
    """
    try:
        file_path = get_file_path()
        response = requests.get(web_address)
        response.raise_for_status()
        with open(file_path, "w") as file:
            file.write(response.text)
        print(f"Downloaded webpage content is in: {file_path}\n")
        extract_movie_titles(file_path)
    except requests.exceptions.RequestException as e:
        print("Error downloading webpage:",e)
    except (FileNotFoundError, IOError) as e:
        print("Error handling related file:", e)


def extract_movie_titles(file_path):
    """
    Use BeautifulSoup to read and return the movie titles from the saved HTML file.
    Used inside the scrapmyweb function to return the title names from the saved file. 
    """
    print("\n The Top 50 Best Movies of 2023 Are: \n ")
    try:
        with open(file_path,"r") as file:
            html_doc=file.read()
        soup=BeautifulSoup(html_doc,"html.parser")
        movies=soup.find_all('div',class_="article_movie_title")
        title_count=0
        for movie in movies:
            title_element=movie.find('a')
            if title_element:
                print(title_element.text.strip())
                title_count+=1
                if title_count>=50:
                    break
    except Exception as e:
        print("Error:",e)


"""
ENTRY FUNCTION : [main()]
"""
def main():

    """
    This function serves as the program's main entry point by 
    prompting the user for either to run or exit the program.
    It uses the scrapmyweb() function as its main logic. 
    """
    web_address = "https://editorial.rottentomatoes.com/guide/best-movies-of-2023/"

    user_input = input("Press Enter to begin the program or 'exit' to quit: \n ")
    if user_input.lower() == 'exit':
        exit()
    scrapMyWeb(web_address)
   
if __name__ == "__main__":
    main()






