def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    start = 0
    end = 0
    ans=""
    count=0
    while end < len(chars):
        if chars[end]==chars[start]:
            count+=1
            end+=1
        else:
            ans+=chars[start]+str(count)
            count=0
            start=end
    #chars=ans
    ans+=chars[start]+str(count)
    chars=ans
    return len(chars)



if __name__ == "__main__":
    chars=["a","a","b","b","c","c","c"]
    compress(chars)