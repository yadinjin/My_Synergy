str = input()
a = e = i = o = u =  0
for j in range(len(str)):
  if str[j] == 'a':
    a += 1
  elif str[j] == 'e':
    e += 1
  elif str[j] == 'i':
    i += 1
  elif str[j] == 'o':
    o += 1
  elif str[j] == 'u':
    u += 1
print('a - ',a,' e - ',e,' i - ',i,' o - ',o,' u - ',u) 