export PYTHONPATH='.'
export DB_USERNAME='drhades'
export DB_PASSWORD='SoyEzequielEnMysql'
export DB_HOST='localhost'
export DB_NAME='queueSYS_test' 

clear 

pytest -s -vvvv $1 $2
