import subprocess

bashCommand = "source /home/daxuiqorsd/virtualenv/django-projekt/dziennik/3.8/bin/activate && cd /home/daxuiqorsd/django-projekt/dziennik"

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()