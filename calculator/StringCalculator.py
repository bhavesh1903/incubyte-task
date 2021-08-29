import re
class StringCalculator:
    def addition(self,numbers):
        if numbers=="":
            return 0

        count=0
        for i in range(len(numbers)):
            if numbers[i].isdigit()==False:
               count+=1
        if count==0:
            return int(numbers)

        numbers = map(int, re.findall(r"-?\d+", numbers))
        numbers = filter(lambda x: x < 1000, numbers)
        return sum(numbers)
