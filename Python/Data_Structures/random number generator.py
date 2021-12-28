def gen_8_bit_random(n):
    output = []
    state = (1 << 7) | 1
    for i in range(n):
        output.append((state))
        newbit = (state ^ (state >> 4) ^ (state >> 5) ^ (state >> 6) ^ (state >> 8)) & 1
        state = (state >> 1) | (newbit << 7)
    return output
    
    
def main():
    size = int(input('Enter the amount of numbers you want to generate: '))
    arr = gen_8_bit_random(size)
    if arr != 0:
        print('8-BIT RANDOM NUMBER GENERATOR')
        print('{:<10s}{:<10s}'.format('BINARY', 'DECIMAL'))
        for i in range(size):
            print('{:<10b}{:<10d}'.format(arr[i], arr[i]))
            
    print('{:d} DIFFERENT NUMBERS'.format(len(set(arr))))

main()