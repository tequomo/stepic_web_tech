#!/bin/sh
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf   /etc/gunicorn.d/test-wsgi
#sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:app
#sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
sudo gunicorn ask.wsgi.application
#sudo /etc/init.d/mysql start
