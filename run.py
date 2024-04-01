import requests
from bs4 import BeautifulSoup
import os

def scrapMyWeb(web_address):
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
                    return
                else:
                    save_location = input("Enter the desired filename: \n")  
                    if not save_location.endswith(".html"):
                        save_location += ".html" 
    

    except requests.exceptions.RequestException as shownerror:
        print("Error downloading webpage:",shownerror)
    except (FileNotFoundError, IOError) as shownerror:
        print("Error handling file:",shownerror)

