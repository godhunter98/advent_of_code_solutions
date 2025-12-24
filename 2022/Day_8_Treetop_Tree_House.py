from pprint import pprint
from get_input import fetch_input

sample_input = fetch_input(2022,8)
nee_input = '''30373
25512
65332
33549
35390
'''

def parse_input(sample:str)->list[list[int]]:
    ls_strings = []
    ls_ints = []
    for i in sample_input.splitlines():
        ls_strings.append(list(i))
    for i in ls_strings:
        intermittend_ls =[]
        for x in i:
            intermittend_ls.append(int(x))
        ls_ints.append(intermittend_ls)
    return ls_ints

def get_coordinates(ls:list)->list[list[list[int]]]:
    coordinates = []
    # This logic won't work as we're simply overwriting the old key.
    for x,sublist in enumerate(ls):
        sub_coordinates = []
        for y,nums in enumerate(sublist):
            sub_coordinates.append([x,y])
        coordinates.append(sub_coordinates)
    return coordinates

def neighbourhood(grid:list,r,c):
    curr = grid[r][c]
    row = grid [r]
    col = [grid[i][c] for i in range(len(grid))]
    left = row[:c]
    right  = row[c+1:]
    up = col[:r]
    down = col [r+1:]

    return curr,left,right,up,down

parsed_input = parse_input(sample_input)
coordinates = get_coordinates(parsed_input)

def is_visible(grid,r,c)-> bool:
    curr,left,right,up,down = neighbourhood(parsed_input,r,c)
    return (
        all(x < curr for x in left)
        or all(x < curr for x in right)
        or all(x < curr for x in up)
        or all(x < curr for x in down)
    )
    
def is_corners(grid,r,c):
    return r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[0]) - 1

print(sum(1 for r in range(len(parsed_input)) for c in range(len(parsed_input[0])) if is_visible(parsed_input,r,c) or is_corners(parsed_input,r,c)))