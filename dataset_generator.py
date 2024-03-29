from configs import *
from EquationGenerator import *
from image_segmenter import *
from PdfMaker import *
from convert_pdf_to_png import *

input_folder = 'dataset'  # Replace with the path to your input folder containing PDFs
output_folder = 'png_dataset'  # Replace with the path to your output folder for PNGs
width = 500  # Replace with the desired width in pixels
height = 500  # Replace with the desired height in pixels

# generate_data_set(500, 10)
# run_csv(KEY_CSV)

# convert_pdfs_in_folder(input_folder, output_folder)
# convert_pdf_to_image(input_folder+r"/0233.pdf", output_folder)

process_all_imgs("png_dataset", "dataset_with_classes")

