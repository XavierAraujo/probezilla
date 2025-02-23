# Setup 

First you will need to install Python packet manager - pip:
```
python3 -m ensurepip
```

Then you'll need to install `virtualenv` Python package to create a local Python environment to execute the validator:
```
sudo -H pip install virtualenv
```

Then you'll need to create and activate the local Python environment and install the required Python dependencies:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e . 
```
