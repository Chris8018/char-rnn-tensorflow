"""




"""

location = 'txt/'
filename = 'mz_311_1.txt'
input_data = ''
output_data = []
string = 'sdf'

with open(location + filename, 'r', encoding="ISO-8859-1") as file:
    input_data = list(map(lambda s: s.replace('\n', ''), file.readlines()))

for i in range(0, len(input_data)):
    if input_data[i].find('Piano right') != -1:
        output_data.append('r {\n')
        while input_data[i].find('End_track') == -1:
            if input_data[i].find('Note_on_c') != -1:
                text = input_data[i].replace(',', '').split(' ')
                output_data.append('{pos} {note} {v}\n'
                                   .format(pos = text[1], note = text[4], v = text[5]))

            i += 1
        output_data.append('}\n\n')

    if input_data[i].find('Piano left') != -1:
        output_data.append('l {\n')
        while input_data[i].find('End_track') == -1:
            if input_data[i].find('Note_on_c') != -1:
                text = input_data[i].replace(',', '').split(' ')
                output_data.append('{pos} {note} {v}\n'
                                   .format(pos=text[1], note=text[4], v=text[5]))

            i += 1
        output_data.append('}\n')
    i += 1

with open('input.txt', 'w') as file:
    file.writelines(output_data)
