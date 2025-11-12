build:
  docker build -t menaimg:latest .

deploy: 
  docker stack deploy --with-registry-auth -c stack.yml quinto

rm:
  docker stack rm quinto