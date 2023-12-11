# fastapi-comics-ratings

Application with comics/ratings API, registration API and tests.
Used stack: *FastAPI*, *PostgreSQL*, *asyncio*, *pytest*.

## Install

Install `fastapi-comics-ratings` from source:

    git clone https://github.com/omka0708/fastapi-comics-ratings
    cd fastapi-comics-ratings
    
You should have `.env` file at the */fastapi-comics-ratings* folder.

Environment file `.env` should contain:
    
    DB_USER=<database user>
    DB_PASS=<database password>
    DB_HOST=comics-db
    DB_PORT=5432
    DB_NAME=<database name>
    PGADMIN_EMAIL=<pgadmin email>
    PGADMIN_PASSWORD=<pgadmin password>
    SECRET_AUTH=<some string>

## Run app

Run this command at the working directory */fastapi-comics-ratings*:

    docker compose up -d --build

Then you should import the database dump `data.sql`, which stores everything for testing the application.

    cat data.sql | docker exec -i comics-db psql -U root "dbname=db"

> Don't use Git Bash on windows for this command, use PowerShell.

## Run tests

Run this command for test entrypoints (only after importing `data.sql`!):

    docker exec -i comics-app pytest -vv -W ignore::DeprecationWarning

## Documentation

You can see documentation at:

    GET localhost:8000

It will redirect you to API documentation. 
