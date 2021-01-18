import argparse

'''
let's learn to add some arguments that our parser can understand.
'''
def get_args():
 parser=argparse.ArgumentParser(description='a simple argument parser',epilog='example usage')
 
 #required arguments
 #parser.add_argument('-x',action='store',required=True,help='help text for option X')
 
 #example to add a long_option which is generally more than a character
 parser.add_argument('-x','--execute',action='store',required=True,help='help text for option X')
 
 #optional arguments
 parser.add_argument('-y',help='help text for option Y',default=False)
 parser.add_argument('-z',help='help option for the argument z',type=int)
 print(parser.parse_args())
 

 
if __name__=='__main__':
 get_args()