# cmpe273-assignment1
This code can display the contents of any existing file from github repository if the girhub url is provided.

clone this github repository

$git clone https://github.com/dharmisha/cmpe273-assignment1.git

$cd cmpe273-assignment1

$docker build -t assignment1-flask-app:latest .

start the server in docker using the following command

$docker run -d -p 5000:5000 assignment1-flask-app https://github.com/dharmisha/assignment1-config-example

The github url provided above can be replaced by any user's github repo whose files need to be read
If no url is mentioned above, it will display existing files from the default url which is:
https://github.com/dharmisha/assignment1-config-example

following command is used to read the contents of a file(dev-config.json)

$curl http://0.0.0.0:5000/v1/dev-config.json

instead of dev-config.json, any filename can be substituted whose contents are required to be read

