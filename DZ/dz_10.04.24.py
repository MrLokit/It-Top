def swap_lines_in_file(filename, pos1, pos2):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) >= pos1 and len(lines) >= pos2:
        temp = lines[pos2 - 1]
        lines[pos2 - 1] = lines[pos1 - 1]
        lines[pos1 - 1] = temp

        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print("Успешно.")
    else:
        print("Ошибка.")

filename = 'fordz_10.04.24.txt'
pos1 = 2
pos2 = 3

swap_lines_in_file(filename, pos1, pos2)
