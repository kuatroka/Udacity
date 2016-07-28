shift_right = 0b1100 >> 2
shift_left = 0b1 << 2

# Your code here!


print bin(shift_right)
print bin(shift_left)

## AND - & Operator - result lesser or igual to the smaller of two elements
print bin(0b1110 & 0b0101)

### OR - | operator = Greater then or iqual to the larger of two elements

print bin(0b1110 | 0b0101)

## return if certain bit is on or off. We do it by using mask where we set certain bit (counting from right) as 1
# then we use the "&" operator on the mask and the input

def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return 'on'
    return 'off'

print check_bit4(0b1010)

# turn on the third bit from the right
a = 0b10111011
mask = 0b100

desired = a | mask
print bin(desired)

## flipping the bits with XOR ^
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)

## slip and slide
def flip_bit(number, n):
    mask = (0b1 << n-1)
    slip = number ^ mask
    result = bin(slip)
    return result

###





