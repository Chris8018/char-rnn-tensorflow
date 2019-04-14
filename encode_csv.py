"""
Structure

note range 22 - 108
velocity 60 or 84
Real denominator - 2^denominator

0, 0, Header, 1, 3, CLOCK_PULSE_PER_QUARTER_NOTE
1, 0, Start_track
1, 0, Title_t, "XXXX"
1, 0, End_track

2, 0, Start_track
2, 0, Title_t, "Piano right"
2, XX, Note_on_c, 0, NOTE, VELOCITY
...
2, XX, End_track

3, 0, Start_track
3, 0, Title_t, "Piano left"
3, XX, Note_on_c, 0, NOTE, VELOCITY
...
3, XX, End_track

0, 0, End_of_file

Simplified version:
{

r {
XX NOTE VELOCITY
...
}

l {
XX NOTE VELOCITY
...
}

}


if "Piano right" or "Piano left" then from next line
while not "End_track"
if "Note_on_c" then
        0          1           2    3   4       5
    TRACK_NUM, POSITION, Note_on_c, 0, NOTE, VELOCITY
    ==> POSITION NOTE VELOCITY


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
