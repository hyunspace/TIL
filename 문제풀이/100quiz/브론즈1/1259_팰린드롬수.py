while True:
    number = input()
    if number == '0':
        break
    check_number = number[::-1]
    if number == check_number:
        print('yes')
    else:
        print('no')