from enum import Enum

_colors = {
    'Blue':'C0',
    'Black':'k',
    'Red':'C3',
    'Green':'C2',
    'Purple':'C4',
    'Orange':'C1',
    'Gray':'gray'
}

Color = Enum('Color', 
            [(n, v) for n, v in _colors.items()], 
            type=str)