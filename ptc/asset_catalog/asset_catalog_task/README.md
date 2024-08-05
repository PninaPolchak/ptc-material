# Asset Catalog 🎬

This program will simulate the storing assets in a distributed system.\
The program upload assets from any number of remote clients to a centralized server for persistent storage.\

- The client run as a CLI tool on a remote machine,(more than 1 client can be active at any given time).
- The client watch the cache for file changes and upload the changed files to the remote server.
- The client not change or move the files from the cache at any point.
- No file be uploaded twice (even when multiple clients are running).
- The client able to recover state from a previous execution.\

The code written in python.🐉\
Run on docker.🐋

## Installation ⬇️

✔️ Clone to code.

✔️ Navigate into project directory.

✔️ Run the service by running :

Build  image

```bash
docker build . -t < image_name > 
```

Run docker container  

```bash
docker run -it --entrypoint bash -v ${pwd}:/app < image_name >
```

✔️ Run the server by running `python server.py`

## Usage ✍

Run `python src/main.py <path_to_file>`
