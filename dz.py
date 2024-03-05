class SuperHero:
    people ='people'
    people = "monster"
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.health_points = health_points*2

    def __str__(self):
        return (f'name: {self.name}\n'
                f'nickname: {self.nickname}\n'
                f'superpower: {self.superpower}\n'
                f'health_points: {(self.health_points)}\n'
                f'catchphrase: {self.catchphrase}\n')
        self.health_points = health_points *2

    def my_function(word):
      print(f' {word}')
    my_function('True in the True_phrase')
    def gen_x(self):
        pass

class Sky (SuperHero):
    sky ='sky'

    def __init__(self, name, nickname, superpower, health_points,catchphrase,damage,fly=False):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
        print(f'damage:{damage**2}\n'
              f'fly:{{fly={True}}}')
        self.health_points = health_points ** 2
        self.damage = damage**2
    def double_health(self):
        self.fly = True
        return self.health_points ** 2

    def crit(self):
        return self.damage **2




class Cosmic(SuperHero):
    cosmic='cosmic'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
        print(f'damage:{damage**2}\n'
              f'fly:{fly}')
        self.health_points = health_points ** 2

class Villain:(SuperHero)






people = SuperHero('Nick', 'Nicki', 'strong',5, 'hello')
print(people)
sky = Sky('Nick', 'Nicki', 'strong',5, 'hello',7,False)
print(sky)
cosmic = Cosmic('Nick', 'Nicki', 'strong',5, 'hello',8,False)
print(cosmic)
print(sky.double_health())
print(sky.fly)
print(sky.crit())
