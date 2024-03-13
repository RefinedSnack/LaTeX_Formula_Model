
CLASSES_TO_LATEX : dict[str, str] = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'plus': '+', 
    'subtraction': '-', 
    'division': r'\div', 
    'multiplication': r'\times', 
    'dot': '.',
    'x': 'x', 
    'y': 'y', 
    'z': 'z',
    "leftarrow": r'\leftarrow', 
    "rightarrow": r'\rightarrow', 
    "leftrightarrow": r'\leftrightarrow', 
    "uparrow": r'\uparrow', 
    "downarrow": r'\downarrow', 
    "updownarrow": r'\updownarrow'
}
LATEX_TO_CLASSES : dict[str, str] = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '+': 'plus', 
    '-': 'subtraction', 
    r'\div': 'division', 
    r'\times': 'multiplication', 
    '.': 'dot',
    'x': 'x', 
    'y': 'y', 
    'z': 'z',
    r'\leftarrow': "leftarrow", 
    r'\rightarrow': "rightarrow", 
    r'\leftrightarrow': "leftrightarrow", 
    r'\uparrow': "uparrow", 
    r'\downarrow': "downarrow", 
    r'\updownarrow': "updownarrow"
}

KEY_CSV: str = "key.csv"
BOARDER: int = 2
SHOW_IMGS = False
TEMP_DIR = "temp_dir"