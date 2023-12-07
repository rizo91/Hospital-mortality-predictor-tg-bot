### Hello, my name is Rizo Rasulov.
I am a developer with a background in Medical Science and years of work experience in medical institutions as a pediatrician. This is my pet project on a medical topic, in which I wanted to explore the possibilities of applying machine learning to the healthcare sector. 
#### My project is a Telegram bot that uses a neural network trained on data from 1000+ intensive care patients (https://physionet.org/content/mimiciii/1.4/). It predicts the likelihood of a favorable (or not-so-favorable) outcome for a patient in the intensive care unit.

Telegram bot tag:
>@Mort_Hospit_bot

#### To get started you will need the following:
* Install the Telegram app
* Get your token from BotFather in Telegram and paste it into the token.txt file.
* Install the necessary libraries from requirements.txt with the command:
> pip install -r requirements.txt

* In case of using Docker - Create a Docker image from the attached Dockerfile:
 > Docker build

#### Model training:
The stages of model training are described in the file mimic_tensorflow_survive.ipynb
At the beginning of the notebook, there is a path variable; in it, you need to specify the path to the project
At the end, saving/loading the model. (in this project, the loaded model is located in the saved_model folder)

#### UI: 
The user interface shows a 2-level menu, divided into 4 parts:
 * General information (gender/age - required to enter/Body Mass Index)
 * Presence of chronic diseases.
 * Vital indicators (HR/RR/...)
 * Laboratory indicators.

The user needs to fill in the values of the required variables and any other additional values available. If some information about the patient is unknown, it will be filled in automatically with the median value of the sample on which the model was trained (mimic_data.csv), what will affect the result.
