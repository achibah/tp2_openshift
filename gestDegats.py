def gestDegats(PVdef, Forceatk, Armuredef):
    if (Forceatk > Armuredef):
        return PVdef-(Forceatk-Armuredef)
    else:
        return PVdef-1
