integers_list = [int(x) for x in input("Enter integers separated by spaces: ").split()]
sum = 0
for ele in integers_list:
    sum += ele
avg = sum/len(integers_list)

file_name = 'numbers_data.txt'
with open(file_name,'w') as writer:
    writer.write(f'List: {integers_list}\n')
    writer.write(f'Sum: {sum}\n')
    writer.write(f'Average: {avg}')

with open(file_name,'r') as reader:
    line_list = reader.readline()
    line_sum = reader.readline()
    line_avg = reader.readline()
    print(line_list)
    print(line_sum)
    print(line_avg)