from collections import defaultdict
def permute_palindrome(st):
    d= defaultdict(int)
    for i in st:
        d[i]+=1
    count=0
    for _,v in d.items():
        if v%2==1:
            count+=1
    # A palindrome permutation allows at most **one** odd count
    return count<=1


print(permute_palindrome("peas"))