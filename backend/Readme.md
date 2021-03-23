`pipenv shell`

`install -r requirements.txt`

`python manage.py loaddata test-data/*.json`

`python manage.py runserver 8000`

`pipenv install`

`python manage.py createsuperuser`


# nginx config: /etc/nginx/nginx.conf

    user benutzername; #benutzername muss dem eigenem benutzernamen entsprechen


# nginx config: /etc/nginx/sites-available/heimabend_nginx.conf

    upstream django {
         server unix:///root/heimabend/backend/heimabend/heimabend.sock;
        #server 127.0.0.1:8001; # for a web port socket (we'll use this first)
    }

    //configuration of the server

    server {
        # the port your site will be served on
        listen      80;
        # the domain name it will serve for
        server_name api.xrdcx.de; # substitute your machine's IP address or FQDN
        charset     utf-8;

        # max upload size
        client_max_body_size 75M;   # adjust to taste

        # Django media
        location /media  {
            alias /root/heimabend/backend/heimabend/media;  # your Django project's media files - amend as required
        }

        location /static {
            alias /root/heimabend/backend/heimabend/static; # your Django project's static files - amend as required
        }

        # Finally, send all non-media requests to the Django server.
        location / {
            uwsgi_pass  django;
            include     /root/heimabend/backend/heimabend/uwsgi_params; # the uwsgi_params file you installed
        }

        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/api.xrdcx.de/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/api.xrdcx.de/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    }
 
 
# How to set up TLS certificate:
    
  https://www.digitalocean.com/community/tutorials/how-to-set-up-let-s-encrypt-with-nginx-server-blocks-on-ubuntu-16-04
    
# How to install nginx for django
    
 https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
 
# packages needed
    python3(.8)
    python3(.8)-dev
    
 
# requirements.txt for all pip3 dependencies
    asgiref==3.2.5
    Django==3.0.4
    django-cors-headers==3.2.1
    djangorestframework==3.11.0
    djangorestframework-simplejwt==4.4.0
    drf-api-tracking==1.6.0
    PyJWT==1.7.1
    PyMySQL==0.9.3
    python-memcached==1.59
    pytz==2019.3
    six==1.14.0
    sqlparse==0.3.1
    uWSGI==2.0.18
    
# uwsgi ini file: heimabend_uswgi.ini
     [uwsgi]
    # Django-related settings
    env = LANG=de_DE.UTF-8
    # the base directory (full path)
    chdir           = /root/heimabend/backend/heimabend
    # Django's wsgi file
    wsgi-file          = /root/heimabend/backend/heimabend/heimabend/wsgi.py
    # the virtualenv (full path)
    home            = /root/heimabend/backend/backendenv

    # process-related settings
    # master
    master          = true
    # maximum number of worker processes
    processes       = 2
    # the socket (use the full path to be safe
    socket          = /root/heimabend/backend/heimabend/heimabend.sock
    # ... with appropriate permissions - may be needed
    chmod-socket    = 666
    # clear environment on exit
    vacuum          = false
    threads = true
 
# To start/restart uwsgi server
    
    1)enter tmux session
    tmux a -t backend
    (or create new one with tmux new -s backend)
    
    2)enter virtualenv
    source /root/heimabend/backend/backend/bin/activate
    
    3)enter directory
    cd /root/heimabend/backend/heimabend
    
    4)start uswsgi
    uwsgi --ini heimabend_uwsgi.ini
    
    
