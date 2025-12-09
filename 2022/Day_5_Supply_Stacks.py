from get_input import fetch_input

all_input = fetch_input(2022,5)

container_stack = '''
            [J] [Z] [G]            
            [Z] [T] [S] [P] [R]    
[R]         [Q] [V] [B] [G] [J]    
[W] [W]     [N] [L] [V] [W] [C]    
[F] [Q]     [T] [G] [C] [T] [T] [W]
[H] [D] [W] [W] [H] [T] [R] [M] [B]
[T] [G] [T] [R] [B] [P] [B] [G] [G]
[S] [S] [B] [D] [F] [L] [Z] [N] [L]
1   2   3   4   5   6   7   8   9 
'''

steps = all_input[313:]

def build_stack(container_stack):
    lines = container_stack.strip('\n').splitlines()
    crate_rows = lines[:-1]
    num_stacks = len(lines[-1].split())
    stacks = [[]for _ in range(num_stacks)]

    for row in crate_rows:
        for i in range(num_stacks):
            chunk = row[i*4:(i+1)*4]
            if '[' in chunk:
                crate = chunk[1]
                stacks[i].append(crate)
    for s in stacks:
        s.reverse()
    return stacks

# The move container function for part-1
def move_container_1(stacks:list,fr:int,to:int,count:int)->list:
    fr -=1
    to -=1
    for i in range(count):
        tbm = stacks[fr].pop()
        stacks[to].append(tbm)
    return stacks

# The move container function for part-2
def move_container_2(stacks:list,fr:int,to:int,count:int)->list:
    fr -=1
    to -=1
    if count == 1:
        tbm = stacks[fr].pop()
        stacks[to].append(tbm)
    else:
        tbm = stacks[fr][-count:]
        stacks[to].extend(tbm)
        stacks[fr]=stacks[fr][:-count]
    return stacks

def generate_final_message(processed_stacks):
    final_output = []
    for sublist in processed_stacks:
        val = sublist[-1]
        final_output.append(val)
    return ''.join(final_output)

def process_steps(steps:str,useful_stack):
    each_step = steps.splitlines()
    for step in each_step:
        _,count,_,fr,_,to = (step.split(' '))
        # move_container_1(useful_stack,int(fr),int(to),int(count)) #toggle accordingly for part-1 and part-2
        move_container_2(useful_stack,int(fr),int(to),int(count))
    return useful_stack

if __name__=="__main__":
    built_stack = build_stack(container_stack)
    processed_stack = process_steps(steps,built_stack)
    print(processed_stack)
    print(generate_final_message(processed_stack))

