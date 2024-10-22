from AlleyCat import AlleyCat
from Cat import Cat
from PersianCat import PersianCat
from SiameseCat import SiameseCat

croquette = SiameseCat("", "Croquette")
croquette.display()
mademoiselle = AlleyCat("Awake", "Mademoiselle")
mademoiselle.display()
minou = PersianCat("", "")
minou.display()
for i in range(Cat.NumberOfLives):
    minou.die()
minou.display()
