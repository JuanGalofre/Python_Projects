def buffer_wizard() -> str:
    pH = float(input("Desired pH"))
    pKa = float(input("PKa of the pair that is going to be used"))
    total_concentration = float(input("Total buffer concentration in M"))
    ratio = 10 ** (pH - pKa)
    acid_concentration = total_concentration / (ratio + 1)
    base_concentration = total_concentration - acid_concentration
    volume_of_buffer = float(input("Volume of buffer that you want to prepare, in L"))
    molar_mass_acid = float(input("Molar mass of acid"))
    molar_mass_base = float(input("Molar mass of base"))
    acid_grams = acid_concentration * volume_of_buffer * molar_mass_acid
    base_grams = base_concentration * volume_of_buffer * molar_mass_base
    rta = "Add " + str(round(acid_grams, 1)) + " gr of acid and " + str(round(base_grams, 1)) + " gr of base."
    return rta
