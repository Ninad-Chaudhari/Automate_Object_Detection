import os
PATH_ROOT = os.getcwd()
PATH_ROOT = PATH_ROOT.replace(" ","")
os.environ['PYTHONPATH'] += ':' + PATH_ROOT + '/tf/research/:'+PATH_ROOT+'/tf/research/slim/:'+PATH_ROOT+'/tf/research/object_detection/utils/:'+PATH_ROOT+'/tf/research/object_detection'

PATH_EVAL = PATH_ROOT +"/tf/research/object_detection/legacy/eval.py"
PATH_CHECK = PATH_ROOT+"/tf/trained"
PATH_EVAL_DIR = PATH_ROOT+"/eval" 
PATH_CONFIG = PATH_ROOT+"/tf/ssd_mobilenet_v1_pets.config"
os.system("python "+PATH_EVAL+ " --logtostderr  --pipeline_config_path="+PATH_CONFIG+" --checkpoint_dir="+PATH_CHECK+" --eval_dir="+PATH_EVAL_DIR)
