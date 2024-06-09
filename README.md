# star-wars
Scrape data about cards from Star Wars Unlimited website 

## Setup project
Below you can find the correct road map to setup correctly the project

1.  Install git, python3 and virtual environment
2.  Clone the repository
3.  Create own virtual environment for python
4.  **Activate** / **Deactivate** virtual environment
5.  Install requirements
6.  Run setup 
7.  Run main project file

## Install git, python3 and virtual environment

```bash
apt install git python3 python3-venv 
```

## Clone the repository
You can fork the repository and clone yours but in this example I'll show you mine

```bash
git clone https://github.com/guerralindao/star-wars.git
```

If you want to clone your repository forked from mine, you need specify your repository container

```bash
git clone https://github.com/your_repository_container/star-wars.git
```

## Create own virtual environment for python

```bash
python3 -m venv your/path/venv
```

## Activate / Deactivate virtual environment
You must activate virtual environment if you want to run the project 

```bash
source your/path/venv/bin/activate
```

To deactivate virtual environment you need to prompt the following string on your terminal

```bash
deactivate
```

## Install requirements
First you need to upgrade your package installer

```bash
pip install --upgrade pip
```

After that you can install all requirements that you can find on txt file (requirements.txt)

```bash
pip install -r requirements.txt
```

## Run setup 
You can find some soluction that you can see on the following points

1. Automation script
2. Manual commands **_( Deleted )_**

### Automation script
You need to run the following command to setup directories and so on (this script works on Linux OS).

```bash
$ python3 setup.py
```

**Lobster folder**
> Folder where you can find every response scrape from script

**Assets folder**
> Folder where you can find images downloaded and responses parsed from scraping, and so on

## Run main project file
You can find some soluction that you can see on the following points, but first you need comment the following lines on main.py

```python
""" Row 13 """
from system.telegram_sendmessage import main as _alert # Library alert administrator [SYSTEM]
...
""" Row 27 """
_alert() # Start send notification to administrator
```

Now you can run the project like you want it

1. Run all modules
2. Run specific modules

### Run all modules

```bash
python3 main.py
```

### Run specific modules

**starwars**
> Start the module that scrape data and parsed it into a file csv

```bash
$ python3 main.py starwars
```

**starwars**
> Start the module that read the response csv and downloads all images 

```bash
$ python3 main.py _download
```
