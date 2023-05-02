
# DEVCOMMIT



## Documentation
Link: https://documenter.getpostman.com/view/26223290/2s93Y5NzDE

The link has a "Run in Postman" button on top right, using which the APIs can be tested.
## Run Locally

Create virtual environment

```bash
  virtualenv venv
```

Activate virtual environment

```bash
  .\venv\Scripts\activate
```

Clone the project

```bash
  git clone https://github.com/krish-patel1003/devcommit.git
```

Go to the project directory

```bash
  cd devcommit
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
  python manage.py runserver
```
## Related Gists
Join query optimization - Django: https://gist.github.com/krish-patel1003/c9064058bdf99831a37d1b97d4e1e533

Input validation optmization - Django: https://gist.github.com/krish-patel1003/06afb31d1a07fa2027d33357cd40e28e
