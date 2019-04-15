#clubpsychic

### Installation

Install virtual environment:
```sh
$ pip install virtualenv
$ cd my_project_folder
$ virtualenv venv
$ source venv/bin/activate (or . venv/bin/activate)
$ pip install -r requirements.txt
echo "$(pwd)" | sudo tee venv/lib/python2.7/site-packages/recipe_app.pth > /dev/null
```
- navigate to setup_app/config folder
- create env.py file from env.py.sample
- create test.py file from test.py.sample
- navigate to setup_app/server folder
```sh
$ python run.py
```

### Starting server

Starting virtual environment and server:
```shpip
$ source venv/bin/activate (or . venv/bin/activate)
```
- navigate to setup_app/server folder
```sh
$ python run.py
```
