import os
import shutil

PATH_ROOT = os.getcwd()
PATH_ROOT = PATH_ROOT.replace(" ","")
print(PATH_ROOT)

PATH_IMAGES = PATH_ROOT + "/images"
PATH_TFRECORD = PATH_ROOT + "/tfrecords"
os.system("pip install tensorflow==1.13.2")
print("Tensorflow installed")
os.system("pip install tf_slim")
print("tf_slim installed")
os.system("pip show tensorflow")

print("Cloning repository from https://github.com/iotiotdotin/tf.git")
os.system("git clone https://github.com/iotiotdotin/tf.git")
os.mkdir(PATH_IMAGES)
os.mkdir(PATH_TFRECORD)
shutil.move(PATH_ROOT + "/generate_tfrecord.py" ,PATH_ROOT+"/tf/research" )

print("Moved tfrecod.py sucessfully")
print("Testing files in cloned repo")
os.chdir(PATH_ROOT + "/tf/research")
os.system("protoc object_detection/protos/*.proto --python_out=.")
os.chdir(PATH_ROOT + "/tf/research/slim")
os.system("python setup.py build")
os.environ['PYTHONPATH'] += ':' + PATH_ROOT + '/tf/research/:'+PATH_ROOT+'/tf/research/slim/:'+PATH_ROOT+'/tf/research/object_detection/utils/:'+PATH_ROOT+'/tf/research/object_detection'

print("Running model_builder_test.py")
os.chdir(PATH_ROOT + "/tf/research/")
os.system("python object_detection/builders/model_builder_test.py")
os.chdir(PATH_ROOT)