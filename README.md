# LangChain + Fast API

## Installation

| dependency | version |
| ---------- | ------- |
| python     | 3.12.2  |

### Setup

```shell
$ poetry shell
```

### Start Milvus Server

```shell
$ cd .docker
$ docker-compose up -d
```

### Start API Server

```shell
$ uvicorn src.main.main:app --reload
```

###

| App     | URL                        |
| ------- | -------------------------- |
| Swagger | http://localhost:8000/docs |
| attu    | http://localhost:13000     |
