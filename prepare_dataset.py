import os
import shutil
import argparse
import glob
import urllib
import tarfile
from requests import get

PATH_ROOT = os.getcwd()

parser = argparse.ArgumentParser(
    description="Data generation in tfrecord fromat")
parser.add_argument("-s",
                    "--split",
                    help="Percentage to split data set into",
                    default="70",
                    type=str)
parser.add_argument("-f",
                    "--filename",
                    help="path to xml json csv file",
                    type=str)

args = parser.parse_args()
filename=""
if args.filename is not None:
    filename = args.filename
file_path = PATH_ROOT + "/images/"+ filename
images_path = PATH_ROOT + "/images"
output_path = PATH_ROOT + "/tfrecords"
csv_path = PATH_ROOT + "/tfrecords/train.csv"                    

os.system("python "+ PATH_ROOT+"/tf/research/generate_tfrecord.py -f " + file_path +" -i "+ images_path + " -o "+output_path+" -c "+csv_path+" -s "+args.split)


print("Downloading pretrained model...")
# Downloading pretrained model
os.chdir(PATH_ROOT + "/tf")
MODEL = 'ssd_mobilenet_v1_coco_2017_11_17'
MODEL_FILE = MODEL + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
DEST_DIR = 'pretrained_model'

if not (os.path.exists(MODEL_FILE)):
  with open(MODEL_FILE, "wb") as file:
    # get request
    response = get(DOWNLOAD_BASE + MODEL_FILE)
    # write to file
    file.write(response.content)
    #opener = urllib.URLopener()
    #opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)

tar = tarfile.open(MODEL_FILE)
tar.extractall()
tar.close()

os.remove(MODEL_FILE)
if (os.path.exists(DEST_DIR)):
  shutil.rmtree(DEST_DIR)
os.rename(MODEL, DEST_DIR)
print("Moving config file to tf folder...")
shutil.move(PATH_ROOT+"/tf/research/object_detection/samples/configs/ssd_mobilenet_v1_pets.config", PATH_ROOT +"/tf") 
