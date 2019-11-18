import json
import numpy as np
from sys import argv


def read_json_file(fileName):
    with open(fileName, 'r') as f:
        return json.load(f)   
    
def will_be_vertical_line(no_rows, rows):
    """
    >>> will_be_vertical_line(10, [0, 9])
    True
    >>> will_be_vertical_line(10, [2, 9])
    False
    """
    return no_rows - 1 in rows and 0 in rows
    
def solve(df_io):
    ip = np.array(df_io)
    (rows, cols) = (np.nonzero(ip))
    is_vertical = will_be_vertical_line(ip.shape[0], rows)
    colours = (ip[rows[0]][cols[0]], ip[rows[1]][cols[1]])    
    if (is_vertical):
        col_diff = abs(cols[0] - cols[1]) * 2
        ip[:, cols[0]::col_diff] = colours[0]
        ip[:, cols[1]::col_diff] = colours[1]
    else:
        row_diff = abs(rows[0] - rows[1]) * 2
        ip[rows[0]::row_diff] = colours[0]
        ip[rows[1]::row_diff] = colours[1]
    
    return ip


def main():
    df = read_json_file(argv[1])
    
    for df1 in df['train']:
        print(solve(df1['input']))
        print() 
    for df2 in df['test']:
        print(solve(df1['input']))
        print() 
    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

