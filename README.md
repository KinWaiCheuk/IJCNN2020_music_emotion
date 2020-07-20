# IJCNN2020_music_emotion
source code for the paper publised in IJCNN 2020 "Regression-based Music Emotion Prediction using Triplet Neural Networks" 

# Dependencies
natsort==7.0.1

tensorflow-GPU==1.13.1

keras==2.3.1

seaborn==0.10.0

scikit-learn==0.19.2

pydub==0.23.1

matplotlib==3.0.2

tqdm

# Instruction
The train the model, please refer to `Training.ipynb`. The model is trained on DEAM dataset, which can be downloaded [here](http://cvml.unige.ch/databases/DEAM/). The data processing steps can be found in `DEAM/Data_Processing.ipynb`.

To use your trained model to predict music emotion, please refer to `Demonstration.ipynb`.



# Demonstration
In each of the region, we picked one song, and the predicted song can be found in `/Demo/*`
![](https://raw.githubusercontent.com/KinWaiCheuk/IJCNN2020_music_emotion/master/Demo/Figure1.png)

[Low](https://raw.githubusercontent.com/KinWaiCheuk/IJCNN2020_music_emotion/master/Demo/Low.mp3)

[UpperLow](https://raw.githubusercontent.com/KinWaiCheuk/IJCNN2020_music_emotion/master/Demo/UpperLow.mp3)

[Middle](https://raw.githubusercontent.com/KinWaiCheuk/IJCNN2020_music_emotion/master/Demo/Middle.mp3)

[LowerHigh](https://raw.githubusercontent.com/KinWaiCheuk/IJCNN2020_music_emotion/master/Demo/LowerHigh.mp3)

[High](https://raw.githubusercontent.com/KinWaiCheuk/IJCNN2020_music_emotion/master/Demo/High.mp3)
