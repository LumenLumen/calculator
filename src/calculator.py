class Calculator :
    # return the sum between 2 operands
    def mysum(self, first_operand, second_operand):
        return first_operand + second_operand

    # Moyenne des nombres 
    def mymean(self, operands):
        sum = 0
        for nb in operands :
            sum = sum + nb
        return sum / len(operands)
    
    # Multiplication
    def mymulti(self,first_operand, second_operand):
         return first_operand * second_operand
#comm jpp