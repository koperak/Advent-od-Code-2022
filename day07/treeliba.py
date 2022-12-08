from treelib import Node, Tree
import re

data = open("input.txt").read().strip().split("\n")

operation_list = [
    ["zmianakatalogu", "^\$\ (.+)\ (.*)"],  # change directory [('cd', '/')]
    ["lista", "^\$\ ls$"],  # list [('ls', '')]
    ["pliki", "^(\d+)\ (.*)"],  # files and it sizes
    ["katalog", "^dir\ (.*)"],  # dir
]

filesystem = Tree()
#filesystem.create_node("/")

working_dir = filesystem.create_node("/")

for line in data:
    for op_name, operation in operation_list:
        parsed = re.findall(operation, line)
        if len(parsed) > 0:
            print(f"{line} - operacja: {op_name}, wynik: {parsed}")
            result = [op_name, parsed]
            continue

    operacja = result[0]
    wynik = result[1]

    match operacja:
        case "zmianakatalogu":
            if wynik[0][1] not in ["..", "/"]:
                # iterate over tags of successors of working_dir to find node id with tag == wynik[0][10]
                child_dir_list = [
                    x
                    for x in working_dir.successors(filesystem.identifier)
                    if filesystem.get_node(x).tag == wynik[0][1]
                ]

                if len(child_dir_list) != 1:
                    raise ValueError(
                        f"lista {child_dir_list} musi zawierać tylko 1 element"
                    )
                else:
                    working_dir = filesystem.get_node(child_dir_list[0])
            elif wynik[0][1] == ".." and not working_dir.is_root():
                if not working_dir.is_root():
                    parent_of_working = filesystem.parent(working_dir.identifier)
                    # before going up .. update parent of working directory size by summin working + parent
                    if parent_of_working.data == None:
                        parent_of_working.data = 0

                    parent_of_working.data += working_dir.data
                    working_dir = parent_of_working
        case "lista":
            pass
        case "pliki":
            if working_dir.data == None:
                working_dir.data = 0
                working_dir.data += int(wynik[0][0])
            else:
                working_dir.data += int(wynik[0][0])
        case "katalog":
            # if not filesystem.contains(wynik[0]):
            # nawet nie sprawdzam czy w aktualnym katalogu istnieje katalog wynik[0]
            filesystem.create_node(wynik[0], parent=working_dir)
        case _:
            print("coś jest nie tak")

filesystem.show()
print(sum([x.data for x in filesystem.filter_nodes(lambda x: x.data < 100000)]))
