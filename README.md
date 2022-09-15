# Celery-Django

## Requirements:
- python -m pip install celery
- pip install django-celery-beat

## Run Project:
### Run All these command parallelly
- PROJECT NAME :      "celery_core" <-- (Don't Run it)
- RUN DJANGO SERVER:  **python3 manage.py runserver**
- RUN CELERY:         **celery -A [PROJECT_NAME].celery worker --loglevel=info**
- RUN CELERY BEAT:    **celery -A [PROJECT_NAME] worker --beat --scheduler django --loglevel=info**

## Additional Information step-by-step:

-- 1st: Create the (celery.py) file in the root of the project directory where settings.py and copy paste the code in your project. <br>
-- 2nd: Add your project name in (celery.py) file, if you copy paste the code from here then replace the (celery_core) according to your project name. [ I add TASK in the celery.py file, if you want to make task.py file its upto you, you can create task.py file in any app of your project, and use it. ] <br>
-- 3rd: Add the celery requirements in your settings.py , Find the Celery portion and copy paste the code in your project from here. <br>
-- 4th: If you use celery beat then add 'django_celery_beat' in your INSTALLED_APP list, and then apply migrations. 
