#!/usr/bin/python3
""" Function that compress a folder """
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo


env.hosts = ['54.237.87.200', '52.86.189.30']
# env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_comp, new_folder))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False
