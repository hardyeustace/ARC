
# coding: utf-8

# In[17]:


import pandas as pd
import json
import numpy as np


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
    ip = np.array(df_io['input'])
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
    df = read_json_file('C:/dev/git/ARC/data/training/0a938d79.json')
    for df in df['train']:
        print(np.array_equal(solve(df), df['output']))
#     print(np.array_equal(solve(df['train'][1]), df['train'][1]['output']))
    
    
#     for input_output in df['train']:
#         print(input_output)
    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

