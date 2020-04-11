#!/usr/bin/python3
# 2. Deploy archive!
from fabric.api import *
from datetime import datetime
from os import path
env.hosts = ['35.231.116.150', '3.89.127.97']


def do_deploy(archive_path):
    """ distributes an archive """
    if not path.exists(archive_path):
        return False
    try:
        arg = archive_path.split("/")
        folder = arg[0]
        archive = os.path.splitext(arg[1])
        filename = archive[0]
        extension = archive[1]
        releases = '/data/web_static/releases/'
        current = '/data/web_static/current'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(releases, filename))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive, releases, filename))
        run('rm /tmp/{}'.format(archive))
        run('mv {1}{0}/web_static/* {1}{0}/'.format(filename, releases))
        run('rm -rf {}{}/web_static'.format(releases, filename))
        run('rm -rf {}'.format(current))
        run('ln -fs {}{}/ {}'.format(releases, filename, current))
        return True
    except:
        return False
