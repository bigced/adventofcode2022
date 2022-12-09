from advent_of_code_2022.day_7 import Folder, cd, find_space_to_save, find_space_to_save2, ls


def test_cd_slash():
    root = Folder("/", None)
    child_directory = Folder("a", root)
    cwd = cd(child_directory, "/")
    assert cwd.name == "/"


def test_cd_child():
    root = Folder("/", None)
    root.children.append(Folder("a", root))

    cwd = cd(root, "a")
    assert cwd.name == "a"


def test_cd_dot_dot():
    root = Folder("/", None)
    a_folder = Folder("a", root)
    root.children.append(a_folder)
    b_folder = Folder("b", a_folder)

    cwd = cd(b_folder, "..")

    assert cwd.name == "a"

    cwd = cd(root, "..")
    assert cwd.name == "/"


def test_ls():
    data = """4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    root = Folder("/", None)
    root.children.append(Folder("a", root))
    cwd = cd(root, "a")
    cwd = ls(cwd, data)

    assert ["j", "d.log", "d.ext", "k"] == [f.name for f in cwd.children]
    assert cwd.children[0].size == 4060174

    assert cwd.size == 24933642

    cwd = cd(cwd, "/")
    assert cwd.size == 24933642


def test_process():
    data = """$ cd /
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
7214296 k"""
    assert 95437 == find_space_to_save(data, 100000)


def test_process2():
    data = """$ cd /
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
7214296 k"""
    assert 24933642 == find_space_to_save2(data)
