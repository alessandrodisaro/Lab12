from dataclasses import dataclass

@dataclass
class Retailer:
    R1: int
    R2: int
    peso: int




    def __str__(self):
        return f"{self.R1} - {self.R2}, peso: {self.peso}"

    # VEDIAMO SE USALO, PER ORA CE MO NON E' USATO
