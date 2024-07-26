#!/bin/bash
cd /root/mlh-portfolio
git fetch && git reset origin/main --hard

# Spin containers down
docker compose -f docker-compose.prod.yml down

# build the new changes
docker compose -f docker-compose.prod.yml up -d --build
