
# coding: utf-8

# In[78]:


import pandas as pd
import json
import numpy as np


def read_json_file(fileName):
    with open(fileName, 'r') as f:
        return json.load(f)   
    
# def will_be_vertical_line(no_rows, rows):
#     """
#     >>> will_be_vertical_line(10, [0, 9])
#     True
#     >>> will_be_vertical_line(10, [2, 9])
#     False
#     """
#     return no_rows - 1 in rows and 0 in rows

def get_dominant_vertical_lines(ip):
    """
    >>> get_dominant_vertical_lines(np.array([[1,0,2], [1,0,2], [1,0,2], [1,0,2],[1,0,2]]))
    [1, 2]
    """    
    col_info = ([np.unique(col) for col in np.transpose(ip)])    
    return [token[0] for token in col_info if len(token)==1 and token[0] != 0]

def get_dominant_horizontal_lines(ip):
    """
    >>> get_dominant_horizontal_lines(np.array([[0,0,0], [1,1,1], [1,0,0], [2,2,2],[0,0,0]]))
    [1, 2]
    """
    row_info = ([np.unique(row) for row in ip]) 
    return [token[0] for token in row_info if len(token)==1 and token[0] != 0]



def solve(df_io):    
    """
    >>> get_dominant_horizontal_lines(np.array([[0,0,0], [1,1,1], [1,0,0], [2,2,2],[0,0,0]]))
    [1, 2]
    """
    ip = np.array(df_io['input'])
    horizontal_lines = get_dominant_horizontal_lines(ip)
    
    if(len(horizontal_lines) == 0):
        vertical_lines = get_dominant_vertical_lines(ip)
        ip[(ip != 0) & (ip != vertical_lines[0]) & (ip != vertical_lines[1])] = 0
    else:      
        ip[(ip != 0) & (ip != horizontal_lines[0]) & (ip != horizontal_lines[1])] = 0

    print(ip)
        
    ##arr[arr > 255] = x
    
#     min_require = min(ip.shape)
#     ip_counts = np.unique(ip, return_counts=True)
#     #find ip_counts that are < row count or col count, these are to be deleted
#     print(ip_counts[1])
#     to_delete = [i for i in range(len(a)) if a[i] > 2]
#     (rows, cols) = (np.nonzero(ip))
#     is_vertical = will_be_vertical_line(ip.shape[0], rows)
#     colours = (ip[rows[0]][cols[0]], ip[rows[1]][cols[1]])    
#     if (is_vertical):
#         col_diff = abs(cols[0] - cols[1]) * 2
#         ip[:, cols[0]::col_diff] = colours[0]
#         ip[:, cols[1]::col_diff] = colours[1]
#     else:
#         row_diff = abs(rows[0] - rows[1]) * 2
#         ip[rows[0]::row_diff] = colours[0]
#         ip[rows[1]::row_diff] = colours[1]
    
    return ip

def main():
    df = read_json_file('C:/dev/git/ARC/data/training/1a07d186.json')
    solve(df['train'][0])
#     for df in df['train']:
#         print(np.array_equal(solve(df), df['output']))
#     print(np.array_equal(solve(df['train'][1]), df['train'][1]['output']))
    
    
#     for input_output in df['train']:
#         print(input_output)
    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

