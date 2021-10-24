# Automate_Object_Detection
## Tutorial :
Click here for tutorial : [Collab](https://colab.research.google.com/drive/1FfevYpXXd-wAzmNWmX3vN7cJQ-xd-49Q#scrollTo=n4EucbVWTa1r)
## Steps to run :
1) Open google collab and mount your drive.
2) Navigate to any folder and clone the repository
>```markdown
>! git clone https://github.com/Ninad-Chaudhari/Automate_Object_Detection.git
>```
3) Run setup.py file
>```markdown
>%run setup.py
>```
4) Upload your images and xml/json/csv annotation files in images folder.
5) Lets prepare our dataset and create tfrecords.
>```markdown
>%run prepare_dataset.py
>```
6) Start training our model.
>#### Parameters:
> -st : Number of steps in training<br> 
> -c : classes in dataset
>```markdown
>!python train.py -st 250 -c 2
>```
7) Freeze the trained model.
>```markdown
>%run eval_freeze.py
>```
8) Check your predictions
>#### Parameters:
>-c : Number of classes in dataset<br>
>-n : Number of images to show predictions on
>```markdown
>%run plot.py -c 2 -n 10
>```
