#!/bin/bash
cd /root/mlh-portfolio
tmux kill-server
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
# start tmux session
SESSION=dev
tmux new-session -d -s $SESSION
tmux new-window -t $SESSION:1 -n 'flask_server'
tmux select-window -t $SESSION:1
tmux split-window -h
tmux send-keys "cd /root/mlh-portfolio; source python3-virtualenv/bin/activate; flask run --host=0.0.0.0" C-m