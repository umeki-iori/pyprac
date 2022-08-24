def arrange_list(listname):
    arrayed_str = ''
    for i in range(len(listname) - 1):
        arrayed_str += f'{listname[i]}, '
        i += 1

    formed_str = arrayed_str + 'and ' + listname[-1]

    print(f"'{formed_str}'")

spam = ['apples', 'bananas', 'tofu', 'cats']
bacon = ['cat', 'dog', 233, 'Hunk', 'sushi']

arrange_list(bacon)