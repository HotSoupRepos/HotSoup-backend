# HotSoup-backend

Backend API for React Native hot food locations app

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

You can view the design document [here](documentation/design.md).

You can view additional resources [here](documentation/resources.md).


### Dependencies
You will need the following dependencies to run or contribute to this project:
* [Python3](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/)

See the [Dependencies](./documentation/dependencies.md) document for installation steps for these dependencies.

### Installing

Git clone this repo and cd into the directory.

To run:
```
docker compose build
docker compose up -d
```

Access server at http://localhost:8000

Sample data can be accessed with http://localhost:8000/locations

To shut down:
docker compose down


## To run googleAPI.py file

1) To get data to print from google API you must first create your own Googole API key (Eventually we will have a business account this is for testing purposes for now)

2) [GoogleAPI](https://developers.google.com/maps/documentation/embed/get-api-key) Use this link for API steps

3) Once API key is created create a .env file name your key GOOGLE_MAP_API_KEY="YOUR-API-KEY-HERE" **very important do not put your API key in the googpleAPI file
you will risk it being exposed on github! 

4) add .env to the .gitignore file so it is not exposed on github

5) test out by running the command python3 googleAPI.py 

6) data from google api should be printed to console

***in settings for google api make sure maps are enabled for API key to be valid- questions about this can be found at link listed above



## Help

Any advice for common problems or issues.

```
command to run if program contains helper info
```

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
