#!/usr/bin/python3
"""
Fabric script for distributing an archive to web servers.
"""

import os
from fabric.api import put, run, env

env.hosts = [
    '<your_web_server_1_ip>',
    '<your_web_server_2_ip>'
]
env.user = 'your_username'
env.key_filename = [
    '/path/to/your/ssh/private/key'
]


def do_deploy(archive_path):
    """
    Distribute an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        print("File doesn't exist at {}".format(archive_path))
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split('.')[0]
        remote_path = "/tmp/{}".format(file_name)
        release_path = "/data/web_static/releases/{}".format(folder_name)

        # Upload the archive to /tmp/ directory on the server
        put(archive_path, remote_path)

        # Create the release directory
        run("sudo mkdir -p {}".format(release_path))

        # Uncompress the archive to the release directory
        run("sudo tar -xzf {} -C {}/".format(remote_path, release_path))

        # Remove the uploaded archive
        run("sudo rm {}".format(remote_path))

        # Move contents to the correct directory
        run("sudo mv {}/web_static/* {}/".format(release_path, release_path))

        # Remove the web_static directory
        run("sudo rm -rf {}/web_static".format(release_path))

        # Remove the current symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print("An error occurred: {}".format(str(e)))
        return False
