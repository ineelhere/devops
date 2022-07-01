## Requirements for this project
* A machine with Linux based OS or macOS
* Python 3
* Docker 

For windows users - You can proceed by installing the [Windows Subsystem for Linux](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10)

### Step 1 - Get a cup of coffee and some good music!

Open up your system and chillax with a cup of coffee (or any beverage you prefer) - legend has it, coffee is the best friend of a developer. Also, if this suits your practice, put on some good music too!

(*Oh c'mon, developers are not always boring...*)


![image.png](https://c.tenor.com/HYb5ETTGZDAAAAAC/tony-stark-coding-tony-stark.gif)

### Step 2 - Primary Setup

* Setup your local and remote git repositories. I am using this https://github.com/ineelhere/devops/tree/dockers for this blog. You will find all the codes here. Try not to pull/use this same repository and setup one of your own on GitHub or any other platform that you prefer.
* Linux users install `figlet` with (https://ubunlog.com/en/figlet-banners-ascii-terminal/)
```
sudo apt install figlet
```
* macOS users install `figlet` (https://formulae.brew.sh/formula/figlet) with 
```
brew install figlet
```
* In your project folder, create a python3 virtual environment (https://docs.python.org/3/library/venv.html)
```
python3 -m venv docker-demo
```
*If this is the first time you are creating a virtual environment, you might need to install the tool first. Should you be in trouble, use this command `sudo apt install python3.10-venv`. Remember to change the python version in the command as per your machine *

* Activate the virtual environment you just created 
```
source docker-demo/bin/activate
```


### Step 3 - Install the relevant python packages
We will need to install the `streamlit` python package now. (https://streamlit.io/)
```
pip3 install streamlit
```
Now when you install `streamlit` you will see that it installs other packages as well - which are it's co-dependencies. Now think of  a scenario that you are reading the article in 2023 and a lot has changed already. Lets say there has been some change in the latest package that changes the whole development procedure. So in that case, the codes listed here will definitely not work!


So, how about we list all the packages installed inside this virtual environment with all specific version information?
```
pip3 freeze requirements.txt
```
This `requirements.txt` file will be your single point of reference to reproduce the exact same environment I have been creating now!


### Step 4 - Code Code Code!!!

We are now ready to write the python code that will basically give our webapp a frontend and allow creating the figlets.

* Import the `streamlit` and `os` packages
```
import streamlit as st
import os
```
* Set a title for the webapp - how about **Turn Text to Figlet** ?
```
st.title("Turn Text to Figlet")
```
* Read input text from user
Here we read the text from the user into a variable (which is also named `text`) using the [text_input](https://docs.streamlit.io/library/api-reference/widgets/st.text_input) widget.
```
text = st.text_input("Enter Text:")
```
* Pass that input to the OS and run figlet
So we are using the `os` package to communicate with our linux kernel here. Using the `os` package we run the command to generate the figlet for text provided by user. The figlet hence generated is being displayed to the user on the app using the [text](https://docs.streamlit.io/library/api-reference/text/st.text) element available from `streamlit` library. We will do this only if the user has actually provided some input - which is why the `if` statement has been used here.
```
if text:
    os.system(f'figlet -c {text} > figlet.txt')
    st.text(open('figlet.txt', 'r').read())
```

P.S. A footer has been used using markdown just for bewutification/reference purposes. If this is something you would want to explore further, please refer to [streamlit documentation](https://docs.streamlit.io/library/api-reference/text/st.markdown)

Here is the whole code (to start with...)
Also available on github - https://github.com/ineelhere/devops/tree/dockers
```
import streamlit as st
import os

st.title("Turn Text to Figlet")

text = st.text_input("Enter Text:")

if text:
    os.system(f'figlet -c {text} > figlet.txt')
    st.text(open('figlet.txt', 'r').read())

st.markdown("""
___
[@ineelhere](https://github.com/ineelhere/)
""", unsafe_allow_html=True)
```

![](https://media3.giphy.com/media/lXo8uSnIkaB9e/giphy.gif)

### Step 5 - Docker-ize the app and push to dockerhub

* If you are new to the concepts of `Docker` then get ready to be *blown away (not literally)*
* Docker containers allow you to ship and run your code in an isolated environment exactly configured according to the environment where you actually developed your app. *(and its much more than that!)*
* Now to run containers we need docker images - and to build docker images, we need to have Dockerfile, which actually has the *instructions* of what has to be done once the container containing your code is run.

Here is the Dockerfile for this project (you will need to change the github sources for building an image with **your** code)
```
#we will use ubuntu as the base image as available at https://hub.docker.com/_/ubuntu
FROM ubuntu:latest

# installing git and figlet
RUN apt-get update \
    && apt-get install -y git \
    && apt-get install -y figlet;

# clone the github repo and set up the env with the required packages
RUN apt-get install -y python3-pip \
    && git clone -b dockers https://github.com/ineelhere/devops.git \
    && pip3 install -r ./devops/requirements.txt;

# expose port 8501
EXPOSE 8501

# mention the entrypoint and command
ENTRYPOINT ["streamlit", "run"]
CMD ["./devops/app.py"]
```

Now build the image by the command
```
docker build -t figletapp .
```
Once the above step is complete, create a [DockerHub](https://hub.docker.com/) account with a username and password. Lets assume your username is "ineelhere" 

Then create a `new repository`. Lets say you named it "figletapp". So the repository name becomes `ineelhere/figletapp` 

On your PC, using the CLI, login with the command
```
docker login
```
Now that you are logged in through your CLI, you will have to tag the local image to the remote repository and basically push the local image to remote destination. Follow these two commands - 
```
docker tag  figletapp:latest ineelhere/figletapp:v1
docker push ineelhere/figletapp:v1
```

So now on your DockerHub account you will see an image has been pushed and ready to be used - just like https://hub.docker.com/repository/docker/ineelhere/figletapp

You can `pull` this image on your system or any destination with the command
```
docker pull ineelhere/firgletapp:v1
```
And run the app with the command 
```
docker run ineelhere/figletapp:v1
```
* So this was a short journey to get started with an expedition involving development and shipping of your code. This might seem very overwhelming now, but trust me, you've got it! Just keep going! :)

* Do read https://www.docker.com/why-docker/ and get a clearer picture.
* For complete guide to building docker images, refer to https://docs.docker.com/engine/reference/builder/

### Step 6 - Enjoy!
That's all for now, folks. Enjoy coding and enjoy life - yes, coders have a life and they also enjoy it ;)

![](https://64.media.tumblr.com/8642075103c54ee6eae9bb3808377121/tumblr_noenylQkFh1s8njeuo1_500.gifv )



# Docker Basics

| COMMANDS                                                                              | DESCRIPTION                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docker images                                                                         | list the docker images                                                                                                                                                                                                                                                                      |
| docker version                                                                        | check docker version                                                                                                                                                                                                                                                                        |
| docker info                                                                           | check docker info - also gives container and machine info                                                                                                                                                                                                                                   |
| docker container ls                                                                   | list containers                                                                                                                                                                                                                                                                             |
| docker run -it image\_name bash                                                       | run the docker image interactively with bash                                                                                                                                                                                                                                                |
| docker container run --publish 80:80 nginx                                            | Downloads nginx image and runs it on port 80. Short notation is -p. Publishing ports is always in HOST:CONTAINER format.                                                                                                                                                                    |
| docker container run --publish 80:801 --detach --name ineelhere nginx                 | downloads nginx image, names the container as "ineelhere" and runs it on port 81. By running in detached mode, we are able to have access to our command line when the container spins up and runs. Without it, we would have logs constantly fed onto the screen.                          |
| docker rm -f $(docker ps -aq)                                                         | removes or deletes all active containers                                                                                                                                                                                                                                                    |
| sudo lsof -i -P -n | grep LISTEN                                                      | check/list open ports                                                                                                                                                                                                                                                                       |
| sudo ss -tulpn | grep LISTEN                                                          | check/list open ports                                                                                                                                                                                                                                                                       |
| sudo kill $(sudo lsof -t -i:3000)                                                     | Kill/stop/close the open port                                                                                                                                                                                                                                                               |
| sudo kill $(sudo lsof -t -i:80)                                                       | Kill/stop/close the open port                                                                                                                                                                                                                                                               |
| docker container run --publish 80:80 --detach nginx                                   | downloads nginx image and runs it on port 80, but on the background                                                                                                                                                                                                                         |
| docker container ls                                                                   | list all active/running containers                                                                                                                                                                                                                                                          |
| docker container ls -a                                                                | list all containers - running and exited/stopped containers                                                                                                                                                                                                                                 |
| docker container ls --all                                                             | list all containers - running and exited/stopped containers                                                                                                                                                                                                                                 |
| docker container ls -aq                                                               | list all containers - running and exited/stopped containers - but only shows the container ids, excluding other details (quiet mode)                                                                                                                                                        |
| docker container logs conatiner\_id/name                                              | gives the logs for a specific container                                                                                                                                                                                                                                                     |
| docker container kill conatiner\_id/name                                              | kill the specific container                                                                                                                                                                                                                                                                 |
| docker container rm -f conatiner\_id/name                                             | deletes a container forcefully (ie, running container can also be deleted with this command without first stopping it)                                                                                                                                                                      |
| docker container run -p 80:80 -d nginx<br>docker container run -p 8080:80 -d nginx    | just because the containers are both listening on port 80 inside (the right number), there is no conflict because on the host they are published on 80, and 8080 separately (the left number).                                                                                              |
| docker container top conatiner\_id/name                                               | shows details of the processes running inside the container                                                                                                                                                                                                                                 |
| docker container stats                                                                | shows performance stats for all containers                                                                                                                                                                                                                                                  |
| docker container inspect conatiner\_id/name                                           | shows details of one container config - and we get back a JSON array of all the data about how this container was started.                                                                                                                                                                  |
| docker container run -it                                                              | start new container interactively                                                                                                                                                                                                                                                           |
| docker container exec -it                                                             | run additional commands in existing container                                                                                                                                                                                                                                               |
| docker container inspect --format '{{.NetworkSettings.IPAddress}}' container\_name/ID | shows the IP address for the container                                                                                                                                                                                                                                                      |
| docker network ls                                                                     | show networks<br>(bridge = default docker virtual network, which is NAT'ed behind the host IP)<br>(host = gains performance by skipping virtual networks but sacrifices the security of container model)<br>(none = removes eth0 and only leaves you with localhost interface in container) |
| docker network inspect network\_name                                                  | shows details of the network config in JSON                                                                                                                                                                                                                                                 |
| docker network create network\_name                                                   | create a network<br>(note - the network driver is builtin or some 3rd party extension that gives you virtual network features)                                                                                                                                                              |
| docker container run --detach --name new\_nginx --network ineelhere nginx             | run the nginx container in the network ineelhere - use "docker network inspect ineelhere" command to see the contaioners section - it must be updated with the name "new\_nginx"                                                                                                            |
| docker network connect ineelhere nginx                                                | connect container "nginx" to network "ineelhere". Use command "docker container inspect nginx" to see the change.                                                                                                                                                                           |

# Docker Errors and Fixes | ineelhere
**These errors were found on a ubuntu system and hence the fixes. The same fix might not be applicable to all OS/platforms**

* Got permission denied while trying to connect to the Docker daemon socket 
  - run `sudo chmod 666 /var/run/docker.sock` 
  - Enjoy!
* docker: Error response from daemon: driver failed programming external connectivity on endpoint elastic_bartik (754d6c0dd38315b4ccf410e1f318545dacefe1eabd336a7d2f6f1a8e40ca3d6a): Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use. 
  - run `sudo lsof -i -P -n | grep LISTEN` or `sudo ss -tulpn | grep LISTEN` | This lists the open ports
  - run `sudo kill $(sudo lsof -t -i:<port_you_want_to_close>` | From the above list, identify the port and run this code!
  - Enjoy!

* [OCI runtime exec failed: exec failed: container_linux.go:344: starting container process](https://stackoverflow.com/questions/55378420/oci-runtime-exec-failed-exec-failed-container-linux-go344-starting-container)

## Basic hands on - 1

* docker container run -d -p 3306:3306 --name db -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql 
* docker container logs db
* look for MYSQL password generated
* docker container run -d --name webserver -p 8088:80 httpd
* docker ps
* docker container run -d --name proxy -p 80:80 nginx
* docker ps
* visit http://localhost/ (so that you know it works!)
* curl localhost:80 (basically the above step, but on terminal)
* cleanup - docker container stop db proxy webserver
* docker ps -a (look for status = exited)
* docker container ls -a (same as above)
* remove the containers - docker container rm proxy webserver db

<hr><br>

*explanations will be added later*
