#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

# Update package information
sudo apt-get update

# Install Nginx if not already installed
sudo apt-get -y install nginx

# Allow HTTP traffic through UFW
sudo ufw allow 'Nginx HTTP'

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
}"

# Add the location block to the Nginx default configuration
sudo sed -i "/listen 80 default_server/a $config_content" /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

# Update package information
sudo apt-get update

# Install Nginx if not already installed
sudo apt-get -y install nginx

# Allow HTTP traffic through UFW
sudo ufw allow 'Nginx HTTP'

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
}"

# Add the location block to the Nginx default configuration
sudo sed -i "/listen 80 default_server/a $config_content" /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
