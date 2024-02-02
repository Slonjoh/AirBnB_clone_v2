#!/usr/bin/python3
"""Fab file to archive web_static content"""
from os import remove
from os.path import exists
from fabric.api import *
from datetime import datetime


env.hosts = ['54.237.87.200', '52.86.189.30']


def do_deploy(archive_path):
    """Deploy function for archive to get deployed to servers"""
    if not exists(archive_path):
        return False
    fileNameExt = archive_path.split('/')[-1]
    fileName = fileNameExt.split(".")[0]
    result = put(archive_path, '/tmp/{}'.format(fileNameExt))
    if result.failed:
        return False
    result = run("sudo rm -rf /data/web_static/releases/{}/".format(fileName))
    if result.failed:
        return False
    result = run("sudo mkdir -p /data/web_static/releases/{}/"
                 .format(fileName))
    if result.failed:
        return False
    result = run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                 .format(fileNameExt, fileName))
    if result.failed:
        return False
    result = run("sudo rm /tmp/{}".format(fileNameExt))
    if result.failed:
        return False
    input = "sudo mv /data/web_static/releases/{}/web_static/*\
    /data/web_static/releases/{}/".format(fileName, fileName)
    result = run(input)
    if result.failed:
        return False
    result = run("sudo rm -rf /data/web_static/releases/{}/web_static"
                 .format(fileName))
    if result.failed:
        return False
    result = run("sudo rm -rf /data/web_static/current")
    if result.failed:
        return False
    result = run("sudo ln -s /data/web_static/releases/{}/ "
                 "/data/web_static/current".format(fileName))
    if result.failed:
        return False
    print("New version deployed!")
    return True
