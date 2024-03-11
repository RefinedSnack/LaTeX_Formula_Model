import imp
import cv2 
import numpy as np
import concurrent
import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import csv
import random
from configs import *


def is_between(im1_x, im1_width, im2_x):
    if im1_x <= im2_x and im2_x <= im1_x+im1_width:
        return True
    return False

def merge(contour1, contour2, contour3) -> tuple[int,int,int,int]:
    x1, y1, w1, h1 = cv2.boundingRect(contour1)
    x2, y2, w2, h2 = cv2.boundingRect(contour2)
    x3, y3, w3, h3 = cv2.boundingRect(contour3)
    x = min([x1, x2, x3])
    y = min([y1, y2, y3])
    w = max([w1, w2, w3])
    h = max([h1, h2, h3]) + np.abs(max([y1, y2, y3]) - min(y1, y2, y3))
    return (x,y,w,h)

def segment_img(input_path: str, output_dir: str, delete_if_exists=True, boarder_size=BOARDER) -> None:
    if delete_if_exists and os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    # Read image
    image = cv2.imread(input_path)
    if SHOW_IMGS: cv2.imshow('original image', image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if SHOW_IMGS: cv2.imshow('gray image', gray)

    # Threshold the image to get binary image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours based on x-coordinate
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])



    skip1 = False
    skip2 = False
    num_skipped = 0

    # Iterate through each contour and save as individual image
    for i, contour in enumerate(contours):
        if skip1:
            skip1 = False
            num_skipped +=1 
            continue
        if skip2:
            skip2 = False
            num_skipped += 1
            continue
        # Get bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        if len(contours) - i > 2:
            x2, y2, w2, h2 = cv2.boundingRect(contours[i+1])
            x3, y3, w3, h3 = cv2.boundingRect(contours[i+2])
            if is_between(x, w, x2) and is_between(x, w, x3):
                x, y, w, h = merge(contour, contours[i+1], contours[i+2])
                skip1 = True
                skip2 = True
        # Crop the symbol region
        symbol = image[y-boarder_size:y+h+boarder_size, x-boarder_size:x+w+boarder_size]
        if SHOW_IMGS: cv2.imshow(f"image {i - num_skipped}", symbol)
        
        # Save the symbol as individual image
        cv2.imwrite(f'{output_dir}/symbol_{i - num_skipped}.png', symbol)

    if SHOW_IMGS: cv2.waitKey(0)
    print(f"processed img: {input_path}.")

def search_csv(csv_file, search_string):
    # Open the CSV file
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        # Loop through each row in the CSV
        for row in reader:
            # Check if the search string is in the first column
            if row and row[0] == search_string:
                return row
    # If the search string is not found, return None
    return None

def make_classes(output_dir, delete_if_exists=True):
    if delete_if_exists and os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    for key, value in CLASSES_TO_LATEX.items():
        place = f'{output_dir}/{key}'
        if delete_if_exists and os.path.exists(place):
            shutil.rmtree(place)
        os.makedirs(place, exist_ok=True)
        
def process_img(folder_path, file_name, output_dir, delete_if_exists=True):
    file_name_without_extension = os.path.splitext(file_name)[0]
    segment_img(f"{folder_path}/{file_name_without_extension}.png", TEMP_DIR, delete_if_exists, random.choice(range(1,10)))
    # new_output_dir = f"{output_dir}/{file_name_without_extension}"
    # if delete_if_exists and os.path.exists(new_output_dir):
    #     shutil.rmtree(new_output_dir)
    # os.makedirs(new_output_dir, exist_ok=True)
    result: list[str] = search_csv(KEY_CSV, file_name_without_extension)
    split_str: list[str] = result[1].split(' ')
    for i,val in enumerate(split_str):
        file_class = LATEX_TO_CLASSES[val]
        shutil.move(f'{TEMP_DIR}/symbol_{i}.png', f'{output_dir}/{file_class}/{file_name_without_extension}_{i}.png')
    # print(f"done with {file_name}")
    
def process_all_imgs(folder_path, output_dir, delete_if_exists=True):
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid directory.")
        return
    make_classes(output_dir, delete_if_exists)
    
    # List all files in the directory
    files = os.listdir(folder_path)

    # Print the files
    print("Files in folder:")
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue
        process_img(folder_path, file_name, output_dir, delete_if_exists)

# process_all_imgs("png_dataset", "dataset_with_classes")
# input_folder = 'dataset'  # Replace with the path to your input folder containing PDFs
# output_folder = 'png_dataset'  # Replace with the path to your output folder for PNGs
# width = 500  # Replace with the desired width in pixels
# height = 500  # Replace with the desired height in pixels

# convert_pdfs_in_folder(input_folder, output_folder, width, height)