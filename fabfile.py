from fabric.api import *

env.hosts = ['fscons.org']

@task(default=True)
def deploy():
    local("git push")
    code_dir = '/var/django/myconf'
    with cd(code_dir):
        run("git pull github master")
        run("python manage.py collectstatic --noinput")
        sudo("/etc/init.d/apache2 restart")

@task(alias="refresh")
def refresh_initial_data():
    code_dir = '/var/django/myconf'
    with cd(code_dir):
        run("python manage.py dumpdata signup schedule people restaurants > initial_data.json")
        get("initial_data.json", ".")

