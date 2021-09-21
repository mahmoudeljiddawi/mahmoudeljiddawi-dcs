# mahmoudeljiddawi-dcs

download the repo 

create a database using MySQLWorkbench with the code founded in the ERDcode.sql file
open index.py and assign app.config['MYSQL_PASSWORD'] =  to the password of your mysql username

in terminal change the directory to the project location

install packages needed using the following command
pipenv install --dev

activate the virtual environment with the following command
pipenv shell

enter the following commands to run the app 

export FLASK_APP=index
flask run
