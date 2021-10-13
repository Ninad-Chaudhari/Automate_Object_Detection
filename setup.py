import os

PATH_ROOT = "/root/"
PATH_IMAGES ="/root/images"
PATH_TFRECORD = "/root/tfrecords"
os.system("pip install tensorflow==1.13.2")
os.system("pip install tf_slim")
os.system("pip show tensorflow")
os.chdir(PATH_ROOT)
os.system("git clone https://github.com/iotiotdotin/tf.git")
os.mkdir(PATH_IMAGES)
os.mkdir(PATH_TFRECORD)


print("Testing files in cloned repo")
os.chdir("/root/tf/research")
os.system("protoc object_detection/protos/*.proto --python_out=.")
os.chdir("/root/tf/research/slim")
os.system("python setup.py build")
os.environ['PYTHONPATH'] += ':/root/tf/research/:/root/tf/research/slim/:/root/tf/research/object_detection/utils/:/root/tf/research/object_detection'

print("Running model_builder_test.py")
os.chdir("/root/tf/research/")
os.system("python object_detection/builders/model_builder_test.py")
