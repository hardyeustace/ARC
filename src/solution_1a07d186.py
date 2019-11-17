
# coding: utf-8

# In[223]:


import pandas as pd
import json
import numpy as np
from sys import argv

def read_json_file(fileName):
    with open(fileName, 'r') as f:
        return json.load(f)   

def get_dominant_horizontal_line_colour(ip):
    """
    >>> get_dominant_horizontal_line_colour(np.array([[0,0,0], [1,1,1], [1,0,0], [2,2,2],[0,0,0]]))
    {1, 2}
    """
    #get unique list of colours per row
    row_info = ([np.unique(row) for row in ip])     
    # identify the whole colour lines, we do this if there is only one unique colour per line
    # and it is not 0 (background colour)
    # we return a set as we could have more than 1 line of a certain colour
    return set([token[0] for token in row_info if len(token)==1 and token[0] != 0])

def remove_unused_colours(ip, line_colours):
    """
    >>> remove_unused_colours(np.array([[0,0,3], [1,5,1], [2,0,6], [2,2,2],[4,4,0]]), {2, 4})
    array([[0, 0, 0],
           [0, 0, 0],
           [2, 0, 0],
           [2, 2, 2],
           [4, 4, 0]])
    """
    #get a list of all unique colours

    all_colours = list(np.unique(ip))
    #remove back ground colour 0
    all_colours.remove(0)
    #remove the line colours
    for line_colour in line_colours:
        all_colours.remove(line_colour)
            
    #for all other colours, (i.e. those not back ground colour of zero of line colours) turn to back ground colour = 0
    for each_colour in all_colours:
        ip[np.where(ip == each_colour)]= 0
    return ip

def solve(my_ip):    
    ip = np.array(my_ip)
    #et the horizontal colours
    horizontal_line_colours = get_dominant_horizontal_line_colour(ip)
    #if there are horizontal line colours, it will tell us if it is horizontal or not
    is_horizontal = (len(horizontal_line_colours) > 0)
    #if not transpose the matrix and get the horizontal line colour
    if(not(is_horizontal)):
        #transpose ip and treat as if horizontal and then transpose back at end
        ip = np.transpose(ip)        
        horizontal_line_colours = get_dominant_horizontal_line_colour(ip)
               
    #remove all colours that are not background colour or full line colours
    ip = remove_unused_colours(ip, horizontal_line_colours)
    #move the floating point colours to the line
    ip = stick_float_points_to_lines(ip, horizontal_line_colours)
    #transpose the matrix back if its not horizontal
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
    for each_colour in other_colours:        
        #colours lines is a tuple which tells us colour and the line number(s) that colour is on
        colour_lines = ([(each_colour, index) for index, value in enumerate(ip) if np.array_equal(value, [each_colour] * len(ip[0]))])        
        #colour_points_arrays is a list of a double array, where the double array contains the row and coloumn indexes where the 
        #line colours are present
        colour_points_arrays = [np.where(ip == each_colour)]  
        new_rows = new_row(colour_points_arrays[0][0], [i[1] for i in colour_lines])
        #clear the old rows
        for each_obj in list(zip(colour_points_arrays[0][0], colour_points_arrays[0][1])):
            ip[each_obj] = 0
        #populate the new
        for each_obj in list(zip(new_rows, colour_points_arrays[0][1])):
            ip[each_obj] = each_colour


    return ip
      

def new_row(current_rows, colour_lines):
    """
    >>> new_row([0], np.array([2, 4]))
    [1]
    >>> new_row([2], np.array([2, 3]))
    [2]
    >>> new_row([1], np.array([2, 1]))
    [1]
    >>> new_row([1], np.array([2]))
    [1]
    >>> new_row([3], np.array([2]))
    [3]
    >>> new_row([4], np.array([2]))
    [3]
    >>> new_row([5], np.array([2]))
    [3]
    >>> new_row([2, 0, 6], np.array([4, 2]))
    [2, 1, 5]
    """
    nearest_rows = find_min_diff(current_rows, colour_lines)
    return [nearest_row - int((current_row - nearest_row) < 0) + int((current_row - nearest_row) > 0) for current_row, nearest_row in zip(current_rows, nearest_rows)]

    

def find_min_diff(rows, dps):
    """
    >>> find_min_diff([3], np.array([44, 6, 8, 7, 15]))
    [6]
    >>> find_min_diff([3], np.array([1, 3, 8, 7, 5]))
    [3]
    >>> find_min_diff([4], np.array([2]))
    [2]
    >>> find_min_diff([4, 3, 8], np.array([44, 6, 8, 7, 15]))
    [6, 6, 8]
    """
    row_diffs = [(abs(dps - row)) for row in rows]
    row_indexes = ([np.argmin(row_diff) for row_diff in row_diffs])
    return [dps[row_index] for row_index in row_indexes]
    
 
def main():
    df = read_json_file(argv[1])
    for df1 in df['train']:
        print(solve(df1))
        print() 
    for df2 in df['test']:
        print(solve(df1))
        print() 
    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

  
    

