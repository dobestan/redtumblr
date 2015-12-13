web: gunicorn redtumblr.wsgi -c etc/config/gunicorn.py
worker: celery --workdir=redtumblr/ --app=redtumblr.celery:app worker
beat: celery --workdir=redtumblr/ --app=redtumblr.celery:app beat
flower: celery --workdir=redtumblr/ --app=redtumblr.celery:app flower
