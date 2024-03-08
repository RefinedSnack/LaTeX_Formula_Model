import os
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor

def convert_pdf_to_image(pdf_path, output_path, width, height, dpi=300, format='png'):
    # Convert each page of the PDF to an image
    images = convert_from_path(pdf_path, dpi=dpi)
    
    # Resize each image to the specified width and height
    resized_images = [image.resize((width, height)) for image in images]
    
    # Save the resized images
    resized_images[0].save(output_path, format=format)
    print(f"Done with {output_path}")
        
def convert_pdfs_in_folder(input_folder, output_folder, width, height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all PDF files in the input folder
    pdf_files = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith('.pdf')]

    # Create a thread pool with 16 threads
    with ThreadPoolExecutor(max_workers=16) as executor:
        # Submit each PDF file for conversion
        for pdf_file in pdf_files:
            output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(pdf_file))[0] + '.png')
            executor.submit(convert_pdf_to_image, pdf_file, output_path, width, height)
            

# Example usage:
input_folder = 'dataset'  # Replace with the path to your input folder containing PDFs
output_folder = 'png_dataset'  # Replace with the path to your output folder for PNGs
width = 500  # Replace with the desired width in pixels
height = 500  # Replace with the desired height in pixels

# convert_pdfs_in_folder(input_folder, output_folder, width, height)
convert_pdf_to_image("dataset/6358.pdf", output_folder + "/6358.png", width, height)
