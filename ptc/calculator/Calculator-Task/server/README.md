# server

The calculator server was written by java.♨️

Type commands below:

- Navigate to server directory.

    `cd < server directory >`

- Run java container with maven.

    `docker run -it --entrypoint bash --name java_server -v ${PWD}:/app -p 8080:8080  maven:3-openjdk-17`

- Install *Dev Container* extension.

- Connect to the container  
type F1 - Dev Container: Attach to Running Container...\
choose the container  *java_server*.

In terminal

- Run maven by *pom.xml*  `mvn package`

- Run the server
 `mvn spring-boot:run`

In browser

- Check the server, send request <http://localhost:8080/api?exercise=${16-4/3}>\
you get result *4.0* ? excellent! 👏 you can continue to the client. ➡
