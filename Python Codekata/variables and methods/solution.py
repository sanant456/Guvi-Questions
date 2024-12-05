a = input()

#.... YOUR CODE STARTS HERE ....

def binary_to_hex(binary_str):
    while len(binary_str)%4!=0:
        binary_str='0'+binary_str
    decimal_rep=int(binary_str,2)
    hex_rep=hex(decimal_rep)[2:]
    return hex_rep
print(binary_to_hex(a))

#.... YOUR CODE ENDS HERE ....
