from pydantic import BaseModel

class HealthSummaryDTO(BaseModel):
    gender: str
    age: int
    race: str
    country: str
    in_us: bool
    educ: str
    marital: str
    preg: bool
    family_pov: bool
    cal: float
    prot: float
    carb: float
    sugr: float
    fibre: float
    chol: float
    bmi: float
    bpxs: float
    bpxd: float
    alq: bool
    smk: bool
    sld: float
    mhds: float