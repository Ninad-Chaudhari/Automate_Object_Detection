import os

PATH_ROOT = "/root/"
PATH_IMAGES ="/root/images"
os.system("pip install tensorflow==1.13.2")
os.system("pip install tf_slim")
os.system("pip show tensorflow")
os.system("cd " + PATH_ROOT)
os.system("git clone https://github.com/iotiotdotin/tf.git")
os.mkdir(PATH_IMAGES)
