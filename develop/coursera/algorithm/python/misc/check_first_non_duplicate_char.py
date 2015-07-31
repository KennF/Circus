import random, string

def check_first_non_duplicate_char(s):
    if not s:
        return None

    for i in range(len(s)):
        if s[i] not in s[i+1:]:
            return s[i]
    return None
       
if __name__ == '__main__':
    print check_first_non_duplicate_char('ABCDA')
    print check_first_non_duplicate_char('ABCD')
    print check_first_non_duplicate_char('')
    print check_first_non_duplicate_char(None)

    aaa = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
    print aaa
    print check_first_non_duplicate_char(aaa)
    