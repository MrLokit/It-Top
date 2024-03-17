str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования'
str2 = list(str1)
for i in range(len(str2)):
    if str2[i] == 'N':
        str2[i] = 'P'
str2 = ''.join(str2)

print(f'str1 = {str1}')
print(f'str2 = {str2}')
