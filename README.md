## Hello, my name is Rizo Rasulov.
#### I am a pediatrician, and this is my pet project on a medical topic, in which I wanted to show the possibilities of machine learning for socially useful purposes.
#### This is a telegram bot that, using a neural network trained on data from 1000 intensive care patients (https://physionet.org/content/mimiciii/1.4/), predicts the likelihood of a favorable (or not so favorable) outcome for a patient in the intensive care unit .
### Telegram bot tag: @Mort_Hospit_bot
## To start you will need:
* get your token from BotFather in telegram and paste it into the token.txt file.
* Install the necessary libraries from requirements.txt with the command:
  > pip install -r requirements.txt

* create a Docker image from the attached Dockerfile:
  > Docker build

## Model training:

#### The stages of model training are described in the file mimic_tensorflow_survive-Copy1.ipynb

* At the beginning of the notebook there is a path variable; in it you need to specify the path to the project
* At the end, saving/loading the model. (in this project, the loaded model is located in the saved_model folder)

## User interaction:

Implemented using a 2-level menu, divided into 4 parts:

* general information (gender/age - required to enter/Body Mass Index)
* Presence of chronic diseases.
* Vital indicators (HR/RR/...)
* Laboratory indicators.

If some information about the patient is unknown, it will be filled with the median value of the sample on which the model was trained (mimic_data.csv). What will affect the result.