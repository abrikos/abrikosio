#!/bin/bash
mkdir -p ~/backup
docker exec -it abrikosio-db-1 pg_dump -U postgres abrikosio > ~/backup/abrikosio_$(date +%F).sql
find ~/backup -type f -mtime +10 -delete