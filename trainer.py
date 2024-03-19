# from tensorflow.keras.applications.inception_v3 import InceptionV3
# from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
# from tensorflow.keras.applications.xception import Xception
# from tensorflow.keras.applications.densenet import DenseNet201
# from tensorflow.keras.applications.efficientnet import EfficientNetB6
# from tensorflow.python.keras. import EfficientNetB6
# from tensorflow import InceptionV3
# from tensorflow import InceptionResNetV2
# from tensorflow import Xception
# from tensorflow import DenseNet201
import pandas as pd
import numpy as np
import os
import tensorflow
import keras
import matplotlib.pyplot as plt
from keras.layers import Dense, Dropout, Flatten, ZeroPadding2D, Conv2D, MaxPooling2D, Activation, GlobalAveragePooling2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input #MobileNetV2
from keras.models import Model, Sequential
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.utils import class_weight
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.xception import Xception
from keras.applications.densenet import DenseNet201
from keras.applications.efficientnet import EfficientNetB6
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import plot_model
import splitfolders
import csv

base_folder: str = r'archive\dataset_4 BIGGER latex equations (arrows)\dataset_with_classes'
split_folder: str = r'archive\dataset_4 BIGGER latex equations (arrows)\split'
saved_model_folder: str = r'saved_model'
exported_model_folder: str = r'exported_model'

#Split folders into train, validation, and test sets
splitfolders.ratio(base_folder, output=split_folder,seed=1337, ratio=(0.6, 0.2,0.2), group_prefix=None)
#define number of classes
NUM_CLASSES = len(os.listdir(split_folder + r'/test'))
class_Labels = ['0','1','2','3','4','5','6','7','8','9','division','dot','downarrow','leftarrow','leftrightarrow','multiplication','plus','rightarrow','subtraction', 'uparrow','updownarrow','x','y','z']
#data generators
train_datagen=ImageDataGenerator(preprocessing_function=preprocess_input) #included in our dependencies

train_generator=train_datagen.flow_from_directory(split_folder + r'/test',
                                                 target_size=(224,224),
                                                 color_mode='rgb',
                                                 batch_size=24,
                                                 class_mode='categorical',
                                                 shuffle=True,
                                                 classes=class_Labels)

val_datagen=ImageDataGenerator(preprocessing_function=preprocess_input) #included in our dependencies

val_generator=val_datagen.flow_from_directory(split_folder + r'/val', # this is where you specify the path to the main data folder
                                                 target_size=(224,224),
                                                 color_mode='rgb',
                                                 batch_size=24,
                                                 class_mode='categorical',
                                                 shuffle=True,
                                                 classes=class_Labels)

with open("class_indices.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Key', 'Value'])
    # Write data
    for key, value in val_generator.class_indices.items():
        writer.writerow([key, value])

#define Model
base_model = EfficientNetB6(weights='imagenet', include_top=False,  input_shape=(224, 224, 3), pooling='avg')
x = Dense(NUM_CLASSES, activation='softmax')(base_model.output)

#model = keras.models.Sequential([
#    md,
#    keras.layers.Dense(NUM_CLASSES, activation='softmax')
#])
model = Model(inputs=base_model.input, outputs=x)
# summarize layers
print(model.summary())

earlystop=EarlyStopping(patience=3) 
learning_rate_reduction=ReduceLROnPlateau(monitor='loss',patience=2,verbose=1,factor=0.1,min_lr=0.0000000001) 
callback=[learning_rate_reduction]

model.compile(optimizer=Adam(lr=0.00001),loss='categorical_crossentropy', metrics=['accuracy'])

step_size_train=train_generator.n//train_generator.batch_size
step_size_val=val_generator.n//val_generator.batch_size
history = model.fit_generator(generator=train_generator, steps_per_epoch=step_size_train, validation_data=val_generator, validation_steps=step_size_val, epochs=1, callbacks=callback)
model.export(exported_model_folder)
model.save(saved_model_folder)
