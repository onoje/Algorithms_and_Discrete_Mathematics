def base_convert(array):
    for i in array:
        binary = bin(i)
        hexadecimal = hex(i)
        binary_bits = -2
        for i in binary:
            binary_bits = binary_bits + 1
        hex_char = -2
        for i in hexadecimal:
            hex_char = hex_char + 1
        print (binary[2:], hexadecimal[2:], binary_bits, hex_char)
            
array = [5, 15, 255, 256, 1023 ,1024]
base_convert(array)
