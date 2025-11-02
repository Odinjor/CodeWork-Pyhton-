# STUDENT name: Ugochukwu Odinjor
# Email: uodinjor1@student.gsu.edu
# CSCI 1301 – 52074
# Python Lab 5
# References: no one
def fathertime():
    h = int(input('HOURS> '))

    m = int(input('MINUTES> '))

    t = int(input('TIME> '))

    time_before = round((h + (m / 60)), 2)
    time_alarm = round((t /60), 2)
    time_after = time_before - time_alarm
    hours = int((time_after // 1))
    if hours < 10: 
        hours = f'{hours:02}'
    minutes = int(round(((round(time_after % 1, 2)) * 60), 0))
    print('OUTPUT')
    print('HOURS:', h, sep="")
    print('MINUTES:', m, sep="")
    print('ALARM:', t, sep="") 
    print('ALARM TIME: ', hours, ':', minutes, sep="")

fathertime()
'''
time_after = time_before - time_alarm
Syntax error: unsupported operand type(s) for -: 'str' and 'str'
time_after = f'{time_before:.2}' - f'{time_alarm:.02}
SyntaxError: unterminated string literal (detected at line 15)

'''
