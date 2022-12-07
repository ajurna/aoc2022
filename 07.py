from dataclasses import dataclass, field
from typing import Optional, Dict

from aoc import get_input

data = get_input(7).splitlines()


@dataclass
class Folder:
    name: str
    parent: Optional["Folder"]
    subfolders: Dict[str, "Folder"] = field(default_factory=dict)
    files: Dict[str, int] = field(default_factory=dict)

    def size(self):
        size = sum(self.files.values())
        for subdir in self.subfolders.values():
            size += subdir.size()
        return size


base_dir = Folder(name='/', parent=None)
current_dir = base_dir
folders = [base_dir]
while data:
    command = data.pop(0).split()
    match command[1]:
        case "cd":
            if command[2] == '/':
                current_dir = base_dir
            elif command[2] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.subfolders[command[2]]
        case "ls":
            while len(data) > 0 and not data[0].startswith('$'):
                file_data = data.pop(0).split()
                if file_data[0] == "dir":
                    new_folder = Folder(name=file_data[1], parent=current_dir)
                    folders.append(new_folder)
                    current_dir.subfolders[file_data[1]] = new_folder
                else:
                    current_dir.files[file_data[1]] = int(file_data[0])


folders_sizes = sorted(f.size() for f in folders if f.size())
print("Part 1:", sum([f for f in folders_sizes if f <= 100000]))

target_size = 30000000 - (70000000 - base_dir.size())
print("Part 2:", [f for f in folders_sizes if f > target_size][0])