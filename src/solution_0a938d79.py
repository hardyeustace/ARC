
# coding: utf-8

# In[14]:


import pandas as pd
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
    """
    >>> solve(np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]))
    array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 3, 3, 3, 3, 3, 3, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 3, 3, 3, 3, 3, 3, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 3, 3, 3, 3, 3, 3, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 3, 3, 3, 3, 3, 3, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2, 2]])
    """
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
#     USED FOR TESTING    
#     df1 = read_json_file("c:/dev/git/ARC/data/training/0a938d79.json")     
#     for df in df1['train']:
#         print(np.array_equal(solve(df['input']), df['output']))
#     for df in df1['test']:
#         print(np.array_equal(solve(df['input']), df['output']))

    df = read_json_file(argv[1])
    
    for df1 in df['train']:
        for row in solve(df1['input']):
            print(' '.join(map(str, row)))
        print() 
    for df2 in df['test']:
        for row in solve(df2['input']):
            print(' '.join(map(str, row)))
        print() 
    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

