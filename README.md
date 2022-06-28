# HotSoup-backend

Backend API for React Native hot food locations app

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

You can view the design document [here](documentation/design.md).

You can view additional resources [here](documentation/resources.md).

### Dependencies

- Describe any prerequisites, libraries, OS version, etc., needed before installing program.
- Docker: https://docs.docker.com/get-docker/

### Installing

#### Linux Ubuntu 20.04 or newer
___

You can install the following required software via the command line (Ctrl + Alt + T).
##### Python 3
Per this [PhoenixNap article](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) for installing Python 3 on Ubuntu 18.04 or 20.04.

###### Check your verion of python:
`python --version`

If the revision level is lower than 3.7.x, or Python is not installed, proceed to the next step.

###### Update and Refresh Repository Links
`sudo apt update`

###### Install Supporting Software
`sudo apt install software-properties-common`

###### Add Deadsnakes PPA
`sudo add-apt-repository ppa:deadsnakes/ppa`


Press enter to continue and then refresh the package lists again:


`sudo apt update`

###### Install Python 3
`sudo apt install python3.8`

###### Verify installation
`python --version`

This should return (3.8.x).

##### Psycopg2
PsycoPG2 is an open-source PostgreSQL driver library for Python. Install per this [Codevoila article](https://www.codevoila.com/post/2/python3-connect-postgresql-with-psycopg2-on-ubuntu).

###### Ensure you have lib-pq-dev installed
`sudo apt-get install libpq-dev`

###### Install Psycopg2 using apt
`sudo apt-get install python3-Psycopg2`

##### Docker
Docker is an open platform for developing, sharing, and running applications. Install Docker from the apt respository per this [DevOpsCube article](https://devopscube.com/how-to-install-and-configure-docker/).

###### Update the apt cache
`sudo apt-get update -y`

###### Add the CPG Key
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

###### Add the Docker apt repository
 ```
 sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"`
```

###### Update the apt cache again
`sudo apt-get update -y`

###### Install Docker components
`sudo apt-get install docker-ce docker-ce-cli containerd.io -y`

###### Verify installation
`sudo docker version`

##### Docker Compose
Docker Compose reads configuration data from the docker-compose.yaml file to spin up a new container in a single command. Install Docker Compose per this [DigitalOcean article](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04docker).

###### Make a new directory
`mkdir -p ~/.docker/cli-plugins/`

###### Download Docker Compose
`curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose`

###### Set permissions so the 'docker compose' command is executable
`chmod +x ~/.docker/cli-plugins/docker-compose`

###### Verify installation
`docker compose version`

This should return v2.3.3


- How/where to download your program
- Any modifications needed to be made to files/folders

### Executing program

- How to run the program
- Step-by-step bullets


Access server at http://localhost:8000

Sample data can be accessed with http://localhost:8000/locations/1

To run:
```
docker compose build
docker compose up
```

To shut down:
docker compose down

## Help

Any advise for common problems or issues.

```
command to run if program contains helper info
```

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
