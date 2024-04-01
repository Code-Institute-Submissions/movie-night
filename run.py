import requests
from bs4 import BeautifulSoup
import os

"""

This Python script scrapes movie titles from a Rotten Tomatoes "Best Movies of the Year" webpage
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
    Downloads the webpage content from the provided URL, saves it to an HTML file.
    In case user runs the code twice, it prompts the user to either use the same html file,
    or create a new one in order to make sure that the user has already run the file twice.  

    """

    try:
        current_directory=os.getcwd()
        html_files=[]
        for filename in os.listdir():
            if filename.endswith(".html"):
                html_files.append(filename)
        if html_files:
            view_existing_files=input("One or more existing (.html)files are found. Do you wish to see them ('y/n'): ")
            if view_existing_files.lower()!='n':
                print("Existing HTML files in the current directory are:\n")
                for index,exisitng_files in enumerate(html_files):
                    print(f"{index+1}.{existing_files}")
                user_choice=input("\nUse existing file (enter number) or create new (enter 'n'): ")
                if user_choice.lower()!='n':
                    file_path=os.path.join(current_directory,html_files[int(user_choice)-1])
                    extract_movie_titles(file_path)
                    return
                else:
                    save_location=input("Enter the desired filename: \n")  
                    if not save_location.endswith(".html"):
                        save_location+=".html" 
            else:
                save_location=input("Enter the desired filename: \n")  
                if not save_location.endswith(".html"):
                    save_location+=".html"
        else:
                save_location=input("Enter the desired filename: \n")  
                if not save_location.endswith(".html"):
                    save_location+=".html"
        
        response = requests.get(web_address)
        response.raise_for_status()
        with open(save_location, "w") as file:
            file.write(response.text)
      
        print(f"Downloaded webpage content saved to: {save_location}\n")
        extract_movie_titles(save_location) 
   
    except requests.exceptions.RequestException as shownerror:
        print("Error downloading webpage:",shownerror)
    except (FileNotFoundError, IOError) as shownerror:
        print("Error handling file:",shownerror)



def extract_movie_titles(file_path):

    """
    Use BeautifulSoup to read and return the movie titles from the saved HTML file.
    """

    print("\nThe Top Best Movies of 2023 Are:\n")
    try:
        with open(file_path,"r") as file:
            html_doc=file.read()
        soup=BeautifulSoup(html_doc,"html.parser")
        movies=soup.find_all('div',class_="article_movie_title")

        for movie in movies:
            title_element=movie.find('a')
            if title_element:
                print(title_element.text.strip())
    except Exception as e:
        print("Error:",e)
