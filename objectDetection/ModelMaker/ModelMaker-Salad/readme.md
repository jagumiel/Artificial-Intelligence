# Model Maker: Training a salad detector.
This is an example project. It trains a model to detect salad and its' ingredients. To do so, it uses _TensorFlow Model Maker_.


## Salad detector
We have trained an EfficientDet-Lite2 model using the _salad dataset_. We don't need to download the dataset, the Jupyter Notebook will take it and administrate it on its own.
This is just an example oriented to work with the Model Maker Library, if you are interested in using your own datasets, you should take a look to the Model Maker versions of knife or weapons detection notebooks.
The _Salads dataset_ is public, and was was created from the Open Images Dataset V4.

Each image in the dataset contains objects labeled as one of the following classes:

- Baked Good
- Cheese
- Salad
- Seafood
- Tomato

This example trains the whole model:
Setting `train_whole_model=True` fine-tunes the whole model instead of just training the head layer to improve accuracy. The trade-off is that it may take longer to train the model.
We have appreciated better results using this option.

Model Maker does not require you to download a saved model to train. You specify the desired network and it will download it for you.


## **[To-Do]:** 
- How to use the checkpoints to get the best result and avoid overfitting?
- Modify the script to pick more than one image and save the labelled photos.