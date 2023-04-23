

# DEVCOMMIT



## Documentation
**Link:** https://documenter.getpostman.com/view/26223290/2s93Y5NzDE

This postman documentation has a **"Run in Postman"** button on top right, using which the APIs can be directly tested in postman.
## Run Locally

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



