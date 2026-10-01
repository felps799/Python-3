while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('----'*20)
    for i in range (0,11,1):
        print(f'{num} x {i} = {num*i}')
    print('----'*20)

