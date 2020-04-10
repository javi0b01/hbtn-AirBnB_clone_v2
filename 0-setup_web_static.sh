#!/usr/bin/env bash
# 0. Prepare your web servers
apt-get update -y
apt-get install nginx -y
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "
<html>
  <head>
    <title>TEST Nginx</title>
  </head>
  <body>
    <p>
      Testing Nginx configuration
    </p>
  </body>
</html>
" | tee -a /data/web_static/releases/test/index.html
rm -rf /data/web_static/current/
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
upd="\\\t# Update the Nginx configuration\n\t# to serve the content of /data/web_static/current/ to hbnb_static\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"
sed -i "38i $upd" /etc/nginx/sites-available/default
service nginx restart
exit 0
