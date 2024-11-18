s = input()
ch_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in ch_list:
        s = s.replace(i, '*')

print(len(s))