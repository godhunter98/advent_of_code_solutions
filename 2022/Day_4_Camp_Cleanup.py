from get_input import fetch_input
from tqdm import tqdm
enter = fetch_input(2022,4)

entries = enter.splitlines()

# Part-1 Solution
def part_1_solution(entry_input):
    count = 0
    for entry in tqdm(entry_input,colour='Green'):
        # print(entry)
        # break
        pairs= []
        for pair in entry.split(','):
            upper,lower = (pair.split('-'))
            upper,lower = int(upper),int(lower)
            ls_1 = [i for i in range(upper,lower+1)]
            pairs.append(ls_1)
            # print(ls_1)
        first_group,second_grouo = pairs
        # print(first_group,second_grouo)
        _,smaller_list = min((len(first_group),first_group),(len(second_grouo),second_grouo))
        _,larger_list = max((len(first_group),first_group),(len(second_grouo),second_grouo))
        # print(smaller_list,larger_list)
        inner_count = 0
        for i in smaller_list:
            if i in larger_list:
                inner_count+=1
        if inner_count==len(smaller_list):
            count+=1
    return count


print(part_1_solution(entries))