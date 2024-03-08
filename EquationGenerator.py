import random
from typing import List

class EquationGenerator:
    def __init__(self) -> None:
        self.greek_letters_lower: List[str] = [r'\alpha', r'\beta', r'\gamma', r'\delta', r'\epsilon', r'\zeta', r'\eta', r'\theta', 
                             r'\iota', r'\kappa', r'\lambda', r'\mu', r'\nu', r'\xi', r'\pi', r'\rho', r'\sigma', 
                             r'\tau', r'\upsilon', r'\phi', r'\chi', r'\psi', r'\omega']
        self.greek_letters_upper: List[str] = [letter.capitalize() for letter in self.greek_letters_lower]
        self.english_letters: List[str] = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        self.logical_symbols: List[str] = [r'\land', r'\lor', r'\neg', r'\rightarrow', r'\leftrightarrow']
        self.binary_operators: List[str] = [r'\oplus', r'\ominus', r'\otimes', r'\oslash', r'\odot', r'\circ']
        self.arrows: List[str] = [r'\leftarrow', r'\rightarrow', r'\leftrightarrow', r'\uparrow', r'\downarrow', r'\updownarrow']

    def generate_random_symbol(self, num_symbols: int) -> str:
        symbols = self.greek_letters_lower + self.greek_letters_upper + self.english_letters
        return ' '.join(random.choices(symbols, k=num_symbols))

    def generate_greek_symbol(self, num_symbols: int) -> str:
        return ' '.join(random.choices(self.greek_letters_lower, k=num_symbols))

    def generate_english_letter(self, num_symbols: int) -> str:
        return ' '.join(random.choices(self.english_letters, k=num_symbols))

    def generate_logical_symbol(self, num_symbols: int) -> str:
        return ' '.join(random.choices(self.logical_symbols, k=num_symbols))

    def generate_binary_operator(self, num_symbols: int) -> str:
        return ' '.join(random.choices(self.binary_operators, k=num_symbols))

    def generate_arrow(self, num_symbols: int) -> str:
        return ' '.join(random.choices(self.arrows, k=num_symbols))

    def generate_fraction(self, numerator_symbols: int, denominator_symbols: int) -> str:
        numerator = self.generate_random_symbol(numerator_symbols)
        denominator = self.generate_random_symbol(denominator_symbols)
        return r'\frac{' + numerator + r'}{' + denominator + r'}'

    def generate_integral(self, upper_symbols: int, lower_symbols: int) -> str:
        upper_part = self.generate_random_symbol(upper_symbols)
        lower_part = self.generate_random_symbol(lower_symbols)
        return r'\int_{' + upper_part + r'}^{' + lower_part + r'}'

    def generate_summation(self, upper_symbols: int, lower_symbols: int) -> str:
        upper_part = self.generate_random_symbol(upper_symbols)
        lower_part = self.generate_random_symbol(lower_symbols)
        return r'\sum_{' + upper_part + r'}^{' + lower_part + r'}'
    
    def generate_super_string(self) -> str:
        equation_parts = [
            self.generate_greek_symbol(num_symbols),
            self.generate_english_letter(num_symbols),
            self.generate_logical_symbol(num_symbols),
            self.generate_binary_operator(num_symbols),
            self.generate_arrow(num_symbols),
        ]
        return ' '.join(equation_parts)


# Example usage:
equation_generator = EquationGenerator()
print("Random Symbol:", equation_generator.generate_random_symbol(5))
print("Greek Symbol:", equation_generator.generate_greek_symbol(3))
print("English Letter:", equation_generator.generate_english_letter(4))
print("Logical Symbol:", equation_generator.generate_logical_symbol(2))
print("Binary Operator:", equation_generator.generate_binary_operator(3))
print("Arrow:", equation_generator.generate_arrow(1))
print("Fraction:", equation_generator.generate_fraction(2, 3))
print("Integral:", equation_generator.generate_integral(2, 2))
print("Summation:", equation_generator.generate_summation(1, 1))
