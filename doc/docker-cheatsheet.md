Developer Guide\: Docker Cheatsheet
======================================

## Docker Cheat Sheet
Docker containerization is used heavily in the EarthquakeHub software suite for both development and deployment. The main reason for this is that it provides a uniform environment among developers (ie. Linux vs Windows vs macOS) and across deployment servers (ie. one container is run on a raspberry pi while another is run on an actual server). The following are a summary of important details to get you up to speed with using docker.

## Concept
To have a better understanding of the commands, it is important to have the correct mental model of what containerization is. A sufficient model is to think of it as running a computer that is inside your computer, similar to how you can run a Windows virtual machine within your Linux computer. In this context we call the virtual machine the "container" and your real computer as the "host."

To be able to create a container, we first have to define what OS it runs, what packages it initially comes with, and other configurations. You can think of this to be similar to an installer disk/image of an operating system (ie Windows XP installer disk), which you can feed into your computer to create as many virtual machines as you want. In the context of containerization, we call this an "image," specifically in docker, an image is defined in a Dockerfile. The Dockerfile is the source code of the image and is where the configurations for the image are defined.

Once you have a `Dockerfile`, which you can _build_ into an `image`, and from which you can create `container` instances, you can now run these containers on your host. This is similar to powering up a virtual machine. Depending on the Dockerfile or the command you used to run the container, certain programs can be made to run inside the container. These can be a nodejs server, a terminal prompt, or as simple as a short program that prints <a href="https://hub.docker.com/_/hello-world" target="_blank">"Hello from Docker!"</a>. An important concept to realize is that  you can enter a running container and perform normal terminal commands from inside it (see `docker exec .. sh` below), similar to how you can perform tasks from within a virtual machine.

Finally, when you are running microservices (ie. a set of containers that each runs a single program for you system, for instance, one is running only the database, another is the HTTP server, while another is a data processing engine), it can be a challenge to orchestrate and manage these individual containers. This is where `docker compose` comes in. Specifically, you can define a set of services inside `docker-compose.yml` file. And in this file, you can set <a href="https://docs.docker.com/network/" target="_blank">how they communicate</a>, <a href="https://docs.docker.com/storage/volumes/" target="_blank">how they can share file storages</a>, and etc. By doing this, you can essentially treat the multiple containers as a group, instead of manually running and connecting each other containers. The convenience commands to interact with the group of containers defined in the `docker-compose.yml` file all begin with `docker compose`. In contrast, when interacting with only a single container, single image, etc, the command only begines with `docker`.

## Docker commands
1. `docker build -t <image-name> <path-to-dockerfile>`
   - Build a Docker image from the specified Dockerfile at the given path and tag it with the provided image name.

2. `docker buildx build --platform <platform-name> -t <image-name> <path-to-dockerfile>`
   - Build a platform-specific Docker image from the specified Dockerfile, targeting the given platform name, and tag it with the provided image name.

3. `docker run --name <container-name> <image-name>`
   - Create and runs a new container from the specified image, giving it the provided container name.
4. `docker run -it --rm <image-name>`
   - Create a default-named container, run it interactively (you'll be inside the container), and delete it once done (when you press ctrl+c).

5. `docker exec -it <container-name> sh`
   - Enter the running container's shell interactively (e.g., bash, sh) for manual debugging or running commands inside the container.

6. `docker inspect <container-name>`
   - Display detailed information about the specified container, including its configuration and network settings.

7. `docker inspect <image-name>`
   - Display detailed information about the specified image, including its layers, tags, and associated containers.

8. `docker logs -f <container-name>`
   - Displays the real-time logs of the specified container, and the `-f` flag follows the log output as it continues.

9. `docker ps -a`
   - Lists all containers in the system, both running and stopped, along with their respective details.

10. Listing
    - `docker image ls`
       - Lists all available Docker images.
    - `docker volume ls`
       - Lists all Docker volumes.
    - `docker network ls`
       - Lists all Docker networks.

11. Removing
    - `docker rm <container-name>`
       - Removes the specified container.
    - `docker rmi <image-name>`
       - Removes the specified image.
    - `docker volume rm <volume-name>`
       - Removes the specified volume.
    - `docker network rm <network-name>`
       - Removes the specified network.

12. `docker pull <image-name>`
    -  Download an image from a remote repository (ie. ghcr.io) defined in the image name. This is in contrast to building it from source, ie a local Dockerfile.

13. `docker push <image-name>`
    - Upload a locally built image to a remote repository. You may need to <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry" target="_blank">authenticate to the remote repository, such as in ghcr.io</a>.


## Docker Compose commands
All these commands assume that you are currently in a directory containing a docker-compose.yml
1. `docker compose up`
   - Builds or pulls the required images, creates and starts the containers defined in the docker-compose file.

2. `docker compose down`
   - Stops and removes all containers, images, and networks defined in the docker-compose file.

3. `docker compose ps -a`
   - Lists all containers defined in the docker-compose file, along with their respective details.
