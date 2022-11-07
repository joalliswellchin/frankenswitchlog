# ------------------------------------------------------------------
# Writing this classes should we need to use them to do calculations
# for now we focus on just the csv to md
# ------------------------------------------------------------------
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
    # all force calculation is in g
    actuation_force: float
    btm_out_force: float

    def __init__(self, material, actuation_force, btm_out_force=0.0):
        self.material = material
        self.actuation_force = actuation_force
        self.btm_out_force = btm_out_force

class Switch:
    th: TopHousing
    bh: BtmHousing
    stem: Stem
    spring: Spring
    switch_tactility: str

    def __init__(self, th, bh, stem, spring, switch_tactility):
        self.th = th
        self.bh = bh
        self.stem = stem
        self.spring = spring
        self.switch_tactility = switch_tactility
    
    def calc_force(self):
        # TODO: find some way to calculate force from specs of switches as an 
        # estimate for the frankenswitch, for now it is just placeholder
        material_map = 1.1
        force = self.spring.actuation_force * (material_map * 1.1)
        self.spring.btm_out_force = force * 1.2
        return force