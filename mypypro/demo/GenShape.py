print('空心正方形')

for i in range(10):
    for j in range(10):
        if i == 0 or i ==9 :
            if j < 9:
                print(' *', end=' ')
            else:
                print(' *')
        else :
            if j == 0 :
                print(' *', end=' ')
            if 0 < j < 9:
                print('  ', end=' ')
            if j == 9:
                print(' *')

    #     j += 1
    # i += 1
