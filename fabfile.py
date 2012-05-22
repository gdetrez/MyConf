from fabric.api import *
from datetime import datetime
env.hosts = ['fscons.org']

@task(default=True)
def deploy():
    local("git push zjyto")
    code_dir = '/var/django/myconf'
    with cd(code_dir):
        run("git pull origin master")
        run("python manage.py collectstatic --noinput")
        sudo("/etc/init.d/apache2 restart")

@task(alias="refresh")
def refresh_initial_data():
    code_dir = '/var/django/myconf'
    fname = "initial_data_%s.json" % datetime.now().strftime("%Y%m%d%H%M")
    with cd(code_dir):
        run("python manage.py dumpdata signup schedule people restaurants > %s" % fname)
        get(fname, "fixtures")

