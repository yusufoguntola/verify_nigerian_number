from enum import Enum


class NigerianTelco(str, Enum):
    AIRTEL = "AIRTEL"
    GLO = "GLO"
    MTN = "MTN"
    MULTI_LINKS = "MULTI-LINKS"
    NINE_MOBILE = "NINE_MOBILE"
    NTEL = "NTEL"
    SMILE = "SMILE"
    STARCOMMS = "STARCOMMS"
    ZOOMMOBILE = "ZOOMMOBILE"

    def __str__(self) -> str:
        return self.value


def get_telco_list():
    return [str(NigerianTelco.AIRTEL), str(NigerianTelco.GLO), str(NigerianTelco.MTN), str(NigerianTelco.MULTI_LINKS),
            str(NigerianTelco.NINE_MOBILE), str(NigerianTelco.NTEL), str(NigerianTelco.SMILE),
            str(NigerianTelco.STARCOMMS), str(NigerianTelco.ZOOMMOBILE)]
