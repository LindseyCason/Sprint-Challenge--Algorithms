#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n)
    for every additional thing added to n the runtime increases by that amount
    a = 0
    while (a < 3 * 3 * 3):
      a = a + 3 * 3
      _______
      n=3
      O(n)=O(3)
      a//27



b)O(n log n)
if n is 3, the initial loop will run 3 times, each time, the while loop will run 2 times per initial loop until j>3. Sum=6
sum = 0
    for i in range(3):
    #3 Loops due to range
      j = 1
      while j < 3:
        #2 Loops Each pass 1*2 = 2, 2*2=4 break
        j *= 2
        sum += 1


c) O(n)
    The function will run a number of times of given bunnies, therefore it is O(n) n equals the amount of bunnies.
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1)
      ----------
    bunnyEars(3) // runs 3 times =O(3) so O(n)

## Exercise II


