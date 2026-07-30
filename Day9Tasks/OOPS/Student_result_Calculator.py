# Student Result Generator (Method Overloading Concept)

class Result:

     def calculate(self,subject1,subject2,subject3=None):
         if subject3 is None:
             total=subject1+subject2
             print("Total Marks(2 Subjects):",total)

         else:
             total=subject1+subject2+subject3+subject4
             print("Total Marks (3 Subjects):",total)
             
result=Result()
result.calculate(93,94)
result.calculate(89,92)



            
