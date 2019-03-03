# crawl

Make a Document out of it.

virtualenv : A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

pyenv  : Python verison switch (2.7 , 3.6 , 3.7) interpreter (switch one version to another version)

Instruction create direcotry :

$ mkdir crawl <br />
crawl $ vi requirements.txt <br />
crawl $ mkdir lib <br />
$ cd lib <br />
lib $ vi settings.yaml <br />
lib $ vi hanlder.py <br />
$ cd .. <br />

crawl $ mkdir ENV <br />  
virtualenv ENV <br />
source ENV/bin/activate <br />
pip install request <br />
pip install pyyaml <br />
pip freeze > requirements.txt <br />

pip install -r requirements.txt
(pip install request) and (pip install pyyaml) all version and package are install in requirements.txt file 
after that no need for installation of (pip install request) and (pip install pyyaml)
only install requirements.txt

pip list :  show the version and package <br />
in website page : go to web developer and network etc. <br />

Request : This means you don’t have to manually add query strings to URLs, or form-encode your POST data. Don’t worry if that made no sense to you. It will in due time.
Requests will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way <br />

So, to request a response from the server, there are mainly two methods: <br />
GET : to request data from the server. <br /> 
      Range :  Limited (1024 charatacter ) <br />
               URL change every time when you changed in website <br /> 
POST : to submit data to be processed to the server. <br />
        more secure version <br />
        Range : unlimited <br />
        URL same and page changed value <br />
        

Beautifulshop using scrapping <br />
import requests import requests <br />
from bs4 import BeautifulSoup <br />
##https://nclt.gov.in/pdf-cause-list?field_bench_target_id=5366&field_bench_court_target_id_entityreference_filter=5386 <br />

##WebSite Get Requests <br />
#html = requests.get('https://nclt.gov.in/exposed-pdf-cause-list-page', verify=False).content <br />
""" FILE WRITE <br />
file_write = open('home.html', 'wb') <br />
file_write.write(html) <br />
file_write.close() <br />
""" <br />
##File Read Operation <br />
content = open('home.html', 'r').read() <br />
##File Parser <br />
soup = BeautifulSoup(content, 'html.parser') <br />
##Class of both <br />
#print(type(soup)) <br />
#print(type(content)) <br />
# 
soup = soup.find('select', {"name":"field_bench_target_id"}) <br />
for record in soup.find_all('option'): <br />
    if not 'Any' in str(record): <br />
        branch_name = record.text.strip() <br />
        branch_value = record.get('value') <br />
        print(branch_name) <br />
        print(branch_value) <br />
        #print(record) <br />
        #print() <br />
        print('') <br />
        print('**'*20) <br />
