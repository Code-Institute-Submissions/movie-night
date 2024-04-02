import requests
from bs4 import BeautifulSoup
import os
import time


"""

This Python script scrapes movie titles from a webpage "Best Movies of the Year 2023" webpage
and filters the list to give the 50 best movies out of a list of more then 150 
and saves the downloaded HTML content. 

It offers the user choices to:
1. Use an existing .html file containing the desired webpage content (for in case,if user ran the script twice).
2. Create a new .html file by downloading the webpage content from the provided URL.

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


def scrapMyWeb(web_address):
    """
    Downloads the webpage content from the provided URL and saves it to an HTML file and extract movie title from the file using its path .
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


def get_new_file_name():
    """
    Prompts the user for a new filename and ensures it has the .html extension.
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
    Checks for existing HTML files, prompts user for choice or new filename,
    and returns the file path.
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
                    chosen_index = int(user_choice) - 1
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



def extract_movie_titles(file_path):
    """
    Use BeautifulSoup to read and return the movie titles from the saved HTML file.
    """
    print("\nThe Top 50 Best Movies of 2023 Are:\n")
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


web_address = "https://editorial.rottentomatoes.com/guide/best-movies-of-2023/"
scrapMyWeb(web_address)




