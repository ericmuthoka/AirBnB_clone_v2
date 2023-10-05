#!/usr/bin/python3
"""
Fabric script for distributing an archive to web servers.
"""

from datetime import datetime
from fabric.api import *
import os


env.hosts = ["52.91.121.146", "3.85.136.181"]
env.user = "ubuntu"


def do_pack():
    """
    Create an archive and return the archive path if successful.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(date)
    tar_command = local("tar -cvzf {} web_static".format(archive_path))

    if tar_command.succeeded:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distribute the archive to the web servers.
    """
    if os.path.exists(archive_path):
        archive_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archive_file[:-4]
        archive_file = "/tmp/" + archive_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archive_file, newest_version))
        run("sudo rm {}".format(archive_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
