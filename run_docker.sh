echo killing old docker processes
docker-compose down -v --remove-orphans
docker volume ls | awk '{print $2}' | xargs -I % docker volume rm %
sudo rm -r ./postgres-data
sudo rm -r ./postgres-kong
sudo rm -r ./prometheus-data
sudo rm -r ./grafana-data


echo delete All volumes volume
docker volume rm flask-on-docker_postgres_data

echo building docker containers
docker-compose up --build -d
