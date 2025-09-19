# 25min~ spent

def getOneBits(n):
    """
    simple solution: find the binary representation
    - remainder method. find the highest power of 2 below n. recur on remainder until 1/0.
    - how to find highest power of 2? start with 
    """
    # Write your code here
    num_ones = 0
    one_pos = []
    curr_power = 6
    curr_pos = 1
    prev_power_of_2 = 2 ** curr_power #2^8 = 256
    while n > 0 and prev_power_of_2 > 0:
        print("n: ", n)
        print("num_ones: ", num_ones)
        print("one_pos: ", one_pos)
        print("curr_power: ", curr_power)
        print("curr_pos: ", curr_pos)
        print("prev_power_of_2: ", prev_power_of_2)
        print("-----")
        
        # prev_power_of_2 is highest 2^n below n
        if n >= prev_power_of_2 and n < prev_power_of_2 * 2:
            n -= prev_power_of_2
            num_ones += 1
            one_pos.append(curr_pos) #
            # we know n is less than half of prev_power_of_2 now
            prev_power_of_2 = prev_power_of_2 // 2
            curr_power -= 1
            curr_pos += 1
        elif n < prev_power_of_2:
            # we know n is less than half of prev_power_of_2 now
            prev_power_of_2 = prev_power_of_2 // 2
            curr_power -= 1
            curr_pos += 1
        else: #n > prev_power_of_2 by more than double. can only happen at the very start because i initialized it to only 2^8 not like 2^20
            prev_power_of_2 = prev_power_of_2 * 2
            curr_power += 1
        
    return [num_ones] + one_pos