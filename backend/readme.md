`pipenv shell`

`python manage.py loaddata test-data/*.json`

# nginx config

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
