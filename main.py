class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype = []
        for i in range(n):
            i = i + 1
            if i % 3 == 0 and i % 5 == 0:
                rtype.append("FizzBuzz")
            elif i % 3 == 0:
                rtype.append("Fizz")
            elif i % 5 == 0:
               rtype.append("Buzz")
            else:
              rtype.append(str(i))
        return rtype
