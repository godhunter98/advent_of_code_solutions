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
    return [[int(ch) for ch in line.strip()] for line in sample.splitlines() if line.strip()]

# Both these functions, now use list comprehension, compressing our code down to just 4 lines from more than 20.

def get_coordinates(ls:list)->list[list[list[int]]]:
    return [[[x,y] for y,char in enumerate(sublist)]for x,sublist in enumerate(ls)]

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