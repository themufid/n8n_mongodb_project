# n8n and MongoDB Integration Project

## Setup

1. Install Docker according to the guide in [Docker Installation Guide](https://docs.docker.com/get-docker/).
2. Make file `docker-compose.yml` with the content:

```yaml
version: '3.1'

services:
  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - 5678:5678
    environment:
      - DB_TYPE=mongodb
      - DB_MONGODB_CONNECTION_URL=mongodb://mongo:27017/n8n
    depends_on:
      - mongo

  mongo:
    image: mongo
    restart: always
    ports:
      - 27017:27017
