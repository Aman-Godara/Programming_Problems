# Q.2 Servers: One server sends request to other in encoded form. Encoding scheme is as follows: a -> 1, b -> 2, ......, e -> 5, z -> 26
# Input: "11”    Possbile decodings: (“aa”, ‘k”)
# Input: “121"   Possbile decodings: (“aba”, “au”, “la”)
# Input: "101”   Possbile decodings: ("ja")
# Input: “127"   Possbile decodings: ("abg", "lg")
# Input: “9999"  Possbile decodings: ("iiii")
# Task is to find all the possible decodings of an input.


def decodings(past, i, signal):
    if i == len(signal):
        return []
        # i has exceed last possible index: return []
        # past may or may not be empty; return [] for both cases
    elif past:
        # past is not empty: merge ith term with past
        number = int(past + signal[i])
        if number > 26:
            # merging with past is not possible: return []
            return []
        else:
            # merging with past is possible
            new_past = chr(number + 96)
            return add_str_to_strlist(new_past, decodings('', i + 1, signal))
    else:
        # past is empty: 2 possiblities for ith term
        new_past = chr(int(signal[i]) + 96)
        out = decodings(signal[i], i + 1, signal) + add_str_to_strlist(new_past, decodings('', i + 1, signal))
        return out


def add_str_to_strlist(str_add, str_list):
    # str_list is an empty list ([]): return a list with only str_add in it ([str_add])
    # str_list is an non empty list (['a', 'bc', 'adf']): return a list of same size with str_add ('w') contatenated to each term (['wa', 'wbc', 'wadf'])
    if str_list:
        for i in range(0, len(str_list)):
            str_list[i] = str_add + str_list[i]
        return str_list
    else:
        return [str_add]


input_signal = '1211'

print(decodings('', 0, input_signal))
# Note: Dynamic Programming can be implemented in the above solution to further enhance the efficiency at the cost of memory
