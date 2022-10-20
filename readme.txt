This project is sourced from https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset

It aims to complete data analysis and visualization through the use of Elastic in a locally-hosted docker container.

In order to gain full use of this Repo you will need an Elastic connection. 
1. Follow the steps to set up the Docker container from here: https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html
2. Create a ".env" file in the top part of the repo. 
3. Fill this file with 
    ELASTIC_USERNAME = <USERNAME>
    ELASTID_PASSWORD = <PASSWORD>
    ELASTIC_CERT = <CERT>