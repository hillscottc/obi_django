""" From http://www.yaconiello.com/blog/deploying-django-site-fabric/
"""
from __future__ import with_statement
import os
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm
# from fabric.colors import green, red

VENV_ROOT = '/home/shill/virtualenvs'
# VENV_WRAPPER_CALL = 'sh /usr/local/bin/virtualenvwrapper.sh'
# env.directory = '/home/shill/dev/obi_django'


def _wrap_local(cmd):
    """Some of fabric's 'local' calls need this to work.
    Usage:
        local(_wrap_local("mkvirtualenv foo"))
    Output:
        [localhost] local: /bin/bash -l -c 'mkvirtualenv foo'
    """
    return "/bin/bash -l -c '{}'".format(cmd)


def hello(name="world"):
    print("Hello %s!, printed." % name)
    local("echo Hello %s!, echoed." % name)
    # with settings(warn_only=True):
    #     result = local('./zzmanage.py test my_app', capture=True)
    # if result.failed and not confirm("Tests failed. Continue anyway?"):
    #     abort("Aborting at user request.")


def build_venv(name=None, venv_root=None):
    """Create (if neccesary) given virtual environment via 'mkvirtualenv'.
    """
    usage = "Usage: fab build_venv:name=xxxx"

    if not name:
        abort(usage)

    if not venv_root:
        venv_root = VENV_ROOT

    if not os.path.isdir(venv_root):
        abort("Invalid venv_root %s" % venv_root)

    if os.path.isdir(os.path.join(venv_root, name)):
        print("Virtual environment already exists.")
    else:
        local(_wrap_local("mkvirtualenv {}".format(name)))






#
#
# def build_commit(warn_only=True):
#     """Build a commit"""
#     local_branch = prompt("checkout branch: ")
#     rebase_branch = prompt("rebase branch: ")
#
#     local('git checkout %s' % local_branch)
#     local('git add .')
#     local('git add -u .')
#
#     message = prompt("commit message: ")
#
#     local('git commit -m "%s"' % message)
#     local('git checkout %s' % rebase_branch)
#     local('git pull origin %s' % rebase_branch)
#     local('git checkout %s' % local_branch)
#     local('git rebase %s' % rebase_branch)
#     local('git checkout %s' % rebase_branch)
#     local('git merge %s' % local_branch)
#     local('git push origin %s' % rebase_branch)
#     local('git checkout %s' % local_branch)
#
#
# def server():
#     """This pushes to the EC2 instance defined below"""
#     # The Elastic IP to your server
#     env.host_string = '999.999.999.999'
#     # your user on that system
#     env.user = 'ubuntu'
#     # Assumes that your *.pem key is in the same directory as your fabfile.py
#     env.key_filename = 'my_ec2_security_group.pem'
#
#
# def staging():
#     # path to the directory on the server where your vhost is set up
#     path = "/home/ubuntu/www/dev.yaconiello.com"
#     # name of the application process
#     process = "staging"
#
#     print(red("Beginning Deploy:"))
#     with cd("%s/app" % path) :
#         run("pwd")
#         print(green("Pulling master from GitHub..."))
#         run("git pull origin master")
#         print(green("Installing requirements..."))
#         run("source %s/venv/bin/activate && pip install -r requirements.txt" % path)
#         print(green("Collecting static files..."))
#         run("source %s/venv/bin/activate && python manage.py collectstatic --noinput" % path)
#         print(green("Syncing the database..."))
#         run("source %s/venv/bin/activate && python manage.py syncdb" % path)
#         print(green("Migrating the database..."))
#         run("source %s/venv/bin/activate && python manage.py migrate" % path)
#         print(green("Restart the uwsgi process"))
#         run("sudo service %s restart" % process)
#     print(red("DONE!"))