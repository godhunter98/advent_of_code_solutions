'''
How do we solve for this?

Sol. We will create a hash-map to store all of the meta-data of any file, like filesystem = {filename:{Parent:,Size:,if_directory:T/F}}
This meta-data will help us add up all the filesizes for a common directory and help us grab the associated filesizes.

TODO - Keep a running total of each directory size.

- 1. Check if the line is a command.
    - cd 'x' - we're currently inside the directory x
    - ls - the following will be names of files and directories inside x
    - cd.. we move a level up
- 2. At all points we should be a able to identify at which level of the filesystem we're in i.e how deep.
- 3. 
'''
from get_input import fetch_input


sample_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

sample_input = fetch_input(2022, 7)

def build_system_tree(sample_input):
    filesystem = {}
    current_path = []
    for line in sample_input.splitlines():
        if line.startswith('$'):
            parts = line.split()
            command = parts[1]
            if command == 'cd':
                dir_name = parts[2]
                if dir_name == '/':
                    current_path = ['/']
                elif dir_name == '..':
                    current_path.pop()
                else:
                    current_path.append(dir_name)
            elif command == 'ls':
                continue
        else:
            parts = line.split()
            if parts[0] == 'dir':
                dir_name = parts[1]
                path = '/'.join(current_path + [dir_name])
                filesystem[path] = {'Parent': '/'.join(current_path), 'Size': 0, 'if_directory': True}
            else:
                size = int(parts[0])
                file_name = parts[1]
                path = '/'.join(current_path + [file_name])
                filesystem[path] = {'Parent': '/'.join(current_path), 'Size': size, 'if_directory': False}
    return filesystem

def compute_directory_sizes(filesystem: dict) -> dict:
    # First, collect all files (snapshot, so it won't change)
    file_entries = [
        (path, meta)
        for path, meta in filesystem.items()
        if not meta['if_directory']
    ]

    for path, meta in file_entries:
        size = meta['Size']
        parent = meta['Parent']

        while parent:
            # If parent is missing, create it once
            if parent not in filesystem:
                filesystem[parent] = {
                    'Parent': '/'.join(parent.split('/')[:-1]) or '',
                    'Size': 0,
                    'if_directory': True,
                }
            filesystem[parent]['Size'] += size
            parent = filesystem[parent]['Parent']

    return filesystem



filesystem = build_system_tree(sample_input)
final_file_system = compute_directory_sizes(filesystem)
# print(final_file_system)
size = 0
for key, value in final_file_system.items():
    if value['if_directory'] and value['Size'] < 100000:
        size += value['Size']
print(size)