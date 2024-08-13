# Airflow Docker-Compose

from website [Runnig Airflow in docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#before-you-begin) that will help introduce you to the use of airflow.

```sh
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.3/docker-compose.yaml'
```

```sh
mkdir -p ./dags ./logs ./plugins ./config
```
```sh
echo -e "AIRFLOW_UID=$(id -u)" > .env
```