# project path
# export CURRENT_DIR=`dirname $(readlink -f $0)`
# export PRJ_DIR=`dirname $CURRENT_DIR`
# go to project root directory
cd /home/riken/Desktop/workplace/COINMARKET/coinmarket
#. ./tasks/environment.sh
# . tasks/environment.sh

# Kill python and AVD process
killall -9 python qemu-system-x86_64

# activate the virtual environment for python
#. env/bin/activate
. env/bin/activate

# update code
# git pull origin $(git rev-parse --abbrev-ref HEAD)

python manage.py signup
# */10 */1 * * * /bin/bash /home/riken/Desktop/workplace/COINMARKET/coinmarket/TASKS/signup.sh >> /home/riken/Desktop/workplace/COINMARKET/coinmarket/TASKS/signup.log 2>&1