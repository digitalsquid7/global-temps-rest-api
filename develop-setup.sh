#!/bin/zsh

if [[ $(docker ps -a | grep global_temps_sql) ]]; then
    docker rm -f global_temps_sql
fi

docker run -d \
  -e "ACCEPT_EULA=Y" \
  -e "SA_PASSWORD=AdminPassword!" \
  -p 1433:1433 \
  --name global_temps_sql \
  --hostname global_temps_sql \
  mcr.microsoft.com/mssql/server:2022-latest
