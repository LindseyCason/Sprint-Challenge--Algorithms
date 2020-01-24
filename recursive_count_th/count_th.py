'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  check="th"
  index=0
  #Base 
  # print(word[index]+word[index+1])
  if len(word) <= 1:
    return 0
  if check in word[index]+word[index+1]:
    return 1+ count_th(word[1:])
  else:
    return count_th(word[1:])
print(count_th(""))
