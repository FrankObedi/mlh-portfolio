tmux kill-server
cd /root/mlh-portfolio
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -s flask_app
source python3-virtualenv/bin/activate
flask run --host=0.0.0.0
#tmux detach-client -s flask_app