import os
import shutil
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor, TimeoutError, as_completed
import time

def convert_pdf_to_image(pdf_path, output_path, dpi=300, format='png', error_files=None, timeout=60):
    try:
        # Convert each page of the PDF to an image
        start_time = time.time()
        images = convert_from_path(pdf_path, dpi=dpi)
        end_time = time.time()
        
        # Save the first image
        images[0].save(output_path, format=format)
        print(f"Converted {pdf_path} to png (Time taken: {end_time - start_time:.2f} seconds)")
    except Exception as e:
        if error_files is not None:
            error_files.append(pdf_path)
        print(f"Error converting {pdf_path}: {e}")

def convert_pdfs_in_folder(input_folder, output_folder, delete_if_exists=True, timeout_per_file=60):
    error_files = []
    
    if delete_if_exists and os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    # List all PDF files in the input folder
    pdf_files = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith('.pdf')]
    try:
        # Create a thread pool with 16 threads
        with ThreadPoolExecutor(max_workers=16) as executor:
            # Submit each PDF file for conversion
            futures = {executor.submit(convert_pdf_to_image, pdf_file, os.path.join(output_folder, os.path.splitext(os.path.basename(pdf_file))[0] + '.png'), timeout=timeout_per_file): pdf_file for pdf_file in pdf_files}
            
            for future in as_completed(futures, timeout=timeout_per_file):
                try:
                    future.result()
                except TimeoutError:
                    print(f"Task {futures[future]} took too long and was terminated.")
                    error_files.append(futures[future])
                except Exception as e:
                    print(f"Error occurred: {e}")
    except:
        print("error")

    # Print summary of error files
    if error_files:
        print("Files with conversion errors:")
        for file in error_files:
            print(file)

# Example usage:
# convert_pdfs_in_folder('input_folder', 'output_folder')
