Python/FastAPI application
Project structure:

├── compose.yaml
├── Dockerfile
├── requirements.txt
├── app
    ├── main.py
    ├── config
        ├──db.py
        ├──scrap_data_insert_db.py

compose.yaml will create the docker container for FAST-API, MYSQL and Selenium

Deploy with docker compose

docker-compose up -d --build
Expected result
Listing containers must show one container running and the port mapping as below:

$ docker ps

C:\Users\saras\OneDrive\Documents\docker\fast_api\app>docker ps -a
CONTAINER ID   IMAGE                                    COMMAND                  CREATED       STATUS          PORTS                           NAMES
4d63429e5dc1   selenium/node-chrome:3.141.59-titanium   "/opt/bin/entry_poin…"   4 hours ago   Up 4 hours                                      fast_api-chrome-1

8bdc06c02fc3   fast_api-api                             "/start.sh"              4 hours ago   Up 4 hours                                      fastapi-application
36143a492fbb   selenium/hub:3.141.59                    "/opt/bin/entry_poin…"   4 hours ago   Up 4 hours    0.0.0.0:4442-4444->4442-4444/tcp  selenium-hub
957dee43b778   mysql                                    "docker-entrypoint.s…"   4 hours ago   Up 4 hours    3307/tcp, 33060/tcp               fast_api-db-1
aa5c17d8b194   33ce09363487                             "python3"                3 days ago    Up 4 hours  

After the application starts, navigate to http://localhost:8000 in your web browser and you should see the following json response:

"Welcome to fast api demo. Try using /docs at the end to do CRUD operation"


For Stopping and removing the containers

$ docker compose down
