# crawl

Make a Document out of it.

virtualenv : A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

pyenv  : Python verison switch (2.7 , 3.6 , 3.7) interpreter (switch one version to another version)

Instruction create direcotry :

$ mkdir crawl
crawl $ vi requirements.txt
crawl $ mkdir lib
$ cd lib
lib $ vi settings.yaml
lib $ vi hanlder.py
$ cd ..

crawl $ makdir ENV  
virtualenv __ENV
source ENV/bin/activate
pip install request
pip install pyyaml
pip freeze > requirements.txt

