# Convin-Backend

## To run the app 

### Prerequisites 

1. Python version 3.8+ [*click here*](https://dev.to/mortoray/how-to-install-python-3-8-on-ubuntu-1bp4)
1. Pip version 20.0+ [*click here*](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
1. Redis-Server version 5.0.7+ [*click here*](https://redis.io/download)

### API Routes 

- `api/` : API Root 
- `api/task` : To view, create, update, modify, delete tasks
- `api/tasktracker` : To view, create, update, modify, delete task trackers


### Steps

- Make a new virtual environment `python3 -m venv <name>`
- Start the virtual environment `source <name>/bin/activate`
- Install the requirements `pip3 install -r requirements.txt`
- Make migrations of the models of the app `python3 manage.py migrate`
- Start the app `python3 manage.py runserver 8080`
- Check if redis-server is working `redis-server &&  redis-cli ping`
- Start the celery worker `celery -A tracker_project worker -l info` (seperate terminal with same virtual environment)
- Start the celery beat `celery -A tracker_project beat -l info` (seperate terminal with same virtual environment)
- Crontab tasks are defined in `tracker_api/tasks.py`


Note :  Pypi project django-celery required a celery version < 4.0, but I , therefore I used celery directly in settings.py