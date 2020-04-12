#!/usr/bin/python3
# 2. Deploy archive!
from fabric.api import *
import os
env.hosts = ['35.231.116.150', '3.89.127.97']


def do_deploy(archive_path):
    """ distributes an archive """
    if not os.path.exists(archive_path):
        return False
    try:
        arg = archive_path.split("/")
        folder = arg[0]
        archive = arg[1]
        arch = os.path.splitext(arg[1])
        filename = arch[0]
        extension = arch[1]
        releases = "/data/web_static/releases/"
        current = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(releases, filename))
        run("tar -xzf /tmp/{} -C {}{}/".
            format(archive, releases, filename))
        run("rm /tmp/{}".format(archive))
        run("mv {}{}/web_static/* {}{}/".
            format(releases, filename, releases, filename))
        run("rm -rf {}{}/web_static".format(releases, filename))
        run("rm -rf {}".format(current))
        run("ln -s {}{}/ {}".format(releases, filename, current))
        return True
    except:
        return False
