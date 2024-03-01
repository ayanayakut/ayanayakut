class SuperHero:
    people ='people'


    def __init__(self,name,nickname,superpower,health_points,
catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def People(self):
           print(self.people)
    def __str__(self):
        return  (f'name: {self.name}\n'
                 f'nickname: {self.nickname}\n'
                 f'superpower: {self.superpower}\n'
                 f'health_points: {(self.health_points)}\n'
                 f'catchphrase: {self.catchphrase}\n')



people=SuperHero(name='Nick',nickname='Niki',superpower='strong',health_points=5,catchphrase='hello')


def double_health(self):
    return self.health_points * 2
print(people)
print(people.name)
print(people.health_points*2)