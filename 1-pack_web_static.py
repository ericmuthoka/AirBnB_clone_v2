#!/usr/bin/python3
"""This module defines a Fabric script that creates a .tgz archive."""

import os
from datetime import datetime
from fabric.api import local, runs_once

@runs_once
def do_pack():
    """Create a .tgz archive of static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    timestamp = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        timestamp.year,
        timestamp.month,
        timestamp.day,
        timestamp.hour,
        timestamp.minute,
        timestamp.second
    )
    try:
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))
        size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, size))
    except Exception:
        archive_path = None
    return archive_path
