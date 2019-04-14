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
    TRACK_NUM, POSITION, Note_on_c, 0, NOTE, VELOCITY
    ==> POSITION NOTE VELOCITY


"""






# def hello(name: str) -> str:
#     """
#     :param name:
#     :return:
#     """
#     return 'hello {0}'.format(name)
#
#
# hello('sdf')