class Weapon:

    def __init__(self):
        self.ammo = 10

    def reload(self):
        self.ammo = 10

class Gun(Weapon):

    def fire(self):
        self.ammo -= 3

class RocketLauncher(Weapon):
    def fire(self):
        self.ammo -= 1

class Trnsformer:

    def __init__(self, left_weapon, right_weapon):
        
        self.left_weapon = Gun()
        self.right_weapon = Gun()
        #self.x = x #public
        #self.__y = y #private
        #self._z = z #protected

    def run(self):
        self.x += 5



