# PART - Google Natural Language API



## To Use It on Mac OS (***hard to work...***)

### Set 'Path'
export GOOGLE_APPLICATION_CREDENTIALS="/Users/wangjialun/Desktop/EC601/Mini\ Project/EC601\ mini\ project-34898095f322.json"

### Activate the VirtualEnv
cd /Users/wangjialun/Desktop/Mini\ Project/Google_NL_API

virtualenv --python python3 env

source env/bin/activate

pip install google-cloud-storage

#### Deactivate

deactivate



## To Use It on Linux ***Devbox, the prefered way to make it!***

### Set 'Path' on Linux
export GOOGLE_APPLICATION_CREDENTIALS="/media/sf_Mini_Project/EC601 mini project-34898095f322.json"

Of course you can change the 'PATH' to your one, by the following line:

`export GOOGLE_APPLICATION_CREDENTIALS="PATH"`



## Some File Descriptions

### ***analyze_sentiment.py***
It works! 
But till now, it can only recognize from an input string. 
Try by the following line:

python analyze_sentiment.py


### ***try_lite.py***
It works! 
It can return directly the sentiment score of a paragraph. 
Try by the following line:

python try_lite.py
