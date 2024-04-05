# Purpose

- **Problem Statement:** Finding the right movie for a group of people can be challenging due to conflicting tastes and the vast number of options. Additionally, discovering interesting new movies within specific genres or based on mood can be time-consuming, especially when looking for the year's best releases.

- **Solution:** This project provides a command-line tool that streamlines movie selection and discovery. It focuses on curating a list of the top 50 best movies from the previous year (2023), leverages web scraping to gather movie information, offers filtering/selection options, and presents the results in a user-friendly format.

- **Key Objectives:**

   * **Efficiency:** Make the movie selection process faster and more enjoyable, specifically for highlighting top releases.
   * **Discovery:** Help users find acclaimed movies from the previous year.


# UX Design

Since the application is currently a simple command-line based, the UX focuses only on clarity of messages, ease of use:

- **Intuitive Commands:** Provide a clean and clear interface and messages to guide users through filtering and selection.
- **Informative Prompts:** Provide clear prompts to help users understand what input is expected at each stage.
- **Error Handling:** Display helpful error messages if the user enters invalid input or encounters unexpected issues.
- **Progress Indicators:** Let the user know the program is working (especially when fetching data from websites) to prevent confusion about whether it's running or stuck.


# Features

### Function Overview

The project currently contains five core functions that work together to achieve its movie selection and discovery goals:

- **`get_new_file_name()`**
    * **Purpose:** Interacts with the user to obtain a desired filename for storing scraped movie data.
    * **Functionality:** Prompts the user for input, potentially includes validation to ensure a valid filename is provided.

- **`reuse_or_create_html_file()`**
    * **Purpose:** Provides flexibility in managing scraped data by allowing the user to either reuse an existing HTML file or create a new one. 
    * **Functionality:**  
        *   Checks for existing HTML files. 
        *   Presents the user with options to view existing files and select one or create a new file. 

- **`scrapMyWeb()`** 
    * **Purpose:**  Orchestrates the core scraping process and interaction with Google Cloud Storage.
    * **Functionality:**
        *   Fetches the webpage containing movie information.
        *   Uploads the downloaded HTML contents to a  Google Cloud Storage bucket.
        *   Calls the `extract_movie_titles` function to process the stored data.

- **`extract_movie_titles()`**
    * **Purpose:**  Isolates and extracts the actual movie titles from the larger HTML document.
    * **Functionality:**
        *   Accesses the HTML file stored in Google Cloud Storage.
        *   Utilizes the BeautifulSoup library to parse the HTML structure. 
        *   Implements specific logic to identify and retrieve the relevant movie title elements.

- **`main()`**
    * **Purpose:** Acts as the entry point to application, coordinating the execution of other functions.
    * **Functionality:** 
        *   Contains the 'url' of the website that is used for Scraping.
        *   Prompts the user either to start the program or exit.
        *   Initiates the web scraping and movie title extraction process.

### Existing Features

- **Start Up Screen**

![](readme_assets/startup.png)

The startup screen prompts the user to either press 'Enter' to start the program or input 'exit' to quit. 

- **User pressed 'Enter' and a existing html file is found**

![](readme_assets/press-enter01.png)

When user presses 'Enter' and existing .html files are found in the same directory, the user can choose to view them.

- **User pressed 'Enter' and no existing html files are found**

![](readme_assets/press-enter02.png)

When user presses 'Enter' and existing .html files are not found in the same directory, the user can choose a file name to scrap the web content to.

- **Viewing existing files**

![](readme_assets/viewfiles.png)

When existing files are found in the program directory, the user if chooses 'y', can view those files.

- **Exiting**

![](readme_assets/exit.png)

The user on several stages during the entire program has been given the option to exit by simply typing 'exit'.


# Flowchart


# Technologies

## Languages

## Program, frameworks , libraries

# Data Model


# Deployment
# Testing
## Manual Testing and debugging
# Credits

