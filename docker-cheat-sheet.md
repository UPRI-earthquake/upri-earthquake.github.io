# Docker Cheat Sheet
1. Building a docker image:
    ```bash
    docker buildx build --platform <specified-platform> -t <image-name>:<tag> .
    ```
    - `docker buildx`: This part of the command indicates that we are using the buildx feature of Docker to build the image which is a CLI plugin that extends the capabilities of the traditional docker build command and enables multi-platform builds.
    - `build`: This is the subcommand used to initiate the image-building process.
    - `--platform <specified-platform>`: This flag specifies the target platform for which we want to build the Docker image. The <specified-platform> should be replaced with the target platform/architecture you want to build the image for. For example, it could be linux/amd64, linux/arm64, linux/arm/v7, etc. In this project, we used the linux/arm/v7 architecture to replicate the architecture used by rshake devices.
    - `-t <image-name>:<tag>`: This flag sets the image name and tag for the Docker image being built. <image-name> should be replaced with the desired name for your image, and <tag> should be replaced with the version or tag you want to assign to the image.
    - `.`: The dot . at the end of the command represents the build context. The build context is the current directory or the directory specified in the command. It contains the files and directories needed for building the Docker image. In this case, the Dockerfile should be present in the build context.
2. Running the docker container from a docker-compose file:
    ```bash
    docker compose up
    ```
3. Interacting with the docker container:
    ```bash
    docker exec -it <image-name>:<tag> /bin/sh
    ```
    - `docker exec`: This part of the command is used to execute a command inside a running Docker container.
    - `-it`: These flags make the execution interactive. -i stands for "interactive," which allows you to interact with the shell, and -t allocates a pseudo-TTY, making the shell output more readable.
    - `<container-name>`: This should be replaced with the name or ID of the Docker container where you want to execute the shell. The container must be running for this command to work.
    - `/bin/sh`: This is the command to be executed inside the container. In this case, it runs the shell /bin/sh, providing you with an interactive shell prompt inside the container.
4. Stopping a running container:
    ```bash
    docker compose down
    ```
5. Removing an image:
    ```bash
    docker rm <image-name>
    ```
6. Removing unused networks in Docker:
    ```bash
    docker network prune
    ```
