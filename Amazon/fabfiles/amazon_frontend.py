from fabric.api import run, env, sudo, lcd, cd, settings

env.key_filename = ["~/code/netmarket/Amazon/Dev-Colin.pem"]

def setup_packages():
   sudo("apt-get install gcc build-essential python-dev git python2.7 vim htop -y") 
   sudo("wget http://pypi.python.org/packages/source/d/distribute/distribute-0.6.27.tar.gz#md5=ecd75ea629fee6d59d26f88c39b2d291")
   run("tar -xvf distribute-0.6.27.tar.gz")
   with cd('distribute-0.6.27'):
        sudo("python setup.py install")
   sudo("easy_install pip")
   
def activate_virtualenv():
    with cd("/home/ubuntu/env/bin"):
        run(". activate")
    
def setup_virtualenv():
    sudo("pip install virtualenv")
    run("virtualenv env")

def setup_repo():
    run("git clone https://github.com/c00w/netmarket.git")
    with cd('netmarket/frontend'):
        sudo("pip install -r requirments.txt") 
        run("pip install -r requirments.txt")

def cleanup():
    sudo("rm *.tar.gz *.tar.bz2 *.tar")

def update_repo():
    with cd('netmarket/frontend'):
        run("git reset --hard HEAD")
        run("git pull")
        sudo("pip install -r requirments.txt") 

def start_server():
    with cd('netmarket/frontend/'):
        with settings(warn_only=True):
            sudo('kill -2 `cat /tmp/supervisord.pid`')
        sudo("supervisord -c supervisord.conf")

def setup_frontend():
    setup_packages()
    #setup_virtualenv()
    #activate_virtualenv()
    setup_repo()
    cleanup()

def deploy_frontend():
    update_repo()
    start_server()

