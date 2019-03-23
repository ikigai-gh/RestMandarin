## Users & post REST api

### Run instructions:
In the directory `RestMandarin` simply run the following: 
```bash
docker-compose up -d
```

And to fill out the database with fake data:
```bash
docker exec -it <container_id> psql --file=postgres/data/db_dump.sql
```