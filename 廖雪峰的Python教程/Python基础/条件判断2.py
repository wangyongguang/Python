w = input('weight: ')
weight = int(w)
if weight < 18.5:
    print('过轻')
elif 18.5<=weight < 25:
    print('正常')
elif 25<=weight<28:
    print('过重')
elif 28<=weight<=32:
    print('肥胖')
else:
    print('严重肥胖')