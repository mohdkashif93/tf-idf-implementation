"""
Name : Mohd. Kashif
Roll No. MT15035
Question No. 3

Note :
Input given to the program should be non empty strings . 
"""
def editDistDP(str1, str2, m, n):
    """
    Create an empty matrix
    """
    dp = []
    for x in range(0,m+1):
        row = []
        for y in range(0,n+1):
            row.append(0)
        dp.append(row)

 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:                            #When first string is empty.
                dp[i][j] = j
       
            elif j == 0:                          #When second string is empty.
                    dp[i][j] = i 
            
            elif str1[i-1] == str2[j-1]:          #When last character is same.        
                dp[i][j] = dp[i-1][j-1]
            else :                                #consider all possibilities when last characetr is different,
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
 
    return dp[m][n]
 
 
def main():
    inp = ["",""]
    print "Enter String 1 : "
    inp[0] = raw_input()
    print "Enter String 2: "
    inp[1] = raw_input()
    """
    inp = raw_input()
    inp = inp.split(' ')
    """
    if len(inp[0])==0 or len(inp[1])==0:
        print "Wrong input !! \n Strings should be non empty.\n Program is exiting !!"
        return
    else:
        print "Edit distance is : "
        print editDistDP(inp[0], inp[1], len(inp[0]), len(inp[1]))
    """
    print "Edit distance is : "
    print editDistDP(inp[0], inp[1], len(inp[0]), len(inp[1]))
    """
main()