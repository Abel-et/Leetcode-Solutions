class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1:'I',2:'II',3 :'III',4:'IV',5:"V",6:'VI',7:"VII",8:'VIII',9:'IX',10:'X',20:"XX",30:"XXX",50:'L',40:'XL',60:'LX',70:"LXX",80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M'}

        integer = str(num)
        n = len(integer)
        factor = int(pow(10,n-1))
        print(factor)
        result = ""

        for i in range(n):
            temp = int(integer[i])
            if factor == 1000:
                for i in range(temp):
                    result += roman[factor]
            else:
                k = temp*factor
                if k>0:
                    result += roman[k]
            factor //= 10
        return result
        
