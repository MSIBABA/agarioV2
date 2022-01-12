
import core
from creep2 import Creep2


def setup():
    print("-------START--------")
    core.fps = 20
    core.WINDOW_SIZE = [800,800]

    #creation creep

    core.memory("creeps",[])

    core.memory("nbCreep",50)

    for i in range(0,core.memory("nbCreep")):
        core.memory("creeps").append(Creep2())

    print("Setup END-----------")

def run():
    core.cleanScreen()
    for c in core.memory("creeps"):
        c.show()



core.main(setup, run)
