from genMob import *

def createMob():
   nommob = ["Géant", "Medusa", "Chupacabra"]
   x = random.choice(nommob)
   return genMob(x)
