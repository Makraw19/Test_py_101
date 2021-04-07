class employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal

skills = []

class developer(employee):
    def __init__(self,name,sal,skill):
        super().__init__(name,sal)
        self.skill = skill
        skills.append(self.skill)
        self.skill = skills

    #getter
    @property
    def total_skill(self):
        self.skill = self.skill

        return self.skill

    #setter
    @total_skill.setter
    def total_skill(self,val):
        self.skill = val
        skills.append(self.skill)
        self.skill = skills

        return self.skill
        

d1 = developer('john',23000,'python')
print(d1.skill)
print(d1.total_skill)
d1.total_skill = 'c#'
print(d1.total_skill)

##class employee:
##    def __init__(self,name,sal):
##        self.name = name
##        self.sal = sal
##        
##
##class programmer(employee):
##    def __init__(self,name,sal,skill):
##        super().__init__(name,sal)
##        skills = []
##        self.skill = skill
##        skills.append(self.skill)
##        self.skill = skills
##
##    #getter
##    @property
##    def skill_get(self):
##        skills = []
##        self.skill = self.skill
##        skills.append(self.skill)
##        self.skill = skills
##        return self.skill
##    #setter
##    @skill_get.setter
##    def skill_get(self,lang):
##        self.skill = lang
##        return self.skill
##        
##        
##
##e1 = employee('sheikh', 25000)
##print(e1.sal)
##
##p1 = programmer('tom','32000','python')
##print(p1.skill)
##
##
##print(p1.skill_get)
##p1.skill_get = 'c#'
##print(p1.skill_get)
