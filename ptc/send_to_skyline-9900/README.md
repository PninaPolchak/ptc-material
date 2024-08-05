# Send To Skyline ╰┈➤

The service edit the data flight for sending to skyline.\
The data send to external queue, and from there to Skyline.\
Written by python.\
Using docker, rabbitMQ and connect to Azure.

## Installation 🚀

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

✔️ Run rabbitMQ

```bash
docker run -p 5672:5672 -p 15672:15672 rabbitmq 
```

## Usage ✍

Run `python main.py`
