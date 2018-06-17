virtualenv -p python3 env
source env/bin/activate
pip install -r std-api-server/requirements.txt
python std-api-server/server.py &
bash std-api-server/test.sh
