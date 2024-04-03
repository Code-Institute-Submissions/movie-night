import requests
import os
import time
import tempfile
from bs4 import BeautifulSoup


"""
HELPER FUNCTIONS: [get_new_file_name() and get_file_path()]
"""


def get_new_file_name():
    """
    Prompts the user for a new filename or exiting the program.
    If the user wishes to continue, it ensures the filename has the
    .html extension, adding it if necessary.
    """
    while True:
        save_location = input(
            "Enter the desired filename or exit the program (type 'exit'): \n")
        if save_location.lower() == 'exit':
            exit()
        elif not save_location.endswith(".html"):
            save_location += ".html"
        return save_location


def reuse_or_create_html_file():
    """
    Saves the existing HTML files into an empty list.
    Runs when there are HTML files present in the program directory
    which is the Gitpod's workspace path.
    If HTML files are already available, it gives the user the
    possibility to perform operations on them, such as using the
    existing file by giving a number related to the movie or
    creating a new one.
    """
    with tempfile.TemporaryDirectory() as temporary_heroku_dir:
        base_path = temporary_heroku_dir
        html_files = []
        for filename in os.listdir(base_path):
            if filename.endswith(".html"):
                html_files.append(filename)

        if html_files:
            print("PLEASE BE RESPECTFUL, DO NOT SCRAP AGAIN IF A SAVED FILE ALREADY EXISTS!\n")
            time.sleep(1)
            print("Loading....")
            time.sleep(2)
            while True:
                view_existing_files = input("One or more existing (.html) files are found. Do you wish to see them ('y/n'): \n ")
                if view_existing_files.lower() in ('y', 'n'):
                    break  # Valid input received
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
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
                            return reuse_or_create_html_file()
                    except ValueError:
                        print("Invalid input. Please enter a number or 'n'.")
                        return reuse_or_create_html_file()
                else:
                    save_location = get_new_file_name()
                    return os.path.join(base_path, save_location)
            else:
                save_location = get_new_file_name()
                return os.path.join(base_path, save_location)
        else:
            save_location = get_new_file_name()
            return os.path.join(base_path, save_location)
          

"""
CORE FUNCTIONS : [scrapMyWeb() and extract_movie_titles()]
"""


def scrapMyWeb(web_address):
    """
    Use the file path and the file (either newly created or exisiting),
    to write the content of the webpage in it.
    """
    try:
        file_path = reuse_or_create_html_file()
        response = requests.get(web_address)
        response.raise_for_status()
        with open(file_path, "w") as file:
            file.write(response.text)
        print(f"Downloaded webpage content is in: {file_path}\n")
        extract_movie_titles(file_path)
    except requests.exceptions.RequestException as e:
        print("Error downloading webpage:", e)
    except (FileNotFoundError, IOError) as e:
        print("Error handling related file:", e)


def extract_movie_titles(file_path):
    """
    Use BeautifulSoup to read and return the movie
    titles from the saved HTML file. Used inside the
    scrapmyweb function to return the title names from
    the saved file.
    """
    print("\n The Top 50 Best Movies of 2023 Are: \n ")
    try:
        with open(file_path, "r") as file:
            html_doc = file.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        movies = soup.find_all('div', class_="article_movie_title")
        title_count = 0
        for movie in movies:
            title_element = movie.find('a')
            if title_element:
                print(title_element.text.strip())
                title_count += 1
                if title_count >= 50:
                    break
    except Exception as e:
        print("Error:", e)


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
