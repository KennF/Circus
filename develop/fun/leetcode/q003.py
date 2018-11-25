def test(input):
    max = 0
    max_sub = ''
    i = 0
    j = 0

    while(j < len(input)):
        if input[j] not in max_sub:
            # print(input[j])
            max_sub = max_sub + input[j]
            if len(max_sub) > max:
                max = len(max_sub)
            j = j + 1
        else:
            # print(max_sub)
            i = i + max_sub.index(input[j]) + 1
            max_sub = input[i: j +1] 
            j = j + 1
    
    print('max is ' + str(max))

    return max



if __name__ == "__main__":
    input1 = 'abcabcbb'
    input2 = 'bbbb'
    input3 = 'pwwkew'
    input4 = 'nfpdmpi'
    input5 = 'bbtablud'
    input6 = 'aab'

    test(input1)
    test(input2)
    test(input3)
    test(input4)
    test(input5)
    test(input6)