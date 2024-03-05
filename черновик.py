# class SuperHero:
#     people ='people'
#
#
#     def __init__(self,name,nickname,superpower,health_points,catchphrase, damage, fly=False):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#         self.damage = damage
#         self.fly = fly
#
#     def People(self):
#            print(self.people)
#     def __str__(self):
#         return  (f'name: {self.name}\n'
#                  f'nickname: {self.nickname}\n'
#                  f'superpower: {self.superpower}\n'
#                  f'health_points: {(self.health_points)}\n'
#                  f'catchphrase: {self.catchphrase}\n')
#
    def double_health(self):
        self.fly = True
        return self.health_points ** 2
#
# people=SuperHero(name='Nick',nickname='Niki',superpower='strong',health_points=5,catchphrase='hello', damage=10)
#
# print(people)
# print(people.name)
# print(people.fly) # False
# people.double_health() # нужно просто вызвать метод, не используя print
# print(people.fly) # True

    # @crit.setter
    def crit(self, value):
        if value is not None and not isinstance(value, Range):
            value = Range(value)

        self._crit = value