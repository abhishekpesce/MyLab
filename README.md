# MyLab
this is how i install snowflake operator in airflow.

to build the airflow i used the official docker-compose file.

Once airflow was up and running using offical docker-compose file 

i created new Dockerfile and requiremnet.txt file

the content of Dockerfile 

FROM apache/airflow:2.2.3
COPY requirements.txt .
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt

and the content of requirement file is 

apache-airflow-providers-snowflake

then i build new docker image using below command

docker build . --tag extending_airflow:latest

once new image was created i changed the docker-compose file to point to new image 

from 
image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.2.3}

to 

image: ${AIRFLOW_IMAGE_NAME:-extending_airflow:latest}

then i pushed the changes to repo.

i rebuild the new container using the new image

docker-compose up --build -d

once my container was running i logged into webserver to check for snowflake operator

pip list | grep snowflake

there it was 

apache-airflow-providers-snowflake       2.6.0
snowflake-connector-python               2.7.6
snowflake-sqlalchemy                     1.3.3

------------------------------
