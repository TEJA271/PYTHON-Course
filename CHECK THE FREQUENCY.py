test_dict = {'My ' : 2 , 'Teacher' : 1 , 'Is' : 2 , 'Fun' : 2}

print('the original dictinary' + str(test_dict))

S = 2
res = 0
for key in test_dict:
    if test_dict[key] == S :
        res = res + 1

print("Frequency of S is :" + str(res))