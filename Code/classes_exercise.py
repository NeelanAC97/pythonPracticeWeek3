class Student:

    class_ = "Student"

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def avtestscore(self,test1,test2,test3): 
        
        totalscore = test1 + test2 + test3
        avgscore = totalscore/3
        
        return avgscore

john = Student("John", "16")

print(getattr(john, "age"))

print(int(john.avtestscore(5,6,4)))

