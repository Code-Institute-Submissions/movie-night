MOVIE NIGHT

This Python script helps you retrieve and display the top 50 best movies of 2023.

## How to use the program

1. The program will prompt you to either press Enter to begin or type "exit" to quit.

2. If you choose to continue, it will then:

    a. Check if a previously downloaded HTML file exists.

    b. If a file exists, it will ask you if you want to use it or create a new one.

    c. If no file exists, or you choose to create a new one, it will download the webpage content and save it as a new HTML file.

Finally, it will parse the saved HTML file and display the top 50 movie titles

## Features

This script offers the following functionalities:

1. User-friendly prompts for starting the program and choosing file options.
2. Ability to reuse previously downloaded webpage content (if available).
3. Downloading the webpage content from a specified URL if no saved file exists.
4. Parsing the downloaded HTML using BeautifulSoup to extract movie titles.
5. Displaying the top 50 extracted movie titles.

### Future features

1. Implement error handlings for situations when target website is changed.
2. Ability to save the extracted movie title to a file.

## Data Model

The script doesn't use a complex data model. It relies on:

1. User input to choose between existing and new files.
2. Downloaded or existing HTML file to store the webpage content.
3. In-memory data structures (lists) to temporarily hold extracted movie titles.

## Testing

1. The code has been tested locally on my machine where local directory was used. Instead of giving an static location, i have used 
   command .getcwd to get the working directory.
2. The code is also tested on GitPod where i have replaced the .getcwd command by a static location of the workspace.

## Bugs

1. No known critical bugs have been identified. However, as with any web scraping script, there's a chance the script might break if the target webpage structure changes significantly.

2. To prevant this, there is already a saved .html file in the same directory which will enable the user to still get the movie title names.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
1. Fork or clone this repository.
2. create a new Heroku app.
3. Set the buildblocks to python and NodeJS in that order.
4. click on deploy.

## Credits

1. This script utilizes the following external libraries:
    a. requests: Used for downloading webpage content.
    b. BeautifulSoup: Used for parsing HTML content.
2. Code Institute for the deployment environment. 
3. Google to search for knowing the common commands that enable web scraping. 
4. The code uses some of the already exisitng and highly common code snippet used for web scraping such as:
    1. requests.get(web_address) ----> This uses the highly common requests library and its get() method.
    2. BeautifulSoup(html_doc,"html.parser") ----> Another highly common class called 'Beautiful soup'.
    3. with open() ----> Uses commonly used with and open function for automatic closing of file and uses 'mode' argument
                        of the function to either read or write the named file. 

