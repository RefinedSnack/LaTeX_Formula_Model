
CLASSES_TO_LATEX : dict[str, str] = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'plus': '+', 
    'subtraction': '-', 
    'division': r'\div', 
    'multiplication': r'\times', 
    'dot': '.',
    'x': 'x', 
    'y': 'y', 
    'z': 'z',
    # 'equals': '=',
    "leftarrow": r'\leftarrow', 
    "rightarrow": r'\rightarrow', 
    "leftrightarrow": r'\leftrightarrow', 
    "uparrow": r'\uparrow', 
    "downarrow": r'\downarrow', 
    "updownarrow": r'\updownarrow'
}
LATEX_TO_CLASSES : dict[str, str] = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '+': 'plus', 
    '-': 'subtraction', 
    r'\div': 'division', 
    r'\times': 'multiplication', 
    '.': 'dot',
    'x': 'x', 
    'y': 'y', 
    'z': 'z',
    # '=': 'equals',
    r"\leftarrow": 'leftarrow', 
    r"\rightarrow": 'rightarrow', 
    r"\leftrightarrow": 'leftrightarrow', 
    r"\uparrow": 'uparrow', 
    r"\downarrow": 'downarrow', 
    r"\updownarrow": 'updownarrow'
}

KEY_CSV: str = "key.csv"
BOARDER: int = 2
SHOW_IMGS = False
TEMP_DIR = "temp_dir"

POSITION_TO_CLASS: dict[int, str] = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'plus',
    11: 'dot',
    12: 'division', 
    13: 'z', 
    14: 'multiplication',
    15: 'subtraction', 
    16: 'x', 
    17: 'y',
    
}
    
