# Algo-QMS

## How to start project
First of all check your local django version with:
```bash
django-admin.py version
```
If it's not 2.0b1 or you get a command not found error, run this command:
```bash
pip install --pre django
```
To clone and run project, execute these commands:
```bash
git clone https://github.com/inzva/Algo-QMS.git
cd Algo-QMS
python3 manage.py migrate
python3 manage.py runserver
```
