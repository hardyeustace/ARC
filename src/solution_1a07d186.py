
# coding: utf-8

# In[144]:


import pandas as pd
import json
import numpy as np
# from itertools import izip

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
    for line_colour in all_colours:
        all_colours.remove(line_colour)
    #for all other colours, (i.e. those not back ground colour of zero of line colours) turn to back ground colour = 0
    for each_colour in all_colours:
        ip[each_colour] = 0
    return ip

def solve(ip):    
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
        for colour_points_array in colour_points_arrays:
            each_colour_lines = [i[1] for i in colour_lines]
            print(each_colour_lines)
            print(colour_points_array[0], colour_points_array[1])
            print(new_row(1, each_colour_lines))
#             print(new_row(colour_points_array[0], [i[1] for i in colour_lines]), colour_points_array[1])
            
#         print(type(colour_points_arrays[0][0]), type(colour_points_arrays[0][1]))
#        print(colour_points_arrays[0][0], colour_points_arrays[0][1])
#         print(colour_points_arrays[0][0], colour_points_arrays[0][1])
#         print(colour_lines)
#         print(new_row(colour_points_arrays[0][0], [2]), colour_points_arrays[0][1])
#         print(list(colour_points_arrays[0][1]).element(2))
#         [x for x in mylist if x in pattern]
#         print(ip[(1, 2, 3), (2, 3, 4)])
#         print(ip[[1, 2], [2, 2]])
#         print(ip[np.array([1, 2]), np.array([2, 2])])
#         print(ncolour_points_arrays[0][0])
#         print(ip[colour_points_arrays[0][0], colour_points_arrays[0][1]])
#         print(ip[[colour_points_array[0]][colour_points_array[1]]])
#         print(colour_points_arrays[1])
#         for i in range(0, len(colour_points_arrays)):
            #here we zip toget the double array of row and column indexes to get a list of tuples with the x, y coordinates of 
            #the colours
#             colour_points = list(zip(colour_points_arrays[i][0], colour_points_arrays[i][1]))        
#             moving_points = [colour_point for colour_point in colour_points if colour_point[0] != my_colour_line[1]]
#             new_points = [(my_colour_line[1] - 1 + (2 * int(moving_point[0] - my_colour_line[1] > 1)), moving_point[1]) for moving_point in moving_points]
#             ip[tuple(np.array(new_points).T)] = my_colour_line[0]
#             ip[tuple(np.array(moving_points).T)] = 0
    return ip
# addition = lambda x: x + 2
 
# a = numpy.array([1, 2, 3, 4, 5, 6])
 
# print("Array after addition function: ", addition(a))        

def new_row(x, colour_lines):
    """
    >>> new_row(0, [2, 4])
    1
    >>> new_row(2, [2, 3])
    2
    >>> new_row(1, [2, 1])
    1
    >>> new_row(1, [2])
    1
    >>> new_row(3, [2])
    3
    >>> new_row(4, [2])
    3
    >>> new_row(5, [2])
    3
    """
    nearest_row = find_min_diff(x, colour_lines)
    return nearest_row - int((x - nearest_row) < 0) + int((x - nearest_row) > 0)
    

def find_min_diff(x, data_points):
    """
    >>> find_min_diff(3, {44, 6, 8, 7, 15})
    6
    >>> find_min_diff(3, {1, 3, 8, 7, 5})
    3
    >>> find_min_diff(4, {2})
    2
    """
    diff = [(abs(dp - x), dp) for dp in data_points]
    return [y for x, y in diff if x==min(diff)[0]][0]
    
 
def main():
    df = read_json_file('C:/dev/git/ARC/data/training/1a07d186.json')
    np.array_equal(solve(df['train'][1]['input']), df['train'][1]['output'])
#     for df in df['train']:
#         print(np.array_equal(solve(df), df['output']))

    
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()    
    

