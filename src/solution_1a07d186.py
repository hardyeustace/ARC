
# coding: utf-8

# In[11]:


import pandas as pd
import json
import numpy as np
# from itertools import izip

def read_json_file(fileName):
    with open(fileName, 'r') as f:
        return json.load(f)   

def get_dominant_horizontal_lines(ip):
    """
    >>> get_dominant_horizontal_lines(np.array([[0,0,0], [1,1,1], [1,0,0], [2,2,2],[0,0,0]]))
    [1, 2]
    """
    row_info = ([np.unique(row) for row in ip]) 
    return [token[0] for token in row_info if len(token)==1 and token[0] != 0]

def remove_unused_colours(ip, other_colours):
    """
    >>> remove_unused_colours(np.array([[0,0,3], [1,5,1], [2,0,6], [2,2,2],[4,4,0]]), (2, 4))
    array([[0, 0, 0],
           [0, 0, 0],
           [2, 0, 0],
           [2, 2, 2],
           [4, 4, 0]])
    """
    
    ip[(ip != 0) & (ip != other_colours[0]) & (ip != other_colours[1])] = 0
    return ip

def solve(df_io):    
    ip = np.array(df_io['input'])
    horizontal_lines = get_dominant_horizontal_lines(ip)
    
    is_horizontal = (len(horizontal_lines) > 0)
    if(not(is_horizontal)):
        #transpose ip and treat as if horizontal and then transpose back at end
        ip = np.transpose(ip)
        horizontal_lines = get_dominant_horizontal_lines(ip)
               
          
    ip = remove_unused_colours(ip, horizontal_lines)
    row_info = ([np.unique(row) for row in ip])         
    ip = stick_float_points_to_lines(ip, horizontal_lines)
    
    if(not(is_horizontal)):
        ip = np.transpose(ip)
    
    return ip



def stick_float_points_to_lines(ip, other_colours):
    """
    >>> stick_float_points_to_lines(np.array([[0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [2, 2, 2, 2, 2], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[4,4,4,4,4], [0, 0, 0, 0, 0],[0, 0, 4, 0, 0]]), (2, 4))
    array([[0, 0, 0, 0, 0],
           [0, 0, 0, 2, 0],
           [2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [4, 4, 4, 4, 4],
           [0, 0, 4, 0, 0],
           [0, 0, 0, 0, 0]])
    """    
    colour_lines = ([(each_colour, index) for index, value in enumerate(ip) for each_colour in set(other_colours) if np.array_equal(value, [each_colour] * ip.shape[1])])    
    colour_points_arrays = [np.where(ip == each_colour) for each_colour in set(other_colours)]  

    for i in range(0, len(colour_points_arrays)):
        colour_points = list(zip(colour_points_arrays[i][0], colour_points_arrays[i][1]))
        my_colour_line = [colour_line for colour_line in colour_lines if colour_line[0] == ip[colour_points[0]]][0]
        moving_points = [colour_point for colour_point in colour_points if colour_point[0] != my_colour_line[1]]
        new_points = [(my_colour_line[1] - 1 + (2 * int(moving_point[0] - my_colour_line[1] > 1)), moving_point[1]) for moving_point in moving_points]
        ip[tuple(np.array(new_points).T)] = my_colour_line[0]
        ip[tuple(np.array(moving_points).T)] = 0
    return ip
        
 
def main():
    df = read_json_file('C:/dev/git/ARC/data/training/1a07d186.json')
    solve(df['train'][1])

    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

