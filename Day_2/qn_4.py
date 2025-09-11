list_of_names = input("Enter list of names(separated by spaces): ")
names_list = list_of_names.split()
names_list.sort()
names_tuple = tuple(names_list)
file_name='names_data.txt'
with open(file_name,'w') as writer:
    writer.write(f'List: {names_list}\n')
    writer.write(f'Tuple: {names_tuple}')

with open(file_name,'r') as reader:
    line_list=reader.readline()
    line_tuple=reader.readline()
    print(line_list)
    print(line_tuple)