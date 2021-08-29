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

        lst=numbers.split(",")
        lst=[int(element) for element in lst]
        return sum(lst)
