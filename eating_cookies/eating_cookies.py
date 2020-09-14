'''
Input: an integer
Returns: an integer
'''
import sys              #to use a sys.argv


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache={1: 1}):
  if n < 0:             #if n is less than zero (for all the negatives)
      return 0
  if n == 0:            #as cookie monster can eat 0 cookies at a time
      return 1
  if n not in cache:
      cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
  return cache[n]

  return eating_cookies(n-1) + eating_cookies(n-2)  + eating_cookies(n-3)

if __name__ == "__main__":
  if len(sys.argv) > 1:  
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')