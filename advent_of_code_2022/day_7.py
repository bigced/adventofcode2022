from advent_of_code_2022.common import get_data_from_file


class Folder:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.children = []

    def __str__(self):
        return "%s %s" % (self.name, self.size)

    @property
    def size(self):
        size = sum([c.size for c in self.children])
        return size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def find_root(parent):
    return parent if parent.parent is None else find_root(parent.parent)


def cd(from_folder, to_folder):
    cwd = None
    if to_folder == "/":
        cwd = find_root(from_folder.parent) if from_folder.parent else from_folder
    elif to_folder == "..":
        cwd = from_folder.parent if from_folder.parent else from_folder

    else:
        for child in from_folder.children:
            if child.name == to_folder:
                cwd = child
    return cwd


def ls(cwd, data):
    for line in data.split("\n"):
        size, filename = line.split(" ")
        cwd.children.append(File(filename, int(size)))
    return cwd


def visitor(cwd, limit, list_of_folder):
    for child in cwd.children:
        if isinstance(child, Folder):
            print(child, child.size, limit)
        if isinstance(child, Folder):
            if child.size <= limit:
                list_of_folder.append(child)
            visitor(child, limit, list_of_folder)


def find_space_to_save(data, limit):
    cwd = Folder("root", None)
    for line in data.split("\n"):
        if line[0] == "$":
            if "cd" in line:
                _, cmd, to_folder = line.split(" ")
                cwd = cd(cwd, to_folder)
        else:
            if "dir" in line:
                new_folder = Folder(line.split(" ")[-1], cwd)
                cwd.children.append(new_folder)
            else:
                size, filename = line.split(" ")
                new_file = File(filename, int(size))
                cwd.children.append(new_file)

    cwd = cd(cwd, "/")
    list_of_folder = []
    visitor(cwd, limit, list_of_folder)
    return sum([f.size for f in list_of_folder])


def visitor2(cwd, list_of_folder):
    for child in cwd.children:
        if isinstance(child, Folder):
            list_of_folder.append(child)
            visitor2(child, list_of_folder)


def find_space_to_save2(data):
    cwd = Folder("root", None)
    for line in data.split("\n"):
        if line[0] == "$":
            if "cd" in line:
                _, cmd, to_folder = line.split(" ")
                cwd = cd(cwd, to_folder)
        else:
            if "dir" in line:
                new_folder = Folder(line.split(" ")[-1], cwd)
                cwd.children.append(new_folder)
            else:
                size, filename = line.split(" ")
                new_file = File(filename, int(size))
                cwd.children.append(new_file)

    cwd = cd(cwd, "/")

    free_space = 70000000 - cwd.size
    list_of_folder = []
    visitor2(cwd, list_of_folder)
    list_of_folder = [c.size for c in list_of_folder if c.size >= 30000000 - free_space]
    return min(list_of_folder)


def main(filename, limit):
    file_data = get_data_from_file(filename)
    space_to_save = find_space_to_save(file_data, limit)
    space_to_save2 = find_space_to_save2(file_data)
    print(f"File to save {space_to_save}")
    print(f"File to save2 {space_to_save2}")


if __name__ in "__main__":
    main("day_7.txt", 100000)
