import matplotlib.pyplot as plt
import random
import subprocess
import tempfile
import os
from EquationGenerator import EquationGenerator
from typing import List
import csv
import shutil
import threading
import concurrent
from concurrent.futures import ThreadPoolExecutor





def render_latex_equation_to_pdf(filename, latex_equation):
    
    latex_template = r"""
    \documentclass{{standalone}}
    \usepackage{{amsmath}}
    \usepackage{{amsfonts}}
    \usepackage{{amssymb}}
    \begin{{document}}
    \huge
    ${}$
    \end{{document}}
    """
    
    latex_code = latex_template.format(latex_equation)
    
    # Write LaTeX code to a temporary .tex file
    with open(f'tex/{filename}.tex', 'w') as f:
        f.write(latex_code)
    
    # Compile LaTeX code into a PDF file
    subprocess.run(['pdflatex', '-halt-on-error', '-output-directory', "logs", f'tex/{filename}.tex'])
    # subprocess.run(['pdflatex', '-halt-on-error', '-output-directory', "logs", f'tex/{filename}.tex'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Move the generated PDF file to the desired location
    pdf_file = f'logs/{filename}.pdf'  # Corrected line
    subprocess.run(['mv', pdf_file, f'dataset/{filename}.pdf'])
    print(f"done with {filename}")


def pad_int_to_4_digits(num: int) -> str:
    return f"{num:04d}"

def create_csv_from_list_of_lists(data: List[List[str]], filename: str) -> None:
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def append_to_csv(data: List[str], filename: str) -> None:
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def test_all_symbols():
    equation_generator: EquationGenerator = EquationGenerator()
    eq: str = equation_generator.generate_super_string()
    print(eq)
    render_latex_equation_to_pdf(f"output/Equation.pdf", eq)


    
def csv_to_list(csv_file_path: str) -> List[List[str]]:
    data: List[List[str]] = []
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def generate_pdf(x: int, eq: str):
    render_latex_equation_to_pdf(f"{pad_int_to_4_digits(x)}", eq)
    
def run_csv(csv_filename):
    data: List[List[str]] = csv_to_list(csv_filename)
    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(generate_pdf, int(filename), equation) for filename, equation in data]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")

def generate_data_set(num_files, max_num_symbols):
    if os.path.exists("dataset"):
        shutil.rmtree("dataset")
    os.makedirs("dataset", exist_ok=True)
    output: List[List[str]] = []
    create_csv_from_list_of_lists(output, "key.csv")
    equation_generator: EquationGenerator = EquationGenerator()
    next_x: int = 0
    for i, eq in enumerate(equation_generator.symbols):
        print((pad_int_to_4_digits(i),eq))
        append_to_csv([pad_int_to_4_digits(i),eq], "key.csv")
        next_x += 1
    
    for num_symbols in range(2, max_num_symbols+1):
        for _ in range(num_files):
            eq: str = equation_generator.generate_random_symbol(num_symbols)
            print((pad_int_to_4_digits(next_x),eq))
            append_to_csv([pad_int_to_4_digits(next_x),eq], "key.csv")
            next_x += 1

    for _ in range(num_files):
        top: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        bot: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        eq = equation_generator.generate_fraction(top, bot)
        print((pad_int_to_4_digits(next_x),eq))
        append_to_csv([pad_int_to_4_digits(next_x),eq], "key.csv")
        next_x += 1
    
    for _ in range(num_files):
        top: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        bot: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        cent: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        eq = equation_generator.generate_integral(top, bot, cent)
        print((pad_int_to_4_digits(next_x),eq))
        append_to_csv([pad_int_to_4_digits(next_x),eq], "key.csv")
        next_x += 1
    
    for _ in range(num_files):
        top: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        bot: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        cent: str = equation_generator.generate_random_symbol(random.choice([1,2,3]))
        eq = equation_generator.generate_summation(top, bot, cent)
        print((pad_int_to_4_digits(next_x),eq))
        append_to_csv([pad_int_to_4_digits(next_x),eq], "key.csv")
        next_x += 1

    
    


# test_all_symbols()
# generate_data_set(1000, 5)
# run_csv("key.csv")
generate_pdf(2008, "15 \dashv I")