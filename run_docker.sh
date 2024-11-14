echo killing old docker processes
docker-compose down -v --remove-orphans
docker volume ls | awk '{print $2}' | xargs -I % docker volume rm %
sudo rm -r ./postgres-data
sudo rm -r /postgres-kong

echo delete database volume
docker volume rm flask-on-docker_postgres_data

echo building docker containers
docker-compose up --build -d
