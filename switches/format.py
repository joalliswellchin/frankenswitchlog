class TopHousing:
    material: str
    origin: str # origin of creator

    def __init__(self, material, origin):
        self.material = material
        self.origin = origin

class BtmHousing:
    material: str
    origin: str # origin of creator

    def __init__(self, material, origin):
        self.material = material
        self.origin = origin

class Stem:
    material: str

    def __init__(self, material):
        self.material = material

class Spring:
    material: str
    actuation_force: str
    btm_out_force: str

    def __init__(self, material, actuation_force, btm_out_force):
        self.material = material
        self.actuation_force = actuation_force
        self.btm_out_force = btm_out_force

class Switch:
    th: TopHousing
    bh: BtmHousing
    stem: Stem
    spring: Spring

    def __init__(self, th, bh, stem, spring):
        self.th = th
        self.bh = bh
        self.stem = stem
        self.spring = spring
    
    def calc_force():
        # TODO: find some way to calculate force from specs of switches as an 
        # estimate for the frankenswitch
        return 0