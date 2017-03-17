from flask import Flask
app = Flask(__name__)
import sys
import requests

url= sys.argv[1] 
owner_name = url.split('/')[3]
repo_name = url.split('/')[4]
git_api_url ="http://api.github.com/repos"

@app.route('/v1/<filename>')
def fetch_git_file(filename):
        headers = {'Accept': 'application/vnd.github.v3.raw'}
        content = requests.get(git_api_url+"/"+owner_name+"/"+repo_name+"/contents/"+filename,headers=headers)
        return content.content

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')