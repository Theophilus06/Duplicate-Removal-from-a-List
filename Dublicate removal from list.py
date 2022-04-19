print('How To Remove Dublicates In A list')
numbers = [1,3,5,6,5,2,1,7,8]
dubli = []
for number in numbers:
    if number not in dubli:
        dubli.append(number)
print(dubli)