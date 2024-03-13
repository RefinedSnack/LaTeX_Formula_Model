import tensorflow as tf
from PIL import Image
import numpy as np
#load the training model
mod = tf.models.load_model('./trained_model')

#load and access the image
picloc = "./png_training_data/train/one_symbols/0025.png"
image = Image.open(picloc).resize((224,224)) #import and resize the impage
image.show()
image = np.expand_dims(np.array(image), axis=0) #adds batch dimensions and convert to numpy array
image = image / 255.0 # Normalize pixel values to [0,1]

prediction = mod.predict(image)
print(prediction)
