<h1 align="center">BairesDev News Project</h1>
<h1 align="center">
    <a href="https://www.docker.com/get-started">🔗 Docker compose project</a>
</h1>



# Table of Contents

1. [About](#about)
2. [Setup](#setup)
3. [Running](#running)


## About

BairesDev News Project was developed using:
- Docker Compose
- Dokcer
- Python/Django
- Angular
- SQLite3

It retrieves feed from:
- https://it.mashable.com/feed.xml
- https://techcrunch.com/feed/
- https://www.theverge.com/rss/index.xml

Every feed is stored to the database (SQLite3).
These news can be access with an Angular Project.

The project uses a Docker compose with two services:
- angular (front-end)
- api (back-end)

## Setup

```bash
# Clone the repository
$ https://github.com/rafavolpato/news-project.git
```

## Running

```bash
# Enter the project directory
cd news-project
# Run the docker-compose file
$ dokcer-compose up

Open the browser go on: http://localhost
```