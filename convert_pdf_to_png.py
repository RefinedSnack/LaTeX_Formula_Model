import os
import shutil
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor

def convert_pdf_to_image(pdf_path, output_path, width, height, dpi=300, format='png'):
    # Convert each page of the PDF to an image
    images = convert_from_path(pdf_path, dpi=dpi)
    
    # Resize each image to the specified width and height
    # resized_images = [image.resize((width, height)) for image in images]
    
    # Save the resized images
    images[0].save(output_path, format=format)
    print(f"Converted {output_path}.pdf to png")
        
def convert_pdfs_in_folder(input_folder, output_folder, width, height, delete_if_exists=True):
    if delete_if_exists and os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    # List all PDF files in the input folder
    pdf_files = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith('.pdf')]

    # Create a thread pool with 16 threads
    with ThreadPoolExecutor(max_workers=16) as executor:
        # Submit each PDF file for conversion
        for pdf_file in pdf_files:
            output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(pdf_file))[0] + '.png')
            executor.submit(convert_pdf_to_image, pdf_file, output_path, width, height)
            
