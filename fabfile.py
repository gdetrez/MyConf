from fabric.api import *

env.hosts = ['fscons.org']

def deploy():
    local("git push")
    code_dir = '/var/django/myconf'
    with cd(code_dir):
        run("git pull")
        run("python manage.py collectstatic --noinput")
        sudo("touch ../wsgi/myconf.wsgi")
