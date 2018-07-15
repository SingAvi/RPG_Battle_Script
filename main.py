from classes.game import Person, bcolors

magic =[{"name": "Fire","cost":10,"dmg":65},{"name": "Water","cost":10,"dmg":70},{"name": "Moist","cost":10,"dmg":75},{"name": "Mist","cost":10,"dmg":80}]

player = Person(500,70,65,40,magic)
print (player.generateMagicDamage(0))
print (player.generateMagicDamage(1))

# print (player.generateDamage())
# print (player.generateDamage())
# print (player.generateDamage())
# print (player.generateDamage())
