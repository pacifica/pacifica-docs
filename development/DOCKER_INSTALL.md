# Install using Docker

This will go over the configuration you should need to setup and start Pacifica using docker-compose.
This is intended to be used by developers who want to start building against the services Pacifica provides.
There are volumes and services you will need to enable to get the system working.

## Configuration of Docker

The docker service is very under provisioned when it comes to memory and CPU for Pacifica usage.
At a minimum you will need to configure the docker service to use 4 CPUs and 8Gb of memory.
Also you will need to give docker permissions to create local volumes and map them if you want
persistent metadata if the services need to be rebuilt.

Documentation on docker volumes is (here)[https://docs.docker.com/storage/volumes/] and changing
memory and CPU documentation is (here)[https://docs.docker.com/config/containers/resource_constraints/]

## Bringing up the Services

Running docker-compose from the core pacifica repository will get the services started in docker.

```
git clone https://github.com/pacifica/pacifica
cd pacifica
docker-compose up
```
