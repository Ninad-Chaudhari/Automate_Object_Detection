import os
import argparse
import shutil

PATH_ROOT = os.getcwd()

parser = argparse.ArgumentParser(
    description="Data generation in tfrecord fromat")
parser.add_argument("-st",
                    "--steps",
                    help="Total steps to be performed in training",
                    default="500",
                    type=str)
parser.add_argument("-c",
                    "--classes",
                    help="Number of classes in dataset",
                    type=str)

args = parser.parse_args()

steps = args.steps
classes = args.classes

shutil.move(PATH_ROOT+"/config.py", PATH_ROOT +"/tf/research")

print("Configuring the model...")
os.system("python " +PATH_ROOT+"/tf/research/config.py -r "+PATH_ROOT+" -s "+steps+" -c "+classes)

print("Started Training...")
os.system("protoc "+PATH_ROOT+ "/tf/research/object_detection/protos/*.proto --python_out=.")

TRAIN = PATH_ROOT + "/tf/research/object_detection/legacy/train.py"
TRAIN_DIR = PATH_ROOT+"/tf/trained"
CONFIG = PATH_ROOT+"/tf/ssd_mobilenet_v1_pets.config"
os.system("python "+TRAIN+" --logtostderr --train_dir="+TRAIN_DIR+" --pipeline_config_path="+CONFIG)