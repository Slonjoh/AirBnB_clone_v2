#!/usr/bin/env bash                                                                                                                                      
# Setup a web servers for the deployment of web_static.                                                                                                  
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/web_static/releases/
sudo chown -R ubuntu:ubuntu /data/web_static/shared/
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
