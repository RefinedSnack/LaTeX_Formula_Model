import random
from typing import List
from configs import *
class EquationGenerator:
    def __init__(self) -> None:
        greek_letters_lower: List[str] = [
                            r'\alpha', r'\beta', r'\gamma', r'\delta', r'\epsilon', r'\zeta', r'\eta', r'\theta', 
                            r'\iota', r'\kappa', r'\lambda', r'\mu', r'\nu', r'\xi', r'\pi', r'\rho', r'\sigma', 
                            r'\tau', r'\upsilon', r'\phi', r'\chi', r'\psi', r'\omega'
                        ]
        greek_letters_upper: List[str] = [letter.capitalize() for letter in greek_letters_lower]
        self.greek_letters = []
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.digits_at_1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.two_digit_nums = [d1 + d2 for d1 in self.digits for d2 in self.digits]
        # self.three_digit_nums = [d1 + d2 for d1 in self.digits for d2 in self.two_digit_nums]
        # self.four_digit_nums_without_comma = [d1 + d2 for d1 in self.digits for d2 in self.three_digit_nums]
        # self.four_digit_nums_with_comma = [d1 + "," + d2 for d1 in self.digits for d2 in self.three_digit_nums]

        self.greek_letters.extend(greek_letters_lower)
        self.greek_letters.extend(greek_letters_upper)
        self.english_letters: List[str] = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        self.logical_symbols: List[str] =  [
                                r'\emptyset', r'\emptyset', r'\emptyset', r'\emptyset', r'\emptyset',
                                r'\emptyset', r'\mathbb{A}',
                                r'\mathbb{H}', r'\mathbb{O}', r'\mathbb{S}',
                                r'\in', r'\notin', r'\ni', r'\subset', r'\subseteq',
                                r'\supset', r'\supseteq', r'\cup', r'\cap', r'\setminus',
                                r'\exists', r'\exists!', r'\nexists', r'\forall', r'\neg',
                                r'\lor', r'\land', r'\Longrightarrow', r'\Rightarrow', r'\Longleftarrow',
                                r'\Leftarrow', r'\iff', r'\Leftrightarrow', r'\top', r'\bot'
                            ]
        self.unary_operators: List[str] = ['+', '-', '!', '\#']
        self.binary_operators: List[str] = [
                                r'\pm', r'\cap', r'\diamond', r'\oplus', r'\mp',
                                r'\cup', r'\bigtriangleup', r'\ominus', r'\times', r'\uplus',
                                r'\bigtriangledown', r'\otimes', r'\div', r'\sqcap', r'\triangleleft',
                                r'\oslash', r'\ast', r'\sqcup', r'\triangleright', r'\odot',
                                r'\star', r'\vee', r'\bigcirc', r'\circ', r'\dagger',
                                r'\wedge', r'\bullet', r'\setminus', r'\ddagger', r'\cdot',
                                r'\wr', r'\amalg'
                            ]
        self.negated_binary_operators: List[str] = [
                                r'\neq', r'\notin', r'\nless', r'\ngtr', r'\nleq',
                                r'\ngeq', r'\nleqslant', r'\ngeqslant', r'\nleqq', r'\ngeqq',
                                r'\lneq', r'\gneq', r'\lneqq', r'\gneqq', r'\lvertneqq',
                                r'\gvertneqq', r'\lnsim', r'\gnsim', r'\lnapprox', r'\gnapprox',
                                r'\nprec', r'\nsucc', r'\npreceq', r'\nsucceq', r'\precneqq',
                                r'\succneqq', r'\precnsim', r'\succnsim', r'\precnapprox', r'\succnapprox',
                                r'\nsim', r'\ncong', r'\nshortmid', r'\nshortparallel', r'\nmid',
                                r'\nparallel', r'\nvdash', r'\nvDash', r'\nVdash', r'\nVDash',
                                r'\ntriangleleft', r'\ntriangleright', r'\ntrianglelefteq', r'\ntrianglerighteq',
                                r'\nsubseteq', r'\nsupseteq', r'\nsubseteqq', r'\nsupseteqq',
                                r'\subsetneq', r'\supsetneq', r'\varsubsetneq', r'\varsupsetneq',
                                r'\subsetneqq', r'\supsetneqq', r'\varsubsetneqq', r'\varsupsetneqq'
                            ]
        self.arrows: List[str] = [r'\leftarrow', r'\rightarrow', r'\leftrightarrow', r'\uparrow', r'\downarrow', r'\updownarrow']
        self.relational_operators: List[str] = [
                            r'<', r'>', r'\nless', r'\ngtr', r'\leq',
                            r'\geq', r'\leqslant', r'\geqslant', r'\nleq',
                            r'\ngeq', r'\nleqslant', r'\ngeqslant', r'\prec',
                            r'\succ', r'\nprec', r'\nsucc', r'\preceq',
                            r'\succeq', r'\npreceq', r'\nsucceq', r'\ll',
                            r'\gg', r'\lll', r'\ggg', r'\subset',
                            r'\supset', r'\not \subset', r'\not \supset',
                            r'\subseteq', r'\supseteq', r'\nsubseteq',
                            r'\nsupseteq', r'\sqsubset', r'\sqsupset',
                            r'\sqsubseteq', r'\sqsupseteq', r'=', r'\doteq',
                            r'\equiv', r'\approx', r'\cong', r'\simeq',
                            r'\sim', r'\propto', r'\neq'
                            r'\parallel', r'\parallel', r'\nparallel', r'\nparallel', r'\asymp',
                            r'\asymp', r'\bowtie', r'\bowtie', r'\vdash', r'\vdash',
                            r'\dashv', r'\dashv', r'\in', r'\in', r'\ni',
                            r'\ni', r'\smile', r'\smile', r'\frown', r'\frown',
                            r'\models', r'\models', r'\notin', r'\notin', r'\perp',
                            r'\perp', r'\mid', r'\mid', r'\smile', r'\smile',
                            r'\frown', r'\frown', r'\models', r'\models', r'\notin',
                            r'\notin', r'\perp', r'\perp', r'\mid', r'\mid'
                        ]
        self.geometry: List[str] = [
                        r'\angle', r'\measuredangle', r'\triangle', r'\square',
                        r'\cong', r'\ncong', r'\sim', r'\nsim',
                        r'\|', r'\nparallel', r'\perp', r'\not\perp'
                    ]
        self.arethmetic_operators: List[str] = ['+', '-', r'\div', r'\times', "."]
        self.xyz: List[str] = ["x", "y", "z"]
        
        self.symbols: List[str] = []
        self.symbols.extend(LATEX_TO_CLASSES.keys())
        # self.symbols.extend(self.digits)
        # self.symbols.extend(self.arethmetic_operators)
        # self.symbols.extend(self.xyz)
        # self.symbols.extend(self.arrows)
        # self.symbols.extend(self.two_digit_nums)
        # self.symbols.extend(self.greek_letters)
        # self.symbols.extend(self.english_letters)
        # self.symbols.extend(self.logical_symbols)
        # self.symbols.extend(self.binary_operators)
        # self.symbols.extend(self.negated_binary_operators)
        # self.symbols.extend(self.arrows)
        # self.symbols.extend(self.relational_operators)
        # self.symbols.extend(self.geometry)
        # self.symbols.extend(self.unary_operators)
        # self.symbols.extend(self.three_digit_nums)
        # self.symbols.extend(self.four_digit_nums_without_comma)
        # self.symbols.extend(self.four_digit_nums_with_comma)

    def generate_random_symbol(self, num_symbols: int) -> str:
        return ' '.join(random.choices(self.symbols, k=num_symbols))

    def generate_fraction(self, numerator_symbols: str, denominator_symbols: str) -> str:
        return r'\frac{' + numerator_symbols + r'}{' + denominator_symbols + r'}'

    def generate_integral(self, upper: str, lower: str, contents: str) -> str:
        return r'\int_{' + upper + r'}^{' + lower + r'}' +  contents

    def generate_summation(self, upper: str, lower: str, contents: str) -> str:
        return r'\sum_{' + upper + r'}^{' + lower + r'}' + contents 
    
    def generate_product(self, upper: str, lower: str, contents: str) -> str:
        return r'\prod_{' + upper + r'}^{' + lower + r'}' + contents 
    
    def generate_super_string(self) -> str:
        return ' '.join(self.symbols)