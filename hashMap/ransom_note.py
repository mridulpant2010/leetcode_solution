from collections import defaultdict
def canConstruct( ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransom = defaultdict(int)
    mag=defaultdict(int)
    for i in ransomNote:
        ransom[i]+=1
    for j in magazine:
        mag[j]+=1
    
    for k,v in mag.items():
        if k in ransom:
            ransom[k]-=v
            if ransom[k]<=0:
                del ransom[k] 
    print(ransom)
    return True if len(ransom)==0 else False

if __name__ == "__main__":
    ransomNote = "bg"
    #"aa"
    magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
    ans = canConstruct( ransomNote, magazine)
    print(ans)