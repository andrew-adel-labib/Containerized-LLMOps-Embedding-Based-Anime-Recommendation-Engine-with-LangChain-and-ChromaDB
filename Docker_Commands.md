# 🐳 Docker Cheatsheet

This cheatsheet summarizes essential Docker commands for quick reference, grouped by function.

---

## 💻 Core Docker CLIs

These are the most fundamental commands for interacting with Docker.

| Command | Description |
| :--- | :--- |
| `docker run [image]` | Run a command in a new container (= create + start) |
| `docker build` | Build an image from a Dockerfile |
| `docker push` | Push an image to a registry |
| `docker pull` | Pull an image from a registry |
| `docker stop [container]` | Gracefully stop a running container |
| `docker rm [container]` | Remove one or more containers |

---

## 🧰 Container Management

Commands for lifecycle management and listing of containers.

| Command | Description |
| :--- | :--- |
| `docker create [image]` | Create a container but do not start it |
| `docker start [container]` | Start a stopped container |
| `docker restart [container]` | Stop and then start a container |
| `docker kill [container]` | Kill the container (sends SIGKILL) |
| `docker pause [container]` | Suspend the container |
| `docker unpause [container]` | Resume the container |
| `docker wait [container]` | Block until one or more containers stop, then print their exit codes |
| `docker ps` | List **running** containers |
| `docker ps -a` | List **all** containers (running and stopped) |
| `docker logs [container]` | Show the container output (stdout + stderr) |
| `docker top [container]` | Display the running processes of a container |
| `docker diff [container]` | Show the differences with the image (modified files) |

---

## 🧑‍💻 Interacting with Containers

Commands for running commands inside or exchanging data with a container.

| Command | Description |
| :--- | :--- |
| `docker exec [container] [command]` | Run a command in an existing container (useful for debugging) |
| `docker attach [container]` | Attach to a running container (stdin/stdout/stderr) |
| `docker cp [container]:[path] [hostpath]` | Copy files **from** the container to the host |
| `docker cp [hostpath] [container]:[path]` | Copy files **into** the container from the host |
| `docker export [container]` | Export the content of the container (tar archive) |
| `docker commit [container] [image]` | Commit a new docker image (snapshot of the container's changes) |

---

## 🫙 Image Management

Commands for viewing, tagging, and cleaning up local images.

| Command | Description |
| :--- | :--- |
| `docker images` | List all local images |
| `docker rmi [image]` | Delete one or more images |
| `docker history [image]` | Show the image history (list of ancestors) |
| `docker inspect [image]` | Show level-info's (in json format) |
| `docker tag [source_image] [target_image]` | Tag an image with a new name/tag |
| `docker import [tarball]` | Create an image from a tarball |

---

## 🧪 Image Transfer

Commands for moving images to and from a registry or manually.

| Command | Description |
| :--- | :--- |
| `docker login` | Log in to a registry |
| `docker logout` | Log out from a registry |
| `docker search [text]` | Search an image on the official registry |
| `docker save [repo]` | Export an image/repo as a tarball |
| `docker load` | Load images from a tarball |

---

## 🏗️ Dockerfile Instructions

These are commands used *inside* a **Dockerfile** to build an image.

| Instruction | Description |
| :--- | :--- |
| `FROM [image]` | Base image for the build |
| `RUN [args]` | Run an arbitrary command inside the container |
| `CMD [args]` | Set the default command to execute when a container starts |
| `ENTRYPOINT [args]` | Configure a container that will run as an executable |
| `COPY [src] [dst]` | Copy path from the context into the container |
| `ADD [src] [dst]` | Same as COPY, but untars archives and accepts HTTPS URLs |
| `WORKDIR [path]` | Set the default working directory |
| `ENV [name] [value]` | Set an environment variable |
| `USER [name]` | Set the default username |
| `MAINTAINER [email]` | Name of the maintainer (metadata) |
