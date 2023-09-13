"""
Backtracking : I will solve the sixth problem from the set of problems which states :
    Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two solutions: (()) and ()()

Time complexity : O(2^n)
Space complexity : O(n) (for storage of the paranthesis)
"""

def gen_Paranthesis(openP, closeP, n, s=[]): #s is a list for printing outputs
     #we analyze the base case first
    if closeP == n / 2:
        print(''.join(s)) #the join() method takes all items in an iterable and joins them into one string.
        return

    else:
        if(openP > closeP): #we surley need to put a closing bracket
            s.append(')')
            gen_Paranthesis(openP, closeP + 1, n, s)
            s.pop()
        if(openP < n / 2): #here we can append an open parenthesis and afterwards enter recursion
            s.append('(')
            gen_Paranthesis(openP + 1, closeP, n, s)
            s.pop()
    return

n = input("Enter the number of parentheses : ")
if n % 2 != 0 :
    print("A solution cannot be computed")
elif n < 2:
    print("A solution cannot be computed")
else:
    gen_Paranthesis(0, 0, int(n))