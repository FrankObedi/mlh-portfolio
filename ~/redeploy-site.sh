#!/bin/bash
cd /root/mlh-portfolio
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# renable services
systemctl daemon-reload
# Restart myportfolio service 
systemctl restart myportfolio