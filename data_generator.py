import matplotlib.pyplot as plt
import random
import subprocess
import tempfile
import os

def generate_latex_equation(num_symbols):
    symbols = []
    greek_letters_lower = [r'\alpha', r'\beta', r'\gamma', r'\delta', r'\epsilon', r'\zeta', r'\eta', r'\theta', 
                     r'\iota', r'\kappa', r'\lambda', r'\mu', r'\nu', r'\xi', r'\pi', r'\rho', r'\sigma', 
                     r'\tau', r'\upsilon', r'\phi', r'\chi', r'\psi', r'\omega']
    greek_letters_upper = [letter.capitalize() for letter in greek_letters_lower]
    english_letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    symbols.extend(greek_letters_lower)
    symbols.extend(greek_letters_upper)
    symbols.extend(english_letters)
    
    logical_symbols = [r'\land', r'\lor', r'\neg', r'\rightarrow', r'\leftrightarrow']
    binary_operators = [r'\oplus', r'\ominus', r'\otimes', r'\oslash', r'\odot', r'\circ']
    arrows = [r'\leftarrow', r'\rightarrow', r'\leftrightarrow', r'\uparrow', r'\downarrow', r'\updownarrow']
    
    
    if num_symbols <= 1:
        # Base case: If the number of symbols is 1 or less, return a single symbol
        return random.choice(symbols)
    
    equation = ''
    
    for _ in range(num_symbols):
        symbol_type = random.choice(['symbols', 'logical', 'binary_operator', 'arrow', 'integral', 'summation', 'number', 'fraction'])
        if symbol_type == 'fraction':
            numerator = generate_latex_equation(2)
            denominator = generate_latex_equation(2)
            equation += r'\frac{' + numerator + r'}{' + denominator + r'}'
        elif symbol_type == 'integral':
            upper_symbols = num_symbols // 2
            lower_symbols = num_symbols - upper_symbols
            upper_part = generate_latex_equation(upper_symbols)
            lower_part = generate_latex_equation(lower_symbols)
            equation += r'\int_{' + upper_part + r'}^{' + lower_part + r'}'
        elif symbol_type == 'summation':
            upper_part = generate_latex_equation(1)
            lower_part = generate_latex_equation(1)
            equation += r'\sum_{' + upper_part + r'}^{' + lower_part + r'}'
        elif symbol_type == 'symbols':
            equation += random.choice(symbols)
        elif symbol_type == 'logical':
            equation += random.choice(logical_symbols)
        elif symbol_type == 'binary_operator':
            equation += random.choice(binary_operators)
        elif symbol_type == 'arrow':
            equation += random.choice(arrows)
        elif symbol_type == 'number':
            number_type = random.choice(['integer', 'decimal', 'scientific'])
            if number_type == 'integer':
                equation += str(random.randint(-10000, 10000))  # Generating integers between -10000 and 10000
            elif number_type == 'decimal':
                equation += "{:.2f}".format(random.uniform(-10000, 10000))  # Generating decimals with two decimal places between -10000 and 10000
            elif number_type == 'scientific':
                coefficient = random.uniform(-10, 10)  # Generating coefficient between -10 and 10
                exponent = random.randint(-10, 10)  # Generating exponent between -10 and 10
                equation += "{:.2e}".format(coefficient * (10 ** exponent))  # Scientific notation with two decimal places
        equation += ' '

    return equation.strip()




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
    with open('equation.tex', 'w') as f:
        f.write(latex_code)
    
    # Compile LaTeX code into a PDF file
    subprocess.run(['pdflatex', '-halt-on-error', 'equation.tex'])
    
    # Move the generated PDF file to the desired location
    pdf_file = 'equation.pdf'
    subprocess.run(['mv', pdf_file, filename])

# Example usage:
eq = generate_latex_equation(20)
print(eq)
render_latex_equation_to_pdf("output/Equation.pdf", eq)
