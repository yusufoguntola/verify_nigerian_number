from enums import get_telco_list, NigerianTelco
from utils import format_to_11_digit


class TelcoManager:
    """Defines telco manager and has utility methods to get telco details"""

    def __init__(self, telco=None):
        if telco:
            self.telco = str(telco)

    def get_prefixes(self):
        """Returns the prefixes for the current telco instance"""
        if self.telco:
            prefixes = []
            for item in self.all_prefixes():
                if item["name"] == self.telco:
                    prefixes.append(item["prefix"])
            return prefixes
        else:
            return self.all_prefixes()

    def get_telco_prefixes(self, telco):
        """Returns prefixes for the telco parameter passed. Safe to use if manager was not initialized with a telco"""
        telco = str(telco)
        prefixes = []
        for item in self.all_prefixes():
            if item["name"] == telco:
                prefixes.append(item["prefix"])
        return prefixes

    def set_telco(self, telco):
        """Set telco instance for a manager that was initialized without a telco"""
        self.telco = str(telco)

    @staticmethod
    def get_telco_list():
        """Returns a list of all telcos in Nigeria. Defaults to utils.get_telco_list"""
        return get_telco_list()

    @staticmethod
    def all_prefixes():
        return [
            {"prefix": "0701", "name": "AIRTEL"},
            {"prefix": "07020", "name": "SMILE"},
            {"prefix": "07025", "name": "MTN"},
            {"prefix": "07026", "name": "MTN"},
            {"prefix": "07027", "name": "MULTI-LINKS"},
            {"prefix": "07028", "name": "STARCOMMS"},
            {"prefix": "07029", "name": "STARCOMMS"},
            {"prefix": "0703", "name": "MTN"},
            {"prefix": "0704", "name": "MTN"},
            {"prefix": "0705", "name": "GLO"},
            {"prefix": "0706", "name": "MTN"},
            {"prefix": "0707", "name": "ZOOMMOBILE"},
            {"prefix": "0708", "name": "AIRTEL"},
            {"prefix": "0709", "name": "MULTI-LINKS"},
            {"prefix": "0802", "name": "AIRTEL"},
            {"prefix": "0803", "name": "MTN"},
            {"prefix": "0804", "name": "NTEL"},
            {"prefix": "0805", "name": "GLO"},
            {"prefix": "0806", "name": "MTN"},
            {"prefix": "0807", "name": "GLO"},
            {"prefix": "0808", "name": "AIRTEL"},
            {"prefix": "0809", "name": "NINE_MOBILE"},
            {"prefix": "0810", "name": "MTN"},
            {"prefix": "0811", "name": "GLO"},
            {"prefix": "0812", "name": "AIRTEL"},
            {"prefix": "0813", "name": "MTN"},
            {"prefix": "0814", "name": "MTN"},
            {"prefix": "0815", "name": "GLO"},
            {"prefix": "0816", "name": "MTN"},
            {"prefix": "0817", "name": "NINE_MOBILE"},
            {"prefix": "0818", "name": "NINE_MOBILE"},
            {"prefix": "0819", "name": "STARCOMMS"},
            {"prefix": "0901", "name": "AIRTEL"},
            {"prefix": "0902", "name": "AIRTEL"},
            {"prefix": "0903", "name": "MTN"},
            {"prefix": "0904", "name": "AIRTEL"},
            {"prefix": "0905", "name": "GLO"},
            {"prefix": "0906", "name": "MTN"},
            {"prefix": "0907", "name": "AIRTEL"},
            {"prefix": "0908", "name": "NINE_MOBILE"},
            {"prefix": "0909", "name": "NINE_MOBILE"},
            {"prefix": "0912", "name": "AIRTEL"},
            {"prefix": "0913", "name": "MTN"},
            {"prefix": "0915", "name": "GLO"},
            {"prefix": "0916", "name": "MTN"},
        ]


class NigerianNUmber:
    def __init__(self, msisdn: str):
        self.msisdn = msisdn
        self.manager = TelcoManager()

    def get_all_telco_prefixes(self):
        return self.manager.all_prefixes()

    def get_telco(self) -> str:
        """Returns the telco this number is attached to"""
        if self.is_airtel():
            self.manager.set_telco(NigerianTelco.AIRTEL)
            return str(NigerianTelco.AIRTEL)
        if self.is_glo():
            self.manager.set_telco(NigerianTelco.GLO)
            return str(NigerianTelco.GLO)
        if self.is_mtn():
            self.manager.set_telco(NigerianTelco.MTN)
            return str(NigerianTelco.MTN)
        if self.is_multi_links():
            self.manager.set_telco(NigerianTelco.MULTI_LINKS)
            return str(NigerianTelco.MULTI_LINKS)
        if self.is_nine_mobile():
            self.manager.set_telco(NigerianTelco.NINE_MOBILE)
            return str(NigerianTelco.NINE_MOBILE)
        if self.is_ntel():
            self.manager.set_telco(NigerianTelco.NTEL)
            return str(NigerianTelco.NTEL)
        if self.is_smile():
            self.manager.set_telco(NigerianTelco.SMILE)
            return str(NigerianTelco.SMILE)
        if self.is_starcomms():
            self.manager.set_telco(NigerianTelco.STARCOMMS)
            return str(NigerianTelco.STARCOMMS)
        if self.is_zoommobile():
            self.manager.set_telco(NigerianTelco.ZOOMMOBILE)
            return str(NigerianTelco.ZOOMMOBILE)

    def format_to_11_digit(self):
        return format_to_11_digit(self.msisdn)

    def internationalize(self) -> str:
        """Returns the MSISDN formatted with Nigerian code without a leading '+'. Sample response: 234700000000"""
        formatted = self.format_to_11_digit()
        return f"234{formatted[1:]}"

    def is_for_telco(self, telco) -> bool:
        """Check whether the MSISDN is for the passed telco"""
        telco = str(telco)
        prefixes = self.manager.get_telco_prefixes(telco)
        formatted = self.format_to_11_digit()
        first_4 = formatted[0:4]
        first_5 = formatted[0:5]
        return first_4 in prefixes or first_5 in prefixes

    def is_airtel(self) -> bool:
        """Check whether the msisdn is an airtel number"""
        return self.is_for_telco(NigerianTelco.AIRTEL)

    def is_glo(self) -> bool:
        """Check whether the msisdn is a glo number"""
        return self.is_for_telco(NigerianTelco.GLO)

    def is_mtn(self) -> bool:
        """Check whether the msisdn is a mtn number"""
        return self.is_for_telco(NigerianTelco.MTN)

    def is_multi_links(self) -> bool:
        """Check whether the msisdn is a multi-links number"""
        return self.is_for_telco(NigerianTelco.MULTI_LINKS)

    def is_nine_mobile(self) -> bool:
        """Check whether the msisdn is a 9Mobile number"""
        return self.is_for_telco(NigerianTelco.NINE_MOBILE)

    def is_ntel(self) -> bool:
        """Check whether the msisdn is a ntel number"""
        return self.is_for_telco(NigerianTelco.NTEL)

    def is_smile(self) -> bool:
        """Check whether the msisdn is a smile number"""
        return self.is_for_telco(NigerianTelco.SMILE)

    def is_starcomms(self) -> bool:
        """Check whether the msisdn is a starcomms number"""
        return self.is_for_telco(NigerianTelco.STARCOMMS)

    def is_zoommobile(self) -> bool:
        """Check whether the msisdn is a zoommobile number"""
        return self.is_for_telco(NigerianTelco.ZOOMMOBILE)
