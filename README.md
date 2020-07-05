**About**

Wilio is a simple tool written in python, which delievers weather data from various sources right at your terminal.
**How it works**
## Technical
Wilio is divided into 4 parts, the model, the repo, the data source and the config.
## The Config
The config stores all the default variables used in the app and holds references to the app settings including the default graphics.
The config takes care of creating the app's folder & the default json file whiAbout

Wilio is a simple tool written in python, which delievers weather data from various sources right at your terminal. How it works
Technical

Wilio is divided into 4 parts, the model, the repo, the data source and the config.
The Config

The config stores all the default variables used in the app and holds references to the app settings including the default graphics. The config takes care of creating the app's folder & the default json file which acts as the local data source for the app.
The model

This is your plain old pojo which holds the data read from the internet / gotten locally from the json file
The data source

Wilio has two data sources namely: The network/ remote data source and local data source. The remote ds fetches data from the internet, whereas the local ds fetches locally stored data from the .json file.
The repo

The repo exposes the data to the app. That is to say, the repo provides the data be it locally or remotely fetched to the whole app. In case the app fails to fetch data remotely, the repo will resort to fetch the data locally, if it does not exist then the user will be notified. Wilio uses your ip address to get your current location however, in the event that you are not connected to the internet, wilio will resort back to the default location which is nairobi.

We recommend that you open the art folder to see the how wilio works and how the expected output looks like
Usage

    Clone the repo
    Go to your terminal switch to the folder containing the repo specifically the main.py.
    Connect to the internet
    In your terminal type $ python3 main.py
Issues, Contributions

The tool is far from perfect so for any issues or contributions just ping me at: gibsonruitiari@gmail.com < >
TODO

    Include tests .
    Include a command which shows the user the acceptable locations.
ch acts as the local data source for the app.
## The model
This is your plain old pojo which holds the data read from the internet / gotten locally from the json file
## The data source
Wilio has two data sources namely: The network/ remote data source and local data source. The remote ds fetches data from the internet,
whereas the local ds fetches locally stored data from the .json file. 
## The repo
The repo exposes the data to the app. That is to say, the repo provides the data be it locally or remotely fetched to the whole app.
In case the app fails to fetch data remotely, the repo will resort to fetch the data locally, if it does not exist then the user will be notified.
Wilio uses your ip address to get your current location however, in the event that you are not connected to the internet, wilio will resort back to
the default location which is nairobi.

*We recommend that you open the art folder to see the how wilio works and how the expected output looks like*

---

## Usage



1. Clone the repo
2. Go to your terminal switch to the folder containing the repo specifically the main.py.
3. Connect to the internet  
4. In your terminal type $ python3 main.py  


---

## Issues, Contributions

The tool is far from perfect so for any issues or contributions just ping me at: gibsonruitiari@gmail.com <* *>


---

## TODO


1. Include tests .
2. Include a command which shows the user the acceptable locations.

