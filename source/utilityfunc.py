# File containing support functions for Pycrypt

import time
import random


def primegen(num_range):    # Generates all prime numbers till num_range
    width = num_range

    print("Width=", width)
    counter = 0
    num_list = []
    start_time = time.time()
    for i in range (3, width+1, 2):
        num_list.append(i)

    for prime in num_list:

        counter+=1
        for multiplyer in num_list[num_list.index(prime):]:

            try:
                num_list.remove(prime*multiplyer)
            except:
                if prime*multiplyer > width:
                    break
                print("Redundant!!!!!!!!!!!!!!!!!!!!!!1", multiplyer, " ", prime)
    num_list.insert(0, 2)
    print("--- %s seconds ---" % (time.time() - start_time))
    return num_list


def key_gen(length):
    # Credits: Jacob Wan
    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))





if __name__ == '__main__':
    print('A random string: ' + key_gen(10))
    print("Prime Num till 256:", primegen(256))