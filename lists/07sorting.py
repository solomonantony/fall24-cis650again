c = [45, 26, 10, 72, 43]
print('before sort', c)
c.sort() #modified the list
print('after sort', c)
c.sort(reverse=True) #sorts in descending order
print('after descending sort', c)
c = [45, 26, 10, 72, 43]
c2 = sorted(c) #creates a sorted c; original c is unaffected
print('After sorted call', 'c', c, 'c2', c2)
