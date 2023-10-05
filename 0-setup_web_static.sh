#!/usr/bin/env bash
# Bash script to set up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/current

# Create a fake HTML file for testing
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <p>This is a test page.</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="
server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location / {
        return 301 /hbnb_static/index.html;
    }
}"

echo "$config_content" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
