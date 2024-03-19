import tensorflow as tf
from PIL import Image
import numpy as np
from configs import *
from image_segmenter import segment_img

def lookup(index: int) -> str:
    return POSITION_TO_CLASS[index]
    
mod: tf.saved_model = None
def identify_image(file):
    global mod
    if mod == None:
        mod = tf.saved_model.load('./trained_model/')
    image = Image.open(file).resize((224,224))
    image = np.expand_dims(np.array(image), axis=0) #adds batch dimensions and convert to numpy array
    image = image / 255.0 # Normalize pixel values to [0,1]

    #convert image to tf.Tensor
    image = tf.convert_to_tensor(image, dtype=tf.float32)

    prediction = mod(image)
    # print(prediction)
    
    max_index = tf.argmax(prediction, axis = 1)

    return int(max_index)


    
    
def convert_to_LaTeX(png_file_path):
    # segement
    num_parts: int = segment_img(png_file_path, "temp_dir", delete_if_exists=True, boarder_size=3)
    # identify each part
    parts_classes: list[str] = []
    for i in range(num_parts):
        png_part = f"temp_dir\\symbol_{i}.png"
        x_class = identify_image(png_part)
        print(x_class)
        continue
        parts_classes.append(x)
        print(x)
    # combine
    parts_classes = [CLASSES_TO_LATEX[x] for x in parts_classes]
    print(f'${" ".join(parts_classes)}$')


def testall():
    lead = r'C:\Users\walte\Documents\cs470\Final_Project\archive\dataset_2 latex equations (simple_handwriting classes)\png_dataset\00'
    img_files = [f'{lead}{i:02}.png' for i in range(len(LATEX_TO_CLASSES))]

    for i,img_file in enumerate(img_files):
        # print(img_file)
        x = identify_image(img_file)
        
        print(i,x,lookup(x))

# # testall()
# convert_to_LaTeX(r'C:\Users\walte\Documents\cs470\Final_Project\archive\dataset_2 latex equations (simple_handwriting classes)\png_dataset\1169.png')
# convert_to_LaTeX(r'C:\Users\walte\Documents\cs470\Final_Project\archive\dataset_2 latex equations (simple_handwriting classes)\png_dataset\1170.png')
# convert_to_LaTeX(r'C:\Users\walte\Documents\cs470\Final_Project\archive\dataset_2 latex equations (simple_handwriting classes)\png_dataset\1171.png')
# convert_to_LaTeX(r'C:\Users\walte\Documents\cs470\Final_Project\archive\dataset_2 latex equations (simple_handwriting classes)\png_dataset\1172.png')