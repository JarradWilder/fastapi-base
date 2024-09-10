from enum import Enum

class OrderType(str, Enum):
    FETCHTV = "fetchtv"
    PHONEMOBILE = "phonemobile"
    COMPLEX = "complex"
    ENTERPRISE = "enterprise"
    HARDWARE = "hardware"
    PHONEFIXED = "phonefixed"
    NBN = "nbn"
    VOIP = "voip"
    OPTICOMM = "opticomm"