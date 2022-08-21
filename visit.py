# This is the code that visits the estate agency
from estate_agency import estate_agency 
import sys
import Pyro4
import Pyro4.util
from client import Person


sys.excepthook = Pyro4.util.excepthook


Estate_agency = Pyro4.Proxy("PYRONAME:object.agency")
naeima = Person("naeima")
naeima.visit(Estate_agency)


