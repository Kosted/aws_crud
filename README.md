**Run project:**

1) create and activate virtulalenv `python3 -m venv venv && source venv/bin/activate`

2) `python -m pip install --upgrade pip`

3) `pip install -r requirements.txt`
 
4) Create .env file in `aws_crud`

5) `python manage.py migrate`

6) `python manage.py runserver`

**Generate secret key:**

`from django.core.management.utils import get_random_secret_key
get_random_secret_key()`

**Install psycopg2:**

`sudo apt-get install python-psycopg2`

`sudo apt-get install libpq-dev`

**PyCharm setup:**

Settings -> Project Interpreter (for current project) -> Press on Gear icon -> add -> Existing environment -> PATH_TO_PROJECT/venv/bin/python

**Setup git hooks for flake8:**

```
flake8 --install-hook git
git config --bool flake8.strict true
```

**Keeping project clean:**

You should clean any errors that `flake8` and `mypy .` shows. 
