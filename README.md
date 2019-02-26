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

pip list :  show the version and package
