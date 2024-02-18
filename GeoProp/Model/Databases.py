from .Species import Species
from .Phases import PhaseType
# from . import Phases.PhaseType as PhaseType

from enum import Enum
from typing import Dict

class Comp(Enum):
    """
    The Comp class stores all of the available species.
    """

    # TODO the use of Enums with classes as the value is proving a huge pain in the arse!!! Need to think of a better way!!

    # these species exist in both CoolProp and Reaktoro

    STEAM = Species("H2O(g)", "Water", ["H", "O"], 0.01801528, +0, PhaseType.GASEOUS)
    WATER = Species("H2O(aq)", "Water", ["H", "O"], 0.01801528, +0, PhaseType.AQUEOUS)
    HYDROGEN = Species("H2(g)", "Hydrogen", ["H"], 0.002, +0, PhaseType.GASEOUS)
    OXYGEN = Species("O2(g)", "Oxygen", ["O"], 0.032, +0, PhaseType.GASEOUS)
    AMMONIA = Species("NH3", "Ammonia", ["N", "H"], 0.0180385, +0, PhaseType.LIQUID)
    AMMONIA_g = Species("NH3(g)", "Ammonia", ["N", "H"], 0.01703052, +0, PhaseType.GASEOUS)
    CARBONDIOXIDE = Species("CO2(g)", "CarbonDioxide", ["C", "O"], 0.0440096, +0, PhaseType.GASEOUS)
    NITROGEN = Species("N2(g)", "Nitrogen", ["N"], 0.0280134, +0, PhaseType.GASEOUS)
    H2S = Species("H2S(g)", "HydrogenSulfide", ["H", "S"], 0.03408088, +0, PhaseType.GASEOUS)
    HELIUM = Species("He(g)", "Helium", ["He"], 0.004002602, +0, PhaseType.GASEOUS)
    ARGON = Species("Ar(g)", "Argon", ["Ar"], 0.039948, +0, PhaseType.GASEOUS)
    METHANE = Species("CH4(g)", "Methane", ["C", "H"], 0.016042459999999998, +0, PhaseType.GASEOUS)
    C2H4_g = Species("C2H4(g)", "Ethylene", ["C", "H"], 0.028053159999999997, +0, PhaseType.GASEOUS)
    SO2_g = Species("SO2(g)", "SulfurDioxide", ["S", "O"], 0.0640638, +0, PhaseType.GASEOUS)
    Kr_g = Species("Kr(g)", "Krypton", ["Kr"], 0.083798, +0, PhaseType.GASEOUS)
    Ne_g = Species("Ne(g)", "Neon", ["Ne"], 0.020179700000000002, +0, PhaseType.GASEOUS)
    Xe_g = Species("Xe(g)", "Xenon", ["Xe"], 0.131293, +0, PhaseType.GASEOUS)

    Almandine = Species("Almandine", None, ["Fe", "Al", "Si", "O"], 0.497747376, 0, PhaseType.MINERAL)
    Andradite = Species("Andradite", None, ["Ca", "Fe", "Si", "O"], 0.5081733, 0, PhaseType.MINERAL)
    Grossular = Species("Grossular", None, ["Ca", "Al", "Si", "O"], 0.45044637600000004, 0, PhaseType.MINERAL)
    Knorringite = Species("Knorringite", None, ["Mg", "Cr", "Si", "O"], 0.4531565, 0, PhaseType.MINERAL)
    Majorite = Species("Majorite", None, ["Mg", "Si", "O"], 0.4015548, 0, PhaseType.MINERAL)
    Pyrope = Species("Pyrope", None, ["Mg", "Al", "Si", "O"], 0.40312737600000004, 0, PhaseType.MINERAL)
    Spessartine = Species("Spessartine", None, ["Mn", "Al", "Si", "O"], 0.495026526, 0, PhaseType.MINERAL)
    Clinohumite = Species("Clinohumite", None, ["Mg", "Si", "O", "H"], 0.62109208, 0, PhaseType.MINERAL)
    Fayalite = Species("Fayalite", None, ["Fe", "Si", "O"], 0.20377309999999998, 0, PhaseType.MINERAL)
    Forsterite = Species("Forsterite", None, ["Mg", "Si", "O"], 0.14069310000000002, 0, PhaseType.MINERAL)
    Monticellite = Species("Monticellite", None, ["Ca", "Mg", "Si", "O"], 0.1564661, 0, PhaseType.MINERAL)
    Tephroite = Species("Tephroite", None, ["Mn", "Si", "O"], 0.2019592, 0, PhaseType.MINERAL)
    Andalusite = Species("Andalusite", None, ["Al", "Si", "O"], 0.162045576, 0, PhaseType.MINERAL)
    Kyanite = Species("Kyanite", None, ["Al", "Si", "O"], 0.162045576, 0, PhaseType.MINERAL)
    Al_Mullite = Species("Al-Mullite", None, ["Al", "Si", "O"], 0.15749374500000002, 0, PhaseType.MINERAL)
    Si_Mullite = Species("Si-Mullite", None, ["Al", "Si", "O"], 0.162045576, 0, PhaseType.MINERAL)
    Fe_Chloritoid = Species("Fe-Chloritoid", None, ["Fe", "Al", "Si", "O", "H"], 0.251905256, 0, PhaseType.MINERAL)
    Mg_Chloritoid = Species("Mg-Chloritoid", None, ["Mg", "Al", "Si", "O", "H"], 0.22036525599999998, 0,
                            PhaseType.MINERAL)
    Mn_Chloritoid = Species("Mn-Chloritoid", None, ["Mn", "Al", "Si", "O", "H"], 0.250998306, 0, PhaseType.MINERAL)
    Fe_Staurolite = Species("Fe-Staurolite", None, ["Fe", "Al", "Si", "O", "H"], 1.691691894, 0, PhaseType.MINERAL)
    Mg_Staurolite = Species("Mg-Staurolite", None, ["Mg", "Al", "Si", "O", "H"], 1.565531894, 0, PhaseType.MINERAL)
    Mn_Staurolite = Species("Mn-Staurolite", None, ["Mn", "Al", "Si", "O", "H"], 1.688064094, 0, PhaseType.MINERAL)
    Hydroxy_Topaz = Species("Hydroxy-Topaz", None, ["Al", "Si", "O", "H"], 0.18006085600000002, 0, PhaseType.MINERAL)
    Akermanite = Species("Akermanite", None, ["Ca", "Mg", "Si", "O"], 0.2726278, 0, PhaseType.MINERAL)
    Julgoldite_FeFe = Species("Julgoldite-FeFe", None, ["Ca", "Fe", "Si", "O", "H"], 1.11893378, 0, PhaseType.MINERAL)
    Merwinite = Species("Merwinite", None, ["Ca", "Mg", "Si", "O"], 0.32870520000000003, 0, PhaseType.MINERAL)
    Pumpellyite_FeAl = Species("Pumpellyite-FeAl", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.97461647, 0,
                               PhaseType.MINERAL)
    Pumpellyite_MgAl = Species("Pumpellyite-MgAl", None, ["Ca", "Mg", "Al", "Si", "O", "H"], 0.94307647, 0,
                               PhaseType.MINERAL)
    Rankinite = Species("Rankinite", None, ["Ca", "Si", "O"], 0.2884008, 0, PhaseType.MINERAL)
    Spurrite = Species("Spurrite", None, ["Ca", "Si", "C", "O"], 0.44456510000000005, 0, PhaseType.MINERAL)
    Tilleyite = Species("Tilleyite", None, ["Ca", "Si", "C", "O"], 0.4885746, 0, PhaseType.MINERAL)
    Zircon = Species("Zircon", None, ["Zr", "Si", "O"], 0.1833071, 0, PhaseType.MINERAL)
    Clinozoisite = Species("Clinozoisite", None, ["Ca", "Al", "Si", "O", "H"], 0.454357254, 0, PhaseType.MINERAL)
    Epidote_ordered = Species("Epidote,ordered", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.483220716, 0,
                              PhaseType.MINERAL)
    Fe_Epidote = Species("Fe-Epidote", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.5120841780000001, 0,
                         PhaseType.MINERAL)
    Lawsonite = Species("Lawsonite", None, ["Ca", "Al", "Si", "O", "H"], 0.314237836, 0, PhaseType.MINERAL)
    Piemontite_ordered = Species("Piemontite,ordered", None, ["Ca", "Mn", "Al", "Si", "O", "H"], 0.48231376600000003, 0,
                                 PhaseType.MINERAL)
    Zoisite = Species("Zoisite", None, ["Ca", "Al", "Si", "O", "H"], 0.454357254, 0, PhaseType.MINERAL)
    Vesuvianite = Species("Vesuvianite", None, ["Ca", "Mg", "Al", "Si", "O", "H"], 2.869452578, 0, PhaseType.MINERAL)
    Fe_Osumilite = Species("Fe-Osumilite", None, ["K", "Fe", "Al", "Si", "O"], 1.04653299, 0, PhaseType.MINERAL)
    Osumilite_1 = Species("Osumilite,1", None, ["K", "Mg", "Al", "Si", "O"], 0.98345299, 0, PhaseType.MINERAL)
    Osumilite_2 = Species("Osumilite,2", None, ["K", "Mg", "Al", "Si", "O"], 0.981880414, 0, PhaseType.MINERAL)
    Fe_Akimotoite = Species("Fe-Akimotoite", None, ["Fe", "Si", "O"], 0.1319287, 0, PhaseType.MINERAL)
    Akimotoite = Species("Akimotoite", None, ["Mg", "Si", "O"], 0.1003887, 0, PhaseType.MINERAL)
    CaSi_Titanite = Species("CaSi-Titanite", None, ["Ca", "Si", "O"], 0.176246, 0, PhaseType.MINERAL)
    Al_Perovskite = Species("Al-Perovskite", None, ["Al", "O"], 0.101961276, 0, PhaseType.MINERAL)
    Ca_Perovskite = Species("Ca-Perovskite", None, ["Ca", "Si", "O"], 0.1161617, 0, PhaseType.MINERAL)
    Fe_Perovskite = Species("Fe-Perovskite", None, ["Fe", "Si", "O"], 0.1319287, 0, PhaseType.MINERAL)
    Mg_Perovskite = Species("Mg-Perovskite", None, ["Mg", "Si", "O"], 0.1003887, 0, PhaseType.MINERAL)
    Phasea = Species("Phasea", None, ["Mg", "Si", "O", "H"], 0.45634524000000004, 0, PhaseType.MINERAL)
    Fe_Ringwoodite = Species("Fe-Ringwoodite", None, ["Fe", "Si", "O"], 0.20377309999999998, 0, PhaseType.MINERAL)
    Mg_Ringwoodite = Species("Mg-Ringwoodite", None, ["Mg", "Si", "O"], 0.14069310000000002, 0, PhaseType.MINERAL)
    Fe_Wadsleyite = Species("Fe-Wadsleyite", None, ["Fe", "Si", "O"], 0.20377309999999998, 0, PhaseType.MINERAL)
    Mg_Wadsleyite = Species("Mg-Wadsleyite", None, ["Mg", "Si", "O"], 0.14069310000000002, 0, PhaseType.MINERAL)
    Acmite = Species("Acmite", None, ["Na", "Fe", "Si", "O"], 0.23100217, 0, PhaseType.MINERAL)
    Ca_Eskola_Pyroxene = Species("Ca-Eskola-Pyroxene", None, ["Ca", "Al", "Si", "O"], 0.199187938, 0, PhaseType.MINERAL)
    Clino_Enstatite = Species("Clino-Enstatite", None, ["Mg", "Si", "O"], 0.2007774, 0, PhaseType.MINERAL)
    Hi_P_Clinoenstatite = Species("Hi-P-Clinoenstatite", None, ["Mg", "Si", "O"], 0.2007774, 0, PhaseType.MINERAL)
    Diopside = Species("Diopside", None, ["Ca", "Mg", "Si", "O"], 0.2165504, 0, PhaseType.MINERAL)
    Enstatite = Species("Enstatite", None, ["Mg", "Si", "O"], 0.2007774, 0, PhaseType.MINERAL)
    Ferrosilite = Species("Ferrosilite", None, ["Fe", "Si", "O"], 0.2638574, 0, PhaseType.MINERAL)
    Hedenbergite = Species("Hedenbergite", None, ["Ca", "Fe", "Si", "O"], 0.24809040000000002, 0, PhaseType.MINERAL)
    Jadeite = Species("Jadeite", None, ["Na", "Al", "Si", "O"], 0.202138708, 0, PhaseType.MINERAL)
    Kosmochlor = Species("Kosmochlor", None, ["Na", "Cr", "Si", "O"], 0.22715327000000002, 0, PhaseType.MINERAL)
    Mg_Tschermaks_Px = Species("Mg-Tschermaks-Px", None, ["Mg", "Al", "Si", "O"], 0.202349976, 0, PhaseType.MINERAL)
    Protoenstatite = Species("Protoenstatite", None, ["Mg", "Si", "O"], 0.2007774, 0, PhaseType.MINERAL)
    Pseudowollastonite = Species("Pseudowollastonite", None, ["Ca", "Si", "O"], 0.1161617, 0, PhaseType.MINERAL)
    Pyroxmangite = Species("Pyroxmangite", None, ["Mn", "Si", "O"], 0.13102175, 0, PhaseType.MINERAL)
    Rhodonite = Species("Rhodonite", None, ["Mn", "Si", "O"], 0.13102175, 0, PhaseType.MINERAL)
    Walstromite = Species("Walstromite", None, ["Ca", "Si", "O"], 0.1161617, 0, PhaseType.MINERAL)
    Wollastonite = Species("Wollastonite", None, ["Ca", "Si", "O"], 0.1161617, 0, PhaseType.MINERAL)
    Anthophyllite = Species("Anthophyllite", None, ["Mg", "Si", "O", "H"], 0.78082048, 0, PhaseType.MINERAL)
    Fe_Anthophyllite = Species("Fe-Anthophyllite", None, ["Fe", "Si", "O", "H"], 1.00160048, 0, PhaseType.MINERAL)
    Cummingtonite = Species("Cummingtonite", None, ["Mg", "Si", "O", "H"], 0.78082048, 0, PhaseType.MINERAL)
    Ferroactinolite = Species("Ferroactinolite", None, ["Ca", "Fe", "Si", "O", "H"], 0.9700664800000001, 0,
                              PhaseType.MINERAL)
    Ferroglaucophane = Species("Ferroglaucophane", None, ["Na", "Fe", "Al", "Si", "O", "H"], 0.878163096, 0,
                               PhaseType.MINERAL)
    Glaucophane = Species("Glaucophane", None, ["Na", "Mg", "Al", "Si", "O", "H"], 0.7835430959999999, 0,
                          PhaseType.MINERAL)
    Grunerite = Species("Grunerite", None, ["Fe", "Si", "O", "H"], 1.00160048, 0, PhaseType.MINERAL)
    Pargasite = Species("Pargasite", None, ["Na", "Ca", "Mg", "Al", "Si", "O", "H"], 0.835824864, 0, PhaseType.MINERAL)
    Riebeckite = Species("Riebeckite", None, ["Na", "Fe", "Si", "O", "H"], 0.93589002, 0, PhaseType.MINERAL)
    Tremolite = Species("Tremolite", None, ["Ca", "Mg", "Si", "O", "H"], 0.81236648, 0, PhaseType.MINERAL)
    Tschermakite = Species("Tschermakite", None, ["Ca", "Mg", "Al", "Si", "O", "H"], 0.815511632, 0, PhaseType.MINERAL)
    Deerite = Species("Deerite", None, ["Fe", "Si", "O", "H"], 2.1522854, 0, PhaseType.MINERAL)
    Ferrocarpholite = Species("Ferrocarpholite", None, ["Fe", "Al", "Si", "O", "H"], 0.330004836, 0, PhaseType.MINERAL)
    Magnesiocarpholite = Species("Magnesiocarpholite", None, ["Mg", "Al", "Si", "O", "H"], 0.298464836, 0,
                                 PhaseType.MINERAL)
    Fe_Sapphirine_221 = Species("Fe-Sapphirine,221", None, ["Fe", "Al", "Si", "O"], 0.815391304, 0, PhaseType.MINERAL)
    Sapphirine_221 = Species("Sapphirine,221", None, ["Mg", "Al", "Si", "O"], 0.689231304, 0, PhaseType.MINERAL)
    Sapphirine_351 = Species("Sapphirine,351", None, ["Mg", "Al", "Si", "O"], 0.69080388, 0, PhaseType.MINERAL)
    Annite = Species("Annite", None, ["K", "Fe", "Al", "Si", "O", "H"], 0.5118800179999999, 0, PhaseType.MINERAL)
    Celadonite = Species("Celadonite", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.396735518, 0, PhaseType.MINERAL)
    Ferroceladonite = Species("Ferroceladonite", None, ["K", "Fe", "Al", "Si", "O", "H"], 0.428275518, 0,
                              PhaseType.MINERAL)
    Eastonite = Species("Eastonite", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.418832594, 0, PhaseType.MINERAL)
    Margarite = Species("Margarite", None, ["Ca", "Al", "Si", "O", "H"], 0.398183832, 0, PhaseType.MINERAL)
    Mn_Biotite = Species("Mn-Biotite", None, ["K", "Mn", "Al", "Si", "O", "H"], 0.5091591679999999, 0,
                         PhaseType.MINERAL)
    Muscovite = Species("Muscovite", None, ["K", "Al", "Si", "O", "H"], 0.39830809400000006, 0, PhaseType.MINERAL)
    Sodaphlogopite = Species("Sodaphlogopite", None, ["Na", "Mg", "Al", "Si", "O", "H"], 0.40115148800000006, 0,
                             PhaseType.MINERAL)
    Paragonite = Species("Paragonite", None, ["Na", "Al", "Si", "O", "H"], 0.38219956400000005, 0, PhaseType.MINERAL)
    Phlogopite = Species("Phlogopite", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.41726001800000007, 0,
                         PhaseType.MINERAL)
    Al_Free_Chlorite = Species("Al-Free-Chlorite", None, ["Mg", "Si", "O", "H"], 0.55422472, 0, PhaseType.MINERAL)
    Amesite_14A = Species("Amesite,14A", None, ["Mg", "Al", "Si", "O", "H"], 0.557369872, 0, PhaseType.MINERAL)
    Clinochlore_ordered = Species("Clinochlore,ordered", None, ["Mg", "Al", "Si", "O", "H"], 0.555797296, 0,
                                  PhaseType.MINERAL)
    Daphnite = Species("Daphnite", None, ["Fe", "Al", "Si", "O", "H"], 0.713497296, 0, PhaseType.MINERAL)
    Mn_Chlorite = Species("Mn-Chlorite", None, ["Mn", "Al", "Si", "O", "H"], 0.7089625460000001, 0, PhaseType.MINERAL)
    Ferrosudoite = Species("Ferrosudoite", None, ["Fe", "Al", "Si", "O", "H"], 0.5999253720000001, 0, PhaseType.MINERAL)
    Sudoite = Species("Sudoite", None, ["Mg", "Al", "Si", "O", "H"], 0.536845372, 0, PhaseType.MINERAL)
    Antigorite = Species("Antigorite", None, ["Mg", "Si", "O", "H"], 4.535951079999999, 0, PhaseType.MINERAL)
    Chrysotile = Species("Chrysotile", None, ["Mg", "Si", "O", "H"], 0.27711236, 0, PhaseType.MINERAL)
    Ferrotalc = Species("Ferrotalc", None, ["Fe", "Si", "O", "H"], 0.47388568000000003, 0, PhaseType.MINERAL)
    Greenalite = Species("Greenalite", None, ["Fe", "Si", "O", "H"], 0.37173236, 0, PhaseType.MINERAL)
    Kaolinite = Species("Kaolinite", None, ["Al", "Si", "O", "H"], 0.258160436, 0, PhaseType.MINERAL)
    Lizardite = Species("Lizardite", None, ["Mg", "Si", "O", "H"], 0.27711236, 0, PhaseType.MINERAL)
    Minnesotaite = Species("Minnesotaite", None, ["Fe", "Si", "O", "H"], 0.47388568000000003, 0, PhaseType.MINERAL)
    Mg_Minnesotaite = Species("Mg-Minnesotaite", None, ["Mg", "Si", "O", "H"], 0.37926568000000005, 0,
                              PhaseType.MINERAL)
    Prehnite = Species("Prehnite", None, ["Ca", "Al", "Si", "O", "H"], 0.41238425600000006, 0, PhaseType.MINERAL)
    PRL_Talc = Species("PRL-Talc", None, ["Al", "Si", "O", "H"], 0.36031375600000004, 0, PhaseType.MINERAL)
    Pyrophyllite = Species("Pyrophyllite", None, ["Al", "Si", "O", "H"], 0.36031375600000004, 0, PhaseType.MINERAL)
    Ferrostilpnomelane = Species("Ferrostilpnomelane", None, ["K", "Fe", "Al", "Si", "O", "H"], 1.078002176, 0,
                                 PhaseType.MINERAL)
    Mg_Stilpnomelane = Species("Mg-Stilpnomelane", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.920302176, 0,
                               PhaseType.MINERAL)
    Talc = Species("Talc", None, ["Mg", "Si", "O", "H"], 0.37926568000000005, 0, PhaseType.MINERAL)
    Tschermak_Talc = Species("Tschermak-Talc", None, ["Mg", "Al", "Si", "O", "H"], 0.38083825600000004, 0,
                             PhaseType.MINERAL)
    Ferri_Prehnite = Species("Ferri-Prehnite", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.44124771800000007, 0,
                             PhaseType.MINERAL)
    Albite_high = Species("Albite,high", None, ["Na", "Al", "Si", "O"], 0.262223008, 0, PhaseType.MINERAL)
    Analcite = Species("Analcite", None, ["Na", "Al", "Si", "O", "H"], 0.220153988, 0, PhaseType.MINERAL)
    Carnegieite_high = Species("Carnegieite,high", None, ["Na", "Al", "Si", "O"], 0.14205440800000002, 0,
                               PhaseType.MINERAL)
    Carnegieite_low = Species("Carnegieite,low", None, ["Na", "Al", "Si", "O"], 0.14205440800000002, 0,
                              PhaseType.MINERAL)
    K_Cymrite = Species("K-Cymrite", None, ["K", "Al", "Si", "O", "H"], 0.296346818, 0, PhaseType.MINERAL)
    Kalsilite = Species("Kalsilite", None, ["K", "Al", "Si", "O"], 0.158162938, 0, PhaseType.MINERAL)
    Microcline = Species("Microcline", None, ["K", "Al", "Si", "O"], 0.278331538, 0, PhaseType.MINERAL)
    Coesite = Species("Coesite", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    Cristobalite_high = Species("Cristobalite,high", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    Stishovite = Species("Stishovite", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    Tridymite_high = Species("Tridymite,high", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    Heulandite = Species("Heulandite", None, ["Ca", "Al", "Si", "O", "H"], 0.6867204560000001, 0, PhaseType.MINERAL)
    Hollandite = Species("Hollandite", None, ["K", "Al", "Si", "O"], 0.278331538, 0, PhaseType.MINERAL)
    Laumontite = Species("Laumontite", None, ["Ca", "Al", "Si", "O", "H"], 0.470436996, 0, PhaseType.MINERAL)
    Meionite = Species("Meionite", None, ["Ca", "Al", "Si", "C", "O"], 0.934708728, 0, PhaseType.MINERAL)
    Sodalite = Species("Sodalite", None, ["Na", "Al", "Si", "O", "Cl"], 0.9692119880000001, 0, PhaseType.MINERAL)
    Stilbite = Species("Stilbite", None, ["Ca", "Al", "Si", "O", "H"], 0.7047357360000001, 0, PhaseType.MINERAL)
    Si_Wadeite = Species("Si-Wadeite", None, ["K", "Si", "O"], 0.3345332, 0, PhaseType.MINERAL)
    Wairakite = Species("Wairakite", None, ["Ca", "Al", "Si", "O", "H"], 0.434406436, 0, PhaseType.MINERAL)
    Baddeleyite = Species("Baddeleyite", None, ["Zr", "O"], 0.1232228, 0, PhaseType.MINERAL)
    Bixbyite = Species("Bixbyite", None, ["Mn", "O"], 0.15787430000000002, 0, PhaseType.MINERAL)
    Corundum = Species("Corundum", None, ["Al", "O"], 0.101961276, 0, PhaseType.MINERAL)
    Cuprite = Species("Cuprite", None, ["Cu", "O"], 0.1430914, 0, PhaseType.MINERAL)
    Eskolaite = Species("Eskolaite", None, ["Cr", "O"], 0.15199040000000003, 0, PhaseType.MINERAL)
    Geikielite = Species("Geikielite", None, ["Mg", "Ti", "O"], 0.1201702, 0, PhaseType.MINERAL)
    Lime = Species("Lime", None, ["Ca", "O"], 0.0560774, 0, PhaseType.MINERAL)
    Manganosite = Species("Manganosite", None, ["Mn", "O"], 0.07093745, 0, PhaseType.MINERAL)
    MgSi_Corundum = Species("MgSi-Corundum", None, ["Mg", "Si", "O"], 0.1003887, 0, PhaseType.MINERAL)
    Periclase = Species("Periclase", None, ["Mg", "O"], 0.040304400000000004, 0, PhaseType.MINERAL)
    Ferropericlase = Species("Ferropericlase", None, ["Fe", "O"], 0.0718444, 0, PhaseType.MINERAL)
    Pyrophanite = Species("Pyrophanite", None, ["Mn", "Ti", "O"], 0.15080325, 0, PhaseType.MINERAL)
    Rutile = Species("Rutile", None, ["Ti", "O"], 0.0798658, 0, PhaseType.MINERAL)
    Tenorite = Species("Tenorite", None, ["Cu", "O"], 0.0795454, 0, PhaseType.MINERAL)
    Ulvospinel = Species("Ulvospinel", None, ["Fe", "Ti", "O"], 0.2235546, 0, PhaseType.MINERAL)
    Brucite = Species("Brucite", None, ["Mg", "O", "H"], 0.05831968, 0, PhaseType.MINERAL)
    Diaspore = Species("Diaspore", None, ["Al", "O", "H"], 0.059988278, 0, PhaseType.MINERAL)
    Goethite = Species("Goethite", None, ["Fe", "O", "H"], 0.08885174, 0, PhaseType.MINERAL)
    Magnesite = Species("Magnesite", None, ["Mg", "C", "O"], 0.0843139, 0, PhaseType.MINERAL)
    Rhodochrosite = Species("Rhodochrosite", None, ["Mn", "C", "O"], 0.11494695, 0, PhaseType.MINERAL)
    Siderite = Species("Siderite", None, ["Fe", "C", "O"], 0.1158539, 0, PhaseType.MINERAL)
    Anhydrite = Species("Anhydrite", None, ["Ca", "S", "O"], 0.1361406, 0, PhaseType.MINERAL)
    Halite = Species("Halite", None, ["Na", "Cl"], 0.05844277, 0, PhaseType.MINERAL)
    Pyrite = Species("Pyrite", None, ["Fe", "S"], 0.119975, 0, PhaseType.MINERAL)
    Sylvite = Species("Sylvite", None, ["K", "Cl"], 0.0745513, 0, PhaseType.MINERAL)
    Copper = Species("Copper", None, ["Cu"], 0.063546, 0, PhaseType.MINERAL)
    Diamond = Species("Diamond", None, ["C"], 0.0120107, 0, PhaseType.MINERAL)
    Graphite = Species("Graphite", None, ["C"], 0.0120107, 0, PhaseType.MINERAL)
    Sulphur = Species("Sulphur", None, ["S"], 0.032065, 0, PhaseType.MINERAL)
    Gibbsite = Species("Gibbsite", None, ["Al", "O", "H"], 0.078003558, 0, PhaseType.MINERAL)
    Boehmite = Species("Boehmite", None, ["Al", "O", "H"], 0.059988278, 0, PhaseType.MINERAL)
    Fluorphlogopite = Species("Fluorphlogopite", None, ["K", "Mg", "Al", "Si", "O", "F"], 0.42124214400000004, 0,
                              PhaseType.MINERAL)
    Hydroxyapatite = Species("Hydroxyapatite", None, ["Ca", "P", "O", "H"], 0.5023114230000001, 0, PhaseType.MINERAL)
    Fluorapatite = Species("Fluorapatite", None, ["Ca", "P", "O", "F"], 0.504302486, 0, PhaseType.MINERAL)
    Chlorapatite = Species("Chlorapatite", None, ["Ca", "P", "O", "Cl"], 0.520757083, 0, PhaseType.MINERAL)
    Arsenic = Species("Arsenic", None, ["As"], 0.0749216, 0, PhaseType.MINERAL)
    Arsenolite = Species("Arsenolite", None, ["As", "O"], 0.1978414, 0, PhaseType.MINERAL)
    Claudetite = Species("Claudetite", None, ["As", "O"], 0.1978414, 0, PhaseType.MINERAL)
    As2O5_s = Species("As2O5(s)", None, ["As", "O"], 0.2298402, 0, PhaseType.MINERAL)
    Realgar_alpha = Species("Realgar,alpha", None, ["As", "S"], 0.10698660000000002, 0, PhaseType.MINERAL)
    Realgar_beta = Species("Realgar,beta", None, ["As", "S"], 0.10698660000000002, 0, PhaseType.MINERAL)
    Orpiment = Species("Orpiment", None, ["As", "S"], 0.2460382, 0, PhaseType.MINERAL)
    Orpiment_am = Species("Orpiment(am)", None, ["As", "S"], 0.2460382, 0, PhaseType.MINERAL)
    Arsenopyrite = Species("Arsenopyrite", None, ["Fe", "As", "S"], 0.16283160000000002, 0, PhaseType.MINERAL)
    Scorodite = Species("Scorodite", None, ["Fe", "As", "H", "O"], 0.23079476000000002, 0, PhaseType.MINERAL)
    Ferric_As_am = Species("Ferric-As(am)", None, ["Fe", "As", "H", "O"], 0.23079476000000002, 0, PhaseType.MINERAL)
    Barium_As = Species("Barium-As", None, ["Ba", "As", "O"], 0.6898194, 0, PhaseType.MINERAL)
    Barium_H_As = Species("Barium-H-As", None, ["Ba", "As", "H", "O"], 0.29526942, 0, PhaseType.MINERAL)
    a_GaOOH = Species("a-GaOOH", None, ["Ga", "O", "H"], 0.10272974, 0, PhaseType.MINERAL)
    Dawsonite = Species("Dawsonite", None, ["Na", "Al", "C", "O", "H"], 0.143994888, 0, PhaseType.MINERAL)
    Sapphirine_793 = Species("Sapphirine,793", None, ["Mg", "Al", "Si", "O"], 0.690017592, 0, PhaseType.MINERAL)
    Fe_Sapphirine_793 = Species("Fe-Sapphirine,793", None, ["Fe", "Al", "Si", "O"], 0.800407592, 0, PhaseType.MINERAL)
    Gedrite = Species("Gedrite", None, ["Mg", "Al", "Si", "O", "H"], 0.783965632, 0, PhaseType.MINERAL)
    Beidellite_Ca = Species("Beidellite-Ca", None, ["Ca", "Al", "Si", "O", "H"], 0.36656231854000004, 0,
                            PhaseType.MINERAL)
    Beidellite_H = Species("Beidellite-H", None, ["Al", "Si", "O", "H"], 0.36028206874, 0, PhaseType.MINERAL)
    Beidellite_K = Species("Beidellite-K", None, ["K", "Al", "Si", "O", "H"], 0.37285188754000004, 0, PhaseType.MINERAL)
    Beidellite_Mg = Species("Beidellite-Mg", None, ["Mg", "Al", "Si", "O", "H"], 0.36395977354000003, 0,
                            PhaseType.MINERAL)
    Beidellite_Na = Species("Beidellite-Na", None, ["Na", "Al", "Si", "O", "H"], 0.36753607264000004, 0,
                            PhaseType.MINERAL)
    Montmorillonite_Ca = Species("Montmorillonite-Ca", None, ["Ca", "Mg", "Al", "Si", "O", "H"], 0.36604336846, 0,
                                 PhaseType.MINERAL)
    Montmorillonite_K = Species("Montmorillonite-K", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.37233293746, 0,
                                PhaseType.MINERAL)
    Montmorillonite_Mg = Species("Montmorillonite-Mg", None, ["Mg", "Al", "Si", "O", "H"], 0.36344082346, 0,
                                 PhaseType.MINERAL)
    Montmorillonite_Na = Species("Montmorillonite-Na", None, ["Na", "Mg", "Al", "Si", "O", "H"], 0.36701712256, 0,
                                 PhaseType.MINERAL)
    Nontronite_Ca = Species("Nontronite-Ca", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.42428924254000006, 0,
                            PhaseType.MINERAL)
    Nontronite_Mg = Species("Nontronite-Mg", None, ["Mg", "Fe", "Al", "Si", "O", "H"], 0.42168669754000004, 0,
                            PhaseType.MINERAL)
    Nontronite_H = Species("Nontronite-H", None, ["Fe", "Al", "Si", "O", "H"], 0.41800899274000003, 0,
                           PhaseType.MINERAL)
    Nontronite_K = Species("Nontronite-K", None, ["K", "Fe", "Al", "Si", "O", "H"], 0.43057881154000005, 0,
                           PhaseType.MINERAL)
    Nontronite_Na = Species("Nontronite-Na", None, ["Na", "Fe", "Al", "Si", "O", "H"], 0.42526299664000006, 0,
                            PhaseType.MINERAL)
    Saponite_Mg = Species("Saponite-Mg", None, ["Mg", "Al", "Si", "O", "H"], 0.38291169754000004, 0, PhaseType.MINERAL)
    Illite = Species("Illite", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.38390069740000005, 0, PhaseType.MINERAL)
    Dolomite_disordered = Species("Dolomite,disordered", None, ["Ca", "Mg", "C", "O"], 0.1844008, 0, PhaseType.MINERAL)
    Dolomite_ordered = Species("Dolomite,ordered", None, ["Ca", "Mg", "C", "O"], 0.1844008, 0, PhaseType.MINERAL)
    Galena = Species("Galena", None, ["Pb", "S"], 0.239265, 0, PhaseType.MINERAL)
    Barite = Species("Barite", None, ["Ba", "S", "O"], 0.23338960000000003, 0, PhaseType.MINERAL)
    Fluorite = Species("Fluorite", None, ["Ca", "F"], 0.078074806, 0, PhaseType.MINERAL)
    Celestite = Species("Celestite", None, ["Sr", "S", "O"], 0.18368260000000003, 0, PhaseType.MINERAL)
    Anglesite = Species("Anglesite", None, ["Pb", "S", "O"], 0.3032626, 0, PhaseType.MINERAL)
    Chalcedony = Species("Chalcedony", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    SiO2_a = Species("SiO2(a)", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    Larnite = Species("Larnite", None, ["Ca", "Si", "O"], 0.1722391, 0, PhaseType.MINERAL)
    Sphene = Species("Sphene", None, ["Ca", "Ti", "Si", "O"], 0.1960275, 0, PhaseType.MINERAL)
    Quartz = Species("Quartz", None, ["Si", "O"], 0.0600843, 0, PhaseType.MINERAL)
    Nepheline = Species("Nepheline", None, ["Na", "Al", "Si", "O"], 0.14205440800000002, 0, PhaseType.MINERAL)
    Hematite = Species("Hematite", None, ["Fe", "O"], 0.1596882, 0, PhaseType.MINERAL)
    Nickel_Oxide = Species("Nickel-Oxide", None, ["Ni", "O"], 0.0746928, 0, PhaseType.MINERAL)
    Ilmenite = Species("Ilmenite", None, ["Fe", "Ti", "O"], 0.15171020000000002, 0, PhaseType.MINERAL)
    Magnetite = Species("Magnetite", None, ["Fe", "O"], 0.23153259999999998, 0, PhaseType.MINERAL)
    Magnesioferrite = Species("Magnesioferrite", None, ["Mg", "Fe", "O"], 0.19999260000000002, 0, PhaseType.MINERAL)
    Calcite = Species("Calcite", None, ["Ca", "C", "O"], 0.1000869, 0, PhaseType.MINERAL)
    Aragonite = Species("Aragonite", None, ["Ca", "C", "O"], 0.1000869, 0, PhaseType.MINERAL)
    Pyrrhotite_trot = Species("Pyrrhotite,trot", None, ["Fe", "S"], 0.08791, 0, PhaseType.MINERAL)
    Troilite = Species("Troilite", None, ["Fe", "S"], 0.08791, 0, PhaseType.MINERAL)
    Troilite_low = Species("Troilite,low", None, ["Fe", "S"], 0.08791, 0, PhaseType.MINERAL)
    Pyrrhotite_trov = Species("Pyrrhotite,trov", None, ["Fe", "S"], 0.080929375, 0, PhaseType.MINERAL)
    Iron = Species("Iron", None, ["Fe"], 0.055845, 0, PhaseType.MINERAL)
    Nickel = Species("Nickel", None, ["Ni"], 0.0586934, 0, PhaseType.MINERAL)
    Sillimanite = Species("Sillimanite", None, ["Al", "Si", "O"], 0.162045576, 0, PhaseType.MINERAL)
    Gehlenite = Species("Gehlenite", None, ["Ca", "Al", "Si", "O"], 0.274200376, 0, PhaseType.MINERAL)
    Cordierite = Species("Cordierite", None, ["Mg", "Al", "Si", "O"], 0.584952852, 0, PhaseType.MINERAL)
    Hydrous_Cordierite = Species("Hydrous-Cordierite", None, ["Mg", "Al", "Si", "O", "H"], 0.6029681319999999, 0, PhaseType.MINERAL)
    Fe_Cordierite = Species("Fe-Cordierite", None, ["Fe", "Al", "Si", "O"], 0.648032852, 0, PhaseType.MINERAL)
    Mn_Cordierite = Species("Mn-Cordierite", None, ["Mn", "Al", "Si", "O"], 0.6462189519999999, 0, PhaseType.MINERAL)
    Ca_Tschermaks_Px = Species("Ca-Tschermaks-Px", None, ["Ca", "Al", "Si", "O"], 0.21812297600000002, 0,
                               PhaseType.MINERAL)
    Albite = Species("Albite", None, ["Na", "Al", "Si", "O"], 0.262223008, 0, PhaseType.MINERAL)
    Sanidine = Species("Sanidine", None, ["K", "Al", "Si", "O"], 0.278331538, 0, PhaseType.MINERAL)
    Anorthite = Species("Anorthite", None, ["Ca", "Al", "Si", "O"], 0.278207276, 0, PhaseType.MINERAL)
    Leucite = Species("Leucite", None, ["K", "Al", "Si", "O"], 0.218247238, 0, PhaseType.MINERAL)
    Spinel = Species("Spinel", None, ["Mg", "Al", "O"], 0.142265676, 0, PhaseType.MINERAL)
    Hercynite = Species("Hercynite", None, ["Fe", "Al", "O"], 0.17380567600000002, 0, PhaseType.MINERAL)
    Picrochromite = Species("Picrochromite", None, ["Mg", "Cr", "O"], 0.1922948, 0, PhaseType.MINERAL)
    Dolomite = Species("Dolomite", None, ["Ca", "Mg", "C", "O"], 0.1844008, 0, PhaseType.MINERAL)
    Ankerite = Species("Ankerite", None, ["Ca", "Fe", "C", "O"], 0.21594080000000002, 0, PhaseType.MINERAL)
    CO_g = Species("CO(g)", None, ["C", "O"], 0.0280101, 0, PhaseType.GASEOUS)
    S2_g = Species("S2(g)", None, ["S"], 0.06413, 0, PhaseType.GASEOUS)
    Phenol_g = Species("Phenol(g)", None, ["C", "H", "O"], 0.09411123999999998, 0, PhaseType.GASEOUS)
    o_Cresol_g = Species("o-Cresol(g)", None, ["C", "H", "O"], 0.10813782, 0, PhaseType.GASEOUS)
    m_Cresol_g = Species("m-Cresol(g)", None, ["C", "H", "O"], 0.10813782, 0, PhaseType.GASEOUS)
    p_Cresol_g = Species("p-Cresol(g)", None, ["C", "H", "O"], 0.10813782, 0, PhaseType.GASEOUS)
    Ethylene_g = Species("Ethylene(g)", None, ["C", "H"], 0.028053159999999997, 0, PhaseType.GASEOUS)
    Rn_g = Species("Rn(g)", None, ["Rn"], 0.222, 0, PhaseType.GASEOUS)
    NO_g = Species("NO(g)", None, ["N", "O"], 0.0300061, 0, PhaseType.GASEOUS)
    N2O_g = Species("N2O(g)", None, ["N", "O"], 0.044012800000000005, 0, PhaseType.GASEOUS)
    Ag_CO3_minus = Species("Ag(CO3)-", None, ["Ag", "C", "O"], 0.1678771, -1.0, PhaseType.AQUEOUS)
    Ag_CO3_2_minus3 = Species("Ag(CO3)2-3", None, ["Ag", "C", "O"], 0.227886, -3.0, PhaseType.AQUEOUS)
    Ag_plus = Species("Ag+", None, ["Ag"], 0.1078682, 1.0, PhaseType.AQUEOUS)
    Ag_plus2 = Species("Ag+2", None, ["Ag"], 0.1078682, 2.0, PhaseType.AQUEOUS)
    AgCl_aq = Species("AgCl(aq)", None, ["Ag", "Cl"], 0.14332119999999998, 0.0, PhaseType.AQUEOUS)
    AgCl2_minus = Species("AgCl2-", None, ["Ag", "Cl"], 0.1787742, -1.0, PhaseType.AQUEOUS)
    AgCl3_minus2 = Species("AgCl3-2", None, ["Ag", "Cl"], 0.2142272, -2.0, PhaseType.AQUEOUS)
    AgCl4_minus3 = Species("AgCl4-3", None, ["Ag", "Cl"], 0.2496802, -3.0, PhaseType.AQUEOUS)
    AgOH_aq = Species("AgOH(aq)", None, ["Ag", "O", "H"], 0.12487554, 0.0, PhaseType.AQUEOUS)
    AgO_minus = Species("AgO-", None, ["Ag", "O"], 0.1238676, -1.0, PhaseType.AQUEOUS)
    AgNO3_aq = Species("AgNO3(aq)", None, ["Ag", "N", "O"], 0.1698731, 0.0, PhaseType.AQUEOUS)
    AlOH_plus2 = Species("AlOH+2", None, ["Al", "O", "H"], 0.043988877999999995, 2.0, PhaseType.AQUEOUS)
    Al_plus3 = Species("Al+3", None, ["Al"], 0.026981538, 3.0, PhaseType.AQUEOUS)
    AlH3SiO4_plus2 = Species("AlH3SiO4+2", None, ["Al", "H", "Si", "O"], 0.122088458, 2.0, PhaseType.AQUEOUS)
    Al_OH_3_aq = Species("Al(OH)3(aq)", None, ["Al", "O", "H"], 0.078003558, 0.0, PhaseType.AQUEOUS)
    Al_OH_4_minus = Species("Al(OH)4-", None, ["Al", "O", "H"], 0.095010898, -1.0, PhaseType.AQUEOUS)
    Al_OH_2_plus = Species("Al(OH)2+", None, ["Al", "O", "H"], 0.060996218, 1.0, PhaseType.AQUEOUS)
    Au_plus = Species("Au+", None, ["Au"], 0.19696655, 1.0, PhaseType.AQUEOUS)
    Au_plus3 = Species("Au+3", None, ["Au"], 0.19696655, 3.0, PhaseType.AQUEOUS)
    B_OH_3_aq = Species("B(OH)3(aq)", None, ["B", "O", "H"], 0.06183302, 0.0, PhaseType.AQUEOUS)
    BF4_minus = Species("BF4-", None, ["B", "F"], 0.086804612, -1.0, PhaseType.AQUEOUS)
    BO2_minus = Species("BO2-", None, ["B", "O"], 0.0428098, -1.0, PhaseType.AQUEOUS)
    Ba_HCO3_plus = Species("Ba(HCO3)+", None, ["Ba", "H", "C", "O"], 0.19834384, 1.0, PhaseType.AQUEOUS)
    Ba_plus2 = Species("Ba+2", None, ["Ba"], 0.137327, 2.0, PhaseType.AQUEOUS)
    BaCl_plus = Species("BaCl+", None, ["Ba", "Cl"], 0.17278, 1.0, PhaseType.AQUEOUS)
    BaOH_plus = Species("BaOH+", None, ["Ba", "O", "H"], 0.15433434000000001, 1.0, PhaseType.AQUEOUS)
    Be_plus2 = Species("Be+2", None, ["Be"], 0.009012182, 2.0, PhaseType.AQUEOUS)
    BeOH_plus = Species("BeOH+", None, ["Be", "O", "H"], 0.026019522, 1.0, PhaseType.AQUEOUS)
    BeO_aq = Species("BeO(aq)", None, ["Be", "O"], 0.025011582, 0.0, PhaseType.AQUEOUS)
    HBeO2_minus = Species("HBeO2-", None, ["H", "Be", "O"], 0.042018922, -1.0, PhaseType.AQUEOUS)
    BeO2_minus2 = Species("BeO2-2", None, ["Be", "O"], 0.041010982, -2.0, PhaseType.AQUEOUS)
    Br_minus = Species("Br-", None, ["Br"], 0.079904, -1.0, PhaseType.AQUEOUS)
    Br3_minus = Species("Br3-", None, ["Br"], 0.239712, -1.0, PhaseType.AQUEOUS)
    HBrO_aq = Species("HBrO(aq)", None, ["H", "Br", "O"], 0.09691134, 0.0, PhaseType.AQUEOUS)
    BrO_minus = Species("BrO-", None, ["Br", "O"], 0.0959034, -1.0, PhaseType.AQUEOUS)
    BrO3_minus = Species("BrO3-", None, ["Br", "O"], 0.12790220000000002, -1.0, PhaseType.AQUEOUS)
    BrO4_minus = Species("BrO4-", None, ["Br", "O"], 0.14390160000000002, -1.0, PhaseType.AQUEOUS)
    CaOH_plus = Species("CaOH+", None, ["Ca", "O", "H"], 0.05708534, 1.0, PhaseType.AQUEOUS)
    Ce_plus4 = Species("Ce+4", None, ["Ce"], 0.140116, 4.0, PhaseType.AQUEOUS)
    CO_aq = Species("CO(aq)", None, ["C", "O"], 0.0280101, 0.0, PhaseType.AQUEOUS)
    CO2_aq = Species("CO2(aq)", None, ["C", "O"], 0.0440095, 0.0, PhaseType.AQUEOUS)
    CO3_minus2 = Species("CO3-2", None, ["C", "O"], 0.060008900000000004, -2.0, PhaseType.AQUEOUS)
    Ca_HCO3_plus = Species("Ca(HCO3)+", None, ["Ca", "H", "C", "O"], 0.10109484, 1.0, PhaseType.AQUEOUS)
    Ca_plus2 = Species("Ca+2", None, ["Ca"], 0.040078, 2.0, PhaseType.AQUEOUS)
    CaCl_plus = Species("CaCl+", None, ["Ca", "Cl"], 0.075531, 1.0, PhaseType.AQUEOUS)
    CaCl2_aq = Species("CaCl2(aq)", None, ["Ca", "Cl"], 0.110984, 0.0, PhaseType.AQUEOUS)
    CaF_plus = Species("CaF+", None, ["Ca", "F"], 0.059076403, 1.0, PhaseType.AQUEOUS)
    CaSO4_aq = Species("CaSO4(aq)", None, ["Ca", "S", "O"], 0.1361406, 0.0, PhaseType.AQUEOUS)
    Cd_plus2 = Species("Cd+2", None, ["Cd"], 0.112411, 2.0, PhaseType.AQUEOUS)
    CdOH_plus = Species("CdOH+", None, ["Cd", "O", "H"], 0.12941834000000002, 1.0, PhaseType.AQUEOUS)
    CdO_aq = Species("CdO(aq)", None, ["Cd", "O"], 0.1284104, 0.0, PhaseType.AQUEOUS)
    HCdO2_minus = Species("HCdO2-", None, ["H", "Cd", "O"], 0.14541774, -1.0, PhaseType.AQUEOUS)
    CdO2_minus2 = Species("CdO2-2", None, ["Cd", "O"], 0.1444098, -2.0, PhaseType.AQUEOUS)
    Ce_plus2 = Species("Ce+2", None, ["Ce"], 0.140116, 2.0, PhaseType.AQUEOUS)
    Ce_plus3 = Species("Ce+3", None, ["Ce"], 0.140116, 3.0, PhaseType.AQUEOUS)
    Cl_minus = Species("Cl-", None, ["Cl"], 0.035453, -1.0, PhaseType.AQUEOUS)
    HClO_aq = Species("HClO(aq)", None, ["H", "Cl", "O"], 0.052460339999999994, 0.0, PhaseType.AQUEOUS)
    ClO_minus = Species("ClO-", None, ["Cl", "O"], 0.051452399999999995, -1.0, PhaseType.AQUEOUS)
    ClO2_minus = Species("ClO2-", None, ["Cl", "O"], 0.0674518, -1.0, PhaseType.AQUEOUS)
    ClO3_minus = Species("ClO3-", None, ["Cl", "O"], 0.0834512, -1.0, PhaseType.AQUEOUS)
    ClO4_minus = Species("ClO4-", None, ["Cl", "O"], 0.0994506, -1.0, PhaseType.AQUEOUS)
    Co_plus2 = Species("Co+2", None, ["Co"], 0.0589332, 2.0, PhaseType.AQUEOUS)
    Co_plus3 = Species("Co+3", None, ["Co"], 0.0589332, 3.0, PhaseType.AQUEOUS)
    CoOH_plus = Species("CoOH+", None, ["Co", "O", "H"], 0.07594054, 1.0, PhaseType.AQUEOUS)
    CoO_aq = Species("CoO(aq)", None, ["Co", "O"], 0.0749326, 0.0, PhaseType.AQUEOUS)
    HCoO2_minus = Species("HCoO2-", None, ["H", "Co", "O"], 0.09193994, -1.0, PhaseType.AQUEOUS)
    CoO2_minus2 = Species("CoO2-2", None, ["Co", "O"], 0.090932, -2.0, PhaseType.AQUEOUS)
    CoOH_plus2 = Species("CoOH+2", None, ["Co", "O", "H"], 0.07594054, 2.0, PhaseType.AQUEOUS)
    Cr2O7_minus2 = Species("Cr2O7-2", None, ["Cr", "O"], 0.215988, -2.0, PhaseType.AQUEOUS)
    CrO4_minus2 = Species("CrO4-2", None, ["Cr", "O"], 0.1159937, -2.0, PhaseType.AQUEOUS)
    Cs_plus = Species("Cs+", None, ["Cs"], 0.13290545, 1.0, PhaseType.AQUEOUS)
    CsBr_aq = Species("CsBr(aq)", None, ["Cs", "Br"], 0.21280945, 0.0, PhaseType.AQUEOUS)
    CsCl_aq = Species("CsCl(aq)", None, ["Cs", "Cl"], 0.16835845, 0.0, PhaseType.AQUEOUS)
    CsI_aq = Species("CsI(aq)", None, ["Cs", "I"], 0.25980992, 0.0, PhaseType.AQUEOUS)
    CsOH_aq = Species("CsOH(aq)", None, ["Cs", "O", "H"], 0.14991279000000002, 0.0, PhaseType.AQUEOUS)
    Cu_plus = Species("Cu+", None, ["Cu"], 0.063546, 1.0, PhaseType.AQUEOUS)
    Cu_plus2 = Species("Cu+2", None, ["Cu"], 0.063546, 2.0, PhaseType.AQUEOUS)
    CuOH_plus = Species("CuOH+", None, ["Cu", "O", "H"], 0.08055334, 1.0, PhaseType.AQUEOUS)
    CuO_aq = Species("CuO(aq)", None, ["Cu", "O"], 0.0795454, 0.0, PhaseType.AQUEOUS)
    HCuO2_minus = Species("HCuO2-", None, ["H", "Cu", "O"], 0.09655274, -1.0, PhaseType.AQUEOUS)
    CuO2_minus2 = Species("CuO2-2", None, ["Cu", "O"], 0.09554480000000001, -2.0, PhaseType.AQUEOUS)
    Dy_plus2 = Species("Dy+2", None, ["Dy"], 0.1625, 2.0, PhaseType.AQUEOUS)
    Dy_plus3 = Species("Dy+3", None, ["Dy"], 0.1625, 3.0, PhaseType.AQUEOUS)
    Dy_plus4 = Species("Dy+4", None, ["Dy"], 0.1625, 4.0, PhaseType.AQUEOUS)
    Er_plus2 = Species("Er+2", None, ["Er"], 0.167259, 2.0, PhaseType.AQUEOUS)
    Er_plus3 = Species("Er+3", None, ["Er"], 0.167259, 3.0, PhaseType.AQUEOUS)
    Er_plus4 = Species("Er+4", None, ["Er"], 0.167259, 4.0, PhaseType.AQUEOUS)
    Eu_plus2 = Species("Eu+2", None, ["Eu"], 0.151964, 2.0, PhaseType.AQUEOUS)
    Eu_plus3 = Species("Eu+3", None, ["Eu"], 0.151964, 3.0, PhaseType.AQUEOUS)
    Eu_plus4 = Species("Eu+4", None, ["Eu"], 0.151964, 4.0, PhaseType.AQUEOUS)
    F_minus = Species("F-", None, ["F"], 0.018998403, -1.0, PhaseType.AQUEOUS)
    Fe_plus2 = Species("Fe+2", None, ["Fe"], 0.055845, 2.0, PhaseType.AQUEOUS)
    Fe_plus3 = Species("Fe+3", None, ["Fe"], 0.055845, 3.0, PhaseType.AQUEOUS)
    FeCl_plus = Species("FeCl+", None, ["Fe", "Cl"], 0.09129799999999999, 1.0, PhaseType.AQUEOUS)
    FeCl2_aq = Species("FeCl2(aq)", None, ["Fe", "Cl"], 0.126751, 0.0, PhaseType.AQUEOUS)
    FeOH_plus2 = Species("FeOH+2", None, ["Fe", "O", "H"], 0.07285234, 2.0, PhaseType.AQUEOUS)
    FeOH_plus = Species("FeOH+", None, ["Fe", "O", "H"], 0.07285234, 1.0, PhaseType.AQUEOUS)
    FeO_plus = Species("FeO+", None, ["Fe", "O"], 0.0718444, 1.0, PhaseType.AQUEOUS)
    FeO_aq = Species("FeO(aq)", None, ["Fe", "O"], 0.0718444, 0.0, PhaseType.AQUEOUS)
    HFeO2_minus = Species("HFeO2-", None, ["H", "Fe", "O"], 0.08885174, -1.0, PhaseType.AQUEOUS)
    HFeO2_aq = Species("HFeO2(aq)", None, ["H", "Fe", "O"], 0.08885174, 0.0, PhaseType.AQUEOUS)
    FeO2_minus = Species("FeO2-", None, ["Fe", "O"], 0.0878438, -1.0, PhaseType.AQUEOUS)
    Ga_plus3 = Species("Ga+3", None, ["Ga"], 0.069723, 3.0, PhaseType.AQUEOUS)
    GaOH_plus2 = Species("GaOH+2", None, ["Ga", "O", "H"], 0.08673033999999999, 2.0, PhaseType.AQUEOUS)
    GaO_plus = Species("GaO+", None, ["Ga", "O"], 0.08572239999999999, 1.0, PhaseType.AQUEOUS)
    HGaO2_aq = Species("HGaO2(aq)", None, ["H", "Ga", "O"], 0.10272973999999999, 0.0, PhaseType.AQUEOUS)
    GaO2_minus = Species("GaO2-", None, ["Ga", "O"], 0.1017218, -1.0, PhaseType.AQUEOUS)
    Gd_plus2 = Species("Gd+2", None, ["Gd"], 0.15725, 2.0, PhaseType.AQUEOUS)
    Gd_plus3 = Species("Gd+3", None, ["Gd"], 0.15725, 3.0, PhaseType.AQUEOUS)
    Gd_plus4 = Species("Gd+4", None, ["Gd"], 0.15725, 4.0, PhaseType.AQUEOUS)
    H_plus = Species("H+", None, ["H"], 0.00100794, 1.0, PhaseType.AQUEOUS)
    H2_aq = Species("H2(aq)", None, ["H"], 0.00201588, 0.0, PhaseType.AQUEOUS)
    NaH2AsO4_aq = Species("NaH2AsO4(aq)", None, ["Na", "H", "As", "O"], 0.16392485, 0.0, PhaseType.AQUEOUS)
    KH2AsO4_aq = Species("KH2AsO4(aq)", None, ["K", "H", "As", "O"], 0.18003338000000002, 0.0, PhaseType.AQUEOUS)
    MgH2AsO4_plus = Species("MgH2AsO4+", None, ["Mg", "H", "As", "O"], 0.16524008, 1.0, PhaseType.AQUEOUS)
    CaH2AsO4_plus = Species("CaH2AsO4+", None, ["Ca", "H", "As", "O"], 0.18101308, 1.0, PhaseType.AQUEOUS)
    SrH2AsO4_plus = Species("SrH2AsO4+", None, ["Sr", "H", "As", "O"], 0.22855508000000002, 1.0, PhaseType.AQUEOUS)
    MnH2AsO4_plus = Species("MnH2AsO4+", None, ["Mn", "H", "As", "O"], 0.19587313, 1.0, PhaseType.AQUEOUS)
    FeH2AsO4_plus = Species("FeH2AsO4+", None, ["Fe", "H", "As", "O"], 0.19678008000000002, 1.0, PhaseType.AQUEOUS)
    CoH2AsO4_plus = Species("CoH2AsO4+", None, ["Co", "H", "As", "O"], 0.19986828, 1.0, PhaseType.AQUEOUS)
    NiH2AsO4_plus = Species("NiH2AsO4+", None, ["Ni", "H", "As", "O"], 0.19962848, 1.0, PhaseType.AQUEOUS)
    CuH2AsO4_plus = Species("CuH2AsO4+", None, ["Cu", "H", "As", "O"], 0.20448107999999998, 1.0, PhaseType.AQUEOUS)
    ZnH2AsO4_plus = Species("ZnH2AsO4+", None, ["Zn", "H", "As", "O"], 0.20634407999999999, 1.0, PhaseType.AQUEOUS)
    PbH2AsO4_plus = Species("PbH2AsO4+", None, ["Pb", "H", "As", "O"], 0.34813508, 1.0, PhaseType.AQUEOUS)
    AlH2AsO4_plus2 = Species("AlH2AsO4+2", None, ["Al", "H", "As", "O"], 0.16791661800000002, 2.0, PhaseType.AQUEOUS)
    FeH2AsO4_plus2 = Species("FeH2AsO4+2", None, ["Fe", "H", "As", "O"], 0.19678008000000002, 2.0, PhaseType.AQUEOUS)
    NaHAsO4_minus = Species("NaHAsO4-", None, ["Na", "H", "As", "O"], 0.16291691000000003, -1.0, PhaseType.AQUEOUS)
    KHAsO4_minus = Species("KHAsO4-", None, ["K", "H", "As", "O"], 0.17902544, -1.0, PhaseType.AQUEOUS)
    MgHAsO4_aq = Species("MgHAsO4(aq)", None, ["Mg", "H", "As", "O"], 0.16423214000000003, 0.0, PhaseType.AQUEOUS)
    CaHAsO4_aq = Species("CaHAsO4(aq)", None, ["Ca", "H", "As", "O"], 0.18000514, 0.0, PhaseType.AQUEOUS)
    SrHAsO4_aq = Species("SrHAsO4(aq)", None, ["Sr", "H", "As", "O"], 0.22754713999999998, 0.0, PhaseType.AQUEOUS)
    MnHAsO4_aq = Species("MnHAsO4(aq)", None, ["Mn", "H", "As", "O"], 0.19486519000000002, 0.0, PhaseType.AQUEOUS)
    FeHAsO4_aq = Species("FeHAsO4(aq)", None, ["Fe", "H", "As", "O"], 0.19577213999999998, 0.0, PhaseType.AQUEOUS)
    CoHAsO4_aq = Species("CoHAsO4(aq)", None, ["Co", "H", "As", "O"], 0.19886034000000002, 0.0, PhaseType.AQUEOUS)
    NiHAsO4_aq = Species("NiHAsO4(aq)", None, ["Ni", "H", "As", "O"], 0.19862054, 0.0, PhaseType.AQUEOUS)
    CuHAsO4_aq = Species("CuHAsO4(aq)", None, ["Cu", "H", "As", "O"], 0.20347314, 0.0, PhaseType.AQUEOUS)
    ZnHAsO4_aq = Species("ZnHAsO4(aq)", None, ["Zn", "H", "As", "O"], 0.20533614, 0.0, PhaseType.AQUEOUS)
    PbHAsO4_aq = Species("PbHAsO4(aq)", None, ["Pb", "H", "As", "O"], 0.34712714, 0.0, PhaseType.AQUEOUS)
    AlHAsO4_plus = Species("AlHAsO4+", None, ["Al", "H", "As", "O"], 0.166908678, 1.0, PhaseType.AQUEOUS)
    FeHAsO4_plus = Species("FeHAsO4+", None, ["Fe", "H", "As", "O"], 0.19577213999999998, 1.0, PhaseType.AQUEOUS)
    NaAsO4_minus2 = Species("NaAsO4-2", None, ["Na", "As", "O"], 0.16190896999999999, -2.0, PhaseType.AQUEOUS)
    KAsO4_minus2 = Species("KAsO4-2", None, ["K", "As", "O"], 0.1780175, -2.0, PhaseType.AQUEOUS)
    MgAsO4_minus = Species("MgAsO4-", None, ["Mg", "As", "O"], 0.16322419999999999, -1.0, PhaseType.AQUEOUS)
    CaAsO4_minus = Species("CaAsO4-", None, ["Ca", "As", "O"], 0.17899720000000002, -1.0, PhaseType.AQUEOUS)
    SrAsO4_minus = Species("SrAsO4-", None, ["Sr", "As", "O"], 0.2265392, -1.0, PhaseType.AQUEOUS)
    MnAsO4_minus = Species("MnAsO4-", None, ["Mn", "As", "O"], 0.19385724999999998, -1.0, PhaseType.AQUEOUS)
    FeAsO4_minus = Species("FeAsO4-", None, ["Fe", "As", "O"], 0.1947642, -1.0, PhaseType.AQUEOUS)
    CoAsO4_minus = Species("CoAsO4-", None, ["Co", "As", "O"], 0.19785239999999998, -1.0, PhaseType.AQUEOUS)
    NiAsO4_minus = Species("NiAsO4-", None, ["Ni", "As", "O"], 0.19761260000000003, -1.0, PhaseType.AQUEOUS)
    CuAsO4_minus = Species("CuAsO4-", None, ["Cu", "As", "O"], 0.2024652, -1.0, PhaseType.AQUEOUS)
    ZnAsO4_minus = Species("ZnAsO4-", None, ["Zn", "As", "O"], 0.20432820000000002, -1.0, PhaseType.AQUEOUS)
    PbAsO4_minus = Species("PbAsO4-", None, ["Pb", "As", "O"], 0.34611919999999996, -1.0, PhaseType.AQUEOUS)
    AlAsO4_aq = Species("AlAsO4(aq)", None, ["Al", "As", "O"], 0.165900738, 0.0, PhaseType.AQUEOUS)
    FeAsO4_aq = Species("FeAsO4(aq)", None, ["Fe", "As", "O"], 0.1947642, 0.0, PhaseType.AQUEOUS)
    NaH2AsO3_aq = Species("NaH2AsO3(aq)", None, ["Na", "H", "As", "O"], 0.14792545, 0.0, PhaseType.AQUEOUS)
    AgH2AsO3_aq = Species("AgH2AsO3(aq)", None, ["Ag", "H", "As", "O"], 0.23280388000000002, 0.0, PhaseType.AQUEOUS)
    MgH2AsO3_plus = Species("MgH2AsO3+", None, ["Mg", "H", "As", "O"], 0.14924068000000001, 1.0, PhaseType.AQUEOUS)
    CaH2AsO3_plus = Species("CaH2AsO3+", None, ["Ca", "H", "As", "O"], 0.16501368, 1.0, PhaseType.AQUEOUS)
    SrH2AsO3_plus = Species("SrH2AsO3+", None, ["Sr", "H", "As", "O"], 0.21255568000000002, 1.0, PhaseType.AQUEOUS)
    BaH2AsO3_plus = Species("BaH2AsO3+", None, ["Ba", "H", "As", "O"], 0.26226268, 1.0, PhaseType.AQUEOUS)
    CuH2AsO3_plus = Species("CuH2AsO3+", None, ["Cu", "H", "As", "O"], 0.18848167999999998, 1.0, PhaseType.AQUEOUS)
    PbH2AsO3_plus = Species("PbH2AsO3+", None, ["Pb", "H", "As", "O"], 0.33213568, 1.0, PhaseType.AQUEOUS)
    AlH2AsO3_plus2 = Species("AlH2AsO3+2", None, ["Al", "H", "As", "O"], 0.15191721800000002, 2.0, PhaseType.AQUEOUS)
    FeH2AsO3_plus2 = Species("FeH2AsO3+2", None, ["Fe", "H", "As", "O"], 0.18078068000000003, 2.0, PhaseType.AQUEOUS)
    H2P2O7_minus2 = Species("H2P2O7-2", None, ["H", "P", "O"], 0.175959202, -2.0, PhaseType.AQUEOUS)
    H2PO4_minus = Species("H2PO4-", None, ["H", "P", "O"], 0.096987241, -1.0, PhaseType.AQUEOUS)
    H2S_aq = Species("H2S(aq)", None, ["H", "S"], 0.03408088, 0.0, PhaseType.AQUEOUS)
    H3VO4_aq = Species("H3VO4(aq)", None, ["H", "V", "O"], 0.11796292, 0.0, PhaseType.AQUEOUS)
    H2VO4_minus = Species("H2VO4-", None, ["H", "V", "O"], 0.11695498, -1.0, PhaseType.AQUEOUS)
    H3P2O7_minus = Species("H3P2O7-", None, ["H", "P", "O"], 0.17696714200000002, -1.0, PhaseType.AQUEOUS)
    H3PO4_aq = Species("H3PO4(aq)", None, ["H", "P", "O"], 0.097995181, 0.0, PhaseType.AQUEOUS)
    HCO3_minus = Species("HCO3-", None, ["H", "C", "O"], 0.06101684, -1.0, PhaseType.AQUEOUS)
    HCrO4_minus = Species("HCrO4-", None, ["H", "Cr", "O"], 0.11700164, -1.0, PhaseType.AQUEOUS)
    HF_aq = Species("HF(aq)", None, ["H", "F"], 0.020006343, 0.0, PhaseType.AQUEOUS)
    HF2_minus = Species("HF2-", None, ["H", "F"], 0.039004746, -1.0, PhaseType.AQUEOUS)
    HNO3_aq = Species("HNO3(aq)", None, ["H", "N", "O"], 0.06301284, 0.0, PhaseType.AQUEOUS)
    HO2_minus = Species("HO2-", None, ["H", "O"], 0.03300674, -1.0, PhaseType.AQUEOUS)
    HPO4_minus2 = Species("HPO4-2", None, ["H", "P", "O"], 0.095979301, -2.0, PhaseType.AQUEOUS)
    HS_minus = Species("HS-", None, ["H", "S"], 0.03307294, -1.0, PhaseType.AQUEOUS)
    HSO3_minus = Species("HSO3-", None, ["H", "S", "O"], 0.08107114000000001, -1.0, PhaseType.AQUEOUS)
    HSO4_minus = Species("HSO4-", None, ["H", "S", "O"], 0.09707054000000001, -1.0, PhaseType.AQUEOUS)
    HSO5_minus = Species("HSO5-", None, ["H", "S", "O"], 0.11306994000000001, -1.0, PhaseType.AQUEOUS)
    HSe_minus = Species("HSe-", None, ["H", "Se"], 0.07996794, -1.0, PhaseType.AQUEOUS)
    H2SeO3_aq = Species("H2SeO3(aq)", None, ["H", "Se", "O"], 0.12897408, 0.0, PhaseType.AQUEOUS)
    HSeO3_minus = Species("HSeO3-", None, ["H", "Se", "O"], 0.12796614, -1.0, PhaseType.AQUEOUS)
    HSeO4_minus = Species("HSeO4-", None, ["H", "Se", "O"], 0.14396554, -1.0, PhaseType.AQUEOUS)
    HSiO3_minus = Species("HSiO3-", None, ["H", "Si", "O"], 0.07709164, -1.0, PhaseType.AQUEOUS)
    HVO4_minus2 = Species("HVO4-2", None, ["H", "V", "O"], 0.11594704, -2.0, PhaseType.AQUEOUS)
    He_aq = Species("He(aq)", None, ["He"], 0.004002602, 0.0, PhaseType.AQUEOUS)
    Hg_plus2 = Species("Hg+2", None, ["Hg"], 0.20059, 2.0, PhaseType.AQUEOUS)
    HgOH_plus = Species("HgOH+", None, ["Hg", "O", "H"], 0.21759734, 1.0, PhaseType.AQUEOUS)
    HgO_aq = Species("HgO(aq)", None, ["Hg", "O"], 0.2165894, 0.0, PhaseType.AQUEOUS)
    HHgO2_minus = Species("HHgO2-", None, ["H", "Hg", "O"], 0.23359674, -1.0, PhaseType.AQUEOUS)
    Hg2_plus2 = Species("Hg2+2", None, ["Hg"], 0.40118, 2.0, PhaseType.AQUEOUS)
    Ho_plus2 = Species("Ho+2", None, ["Ho"], 0.16493032, 2.0, PhaseType.AQUEOUS)
    Ho_plus3 = Species("Ho+3", None, ["Ho"], 0.16493032, 3.0, PhaseType.AQUEOUS)
    Ho_plus4 = Species("Ho+4", None, ["Ho"], 0.16493032, 4.0, PhaseType.AQUEOUS)
    I_minus = Species("I-", None, ["I"], 0.12690447, -1.0, PhaseType.AQUEOUS)
    I3_minus = Species("I3-", None, ["I"], 0.38071341, -1.0, PhaseType.AQUEOUS)
    HIO_aq = Species("HIO(aq)", None, ["H", "I", "O"], 0.14391181, 0.0, PhaseType.AQUEOUS)
    IO_minus = Species("IO-", None, ["I", "O"], 0.14290387, -1.0, PhaseType.AQUEOUS)
    IO3_minus = Species("IO3-", None, ["I", "O"], 0.17490266999999998, -1.0, PhaseType.AQUEOUS)
    IO4_minus = Species("IO4-", None, ["I", "O"], 0.19090206999999998, -1.0, PhaseType.AQUEOUS)
    In_plus3 = Species("In+3", None, ["In"], 0.114818, 3.0, PhaseType.AQUEOUS)
    InOH_plus2 = Species("InOH+2", None, ["In", "O", "H"], 0.13182534, 2.0, PhaseType.AQUEOUS)
    InO_plus = Species("InO+", None, ["In", "O"], 0.1308174, 1.0, PhaseType.AQUEOUS)
    HInO2_aq = Species("HInO2(aq)", None, ["H", "In", "O"], 0.14782474, 0.0, PhaseType.AQUEOUS)
    InO2_minus = Species("InO2-", None, ["In", "O"], 0.1468168, -1.0, PhaseType.AQUEOUS)
    K_plus = Species("K+", None, ["K"], 0.0390983, 1.0, PhaseType.AQUEOUS)
    KBr_aq = Species("KBr(aq)", None, ["K", "Br"], 0.1190023, 0.0, PhaseType.AQUEOUS)
    KCl_aq = Species("KCl(aq)", None, ["K", "Cl"], 0.0745513, 0.0, PhaseType.AQUEOUS)
    KAlO2_aq = Species("KAlO2(aq)", None, ["K", "Al", "O"], 0.098078638, 0.0, PhaseType.AQUEOUS)
    KhSO4_aq = Species("KhSO4(aq)", None, ["K", "H", "S", "O"], 0.13616884, 0.0, PhaseType.AQUEOUS)
    KI_aq = Species("KI(aq)", None, ["K", "I"], 0.16600277, 0.0, PhaseType.AQUEOUS)
    KOH_aq = Species("KOH(aq)", None, ["K", "O", "H"], 0.05610564, 0.0, PhaseType.AQUEOUS)
    KSO4_minus = Species("KSO4-", None, ["K", "S", "O"], 0.13516090000000003, -1.0, PhaseType.AQUEOUS)
    Kr_aq = Species("Kr(aq)", None, ["Kr"], 0.083798, 0.0, PhaseType.AQUEOUS)
    La_plus3 = Species("La+3", None, ["La"], 0.1389055, 3.0, PhaseType.AQUEOUS)
    Li_plus = Species("Li+", None, ["Li"], 0.006941, 1.0, PhaseType.AQUEOUS)
    LiCl_aq = Species("LiCl(aq)", None, ["Li", "Cl"], 0.042394, 0.0, PhaseType.AQUEOUS)
    LiOH_aq = Species("LiOH(aq)", None, ["Li", "O", "H"], 0.02394834, 0.0, PhaseType.AQUEOUS)
    Lu_plus3 = Species("Lu+3", None, ["Lu"], 0.174967, 3.0, PhaseType.AQUEOUS)
    Lu_plus4 = Species("Lu+4", None, ["Lu"], 0.174967, 4.0, PhaseType.AQUEOUS)
    Mg_HCO3_plus = Species("Mg(HCO3)+", None, ["Mg", "H", "C", "O"], 0.08532184000000001, 1.0, PhaseType.AQUEOUS)
    Mg_plus2 = Species("Mg+2", None, ["Mg"], 0.024305, 2.0, PhaseType.AQUEOUS)
    MgCl_plus = Species("MgCl+", None, ["Mg", "Cl"], 0.059758, 1.0, PhaseType.AQUEOUS)
    MgF_plus = Species("MgF+", None, ["Mg", "F"], 0.043303403000000004, 1.0, PhaseType.AQUEOUS)
    MgOH_plus = Species("MgOH+", None, ["Mg", "O", "H"], 0.04131234, 1.0, PhaseType.AQUEOUS)
    Mn_plus2 = Species("Mn+2", None, ["Mn"], 0.05493805, 2.0, PhaseType.AQUEOUS)
    Mn_plus3 = Species("Mn+3", None, ["Mn"], 0.05493805, 3.0, PhaseType.AQUEOUS)
    MnCl_plus = Species("MnCl+", None, ["Mn", "Cl"], 0.09039105, 1.0, PhaseType.AQUEOUS)
    MnOH_plus = Species("MnOH+", None, ["Mn", "O", "H"], 0.07194539, 1.0, PhaseType.AQUEOUS)
    MnO_aq = Species("MnO(aq)", None, ["Mn", "O"], 0.07093745, 0.0, PhaseType.AQUEOUS)
    HMnO2_minus = Species("HMnO2-", None, ["H", "Mn", "O"], 0.08794479, -1.0, PhaseType.AQUEOUS)
    MnO2_minus2 = Species("MnO2-2", None, ["Mn", "O"], 0.08693685000000001, -2.0, PhaseType.AQUEOUS)
    MnO4_minus = Species("MnO4-", None, ["Mn", "O"], 0.11893565, -1.0, PhaseType.AQUEOUS)
    MnO4_minus2 = Species("MnO4-2", None, ["Mn", "O"], 0.11893565, -2.0, PhaseType.AQUEOUS)
    MnSO4_aq = Species("MnSO4(aq)", None, ["Mn", "S", "O"], 0.15100065000000001, 0.0, PhaseType.AQUEOUS)
    HMoO4_minus = Species("HMoO4-", None, ["H", "Mo", "O"], 0.16094554, -1.0, PhaseType.AQUEOUS)
    MoO4_minus2 = Species("MoO4-2", None, ["Mo", "O"], 0.1599376, -2.0, PhaseType.AQUEOUS)
    N2_aq = Species("N2(aq)", None, ["N"], 0.0280134, 0.0, PhaseType.AQUEOUS)
    NH3_aq = Species("NH3(aq)", None, ["N", "H"], 0.01703052, 0.0, PhaseType.AQUEOUS)
    NH4_plus = Species("NH4+", None, ["N", "H"], 0.01803846, 1.0, PhaseType.AQUEOUS)
    NO2_minus = Species("NO2-", None, ["N", "O"], 0.046005500000000005, -1.0, PhaseType.AQUEOUS)
    NO3_minus = Species("NO3-", None, ["N", "O"], 0.0620049, -1.0, PhaseType.AQUEOUS)
    Na_plus = Species("Na+", None, ["Na"], 0.02298977, 1.0, PhaseType.AQUEOUS)
    NaAl_OH_4_aq = Species("NaAl(OH)4(aq)", None, ["Na", "Al", "O", "H"], 0.118000668, 0.0, PhaseType.AQUEOUS)
    NaBr_aq = Species("NaBr(aq)", None, ["Na", "Br"], 0.10289377, 0.0, PhaseType.AQUEOUS)
    NaCl_aq = Species("NaCl(aq)", None, ["Na", "Cl"], 0.05844277, 0.0, PhaseType.AQUEOUS)
    NaF_aq = Species("NaF(aq)", None, ["Na", "F"], 0.041988173000000004, 0.0, PhaseType.AQUEOUS)
    NaHSiO3_aq = Species("NaHSiO3(aq)", None, ["Na", "H", "Si", "O"], 0.10008141000000001, 0.0, PhaseType.AQUEOUS)
    NaI_aq = Species("NaI(aq)", None, ["Na", "I"], 0.14989423999999998, 0.0, PhaseType.AQUEOUS)
    NaOH_aq = Species("NaOH(aq)", None, ["Na", "O", "H"], 0.03999711, 0.0, PhaseType.AQUEOUS)
    Nd_plus2 = Species("Nd+2", None, ["Nd"], 0.14424, 2.0, PhaseType.AQUEOUS)
    Nd_plus3 = Species("Nd+3", None, ["Nd"], 0.14424, 3.0, PhaseType.AQUEOUS)
    Nd_plus4 = Species("Nd+4", None, ["Nd"], 0.14424, 4.0, PhaseType.AQUEOUS)
    Ne_aq = Species("Ne(aq)", None, ["Ne"], 0.0201797, 0.0, PhaseType.AQUEOUS)
    Ni_plus2 = Species("Ni+2", None, ["Ni"], 0.0586934, 2.0, PhaseType.AQUEOUS)
    NiCl_plus = Species("NiCl+", None, ["Ni", "Cl"], 0.09414639999999999, 1.0, PhaseType.AQUEOUS)
    NiOH_plus = Species("NiOH+", None, ["Ni", "O", "H"], 0.07570074, 1.0, PhaseType.AQUEOUS)
    NiO_aq = Species("NiO(aq)", None, ["Ni", "O"], 0.0746928, 0.0, PhaseType.AQUEOUS)
    HNiO2_minus = Species("HNiO2-", None, ["H", "Ni", "O"], 0.09170014, -1.0, PhaseType.AQUEOUS)
    NiO2_minus2 = Species("NiO2-2", None, ["Ni", "O"], 0.0906922, -2.0, PhaseType.AQUEOUS)
    O2_aq = Species("O2(aq)", None, ["O"], 0.0319988, 0.0, PhaseType.AQUEOUS)
    OH_minus = Species("OH-", None, ["O", "H"], 0.01700734, -1.0, PhaseType.AQUEOUS)
    PO4_minus3 = Species("PO4-3", None, ["P", "O"], 0.094971361, -3.0, PhaseType.AQUEOUS)
    Pb_plus2 = Species("Pb+2", None, ["Pb"], 0.2072, 2.0, PhaseType.AQUEOUS)
    PbCl_plus = Species("PbCl+", None, ["Pb", "Cl"], 0.242653, 1.0, PhaseType.AQUEOUS)
    PbCl2_aq = Species("PbCl2(aq)", None, ["Pb", "Cl"], 0.27810599999999996, 0.0, PhaseType.AQUEOUS)
    PbCl3_minus = Species("PbCl3-", None, ["Pb", "Cl"], 0.313559, -1.0, PhaseType.AQUEOUS)
    PbCl4_minus2 = Species("PbCl4-2", None, ["Pb", "Cl"], 0.349012, -2.0, PhaseType.AQUEOUS)
    PbOH_plus = Species("PbOH+", None, ["Pb", "O", "H"], 0.22420734, 1.0, PhaseType.AQUEOUS)
    PbO_aq = Species("PbO(aq)", None, ["Pb", "O"], 0.2231994, 0.0, PhaseType.AQUEOUS)
    HPbO2_minus = Species("HPbO2-", None, ["H", "Pb", "O"], 0.24020674, -1.0, PhaseType.AQUEOUS)
    Pd_OH_plus = Species("Pd(OH)+", None, ["Pd", "O", "H"], 0.12342734, 1.0, PhaseType.AQUEOUS)
    PdSO4_aq = Species("PdSO4(aq)", None, ["Pd", "S", "O"], 0.2024826, 0.0, PhaseType.AQUEOUS)
    Pd_SO4_2_minus2 = Species("Pd(SO4)2-2", None, ["Pd", "S", "O"], 0.2985452, -2.0, PhaseType.AQUEOUS)
    Pd_SO4_3_minus4 = Species("Pd(SO4)3-4", None, ["Pd", "S", "O"], 0.3946078, -4.0, PhaseType.AQUEOUS)
    Pd_plus2 = Species("Pd+2", None, ["Pd"], 0.10642, 2.0, PhaseType.AQUEOUS)
    PdCl_plus = Species("PdCl+", None, ["Pd", "Cl"], 0.141873, 1.0, PhaseType.AQUEOUS)
    PdCl2_aq = Species("PdCl2(aq)", None, ["Pd", "Cl"], 0.17732599999999998, 0.0, PhaseType.AQUEOUS)
    PdCl3_minus = Species("PdCl3-", None, ["Pd", "Cl"], 0.212779, -1.0, PhaseType.AQUEOUS)
    PdCl4_minus2 = Species("PdCl4-2", None, ["Pd", "Cl"], 0.248232, -2.0, PhaseType.AQUEOUS)
    PdO_aq = Species("PdO(aq)", None, ["Pd", "O"], 0.1224194, 0.0, PhaseType.AQUEOUS)
    Pr_plus2 = Species("Pr+2", None, ["Pr"], 0.14090765, 2.0, PhaseType.AQUEOUS)
    Pr_plus3 = Species("Pr+3", None, ["Pr"], 0.14090765, 3.0, PhaseType.AQUEOUS)
    Pr_plus4 = Species("Pr+4", None, ["Pr"], 0.14090765, 4.0, PhaseType.AQUEOUS)
    Pt_OH_plus = Species("Pt(OH)+", None, ["Pt", "O", "H"], 0.21208534, 1.0, PhaseType.AQUEOUS)
    PtSO4_aq = Species("PtSO4(aq)", None, ["Pt", "S", "O"], 0.2911406, 0.0, PhaseType.AQUEOUS)
    Pt_SO4_2_minus2 = Species("Pt(SO4)2-2", None, ["Pt", "S", "O"], 0.38720319999999997, -2.0, PhaseType.AQUEOUS)
    Pt_SO4_3_minus4 = Species("Pt(SO4)3-4", None, ["Pt", "S", "O"], 0.4832658, -4.0, PhaseType.AQUEOUS)
    Pt_plus2 = Species("Pt+2", None, ["Pt"], 0.195078, 2.0, PhaseType.AQUEOUS)
    PtCl_plus = Species("PtCl+", None, ["Pt", "Cl"], 0.23053099999999999, 1.0, PhaseType.AQUEOUS)
    PtCl2_aq = Species("PtCl2(aq)", None, ["Pt", "Cl"], 0.265984, 0.0, PhaseType.AQUEOUS)
    PtCl3_minus = Species("PtCl3-", None, ["Pt", "Cl"], 0.301437, -1.0, PhaseType.AQUEOUS)
    PtCl4_minus2 = Species("PtCl4-2", None, ["Pt", "Cl"], 0.33689, -2.0, PhaseType.AQUEOUS)
    PtO_aq = Species("PtO(aq)", None, ["Pt", "O"], 0.2110774, 0.0, PhaseType.AQUEOUS)
    Ra_plus2 = Species("Ra+2", None, ["Ra"], 0.226, 2.0, PhaseType.AQUEOUS)
    Rb_plus = Species("Rb+", None, ["Rb"], 0.0854678, 1.0, PhaseType.AQUEOUS)
    RbBr_aq = Species("RbBr(aq)", None, ["Rb", "Br"], 0.1653718, 0.0, PhaseType.AQUEOUS)
    RbCl_aq = Species("RbCl(aq)", None, ["Rb", "Cl"], 0.1209208, 0.0, PhaseType.AQUEOUS)
    RbF_aq = Species("RbF(aq)", None, ["Rb", "F"], 0.104466203, 0.0, PhaseType.AQUEOUS)
    RbI_aq = Species("RbI(aq)", None, ["Rb", "I"], 0.21237226999999997, 0.0, PhaseType.AQUEOUS)
    RbOH_aq = Species("RbOH(aq)", None, ["Rb", "O", "H"], 0.10247513999999999, 0.0, PhaseType.AQUEOUS)
    ReO4_minus = Species("ReO4-", None, ["Re", "O"], 0.2502046, -1.0, PhaseType.AQUEOUS)
    Rh_OH_plus = Species("Rh(OH)+", None, ["Rh", "O", "H"], 0.11991283999999999, 1.0, PhaseType.AQUEOUS)
    Rh_OH_plus2 = Species("Rh(OH)+2", None, ["Rh", "O", "H"], 0.11991283999999999, 2.0, PhaseType.AQUEOUS)
    RhSO4_aq = Species("RhSO4(aq)", None, ["Rh", "S", "O"], 0.19896809999999998, 0.0, PhaseType.AQUEOUS)
    Rh_SO4_plus = Species("Rh(SO4)+", None, ["Rh", "S", "O"], 0.19896809999999998, 1.0, PhaseType.AQUEOUS)
    Rh_SO4_2_minus = Species("Rh(SO4)2-", None, ["Rh", "S", "O"], 0.2950307, -1.0, PhaseType.AQUEOUS)
    Rh_SO4_2_minus2 = Species("Rh(SO4)2-2", None, ["Rh", "S", "O"], 0.2950307, -2.0, PhaseType.AQUEOUS)
    Rh_SO4_3_minus3 = Species("Rh(SO4)3-3", None, ["Rh", "S", "O"], 0.39109330000000003, -3.0, PhaseType.AQUEOUS)
    Rh_SO4_3_minus4 = Species("Rh(SO4)3-4", None, ["Rh", "S", "O"], 0.39109330000000003, -4.0, PhaseType.AQUEOUS)
    Rh_plus2 = Species("Rh+2", None, ["Rh"], 0.1029055, 2.0, PhaseType.AQUEOUS)
    Rh_plus3 = Species("Rh+3", None, ["Rh"], 0.1029055, 3.0, PhaseType.AQUEOUS)
    RhCl_plus = Species("RhCl+", None, ["Rh", "Cl"], 0.1383585, 1.0, PhaseType.AQUEOUS)
    RhCl_plus2 = Species("RhCl+2", None, ["Rh", "Cl"], 0.1383585, 2.0, PhaseType.AQUEOUS)
    RhCl2_aq = Species("RhCl2(aq)", None, ["Rh", "Cl"], 0.1738115, 0.0, PhaseType.AQUEOUS)
    RhCl2_plus = Species("RhCl2+", None, ["Rh", "Cl"], 0.1738115, 1.0, PhaseType.AQUEOUS)
    RhCl3_aq = Species("RhCl3(aq)", None, ["Rh", "Cl"], 0.2092645, 0.0, PhaseType.AQUEOUS)
    RhCl3_minus = Species("RhCl3-", None, ["Rh", "Cl"], 0.2092645, -1.0, PhaseType.AQUEOUS)
    RhCl4_minus = Species("RhCl4-", None, ["Rh", "Cl"], 0.24471749999999998, -1.0, PhaseType.AQUEOUS)
    RhCl4_minus2 = Species("RhCl4-2", None, ["Rh", "Cl"], 0.24471749999999998, -2.0, PhaseType.AQUEOUS)
    RhO_aq = Species("RhO(aq)", None, ["Rh", "O"], 0.1189049, 0.0, PhaseType.AQUEOUS)
    RhO_plus = Species("RhO+", None, ["Rh", "O"], 0.1189049, 1.0, PhaseType.AQUEOUS)
    Rn_aq = Species("Rn(aq)", None, ["Rn"], 0.222, 0.0, PhaseType.AQUEOUS)
    Ru_OH_plus = Species("Ru(OH)+", None, ["Ru", "O", "H"], 0.11807733999999999, 1.0, PhaseType.AQUEOUS)
    Ru_OH_plus2 = Species("Ru(OH)+2", None, ["Ru", "O", "H"], 0.11807733999999999, 2.0, PhaseType.AQUEOUS)
    RuO4_minus2 = Species("RuO4-2", None, ["Ru", "O"], 0.16506759999999998, -2.0, PhaseType.AQUEOUS)
    RuSO4_aq = Species("RuSO4(aq)", None, ["Ru", "S", "O"], 0.1971326, 0.0, PhaseType.AQUEOUS)
    Ru_SO4_plus = Species("Ru(SO4)+", None, ["Ru", "S", "O"], 0.1971326, 1.0, PhaseType.AQUEOUS)
    Ru_SO4_2_minus = Species("Ru(SO4)2-", None, ["Ru", "S", "O"], 0.2931952, -1.0, PhaseType.AQUEOUS)
    Ru_SO4_2_minus2 = Species("Ru(SO4)2-2", None, ["Ru", "S", "O"], 0.2931952, -2.0, PhaseType.AQUEOUS)
    Ru_SO4_3_minus3 = Species("Ru(SO4)3-3", None, ["Ru", "S", "O"], 0.3892578, -3.0, PhaseType.AQUEOUS)
    Ru_SO4_3_minus4 = Species("Ru(SO4)3-4", None, ["Ru", "S", "O"], 0.3892578, -4.0, PhaseType.AQUEOUS)
    Ru_plus2 = Species("Ru+2", None, ["Ru"], 0.10107, 2.0, PhaseType.AQUEOUS)
    Ru_plus3 = Species("Ru+3", None, ["Ru"], 0.10107, 3.0, PhaseType.AQUEOUS)
    RuCl_plus = Species("RuCl+", None, ["Ru", "Cl"], 0.136523, 1.0, PhaseType.AQUEOUS)
    RuCl_plus2 = Species("RuCl+2", None, ["Ru", "Cl"], 0.136523, 2.0, PhaseType.AQUEOUS)
    RuCl2_aq = Species("RuCl2(aq)", None, ["Ru", "Cl"], 0.171976, 0.0, PhaseType.AQUEOUS)
    RuCl2_plus = Species("RuCl2+", None, ["Ru", "Cl"], 0.171976, 1.0, PhaseType.AQUEOUS)
    RuCl3_aq = Species("RuCl3(aq)", None, ["Ru", "Cl"], 0.20742899999999997, 0.0, PhaseType.AQUEOUS)
    RuCl3_minus = Species("RuCl3-", None, ["Ru", "Cl"], 0.20742899999999997, -1.0, PhaseType.AQUEOUS)
    RuCl4_minus = Species("RuCl4-", None, ["Ru", "Cl"], 0.242882, -1.0, PhaseType.AQUEOUS)
    RuCl4_minus2 = Species("RuCl4-2", None, ["Ru", "Cl"], 0.242882, -2.0, PhaseType.AQUEOUS)
    RuCl5_minus2 = Species("RuCl5-2", None, ["Ru", "Cl"], 0.278335, -2.0, PhaseType.AQUEOUS)
    RuCl6_minus3 = Species("RuCl6-3", None, ["Ru", "Cl"], 0.31378799999999996, -3.0, PhaseType.AQUEOUS)
    RuO_aq = Species("RuO(aq)", None, ["Ru", "O"], 0.11706939999999999, 0.0, PhaseType.AQUEOUS)
    RuO_plus = Species("RuO+", None, ["Ru", "O"], 0.11706939999999999, 1.0, PhaseType.AQUEOUS)
    S2_minus2 = Species("S2-2", None, ["S"], 0.06413, -2.0, PhaseType.AQUEOUS)
    S2O3_minus2 = Species("S2O3-2", None, ["S", "O"], 0.11212820000000001, -2.0, PhaseType.AQUEOUS)
    HS2O3_minus = Species("HS2O3-", None, ["H", "S", "O"], 0.11313614000000001, -1.0, PhaseType.AQUEOUS)
    H2S2O3_aq = Species("H2S2O3(aq)", None, ["H", "S", "O"], 0.11414408000000001, 0.0, PhaseType.AQUEOUS)
    S2O4_minus2 = Species("S2O4-2", None, ["S", "O"], 0.1281276, -2.0, PhaseType.AQUEOUS)
    HS2O4_minus = Species("HS2O4-", None, ["H", "S", "O"], 0.12913554, -1.0, PhaseType.AQUEOUS)
    H2S2O4_aq = Species("H2S2O4(aq)", None, ["H", "S", "O"], 0.13014348, 0.0, PhaseType.AQUEOUS)
    S2O5_minus2 = Species("S2O5-2", None, ["S", "O"], 0.144127, -2.0, PhaseType.AQUEOUS)
    S2O6_minus2 = Species("S2O6-2", None, ["S", "O"], 0.1601264, -2.0, PhaseType.AQUEOUS)
    S2O8_minus2 = Species("S2O8-2", None, ["S", "O"], 0.1921252, -2.0, PhaseType.AQUEOUS)
    S3_minus2 = Species("S3-2", None, ["S"], 0.096195, -2.0, PhaseType.AQUEOUS)
    S3O6_minus2 = Species("S3O6-2", None, ["S", "O"], 0.1921914, -2.0, PhaseType.AQUEOUS)
    S4_minus2 = Species("S4-2", None, ["S"], 0.12826, -2.0, PhaseType.AQUEOUS)
    S4O6_minus2 = Species("S4O6-2", None, ["S", "O"], 0.22425640000000002, -2.0, PhaseType.AQUEOUS)
    S5_minus2 = Species("S5-2", None, ["S"], 0.16032500000000002, -2.0, PhaseType.AQUEOUS)
    S5O6_minus2 = Species("S5O6-2", None, ["S", "O"], 0.25632140000000003, -2.0, PhaseType.AQUEOUS)
    SO2_aq = Species("SO2(aq)", None, ["S", "O"], 0.0640638, 0.0, PhaseType.AQUEOUS)
    SO3_minus2 = Species("SO3-2", None, ["S", "O"], 0.0800632, -2.0, PhaseType.AQUEOUS)
    SO4_minus2 = Species("SO4-2", None, ["S", "O"], 0.0960626, -2.0, PhaseType.AQUEOUS)
    Sc_plus3 = Species("Sc+3", None, ["Sc"], 0.04495591, 3.0, PhaseType.AQUEOUS)
    ScOH_plus2 = Species("ScOH+2", None, ["Sc", "O", "H"], 0.06196325, 2.0, PhaseType.AQUEOUS)
    ScO_plus = Species("ScO+", None, ["Sc", "O"], 0.06095531, 1.0, PhaseType.AQUEOUS)
    HScO2_aq = Species("HScO2(aq)", None, ["H", "Sc", "O"], 0.07796265, 0.0, PhaseType.AQUEOUS)
    ScO2_minus = Species("ScO2-", None, ["Sc", "O"], 0.07695471000000001, -1.0, PhaseType.AQUEOUS)
    SeO3_minus2 = Species("SeO3-2", None, ["Se", "O"], 0.12695820000000002, -2.0, PhaseType.AQUEOUS)
    SeO4_minus2 = Species("SeO4-2", None, ["Se", "O"], 0.14295760000000002, -2.0, PhaseType.AQUEOUS)
    SiF6_minus2 = Species("SiF6-2", None, ["Si", "F"], 0.14207591800000002, -2.0, PhaseType.AQUEOUS)
    SiO2_aq = Species("SiO2(aq)", None, ["Si", "O"], 0.0600843, 0.0, PhaseType.AQUEOUS)
    Sm_plus2 = Species("Sm+2", None, ["Sm"], 0.15036, 2.0, PhaseType.AQUEOUS)
    Sm_plus3 = Species("Sm+3", None, ["Sm"], 0.15036, 3.0, PhaseType.AQUEOUS)
    Sm_plus4 = Species("Sm+4", None, ["Sm"], 0.15036, 4.0, PhaseType.AQUEOUS)
    Sn_plus2 = Species("Sn+2", None, ["Sn"], 0.11871, 2.0, PhaseType.AQUEOUS)
    SnO_aq = Species("SnO(aq)", None, ["Sn", "O"], 0.1347094, 0.0, PhaseType.AQUEOUS)
    SnOH_plus = Species("SnOH+", None, ["Sn", "O", "H"], 0.13571734000000002, 1.0, PhaseType.AQUEOUS)
    HSnO2_minus = Species("HSnO2-", None, ["H", "Sn", "O"], 0.15171674, -1.0, PhaseType.AQUEOUS)
    Sr_HCO3_plus = Species("Sr(HCO3)+", None, ["Sr", "H", "C", "O"], 0.14863684, 1.0, PhaseType.AQUEOUS)
    Sr_plus2 = Species("Sr+2", None, ["Sr"], 0.08762, 2.0, PhaseType.AQUEOUS)
    SrCl_plus = Species("SrCl+", None, ["Sr", "Cl"], 0.123073, 1.0, PhaseType.AQUEOUS)
    SrF_plus = Species("SrF+", None, ["Sr", "F"], 0.106618403, 1.0, PhaseType.AQUEOUS)
    SrOH_plus = Species("SrOH+", None, ["Sr", "O", "H"], 0.10462734, 1.0, PhaseType.AQUEOUS)
    Tb_plus2 = Species("Tb+2", None, ["Tb"], 0.15892534, 2.0, PhaseType.AQUEOUS)
    Tb_plus3 = Species("Tb+3", None, ["Tb"], 0.15892534, 3.0, PhaseType.AQUEOUS)
    Tb_plus4 = Species("Tb+4", None, ["Tb"], 0.15892534, 4.0, PhaseType.AQUEOUS)
    Th_plus4 = Species("Th+4", None, ["Th"], 0.2320381, 4.0, PhaseType.AQUEOUS)
    Tl_plus = Species("Tl+", None, ["Tl"], 0.2043833, 1.0, PhaseType.AQUEOUS)
    Tl_plus3 = Species("Tl+3", None, ["Tl"], 0.2043833, 3.0, PhaseType.AQUEOUS)
    TlOH_aq = Species("TlOH(aq)", None, ["Tl", "O", "H"], 0.22139064, 0.0, PhaseType.AQUEOUS)
    TlOH_plus2 = Species("TlOH+2", None, ["Tl", "O", "H"], 0.22139064, 2.0, PhaseType.AQUEOUS)
    TlO_plus = Species("TlO+", None, ["Tl", "O"], 0.2203827, 1.0, PhaseType.AQUEOUS)
    HTlO2_aq = Species("HTlO2(aq)", None, ["H", "Tl", "O"], 0.23739004, 0.0, PhaseType.AQUEOUS)
    TlO2_minus = Species("TlO2-", None, ["Tl", "O"], 0.23638209999999998, -1.0, PhaseType.AQUEOUS)
    Tm_plus2 = Species("Tm+2", None, ["Tm"], 0.16893421, 2.0, PhaseType.AQUEOUS)
    Tm_plus3 = Species("Tm+3", None, ["Tm"], 0.16893421, 3.0, PhaseType.AQUEOUS)
    Tm_plus4 = Species("Tm+4", None, ["Tm"], 0.16893421, 4.0, PhaseType.AQUEOUS)
    U_plus3 = Species("U+3", None, ["U"], 0.23802891, 3.0, PhaseType.AQUEOUS)
    U_plus4 = Species("U+4", None, ["U"], 0.23802891, 4.0, PhaseType.AQUEOUS)
    UO2_plus = Species("UO2+", None, ["U", "O"], 0.27002771000000003, 1.0, PhaseType.AQUEOUS)
    UO2_plus2 = Species("UO2+2", None, ["U", "O"], 0.27002771000000003, 2.0, PhaseType.AQUEOUS)
    VO_plus = Species("VO+", None, ["V", "O"], 0.0669409, 1.0, PhaseType.AQUEOUS)
    VO_plus2 = Species("VO+2", None, ["V", "O"], 0.0669409, 2.0, PhaseType.AQUEOUS)
    VOH_plus = Species("VOH+", None, ["V", "O", "H"], 0.06794884, 1.0, PhaseType.AQUEOUS)
    VOH_plus2 = Species("VOH+2", None, ["V", "O", "H"], 0.06794884, 2.0, PhaseType.AQUEOUS)
    VO2_plus = Species("VO2+", None, ["V", "O"], 0.0829403, 1.0, PhaseType.AQUEOUS)
    Vooh_plus = Species("Vooh+", None, ["V", "O", "H"], 0.08394824, 1.0, PhaseType.AQUEOUS)
    WO4_minus2 = Species("WO4-2", None, ["W", "O"], 0.2478376, -2.0, PhaseType.AQUEOUS)
    HWO4_minus = Species("HWO4-", None, ["H", "W", "O"], 0.24884554000000003, -1.0, PhaseType.AQUEOUS)
    Xe_aq = Species("Xe(aq)", None, ["Xe"], 0.131293, 0.0, PhaseType.AQUEOUS)
    Y_plus3 = Species("Y+3", None, ["Y"], 0.08890585, 3.0, PhaseType.AQUEOUS)
    YOH_plus2 = Species("YOH+2", None, ["Y", "O", "H"], 0.10591318999999999, 2.0, PhaseType.AQUEOUS)
    YO_plus = Species("YO+", None, ["Y", "O"], 0.10490524999999999, 1.0, PhaseType.AQUEOUS)
    HYO2_aq = Species("HYO2(aq)", None, ["H", "Y", "O"], 0.12191258999999999, 0.0, PhaseType.AQUEOUS)
    YO2_minus = Species("YO2-", None, ["Y", "O"], 0.12090465, -1.0, PhaseType.AQUEOUS)
    Yb_plus2 = Species("Yb+2", None, ["Yb"], 0.17304, 2.0, PhaseType.AQUEOUS)
    Yb_plus3 = Species("Yb+3", None, ["Yb"], 0.17304, 3.0, PhaseType.AQUEOUS)
    Yb_plus4 = Species("Yb+4", None, ["Yb"], 0.17304, 4.0, PhaseType.AQUEOUS)
    Zn_plus2 = Species("Zn+2", None, ["Zn"], 0.065409, 2.0, PhaseType.AQUEOUS)
    ZnCl_plus = Species("ZnCl+", None, ["Zn", "Cl"], 0.100862, 1.0, PhaseType.AQUEOUS)
    ZnCl2_aq = Species("ZnCl2(aq)", None, ["Zn", "Cl"], 0.136315, 0.0, PhaseType.AQUEOUS)
    ZnCl3_minus = Species("ZnCl3-", None, ["Zn", "Cl"], 0.17176799999999998, -1.0, PhaseType.AQUEOUS)
    ZnOH_plus = Species("ZnOH+", None, ["Zn", "O", "H"], 0.08241633999999999, 1.0, PhaseType.AQUEOUS)
    ZnO_aq = Species("ZnO(aq)", None, ["Zn", "O"], 0.08140839999999999, 0.0, PhaseType.AQUEOUS)
    HZnO2_minus = Species("HZnO2-", None, ["H", "Zn", "O"], 0.09841574, -1.0, PhaseType.AQUEOUS)
    ZnO2_minus2 = Species("ZnO2-2", None, ["Zn", "O"], 0.09740779999999999, -2.0, PhaseType.AQUEOUS)
    U_OH_plus2 = Species("U(OH)+2", None, ["U", "O", "H"], 0.25503625, 2.0, PhaseType.AQUEOUS)
    UO_plus = Species("UO+", None, ["U", "O"], 0.25402831000000003, 1.0, PhaseType.AQUEOUS)
    HUO2_aq = Species("HUO2(aq)", None, ["U", "O", "H"], 0.27103565, 0.0, PhaseType.AQUEOUS)
    U_OH_plus3 = Species("U(OH)+3", None, ["U", "O", "H"], 0.25503625, 3.0, PhaseType.AQUEOUS)
    UO_plus2 = Species("UO+2", None, ["U", "O"], 0.25402831000000003, 2.0, PhaseType.AQUEOUS)
    HUO2_plus = Species("HUO2+", None, ["U", "O", "H"], 0.27103565, 1.0, PhaseType.AQUEOUS)
    UO2_aq = Species("UO2(aq)", None, ["U", "O"], 0.27002771000000003, 0.0, PhaseType.AQUEOUS)
    HUO3_minus = Species("HUO3-", None, ["U", "O", "H"], 0.28703505, -1.0, PhaseType.AQUEOUS)
    UO2OH_aq = Species("UO2OH(aq)", None, ["U", "O", "H"], 0.28703505, 0.0, PhaseType.AQUEOUS)
    UO3_minus = Species("UO3-", None, ["U", "O"], 0.28602711000000003, -1.0, PhaseType.AQUEOUS)
    UO2OH_plus = Species("UO2OH+", None, ["U", "O", "H"], 0.28703505, 1.0, PhaseType.AQUEOUS)
    UO3_aq = Species("UO3(aq)", None, ["U", "O"], 0.28602711000000003, 0.0, PhaseType.AQUEOUS)
    HUO4_minus = Species("HUO4-", None, ["U", "O", "H"], 0.30303445, -1.0, PhaseType.AQUEOUS)
    UO4_minus2 = Species("UO4-2", None, ["U", "O"], 0.30202651, -2.0, PhaseType.AQUEOUS)
    Fr_plus = Species("Fr+", None, ["Fr"], 0.223, 1.0, PhaseType.AQUEOUS)
    HNO2_aq = Species("HNO2(aq)", None, ["H", "N", "O"], 0.047013440000000004, 0.0, PhaseType.AQUEOUS)
    H2N2O2_aq = Species("H2N2O2(aq)", None, ["H", "N", "O"], 0.06202808, 0.0, PhaseType.AQUEOUS)
    HN2O2_minus = Species("HN2O2-", None, ["H", "N", "O"], 0.06102014, -1.0, PhaseType.AQUEOUS)
    N2O2_minus2 = Species("N2O2-2", None, ["N", "O"], 0.0600122, -2.0, PhaseType.AQUEOUS)
    N2H5_plus = Species("N2H5+", None, ["N", "H"], 0.0330531, 1.0, PhaseType.AQUEOUS)
    N2H6_plus2 = Species("N2H6+2", None, ["N", "H"], 0.03406104, 2.0, PhaseType.AQUEOUS)
    H3PO2_aq = Species("H3PO2(aq)", None, ["H", "P", "O"], 0.06599638099999999, 0.0, PhaseType.AQUEOUS)
    H2PO2_minus = Species("H2PO2-", None, ["H", "P", "O"], 0.06498844100000001, -1.0, PhaseType.AQUEOUS)
    H3PO3_aq = Species("H3PO3(aq)", None, ["H", "P", "O"], 0.081995781, 0.0, PhaseType.AQUEOUS)
    H2PO3_minus = Species("H2PO3-", None, ["H", "P", "O"], 0.080987841, -1.0, PhaseType.AQUEOUS)
    HPO3_minus2 = Species("HPO3-2", None, ["H", "P", "O"], 0.079979901, -2.0, PhaseType.AQUEOUS)
    P2O7_minus4 = Species("P2O7-4", None, ["P", "O"], 0.173943322, -4.0, PhaseType.AQUEOUS)
    HP2O7_minus3 = Species("HP2O7-3", None, ["H", "P", "O"], 0.174951262, -3.0, PhaseType.AQUEOUS)
    H4P2O7_aq = Species("H4P2O7(aq)", None, ["H", "P", "O"], 0.177975082, 0.0, PhaseType.AQUEOUS)
    AsO4_minus3 = Species("AsO4-3", None, ["As", "O"], 0.13891920000000002, -3.0, PhaseType.AQUEOUS)
    H3AsO4_aq = Species("H3AsO4(aq)", None, ["H", "As", "O"], 0.14194302, 0.0, PhaseType.AQUEOUS)
    H2AsO4_minus = Species("H2AsO4-", None, ["H", "As", "O"], 0.14093508, -1.0, PhaseType.AQUEOUS)
    HAsO4_minus2 = Species("HAsO4-2", None, ["H", "As", "O"], 0.13992714, -2.0, PhaseType.AQUEOUS)
    HAsO2_aq = Species("HAsO2(aq)", None, ["H", "As", "O"], 0.10792834000000001, 0.0, PhaseType.AQUEOUS)
    H2AsO3_minus = Species("H2AsO3-", None, ["H", "As", "O"], 0.12493568000000001, -1.0, PhaseType.AQUEOUS)
    HAsO3_minus2 = Species("HAsO3-2", None, ["H", "As", "O"], 0.12392774000000001, -2.0, PhaseType.AQUEOUS)
    AsO3_minus3 = Species("AsO3-3", None, ["As", "O"], 0.12291980000000001, -3.0, PhaseType.AQUEOUS)
    As3S4_HS_2_minus = Species("As3S4(HS)2-", None, ["As", "S", "H"], 0.4191706800000001, -1.0, PhaseType.AQUEOUS)
    HSbO2_aq = Species("HSbO2(aq)", None, ["H", "Sb", "O"], 0.15476673999999999, 0.0, PhaseType.AQUEOUS)
    SbO2_minus = Species("SbO2-", None, ["Sb", "O"], 0.1537588, -1.0, PhaseType.AQUEOUS)
    Bi_plus3 = Species("Bi+3", None, ["Bi"], 0.20898038, 3.0, PhaseType.AQUEOUS)
    BiO_plus = Species("BiO+", None, ["Bi", "O"], 0.22497978, 1.0, PhaseType.AQUEOUS)
    BiOH_plus2 = Species("BiOH+2", None, ["Bi", "O", "H"], 0.22598772, 2.0, PhaseType.AQUEOUS)
    HBiO2_aq = Species("HBiO2(aq)", None, ["H", "Bi", "O"], 0.24198712, 0.0, PhaseType.AQUEOUS)
    BiO2_minus = Species("BiO2-", None, ["Bi", "O"], 0.24097918, -1.0, PhaseType.AQUEOUS)
    H2O2_aq = Species("H2O2(aq)", None, ["H", "O"], 0.03401468, 0.0, PhaseType.AQUEOUS)
    HClO2_aq = Species("HClO2(aq)", None, ["H", "Cl", "O"], 0.06845973999999999, 0.0, PhaseType.AQUEOUS)
    HIO3_aq = Species("HIO3(aq)", None, ["H", "I", "O"], 0.17591061000000002, 0.0, PhaseType.AQUEOUS)
    V_plus2 = Species("V+2", None, ["V"], 0.0509415, 2.0, PhaseType.AQUEOUS)
    V_plus3 = Species("V+3", None, ["V"], 0.0509415, 3.0, PhaseType.AQUEOUS)
    VO4_minus3 = Species("VO4-3", None, ["V", "O"], 0.1149391, -3.0, PhaseType.AQUEOUS)
    Cr_plus2 = Species("Cr+2", None, ["Cr"], 0.0519961, 2.0, PhaseType.AQUEOUS)
    Cr_plus3 = Species("Cr+3", None, ["Cr"], 0.0519961, 3.0, PhaseType.AQUEOUS)
    CrOH_plus2 = Species("CrOH+2", None, ["Cr", "O", "H"], 0.06900344, 2.0, PhaseType.AQUEOUS)
    CrO_plus = Species("CrO+", None, ["Cr", "O"], 0.0679955, 1.0, PhaseType.AQUEOUS)
    HCrO2_aq = Species("HCrO2(aq)", None, ["H", "Cr", "O"], 0.08500284, 0.0, PhaseType.AQUEOUS)
    CrO2_minus = Species("CrO2-", None, ["Cr", "O"], 0.08399490000000001, -1.0, PhaseType.AQUEOUS)
    Zr_plus4 = Species("Zr+4", None, ["Zr"], 0.091224, 4.0, PhaseType.AQUEOUS)
    Zr_OH_plus3 = Species("Zr(OH)+3", None, ["Zr", "O", "H"], 0.10823134, 3.0, PhaseType.AQUEOUS)
    ZrO_plus2 = Species("ZrO+2", None, ["Zr", "O"], 0.1072234, 2.0, PhaseType.AQUEOUS)
    HZrO2_plus = Species("HZrO2+", None, ["Zr", "O", "H"], 0.12423073999999999, 1.0, PhaseType.AQUEOUS)
    ZrO2_aq = Species("ZrO2(aq)", None, ["Zr", "O"], 0.1232228, 0.0, PhaseType.AQUEOUS)
    HZrO3_minus = Species("HZrO3-", None, ["Zr", "O", "H"], 0.14023014000000003, -1.0, PhaseType.AQUEOUS)
    HNbO3_aq = Species("HNbO3(aq)", None, ["H", "Nb", "O"], 0.14191252, 0.0, PhaseType.AQUEOUS)
    NbO3_minus = Species("NbO3-", None, ["Nb", "O"], 0.14090458, -1.0, PhaseType.AQUEOUS)
    TcO4_minus = Species("TcO4-", None, ["Tc", "O"], 0.16199760000000002, -1.0, PhaseType.AQUEOUS)
    Pm_plus2 = Species("Pm+2", None, ["Pm"], 0.145, 2.0, PhaseType.AQUEOUS)
    Pm_plus3 = Species("Pm+3", None, ["Pm"], 0.145, 3.0, PhaseType.AQUEOUS)
    Pm_plus4 = Species("Pm+4", None, ["Pm"], 0.145, 4.0, PhaseType.AQUEOUS)
    Hf_plus4 = Species("Hf+4", None, ["Hf"], 0.17849, 4.0, PhaseType.AQUEOUS)
    HfOH_plus3 = Species("HfOH+3", None, ["Hf", "O", "H"], 0.19549734000000002, 3.0, PhaseType.AQUEOUS)
    HfO_plus2 = Species("HfO+2", None, ["Hf", "O"], 0.1944894, 2.0, PhaseType.AQUEOUS)
    HHfO2_plus = Species("HHfO2+", None, ["H", "Hf", "O"], 0.21149674000000002, 1.0, PhaseType.AQUEOUS)
    HfO2_aq = Species("HfO2(aq)", None, ["Hf", "O"], 0.2104888, 0.0, PhaseType.AQUEOUS)
    HHfO3_minus = Species("HHfO3-", None, ["H", "Hf", "O"], 0.22749614, -1.0, PhaseType.AQUEOUS)
    La_plus2 = Species("La+2", None, ["La"], 0.1389055, 2.0, PhaseType.AQUEOUS)
    LaCO3_plus = Species("LaCO3+", None, ["La", "C", "O"], 0.1989144, 1.0, PhaseType.AQUEOUS)
    LaHCO3_plus2 = Species("LaHCO3+2", None, ["La", "H", "C", "O"], 0.19992233999999998, 2.0, PhaseType.AQUEOUS)
    LaOH_plus2 = Species("LaOH+2", None, ["La", "O", "H"], 0.15591284, 2.0, PhaseType.AQUEOUS)
    LaO_plus = Species("LaO+", None, ["La", "O"], 0.15490489999999998, 1.0, PhaseType.AQUEOUS)
    LaO2H_aq = Species("LaO2H(aq)", None, ["La", "O", "H"], 0.17191224, 0.0, PhaseType.AQUEOUS)
    LaO2_minus = Species("LaO2-", None, ["La", "O"], 0.17090429999999998, -1.0, PhaseType.AQUEOUS)
    LaCl_plus2 = Species("LaCl+2", None, ["La", "Cl"], 0.17435849999999997, 2.0, PhaseType.AQUEOUS)
    LaCl2_plus = Species("LaCl2+", None, ["La", "Cl"], 0.20981149999999998, 1.0, PhaseType.AQUEOUS)
    LaCl3_aq = Species("LaCl3(aq)", None, ["La", "Cl"], 0.2452645, 0.0, PhaseType.AQUEOUS)
    LaCl4_minus = Species("LaCl4-", None, ["La", "Cl"], 0.28071749999999995, -1.0, PhaseType.AQUEOUS)
    LaNO3_plus2 = Species("LaNO3+2", None, ["La", "N", "O"], 0.2009104, 2.0, PhaseType.AQUEOUS)
    LaF_plus2 = Species("LaF+2", None, ["La", "F"], 0.15790390299999998, 2.0, PhaseType.AQUEOUS)
    LaF2_plus = Species("LaF2+", None, ["La", "F"], 0.17690230599999998, 1.0, PhaseType.AQUEOUS)
    LaF3_aq = Species("LaF3(aq)", None, ["La", "F"], 0.195900709, 0.0, PhaseType.AQUEOUS)
    LaF4_minus = Species("LaF4-", None, ["La", "F"], 0.214899112, -1.0, PhaseType.AQUEOUS)
    LaH2PO4_plus2 = Species("LaH2PO4+2", None, ["La", "H", "P", "O"], 0.23589274099999996, 2.0, PhaseType.AQUEOUS)
    LaSO4_plus = Species("LaSO4+", None, ["La", "S", "O"], 0.2349681, 1.0, PhaseType.AQUEOUS)
    CeCO3_plus = Species("CeCO3+", None, ["Ce", "C", "O"], 0.2001249, 1.0, PhaseType.AQUEOUS)
    CeHCO3_plus2 = Species("CeHCO3+2", None, ["Ce", "H", "C", "O"], 0.20113283999999998, 2.0, PhaseType.AQUEOUS)
    CeOH_plus2 = Species("CeOH+2", None, ["Ce", "O", "H"], 0.15712334, 2.0, PhaseType.AQUEOUS)
    CeO_plus = Species("CeO+", None, ["Ce", "O"], 0.1561154, 1.0, PhaseType.AQUEOUS)
    CeO2H_aq = Species("CeO2H(aq)", None, ["Ce", "O", "H"], 0.17312274, 0.0, PhaseType.AQUEOUS)
    CeO2_minus = Species("CeO2-", None, ["Ce", "O"], 0.17211479999999998, -1.0, PhaseType.AQUEOUS)
    CeCl_plus2 = Species("CeCl+2", None, ["Ce", "Cl"], 0.17556899999999998, 2.0, PhaseType.AQUEOUS)
    CeCl2_plus = Species("CeCl2+", None, ["Ce", "Cl"], 0.211022, 1.0, PhaseType.AQUEOUS)
    CeCl3_aq = Species("CeCl3(aq)", None, ["Ce", "Cl"], 0.246475, 0.0, PhaseType.AQUEOUS)
    CeCl4_minus = Species("CeCl4-", None, ["Ce", "Cl"], 0.28192799999999996, -1.0, PhaseType.AQUEOUS)
    CeH2PO4_plus2 = Species("CeH2PO4+2", None, ["Ce", "H", "P", "O"], 0.23710324099999996, 2.0, PhaseType.AQUEOUS)
    CeNO3_plus2 = Species("CeNO3+2", None, ["Ce", "N", "O"], 0.2021209, 2.0, PhaseType.AQUEOUS)
    CeF_plus2 = Species("CeF+2", None, ["Ce", "F"], 0.159114403, 2.0, PhaseType.AQUEOUS)
    CeF2_plus = Species("CeF2+", None, ["Ce", "F"], 0.17811280599999998, 1.0, PhaseType.AQUEOUS)
    CeF3_aq = Species("CeF3(aq)", None, ["Ce", "F"], 0.197111209, 0.0, PhaseType.AQUEOUS)
    CeF4_minus = Species("CeF4-", None, ["Ce", "F"], 0.216109612, -1.0, PhaseType.AQUEOUS)
    CeBr_plus2 = Species("CeBr+2", None, ["Ce", "Br"], 0.22002, 2.0, PhaseType.AQUEOUS)
    CeIO3_plus2 = Species("CeIO3+2", None, ["Ce", "I", "O"], 0.31501866999999995, 2.0, PhaseType.AQUEOUS)
    CeClO4_plus2 = Species("CeClO4+2", None, ["Ce", "Cl", "O"], 0.23956659999999996, 2.0, PhaseType.AQUEOUS)
    CeSO4_plus = Species("CeSO4+", None, ["Ce", "S", "O"], 0.23617860000000002, 1.0, PhaseType.AQUEOUS)
    PrCO3_plus = Species("PrCO3+", None, ["Pr", "C", "O"], 0.20091654999999997, 1.0, PhaseType.AQUEOUS)
    PrHCO3_plus2 = Species("PrHCO3+2", None, ["Pr", "H", "C", "O"], 0.20192449, 2.0, PhaseType.AQUEOUS)
    PrCl_plus2 = Species("PrCl+2", None, ["Pr", "Cl"], 0.17636065, 2.0, PhaseType.AQUEOUS)
    PrCl2_plus = Species("PrCl2+", None, ["Pr", "Cl"], 0.21181365, 1.0, PhaseType.AQUEOUS)
    PrCl3_aq = Species("PrCl3(aq)", None, ["Pr", "Cl"], 0.24726664999999998, 0.0, PhaseType.AQUEOUS)
    PrCl4_minus = Species("PrCl4-", None, ["Pr", "Cl"], 0.28271965, -1.0, PhaseType.AQUEOUS)
    PrH2PO4_plus2 = Species("PrH2PO4+2", None, ["Pr", "H", "P", "O"], 0.237894891, 2.0, PhaseType.AQUEOUS)
    PrNO3_plus2 = Species("PrNO3+2", None, ["Pr", "N", "O"], 0.20291255000000002, 2.0, PhaseType.AQUEOUS)
    PrF_plus2 = Species("PrF+2", None, ["Pr", "F"], 0.159906053, 2.0, PhaseType.AQUEOUS)
    PrF2_plus = Species("PrF2+", None, ["Pr", "F"], 0.178904456, 1.0, PhaseType.AQUEOUS)
    PrF3_aq = Species("PrF3(aq)", None, ["Pr", "F"], 0.197902859, 0.0, PhaseType.AQUEOUS)
    PrF4_minus = Species("PrF4-", None, ["Pr", "F"], 0.21690126199999998, -1.0, PhaseType.AQUEOUS)
    PrOH_plus2 = Species("PrOH+2", None, ["Pr", "O", "H"], 0.15791499, 2.0, PhaseType.AQUEOUS)
    PrO_plus = Species("PrO+", None, ["Pr", "O"], 0.15690705, 1.0, PhaseType.AQUEOUS)
    PrO2H_aq = Species("PrO2H(aq)", None, ["Pr", "O", "H"], 0.17391439, 0.0, PhaseType.AQUEOUS)
    PrO2_minus = Species("PrO2-", None, ["Pr", "O"], 0.17290645, -1.0, PhaseType.AQUEOUS)
    PrSO4_plus = Species("PrSO4+", None, ["Pr", "S", "O"], 0.23697025, 1.0, PhaseType.AQUEOUS)
    NdCO3_plus = Species("NdCO3+", None, ["Nd", "C", "O"], 0.2042489, 1.0, PhaseType.AQUEOUS)
    NdHCO3_plus2 = Species("NdHCO3+2", None, ["Nd", "H", "C", "O"], 0.20525684, 2.0, PhaseType.AQUEOUS)
    NdOH_plus2 = Species("NdOH+2", None, ["Nd", "O", "H"], 0.16124734000000002, 2.0, PhaseType.AQUEOUS)
    NdO_plus = Species("NdO+", None, ["Nd", "O"], 0.1602394, 1.0, PhaseType.AQUEOUS)
    NdO2H_aq = Species("NdO2H(aq)", None, ["Nd", "O", "H"], 0.17724674, 0.0, PhaseType.AQUEOUS)
    NdO2_minus = Species("NdO2-", None, ["Nd", "O"], 0.1762388, -1.0, PhaseType.AQUEOUS)
    NdCl_plus2 = Species("NdCl+2", None, ["Nd", "Cl"], 0.179693, 2.0, PhaseType.AQUEOUS)
    NdCl2_plus = Species("NdCl2+", None, ["Nd", "Cl"], 0.215146, 1.0, PhaseType.AQUEOUS)
    NdCl3_aq = Species("NdCl3(aq)", None, ["Nd", "Cl"], 0.250599, 0.0, PhaseType.AQUEOUS)
    NdCl4_minus = Species("NdCl4-", None, ["Nd", "Cl"], 0.286052, -1.0, PhaseType.AQUEOUS)
    NdH2PO4_plus2 = Species("NdH2PO4+2", None, ["Nd", "H", "P", "O"], 0.24122724099999998, 2.0, PhaseType.AQUEOUS)
    NdNO3_plus2 = Species("NdNO3+2", None, ["Nd", "N", "O"], 0.2062449, 2.0, PhaseType.AQUEOUS)
    NdF_plus2 = Species("NdF+2", None, ["Nd", "F"], 0.163238403, 2.0, PhaseType.AQUEOUS)
    NdF2_plus = Species("NdF2+", None, ["Nd", "F"], 0.182236806, 1.0, PhaseType.AQUEOUS)
    NdF3_aq = Species("NdF3(aq)", None, ["Nd", "F"], 0.20123520900000003, 0.0, PhaseType.AQUEOUS)
    NdF4_minus = Species("NdF4-", None, ["Nd", "F"], 0.22023361200000002, -1.0, PhaseType.AQUEOUS)
    NdSO4_plus = Species("NdSO4+", None, ["Nd", "S", "O"], 0.24030260000000003, 1.0, PhaseType.AQUEOUS)
    SmCO3_plus = Species("SmCO3+", None, ["Sm", "C", "O"], 0.21036889999999997, 1.0, PhaseType.AQUEOUS)
    SmOH_plus2 = Species("SmOH+2", None, ["Sm", "O", "H"], 0.16736734, 2.0, PhaseType.AQUEOUS)
    SmO_plus = Species("SmO+", None, ["Sm", "O"], 0.1663594, 1.0, PhaseType.AQUEOUS)
    SmO2H_aq = Species("SmO2H(aq)", None, ["Sm", "O", "H"], 0.18336674, 0.0, PhaseType.AQUEOUS)
    SmO2_minus = Species("SmO2-", None, ["Sm", "O"], 0.1823588, -1.0, PhaseType.AQUEOUS)
    SmHCO3_plus2 = Species("SmHCO3+2", None, ["Sm", "H", "C", "O"], 0.21137684, 2.0, PhaseType.AQUEOUS)
    SmCl_plus2 = Species("SmCl+2", None, ["Sm", "Cl"], 0.185813, 2.0, PhaseType.AQUEOUS)
    SmCl2_plus = Species("SmCl2+", None, ["Sm", "Cl"], 0.221266, 1.0, PhaseType.AQUEOUS)
    SmCl3_aq = Species("SmCl3(aq)", None, ["Sm", "Cl"], 0.256719, 0.0, PhaseType.AQUEOUS)
    SmCl4_minus = Species("SmCl4-", None, ["Sm", "Cl"], 0.292172, -1.0, PhaseType.AQUEOUS)
    SmH2PO4_plus2 = Species("SmH2PO4+2", None, ["Sm", "H", "P", "O"], 0.247347241, 2.0, PhaseType.AQUEOUS)
    SmNO3_plus2 = Species("SmNO3+2", None, ["Sm", "N", "O"], 0.21236490000000002, 2.0, PhaseType.AQUEOUS)
    SmF_plus2 = Species("SmF+2", None, ["Sm", "F"], 0.169358403, 2.0, PhaseType.AQUEOUS)
    SmF2_plus = Species("SmF2+", None, ["Sm", "F"], 0.188356806, 1.0, PhaseType.AQUEOUS)
    SmF3_aq = Species("SmF3(aq)", None, ["Sm", "F"], 0.20735520899999998, 0.0, PhaseType.AQUEOUS)
    SmF4_minus = Species("SmF4-", None, ["Sm", "F"], 0.22635361199999998, -1.0, PhaseType.AQUEOUS)
    SmSO4_plus = Species("SmSO4+", None, ["Sm", "S", "O"], 0.2464226, 1.0, PhaseType.AQUEOUS)
    EuCO3_plus = Species("EuCO3+", None, ["Eu", "C", "O"], 0.21197289999999996, 1.0, PhaseType.AQUEOUS)
    EuOH_plus2 = Species("EuOH+2", None, ["Eu", "O", "H"], 0.16897134, 2.0, PhaseType.AQUEOUS)
    EuO_plus = Species("EuO+", None, ["Eu", "O"], 0.16796339999999998, 1.0, PhaseType.AQUEOUS)
    EuO2H_aq = Species("EuO2H(aq)", None, ["Eu", "O", "H"], 0.18497074, 0.0, PhaseType.AQUEOUS)
    EuO2_minus = Species("EuO2-", None, ["Eu", "O"], 0.18396279999999998, -1.0, PhaseType.AQUEOUS)
    EuHCO3_plus2 = Species("EuHCO3+2", None, ["Eu", "H", "C", "O"], 0.21298084, 2.0, PhaseType.AQUEOUS)
    EuCl_plus2 = Species("EuCl+2", None, ["Eu", "Cl"], 0.187417, 2.0, PhaseType.AQUEOUS)
    EuCl2_plus = Species("EuCl2+", None, ["Eu", "Cl"], 0.22286999999999998, 1.0, PhaseType.AQUEOUS)
    EuCl3_aq = Species("EuCl3(aq)", None, ["Eu", "Cl"], 0.25832299999999997, 0.0, PhaseType.AQUEOUS)
    EuCl4_minus = Species("EuCl4-", None, ["Eu", "Cl"], 0.293776, -1.0, PhaseType.AQUEOUS)
    EuF_plus = Species("EuF+", None, ["Eu", "F"], 0.17096240299999999, 1.0, PhaseType.AQUEOUS)
    EuF2_aq = Species("EuF2(aq)", None, ["Eu", "F"], 0.18996080599999998, 0.0, PhaseType.AQUEOUS)
    EuF3_minus = Species("EuF3-", None, ["Eu", "F"], 0.20895920899999998, -1.0, PhaseType.AQUEOUS)
    EuF4_minus2 = Species("EuF4-2", None, ["Eu", "F"], 0.22795761199999998, -2.0, PhaseType.AQUEOUS)
    EuCl_plus = Species("EuCl+", None, ["Eu", "Cl"], 0.187417, 1.0, PhaseType.AQUEOUS)
    EuCl2_aq = Species("EuCl2(aq)", None, ["Eu", "Cl"], 0.22286999999999998, 0.0, PhaseType.AQUEOUS)
    EuCl3_minus = Species("EuCl3-", None, ["Eu", "Cl"], 0.25832299999999997, -1.0, PhaseType.AQUEOUS)
    EuCl4_minus2 = Species("EuCl4-2", None, ["Eu", "Cl"], 0.293776, -2.0, PhaseType.AQUEOUS)
    EuH2PO4_plus2 = Species("EuH2PO4+2", None, ["Eu", "H", "P", "O"], 0.248951241, 2.0, PhaseType.AQUEOUS)
    EuNO3_plus2 = Species("EuNO3+2", None, ["Eu", "N", "O"], 0.21396890000000002, 2.0, PhaseType.AQUEOUS)
    EuF_plus2 = Species("EuF+2", None, ["Eu", "F"], 0.17096240299999999, 2.0, PhaseType.AQUEOUS)
    EuF2_plus = Species("EuF2+", None, ["Eu", "F"], 0.18996080599999998, 1.0, PhaseType.AQUEOUS)
    EuF3_aq = Species("EuF3(aq)", None, ["Eu", "F"], 0.20895920899999998, 0.0, PhaseType.AQUEOUS)
    EuF4_minus = Species("EuF4-", None, ["Eu", "F"], 0.22795761199999998, -1.0, PhaseType.AQUEOUS)
    EuSO4_plus = Species("EuSO4+", None, ["Eu", "S", "O"], 0.24802659999999999, 1.0, PhaseType.AQUEOUS)
    GdCO3_plus = Species("GdCO3+", None, ["Gd", "C", "O"], 0.21725889999999998, 1.0, PhaseType.AQUEOUS)
    GdOH_plus2 = Species("GdOH+2", None, ["Gd", "O", "H"], 0.17425734, 2.0, PhaseType.AQUEOUS)
    GdO_plus = Species("GdO+", None, ["Gd", "O"], 0.1732494, 1.0, PhaseType.AQUEOUS)
    GdO2H_aq = Species("GdO2H(aq)", None, ["Gd", "O", "H"], 0.19025674, 0.0, PhaseType.AQUEOUS)
    GdO2_minus = Species("GdO2-", None, ["Gd", "O"], 0.1892488, -1.0, PhaseType.AQUEOUS)
    GdHCO3_plus2 = Species("GdHCO3+2", None, ["Gd", "H", "C", "O"], 0.21826684000000002, 2.0, PhaseType.AQUEOUS)
    GdCl_plus2 = Species("GdCl+2", None, ["Gd", "Cl"], 0.192703, 2.0, PhaseType.AQUEOUS)
    GdCl2_plus = Species("GdCl2+", None, ["Gd", "Cl"], 0.228156, 1.0, PhaseType.AQUEOUS)
    GdCl3_aq = Species("GdCl3(aq)", None, ["Gd", "Cl"], 0.263609, 0.0, PhaseType.AQUEOUS)
    GdCl4_minus = Species("GdCl4-", None, ["Gd", "Cl"], 0.299062, -1.0, PhaseType.AQUEOUS)
    GdH2PO4_plus2 = Species("GdH2PO4+2", None, ["Gd", "H", "P", "O"], 0.254237241, 2.0, PhaseType.AQUEOUS)
    GdNO3_plus2 = Species("GdNO3+2", None, ["Gd", "N", "O"], 0.21925490000000003, 2.0, PhaseType.AQUEOUS)
    GdF_plus2 = Species("GdF+2", None, ["Gd", "F"], 0.176248403, 2.0, PhaseType.AQUEOUS)
    GdF2_plus = Species("GdF2+", None, ["Gd", "F"], 0.195246806, 1.0, PhaseType.AQUEOUS)
    GdF3_aq = Species("GdF3(aq)", None, ["Gd", "F"], 0.214245209, 0.0, PhaseType.AQUEOUS)
    GdF4_minus = Species("GdF4-", None, ["Gd", "F"], 0.233243612, -1.0, PhaseType.AQUEOUS)
    GdSO4_plus = Species("GdSO4+", None, ["Gd", "S", "O"], 0.2533126, 1.0, PhaseType.AQUEOUS)
    TbCO3_plus = Species("TbCO3+", None, ["Tb", "C", "O"], 0.21893424, 1.0, PhaseType.AQUEOUS)
    TbOH_plus2 = Species("TbOH+2", None, ["Tb", "O", "H"], 0.17593268, 2.0, PhaseType.AQUEOUS)
    TbO_plus = Species("TbO+", None, ["Tb", "O"], 0.17492474, 1.0, PhaseType.AQUEOUS)
    TbO2H_aq = Species("TbO2H(aq)", None, ["Tb", "O", "H"], 0.19193208, 0.0, PhaseType.AQUEOUS)
    TbO2_minus = Species("TbO2-", None, ["Tb", "O"], 0.19092414, -1.0, PhaseType.AQUEOUS)
    TbHCO3_plus2 = Species("TbHCO3+2", None, ["Tb", "H", "C", "O"], 0.21994218, 2.0, PhaseType.AQUEOUS)
    TbCl_plus2 = Species("TbCl+2", None, ["Tb", "Cl"], 0.19437833999999998, 2.0, PhaseType.AQUEOUS)
    TbCl2_plus = Species("TbCl2+", None, ["Tb", "Cl"], 0.22983134, 1.0, PhaseType.AQUEOUS)
    TbCl3_aq = Species("TbCl3(aq)", None, ["Tb", "Cl"], 0.26528434, 0.0, PhaseType.AQUEOUS)
    TbCl4_minus = Species("TbCl4-", None, ["Tb", "Cl"], 0.30073733999999996, -1.0, PhaseType.AQUEOUS)
    TbH2PO4_plus2 = Species("TbH2PO4+2", None, ["Tb", "H", "P", "O"], 0.255912581, 2.0, PhaseType.AQUEOUS)
    TbNO3_plus2 = Species("TbNO3+2", None, ["Tb", "N", "O"], 0.22093024, 2.0, PhaseType.AQUEOUS)
    TbF_plus2 = Species("TbF+2", None, ["Tb", "F"], 0.177923743, 2.0, PhaseType.AQUEOUS)
    TbF2_plus = Species("TbF2+", None, ["Tb", "F"], 0.196922146, 1.0, PhaseType.AQUEOUS)
    TbF3_aq = Species("TbF3(aq)", None, ["Tb", "F"], 0.21592054900000002, 0.0, PhaseType.AQUEOUS)
    TbF4_minus = Species("TbF4-", None, ["Tb", "F"], 0.23491895200000001, -1.0, PhaseType.AQUEOUS)
    TbSO4_plus = Species("TbSO4+", None, ["Tb", "S", "O"], 0.25498794, 1.0, PhaseType.AQUEOUS)
    DyCO3_plus = Species("DyCO3+", None, ["Dy", "C", "O"], 0.2225089, 1.0, PhaseType.AQUEOUS)
    DyHCO3_plus2 = Species("DyHCO3+2", None, ["Dy", "H", "C", "O"], 0.22351684, 2.0, PhaseType.AQUEOUS)
    DyCl_plus2 = Species("DyCl+2", None, ["Dy", "Cl"], 0.197953, 2.0, PhaseType.AQUEOUS)
    DyCl2_plus = Species("DyCl2+", None, ["Dy", "Cl"], 0.233406, 1.0, PhaseType.AQUEOUS)
    DyCl3_aq = Species("DyCl3(aq)", None, ["Dy", "Cl"], 0.268859, 0.0, PhaseType.AQUEOUS)
    DyCl4_minus = Species("DyCl4-", None, ["Dy", "Cl"], 0.304312, -1.0, PhaseType.AQUEOUS)
    DyH2PO4_plus2 = Species("DyH2PO4+2", None, ["Dy", "H", "P", "O"], 0.259487241, 2.0, PhaseType.AQUEOUS)
    DyNO3_plus2 = Species("DyNO3+2", None, ["Dy", "N", "O"], 0.2245049, 2.0, PhaseType.AQUEOUS)
    DyF_plus2 = Species("DyF+2", None, ["Dy", "F"], 0.181498403, 2.0, PhaseType.AQUEOUS)
    DyF2_plus = Species("DyF2+", None, ["Dy", "F"], 0.200496806, 1.0, PhaseType.AQUEOUS)
    DyF3_aq = Species("DyF3(aq)", None, ["Dy", "F"], 0.21949520900000002, 0.0, PhaseType.AQUEOUS)
    DyF4_minus = Species("DyF4-", None, ["Dy", "F"], 0.23849361200000002, -1.0, PhaseType.AQUEOUS)
    DyOH_plus2 = Species("DyOH+2", None, ["Dy", "O", "H"], 0.17950734000000002, 2.0, PhaseType.AQUEOUS)
    DyO_plus = Species("DyO+", None, ["Dy", "O"], 0.1784994, 1.0, PhaseType.AQUEOUS)
    DyO2H_aq = Species("DyO2H(aq)", None, ["Dy", "O", "H"], 0.19550674, 0.0, PhaseType.AQUEOUS)
    DyO2_minus = Species("DyO2-", None, ["Dy", "O"], 0.1944988, -1.0, PhaseType.AQUEOUS)
    DySO4_plus = Species("DySO4+", None, ["Dy", "S", "O"], 0.25856260000000003, 1.0, PhaseType.AQUEOUS)
    HoCO3_plus = Species("HoCO3+", None, ["Ho", "C", "O"], 0.22493922, 1.0, PhaseType.AQUEOUS)
    HoHCO3_plus2 = Species("HoHCO3+2", None, ["Ho", "H", "C", "O"], 0.22594715999999998, 2.0, PhaseType.AQUEOUS)
    HoCl_plus2 = Species("HoCl+2", None, ["Ho", "Cl"], 0.20038331999999998, 2.0, PhaseType.AQUEOUS)
    HoCl2_plus = Species("HoCl2+", None, ["Ho", "Cl"], 0.23583632, 1.0, PhaseType.AQUEOUS)
    HoCl3_aq = Species("HoCl3(aq)", None, ["Ho", "Cl"], 0.27128932, 0.0, PhaseType.AQUEOUS)
    HoCl4_minus = Species("HoCl4-", None, ["Ho", "Cl"], 0.30674232, -1.0, PhaseType.AQUEOUS)
    HoH2PO4_plus2 = Species("HoH2PO4+2", None, ["Ho", "H", "P", "O"], 0.26191756099999997, 2.0, PhaseType.AQUEOUS)
    HoNO3_plus2 = Species("HoNO3+2", None, ["Ho", "N", "O"], 0.22693522, 2.0, PhaseType.AQUEOUS)
    HoF_plus2 = Species("HoF+2", None, ["Ho", "F"], 0.183928723, 2.0, PhaseType.AQUEOUS)
    HoF2_plus = Species("HoF2+", None, ["Ho", "F"], 0.20292712599999999, 1.0, PhaseType.AQUEOUS)
    HoF3_aq = Species("HoF3(aq)", None, ["Ho", "F"], 0.221925529, 0.0, PhaseType.AQUEOUS)
    HoF4_minus = Species("HoF4-", None, ["Ho", "F"], 0.240923932, -1.0, PhaseType.AQUEOUS)
    HoOH_plus2 = Species("HoOH+2", None, ["Ho", "O", "H"], 0.18193766, 2.0, PhaseType.AQUEOUS)
    HoO_plus = Species("HoO+", None, ["Ho", "O"], 0.18092972, 1.0, PhaseType.AQUEOUS)
    HoO2H_aq = Species("HoO2H(aq)", None, ["Ho", "O", "H"], 0.19793706, 0.0, PhaseType.AQUEOUS)
    HoO2_minus = Species("HoO2-", None, ["Ho", "O"], 0.19692911999999999, -1.0, PhaseType.AQUEOUS)
    HoSO4_plus = Species("HoSO4+", None, ["Ho", "S", "O"], 0.26099292, 1.0, PhaseType.AQUEOUS)
    ErCO3_plus = Species("ErCO3+", None, ["Er", "C", "O"], 0.22726789999999997, 1.0, PhaseType.AQUEOUS)
    ErHCO3_plus2 = Species("ErHCO3+2", None, ["Er", "H", "C", "O"], 0.22827584, 2.0, PhaseType.AQUEOUS)
    ErCl_plus2 = Species("ErCl+2", None, ["Er", "Cl"], 0.202712, 2.0, PhaseType.AQUEOUS)
    ErCl2_plus = Species("ErCl2+", None, ["Er", "Cl"], 0.238165, 1.0, PhaseType.AQUEOUS)
    ErCl3_aq = Species("ErCl3(aq)", None, ["Er", "Cl"], 0.273618, 0.0, PhaseType.AQUEOUS)
    ErCl4_minus = Species("ErCl4-", None, ["Er", "Cl"], 0.309071, -1.0, PhaseType.AQUEOUS)
    ErH2PO4_plus2 = Species("ErH2PO4+2", None, ["Er", "H", "P", "O"], 0.264246241, 2.0, PhaseType.AQUEOUS)
    ErNO3_plus2 = Species("ErNO3+2", None, ["Er", "N", "O"], 0.22926390000000002, 2.0, PhaseType.AQUEOUS)
    ErF_plus2 = Species("ErF+2", None, ["Er", "F"], 0.186257403, 2.0, PhaseType.AQUEOUS)
    ErF2_plus = Species("ErF2+", None, ["Er", "F"], 0.20525580599999999, 1.0, PhaseType.AQUEOUS)
    ErF3_aq = Species("ErF3(aq)", None, ["Er", "F"], 0.22425420899999998, 0.0, PhaseType.AQUEOUS)
    ErF4_minus = Species("ErF4-", None, ["Er", "F"], 0.24325261199999998, -1.0, PhaseType.AQUEOUS)
    ErOH_plus2 = Species("ErOH+2", None, ["Er", "O", "H"], 0.18426634, 2.0, PhaseType.AQUEOUS)
    ErO_plus = Species("ErO+", None, ["Er", "O"], 0.1832584, 1.0, PhaseType.AQUEOUS)
    ErO2H_aq = Species("ErO2H(aq)", None, ["Er", "O", "H"], 0.20026574, 0.0, PhaseType.AQUEOUS)
    ErO2_minus = Species("ErO2-", None, ["Er", "O"], 0.19925779999999998, -1.0, PhaseType.AQUEOUS)
    ErSO4_plus = Species("ErSO4+", None, ["Er", "S", "O"], 0.2633216, 1.0, PhaseType.AQUEOUS)
    TmCO3_plus = Species("TmCO3+", None, ["Tm", "C", "O"], 0.22894311, 1.0, PhaseType.AQUEOUS)
    TmHCO3_plus2 = Species("TmHCO3+2", None, ["Tm", "H", "C", "O"], 0.22995105, 2.0, PhaseType.AQUEOUS)
    TmCl_plus2 = Species("TmCl+2", None, ["Tm", "Cl"], 0.20438720999999999, 2.0, PhaseType.AQUEOUS)
    TmCl2_plus = Species("TmCl2+", None, ["Tm", "Cl"], 0.23984021, 1.0, PhaseType.AQUEOUS)
    TmCl3_aq = Species("TmCl3(aq)", None, ["Tm", "Cl"], 0.27529321, 0.0, PhaseType.AQUEOUS)
    TmCl4_minus = Species("TmCl4-", None, ["Tm", "Cl"], 0.31074621, -1.0, PhaseType.AQUEOUS)
    TmH2PO4_plus2 = Species("TmH2PO4+2", None, ["Tm", "H", "P", "O"], 0.265921451, 2.0, PhaseType.AQUEOUS)
    TmNO3_plus2 = Species("TmNO3+2", None, ["Tm", "N", "O"], 0.23093911, 2.0, PhaseType.AQUEOUS)
    TmF_plus2 = Species("TmF+2", None, ["Tm", "F"], 0.187932613, 2.0, PhaseType.AQUEOUS)
    TmF2_plus = Species("TmF2+", None, ["Tm", "F"], 0.206931016, 1.0, PhaseType.AQUEOUS)
    TmF3_aq = Species("TmF3(aq)", None, ["Tm", "F"], 0.22592941900000002, 0.0, PhaseType.AQUEOUS)
    TmF4_minus = Species("TmF4-", None, ["Tm", "F"], 0.24492782200000002, -1.0, PhaseType.AQUEOUS)
    TmOH_plus2 = Species("TmOH+2", None, ["Tm", "O", "H"], 0.18594155, 2.0, PhaseType.AQUEOUS)
    TmO_plus = Species("TmO+", None, ["Tm", "O"], 0.18493361, 1.0, PhaseType.AQUEOUS)
    TmO2H_aq = Species("TmO2H(aq)", None, ["Tm", "O", "H"], 0.20194095, 0.0, PhaseType.AQUEOUS)
    TmO2_minus = Species("TmO2-", None, ["Tm", "O"], 0.20093301, -1.0, PhaseType.AQUEOUS)
    TmSO4_plus = Species("TmSO4+", None, ["Tm", "S", "O"], 0.26499681, 1.0, PhaseType.AQUEOUS)
    YbCO3_plus = Species("YbCO3+", None, ["Yb", "C", "O"], 0.2330489, 1.0, PhaseType.AQUEOUS)
    YbOH_plus2 = Species("YbOH+2", None, ["Yb", "O", "H"], 0.19004734, 2.0, PhaseType.AQUEOUS)
    YbO_plus = Species("YbO+", None, ["Yb", "O"], 0.1890394, 1.0, PhaseType.AQUEOUS)
    YbO2H_aq = Species("YbO2H(aq)", None, ["Yb", "O", "H"], 0.20604674, 0.0, PhaseType.AQUEOUS)
    YbO2_minus = Species("YbO2-", None, ["Yb", "O"], 0.2050388, -1.0, PhaseType.AQUEOUS)
    YbHCO3_plus2 = Species("YbHCO3+2", None, ["Yb", "H", "C", "O"], 0.23405684, 2.0, PhaseType.AQUEOUS)
    YbCl_plus2 = Species("YbCl+2", None, ["Yb", "Cl"], 0.20849299999999998, 2.0, PhaseType.AQUEOUS)
    YbCl2_plus = Species("YbCl2+", None, ["Yb", "Cl"], 0.243946, 1.0, PhaseType.AQUEOUS)
    YbCl3_aq = Species("YbCl3(aq)", None, ["Yb", "Cl"], 0.279399, 0.0, PhaseType.AQUEOUS)
    YbCl4_minus = Species("YbCl4-", None, ["Yb", "Cl"], 0.314852, -1.0, PhaseType.AQUEOUS)
    YbH2PO4_plus2 = Species("YbH2PO4+2", None, ["Yb", "H", "P", "O"], 0.270027241, 2.0, PhaseType.AQUEOUS)
    YbNO3_plus2 = Species("YbNO3+2", None, ["Yb", "N", "O"], 0.2350449, 2.0, PhaseType.AQUEOUS)
    YbF_plus2 = Species("YbF+2", None, ["Yb", "F"], 0.192038403, 2.0, PhaseType.AQUEOUS)
    YbF2_plus = Species("YbF2+", None, ["Yb", "F"], 0.211036806, 1.0, PhaseType.AQUEOUS)
    YbF3_aq = Species("YbF3(aq)", None, ["Yb", "F"], 0.23003520900000002, 0.0, PhaseType.AQUEOUS)
    YbF4_minus = Species("YbF4-", None, ["Yb", "F"], 0.24903361200000002, -1.0, PhaseType.AQUEOUS)
    YbSO4_plus = Species("YbSO4+", None, ["Yb", "S", "O"], 0.2691026, 1.0, PhaseType.AQUEOUS)
    LuCO3_plus = Species("LuCO3+", None, ["Lu", "C", "O"], 0.23497590000000002, 1.0, PhaseType.AQUEOUS)
    LuOH_plus2 = Species("LuOH+2", None, ["Lu", "O", "H"], 0.19197434000000002, 2.0, PhaseType.AQUEOUS)
    LuO_plus = Species("LuO+", None, ["Lu", "O"], 0.1909664, 1.0, PhaseType.AQUEOUS)
    LuO2H_aq = Species("LuO2H(aq)", None, ["Lu", "O", "H"], 0.20797374000000002, 0.0, PhaseType.AQUEOUS)
    LuO2_minus = Species("LuO2-", None, ["Lu", "O"], 0.2069658, -1.0, PhaseType.AQUEOUS)
    LuHCO3_plus2 = Species("LuHCO3+2", None, ["Lu", "H", "C", "O"], 0.23598384, 2.0, PhaseType.AQUEOUS)
    LuCl_plus2 = Species("LuCl+2", None, ["Lu", "Cl"], 0.21042, 2.0, PhaseType.AQUEOUS)
    LuCl2_plus = Species("LuCl2+", None, ["Lu", "Cl"], 0.245873, 1.0, PhaseType.AQUEOUS)
    LuCl3_aq = Species("LuCl3(aq)", None, ["Lu", "Cl"], 0.281326, 0.0, PhaseType.AQUEOUS)
    LuCl4_minus = Species("LuCl4-", None, ["Lu", "Cl"], 0.31677900000000003, -1.0, PhaseType.AQUEOUS)
    LuH2PO4_plus2 = Species("LuH2PO4+2", None, ["Lu", "H", "P", "O"], 0.271954241, 2.0, PhaseType.AQUEOUS)
    LuNO3_plus2 = Species("LuNO3+2", None, ["Lu", "N", "O"], 0.2369719, 2.0, PhaseType.AQUEOUS)
    LuF_plus2 = Species("LuF+2", None, ["Lu", "F"], 0.193965403, 2.0, PhaseType.AQUEOUS)
    LuF2_plus = Species("LuF2+", None, ["Lu", "F"], 0.212963806, 1.0, PhaseType.AQUEOUS)
    LuF3_aq = Species("LuF3(aq)", None, ["Lu", "F"], 0.23196220900000003, 0.0, PhaseType.AQUEOUS)
    LuF4_minus = Species("LuF4-", None, ["Lu", "F"], 0.250960612, -1.0, PhaseType.AQUEOUS)
    LuSO4_plus = Species("LuSO4+", None, ["Lu", "S", "O"], 0.27102960000000004, 1.0, PhaseType.AQUEOUS)
    NaSO4_minus = Species("NaSO4-", None, ["Na", "S", "O"], 0.11905237, -1.0, PhaseType.AQUEOUS)
    MgSO4_aq = Species("MgSO4(aq)", None, ["Mg", "S", "O"], 0.1203676, 0.0, PhaseType.AQUEOUS)
    HCl_aq = Species("HCl(aq)", None, ["H", "Cl"], 0.03646094, 0.0, PhaseType.AQUEOUS)
    MgCO3_aq = Species("MgCO3(aq)", None, ["Mg", "C", "O"], 0.0843139, 0.0, PhaseType.AQUEOUS)
    CaCO3_aq = Species("CaCO3(aq)", None, ["Ca", "C", "O"], 0.1000869, 0.0, PhaseType.AQUEOUS)
    SrCO3_aq = Species("SrCO3(aq)", None, ["Sr", "C", "O"], 0.1476289, 0.0, PhaseType.AQUEOUS)
    BaCO3_aq = Species("BaCO3(aq)", None, ["Ba", "C", "O"], 0.1973359, 0.0, PhaseType.AQUEOUS)
    BeCl_plus = Species("BeCl+", None, ["Be", "Cl"], 0.044465182, 1.0, PhaseType.AQUEOUS)
    BeCl2_aq = Species("BeCl2(aq)", None, ["Be", "Cl"], 0.079918182, 0.0, PhaseType.AQUEOUS)
    FeCl_plus2 = Species("FeCl+2", None, ["Fe", "Cl"], 0.09129799999999999, 2.0, PhaseType.AQUEOUS)
    CoCl_plus = Species("CoCl+", None, ["Co", "Cl"], 0.0943862, 1.0, PhaseType.AQUEOUS)
    CuCl_aq = Species("CuCl(aq)", None, ["Cu", "Cl"], 0.098999, 0.0, PhaseType.AQUEOUS)
    CuCl2_minus = Species("CuCl2-", None, ["Cu", "Cl"], 0.13445200000000002, -1.0, PhaseType.AQUEOUS)
    CuCl3_minus2 = Species("CuCl3-2", None, ["Cu", "Cl"], 0.169905, -2.0, PhaseType.AQUEOUS)
    CuCl_plus = Species("CuCl+", None, ["Cu", "Cl"], 0.098999, 1.0, PhaseType.AQUEOUS)
    CuCl2_aq = Species("CuCl2(aq)", None, ["Cu", "Cl"], 0.13445200000000002, 0.0, PhaseType.AQUEOUS)
    CuCl3_minus = Species("CuCl3-", None, ["Cu", "Cl"], 0.169905, -1.0, PhaseType.AQUEOUS)
    CuCl4_minus2 = Species("CuCl4-2", None, ["Cu", "Cl"], 0.20535799999999998, -2.0, PhaseType.AQUEOUS)
    CdCl_plus = Species("CdCl+", None, ["Cd", "Cl"], 0.147864, 1.0, PhaseType.AQUEOUS)
    CdCl2_aq = Species("CdCl2(aq)", None, ["Cd", "Cl"], 0.183317, 0.0, PhaseType.AQUEOUS)
    CdCl3_minus = Species("CdCl3-", None, ["Cd", "Cl"], 0.21877, -1.0, PhaseType.AQUEOUS)
    CdCl4_minus2 = Species("CdCl4-2", None, ["Cd", "Cl"], 0.254223, -2.0, PhaseType.AQUEOUS)
    TlCl_aq = Species("TlCl(aq)", None, ["Tl", "Cl"], 0.2398363, 0.0, PhaseType.AQUEOUS)
    TlCl_plus2 = Species("TlCl+2", None, ["Tl", "Cl"], 0.2398363, 2.0, PhaseType.AQUEOUS)
    AuCl_aq = Species("AuCl(aq)", None, ["Au", "Cl"], 0.23241954999999997, 0.0, PhaseType.AQUEOUS)
    AuCl2_minus = Species("AuCl2-", None, ["Au", "Cl"], 0.26787255, -1.0, PhaseType.AQUEOUS)
    AuCl3_minus2 = Species("AuCl3-2", None, ["Au", "Cl"], 0.30332555, -2.0, PhaseType.AQUEOUS)
    AuCl4_minus = Species("AuCl4-", None, ["Au", "Cl"], 0.33877855, -1.0, PhaseType.AQUEOUS)
    HgCl_plus = Species("HgCl+", None, ["Hg", "Cl"], 0.236043, 1.0, PhaseType.AQUEOUS)
    HgCl2_aq = Species("HgCl2(aq)", None, ["Hg", "Cl"], 0.27149599999999996, 0.0, PhaseType.AQUEOUS)
    HgCl3_minus = Species("HgCl3-", None, ["Hg", "Cl"], 0.30694899999999997, -1.0, PhaseType.AQUEOUS)
    HgCl4_minus2 = Species("HgCl4-2", None, ["Hg", "Cl"], 0.342402, -2.0, PhaseType.AQUEOUS)
    InCl_plus2 = Species("InCl+2", None, ["In", "Cl"], 0.150271, 2.0, PhaseType.AQUEOUS)
    BeF_plus = Species("BeF+", None, ["Be", "F"], 0.028010585, 1.0, PhaseType.AQUEOUS)
    BeF2_aq = Species("BeF2(aq)", None, ["Be", "F"], 0.047008988, 0.0, PhaseType.AQUEOUS)
    BeF3_minus = Species("BeF3-", None, ["Be", "F"], 0.066007391, -1.0, PhaseType.AQUEOUS)
    BeF4_minus2 = Species("BeF4-2", None, ["Be", "F"], 0.085005794, -2.0, PhaseType.AQUEOUS)
    MnF_plus = Species("MnF+", None, ["Mn", "F"], 0.073936453, 1.0, PhaseType.AQUEOUS)
    FeF_plus = Species("FeF+", None, ["Fe", "F"], 0.074843403, 1.0, PhaseType.AQUEOUS)
    FeF_plus2 = Species("FeF+2", None, ["Fe", "F"], 0.074843403, 2.0, PhaseType.AQUEOUS)
    CoF_plus = Species("CoF+", None, ["Co", "F"], 0.077931603, 1.0, PhaseType.AQUEOUS)
    NiF_plus = Species("NiF+", None, ["Ni", "F"], 0.077691803, 1.0, PhaseType.AQUEOUS)
    CuF_plus = Species("CuF+", None, ["Cu", "F"], 0.082544403, 1.0, PhaseType.AQUEOUS)
    ZnF_plus = Species("ZnF+", None, ["Zn", "F"], 0.08440740299999999, 1.0, PhaseType.AQUEOUS)
    AgF_aq = Species("AgF(aq)", None, ["Ag", "F"], 0.126866603, 0.0, PhaseType.AQUEOUS)
    CdF_plus = Species("CdF+", None, ["Cd", "F"], 0.131409403, 1.0, PhaseType.AQUEOUS)
    CdF2_aq = Species("CdF2(aq)", None, ["Cd", "F"], 0.150407806, 0.0, PhaseType.AQUEOUS)
    BaF_plus = Species("BaF+", None, ["Ba", "F"], 0.156325403, 1.0, PhaseType.AQUEOUS)
    TlF_aq = Species("TlF(aq)", None, ["Tl", "F"], 0.223381703, 0.0, PhaseType.AQUEOUS)
    HgF_plus = Species("HgF+", None, ["Hg", "F"], 0.219588403, 1.0, PhaseType.AQUEOUS)
    InF_plus2 = Species("InF+2", None, ["In", "F"], 0.133816403, 2.0, PhaseType.AQUEOUS)
    PbF_plus = Species("PbF+", None, ["Pb", "F"], 0.226198403, 1.0, PhaseType.AQUEOUS)
    PbF2_aq = Species("PbF2(aq)", None, ["Pb", "F"], 0.245196806, 0.0, PhaseType.AQUEOUS)
    Ag_HS_2_minus = Species("Ag(HS)2-", None, ["Ag", "H", "S"], 0.17401408000000002, -1.0, PhaseType.AQUEOUS)
    Au_HS_2_minus = Species("Au(HS)2-", None, ["Au", "H", "S"], 0.26311243, -1.0, PhaseType.AQUEOUS)
    Pb_HS_2_aq = Species("Pb(HS)2(aq)", None, ["Pb", "H", "S"], 0.27334588, 0.0, PhaseType.AQUEOUS)
    Pb_HS_3_minus = Species("Pb(HS)3-", None, ["Pb", "H", "S"], 0.30641882, -1.0, PhaseType.AQUEOUS)
    Mg_HSiO3_plus = Species("Mg(HSiO3)+", None, ["Mg", "H", "Si", "O"], 0.10139664000000001, 1.0, PhaseType.AQUEOUS)
    Ca_HSiO3_plus = Species("Ca(HSiO3)+", None, ["Ca", "H", "Si", "O"], 0.11716964, 1.0, PhaseType.AQUEOUS)
    AlF_plus2 = Species("AlF+2", None, ["Al", "F"], 0.045979940999999996, 2.0, PhaseType.AQUEOUS)
    AlF2_plus = Species("AlF2+", None, ["Al", "F"], 0.064978344, 1.0, PhaseType.AQUEOUS)
    AlF3_aq = Species("AlF3(aq)", None, ["Al", "F"], 0.083976747, 0.0, PhaseType.AQUEOUS)
    AlF4_minus = Species("AlF4-", None, ["Al", "F"], 0.10297515, -1.0, PhaseType.AQUEOUS)
    Al_OH_2F2_minus = Species("Al(OH)2F2-", None, ["Al", "O", "H", "F"], 0.098993024, -1.0, PhaseType.AQUEOUS)
    Al_OH_2F_aq = Species("Al(OH)2F(aq)", None, ["Al", "O", "H", "F"], 0.079994621, 0.0, PhaseType.AQUEOUS)
    Al_OH_F2_aq = Species("Al(OH)F2(aq)", None, ["Al", "O", "H", "F"], 0.081985684, 0.0, PhaseType.AQUEOUS)
    AlSO4_plus = Species("AlSO4+", None, ["Al", "S", "O"], 0.123044138, 1.0, PhaseType.AQUEOUS)
    NaAl_OH_3F_aq = Species("NaAl(OH)3F(aq)", None, ["Na", "Al", "O", "H", "F"], 0.119991731, 0.0, PhaseType.AQUEOUS)
    NaAl_OH_2F2_aq = Species("NaAl(OH)2F2(aq)", None, ["Na", "Al", "O", "H", "F"], 0.121982794, 0.0, PhaseType.AQUEOUS)
    CH4_aq = Species("CH4(aq)", None, ["C", "H"], 0.016042459999999998, 0.0, PhaseType.AQUEOUS)
    H_Acetate_aq = Species("H-Acetate(aq)", None, ["C", "H", "O"], 0.06005196, 0.0, PhaseType.AQUEOUS)
    Acetate_minus = Species("Acetate-", None, ["C", "H", "O"], 0.05904402, -1.0, PhaseType.AQUEOUS)
    _1_Butanamine_aq = Species("1-Butanamine(aq)", None, ["C", "H", "N"], 0.07313684, 0.0, PhaseType.AQUEOUS)
    _1_Butanol_aq = Species("1-Butanol(aq)", None, ["C", "H", "O"], 0.0741216, 0.0, PhaseType.AQUEOUS)
    _1_Butene_aq = Species("1-Butene(aq)", None, ["C", "H"], 0.056106319999999994, 0.0, PhaseType.AQUEOUS)
    _1_Butyne_aq = Species("1-Butyne(aq)", None, ["C", "H"], 0.05409044, 0.0, PhaseType.AQUEOUS)
    _1_Heptanamine_aq = Species("1-Heptanamine(aq)", None, ["C", "H", "N"], 0.11521657999999999, 0.0, PhaseType.AQUEOUS)
    _1_Heptanol_aq = Species("1-Heptanol(aq)", None, ["C", "H", "O"], 0.11620133999999999, 0.0, PhaseType.AQUEOUS)
    _1_Heptene_aq = Species("1-Heptene(aq)", None, ["C", "H"], 0.09818605999999999, 0.0, PhaseType.AQUEOUS)
    _1_Heptyne_aq = Species("1-Heptyne(aq)", None, ["C", "H"], 0.09617018, 0.0, PhaseType.AQUEOUS)
    _1_Hexanamine_aq = Species("1-Hexanamine(aq)", None, ["C", "H", "N"], 0.10118999999999999, 0.0, PhaseType.AQUEOUS)
    _1_Hexanol_aq = Species("1-Hexanol(aq)", None, ["C", "H", "O"], 0.10217475999999999, 0.0, PhaseType.AQUEOUS)
    _1_Hexene_aq = Species("1-Hexene(aq)", None, ["C", "H"], 0.08415948, 0.0, PhaseType.AQUEOUS)
    _1_Hexyne_aq = Species("1-Hexyne(aq)", None, ["C", "H"], 0.0821436, 0.0, PhaseType.AQUEOUS)
    _1_Octanamine_aq = Species("1-Octanamine(aq)", None, ["C", "H", "N"], 0.12924316, 0.0, PhaseType.AQUEOUS)
    _1_Octanol_aq = Species("1-Octanol(aq)", None, ["C", "H", "O"], 0.13022792, 0.0, PhaseType.AQUEOUS)
    _1_Octene_aq = Species("1-Octene(aq)", None, ["C", "H"], 0.11221263999999999, 0.0, PhaseType.AQUEOUS)
    _1_Octyne_aq = Species("1-Octyne(aq)", None, ["C", "H"], 0.11019675999999999, 0.0, PhaseType.AQUEOUS)
    _1_Pentanamine_aq = Species("1-Pentanamine(aq)", None, ["C", "H", "N"], 0.08716341999999999, 0.0, PhaseType.AQUEOUS)
    _1_Pentanol_aq = Species("1-Pentanol(aq)", None, ["C", "H", "O"], 0.08814817999999999, 0.0, PhaseType.AQUEOUS)
    _1_Pentene_aq = Species("1-Pentene(aq)", None, ["C", "H"], 0.0701329, 0.0, PhaseType.AQUEOUS)
    _1_Pentyne_aq = Species("1-Pentyne(aq)", None, ["C", "H"], 0.06811702, 0.0, PhaseType.AQUEOUS)
    _1_Propanamine_aq = Species("1-Propanamine(aq)", None, ["C", "H", "N"], 0.05911026, 0.0, PhaseType.AQUEOUS)
    _1_Propanol_aq = Species("1-Propanol(aq)", None, ["C", "H", "O"], 0.06009502, 0.0, PhaseType.AQUEOUS)
    _1_Propene_aq = Species("1-Propene(aq)", None, ["C", "H"], 0.04207974, 0.0, PhaseType.AQUEOUS)
    _1_Propyne_aq = Species("1-Propyne(aq)", None, ["C", "H"], 0.04006386, 0.0, PhaseType.AQUEOUS)
    _2_Butanone_aq = Species("2-Butanone(aq)", None, ["C", "H", "O"], 0.07210572, 0.0, PhaseType.AQUEOUS)
    _2_Heptanone_aq = Species("2-Heptanone(aq)", None, ["C", "H", "O"], 0.11418545999999999, 0.0, PhaseType.AQUEOUS)
    _2_Hexanone_aq = Species("2-Hexanone(aq)", None, ["C", "H", "O"], 0.10015887999999999, 0.0, PhaseType.AQUEOUS)
    _2_Hydroxybutanoate = Species("2-Hydroxybutanoate", None, ["C", "H", "O"], 0.10309658, -1.0, PhaseType.AQUEOUS)
    _2_Hydroxybutanoic_aq = Species("2-Hydroxybutanoic(aq)", None, ["C", "H", "O"], 0.10410452, 0.0, PhaseType.AQUEOUS)
    _2_Hydroxydecanoate = Species("2-Hydroxydecanoate", None, ["C", "H", "O"], 0.18725606, -1.0, PhaseType.AQUEOUS)
    _2_Hydroxydecanoic_aq = Species("2-Hydroxydecanoic(aq)", None, ["C", "H", "O"], 0.188264, 0.0, PhaseType.AQUEOUS)
    _2_Hydroxyheptanoic = Species("2-Hydroxyheptanoic", None, ["C", "H", "O"], 0.14618426, 0.0, PhaseType.AQUEOUS)
    _2_Hydroxyhexanoate = Species("2-Hydroxyhexanoate", None, ["C", "H", "O"], 0.13114974000000001, -1.0,
                                  PhaseType.AQUEOUS)
    _2_Hydroxyhexanoic_aq = Species("2-Hydroxyhexanoic(aq)", None, ["C", "H", "O"], 0.13215768, 0.0, PhaseType.AQUEOUS)
    _2_Hydroxynonanoate = Species("2-Hydroxynonanoate", None, ["C", "H", "O"], 0.17322948, -1.0, PhaseType.AQUEOUS)
    _2_Hydroxynonanoic_aq = Species("2-Hydroxynonanoic(aq)", None, ["C", "H", "O"], 0.17423741999999998, 0.0,
                                    PhaseType.AQUEOUS)
    _2_Hydroxyoctanoate = Species("2-Hydroxyoctanoate", None, ["C", "H", "O"], 0.15920289999999998, -1.0,
                                  PhaseType.AQUEOUS)
    _2_Hydroxyoctanoic_aq = Species("2-Hydroxyoctanoic(aq)", None, ["C", "H", "O"], 0.16021084, 0.0, PhaseType.AQUEOUS)
    _2_Hydroxypentanoic = Species("2-Hydroxypentanoic", None, ["C", "H", "O"], 0.1181311, 0.0, PhaseType.AQUEOUS)
    _2_Octanone_aq = Species("2-Octanone(aq)", None, ["C", "H", "O"], 0.12821204, 0.0, PhaseType.AQUEOUS)
    _2_Pentanone_aq = Species("2-Pentanone(aq)", None, ["C", "H", "O"], 0.0861323, 0.0, PhaseType.AQUEOUS)
    A_Aminobutyric_aq = Species("A-Aminobutyric(aq)", None, ["C", "H", "O", "N"], 0.10311975999999999, 0.0,
                                PhaseType.AQUEOUS)
    Acetamide_aq = Species("Acetamide(aq)", None, ["C", "H", "O", "N"], 0.0590672, 0.0, PhaseType.AQUEOUS)
    Acetone_aq = Species("Acetone(aq)", None, ["C", "H", "O"], 0.05807914, 0.0, PhaseType.AQUEOUS)
    Adipate = Species("Adipate", None, ["C", "H", "O"], 0.14412532, -2.0, PhaseType.AQUEOUS)
    Adipic_Acid_aq = Species("Adipic-Acid(aq)", None, ["C", "H", "O"], 0.1461412, 0.0, PhaseType.AQUEOUS)
    Alanylglycine_aq = Species("Alanylglycine(aq)", None, ["C", "H", "N", "O"], 0.1461445, 0.0, PhaseType.AQUEOUS)
    Asparagine_aq = Species("Asparagine(aq)", None, ["C", "H", "O", "N"], 0.13211792, 0.0, PhaseType.AQUEOUS)
    Aspartic_Acid_aq = Species("Aspartic-Acid(aq)", None, ["C", "H", "O", "N"], 0.13310268, 0.0, PhaseType.AQUEOUS)
    Azelaic_Acid_aq = Species("Azelaic-Acid(aq)", None, ["C", "H", "O"], 0.18822094, 0.0, PhaseType.AQUEOUS)
    Azelate = Species("Azelate", None, ["C", "H", "O"], 0.18620505999999998, -2.0, PhaseType.AQUEOUS)
    Benzene_aq = Species("Benzene(aq)", None, ["C", "H"], 0.07811183999999999, 0.0, PhaseType.AQUEOUS)
    Benzoate = Species("Benzoate", None, ["C", "H", "O"], 0.12111339999999998, -1.0, PhaseType.AQUEOUS)
    Benzoic_Acid_aq = Species("Benzoic-Acid(aq)", None, ["C", "H", "O"], 0.12212134, 0.0, PhaseType.AQUEOUS)
    o_Cresol_aq = Species("o-Cresol(aq)", None, ["C", "H", "O"], 0.10813782, 0.0, PhaseType.AQUEOUS)
    m_Cresol_aq = Species("m-Cresol(aq)", None, ["C", "H", "O"], 0.10813782, 0.0, PhaseType.AQUEOUS)
    p_Cresol_aq = Species("p-Cresol(aq)", None, ["C", "H", "O"], 0.10813782, 0.0, PhaseType.AQUEOUS)
    Decanoate = Species("Decanoate", None, ["C", "H", "O"], 0.17125665999999998, -1.0, PhaseType.AQUEOUS)
    Decanoic_Acid_aq = Species("Decanoic-Acid(aq)", None, ["C", "H", "O"], 0.1722646, 0.0, PhaseType.AQUEOUS)
    _2_3_DMP_aq = Species("2,3-DMP(aq)", None, ["C", "H", "O"], 0.12216439999999999, 0.0, PhaseType.AQUEOUS)
    _2_4_DMP_aq = Species("2,4-DMP(aq)", None, ["C", "H", "O"], 0.12216439999999999, 0.0, PhaseType.AQUEOUS)
    _2_5_DMP_aq = Species("2,5-DMP(aq)", None, ["C", "H", "O"], 0.12216439999999999, 0.0, PhaseType.AQUEOUS)
    _2_6_DMP_aq = Species("2,6-DMP(aq)", None, ["C", "H", "O"], 0.12216439999999999, 0.0, PhaseType.AQUEOUS)
    _3_4_DMP_aq = Species("3,4-DMP(aq)", None, ["C", "H", "O"], 0.12216439999999999, 0.0, PhaseType.AQUEOUS)
    _3_5_DMP_aq = Species("3,5-DMP(aq)", None, ["C", "H", "O"], 0.12216439999999999, 0.0, PhaseType.AQUEOUS)
    Dodecanoate = Species("Dodecanoate", None, ["C", "H", "O"], 0.19930981999999997, -1.0, PhaseType.AQUEOUS)
    Dodecanoic_Acid_aq = Species("Dodecanoic-Acid(aq)", None, ["C", "H", "O"], 0.20031775999999998, 0.0,
                                 PhaseType.AQUEOUS)
    Ethanamine_aq = Species("Ethanamine(aq)", None, ["C", "H", "N"], 0.04508368, 0.0, PhaseType.AQUEOUS)
    Ethane_aq = Species("Ethane(aq)", None, ["C", "H"], 0.03006904, 0.0, PhaseType.AQUEOUS)
    Ethanol_aq = Species("Ethanol(aq)", None, ["C", "H", "O"], 0.04606844, 0.0, PhaseType.AQUEOUS)
    Ethylacetate_aq = Species("Ethylacetate(aq)", None, ["C", "H", "O"], 0.08810512, 0.0, PhaseType.AQUEOUS)
    Ethylbenzene_aq = Species("Ethylbenzene(aq)", None, ["C", "H"], 0.106165, 0.0, PhaseType.AQUEOUS)
    Ethylene_aq = Species("Ethylene(aq)", None, ["C", "H"], 0.028053159999999997, 0.0, PhaseType.AQUEOUS)
    Ethyne_aq = Species("Ethyne(aq)", None, ["C", "H"], 0.02603728, 0.0, PhaseType.AQUEOUS)
    Glutamic_Acid_aq = Species("Glutamic-Acid(aq)", None, ["C", "H", "O", "N"], 0.14712926, 0.0, PhaseType.AQUEOUS)
    Glutamine_aq = Species("Glutamine(aq)", None, ["C", "H", "O", "N"], 0.1461445, 0.0, PhaseType.AQUEOUS)
    Glutarate = Species("Glutarate", None, ["C", "H", "O"], 0.13009874, -2.0, PhaseType.AQUEOUS)
    Glutaric_Acid_aq = Species("Glutaric-Acid(aq)", None, ["C", "H", "O"], 0.13211462000000002, 0.0, PhaseType.AQUEOUS)
    Diglycine_aq = Species("Diglycine(aq)", None, ["C", "H", "N", "O"], 0.13211792, 0.0, PhaseType.AQUEOUS)
    H_Adipate = Species("H-Adipate", None, ["C", "H", "O"], 0.14513326, -1.0, PhaseType.AQUEOUS)
    H_Azelate = Species("H-Azelate", None, ["C", "H", "O"], 0.187213, -1.0, PhaseType.AQUEOUS)
    H_Glutarate = Species("H-Glutarate", None, ["C", "H", "O"], 0.13110668, -1.0, PhaseType.AQUEOUS)
    H_Malonate = Species("H-Malonate", None, ["C", "H", "O"], 0.10305352, -1.0, PhaseType.AQUEOUS)
    H_Oxalate = Species("H-Oxalate", None, ["C", "H", "O"], 0.08902694, -1.0, PhaseType.AQUEOUS)
    H_Pimelate = Species("H-Pimelate", None, ["C", "H", "O"], 0.15915984, -1.0, PhaseType.AQUEOUS)
    H_Sebacate = Species("H-Sebacate", None, ["C", "H", "O"], 0.20123957999999997, -1.0, PhaseType.AQUEOUS)
    H_Suberate = Species("H-Suberate", None, ["C", "H", "O"], 0.17318642, -1.0, PhaseType.AQUEOUS)
    H_Succinate = Species("H-Succinate", None, ["C", "H", "O"], 0.11708009999999999, -1.0, PhaseType.AQUEOUS)
    Heptanoate = Species("Heptanoate", None, ["C", "H", "O"], 0.12917692, -1.0, PhaseType.AQUEOUS)
    Heptanoic_Acid_aq = Species("Heptanoic-Acid(aq)", None, ["C", "H", "O"], 0.13018485999999999, 0.0,
                                PhaseType.AQUEOUS)
    Hexanoate = Species("Hexanoate", None, ["C", "H", "O"], 0.11515033999999999, -1.0, PhaseType.AQUEOUS)
    Hexanoic_Acid_aq = Species("Hexanoic-Acid(aq)", None, ["C", "H", "O"], 0.11615828, 0.0, PhaseType.AQUEOUS)
    Isoleucine_aq = Species("Isoleucine(aq)", None, ["C", "H", "O", "N"], 0.13117292, 0.0, PhaseType.AQUEOUS)
    Leucine_aq = Species("Leucine(aq)", None, ["C", "H", "O", "N"], 0.13117292, 0.0, PhaseType.AQUEOUS)
    m_Toluate = Species("m-Toluate", None, ["C", "H", "O"], 0.13513998, -1.0, PhaseType.AQUEOUS)
    m_Toluic_Acid_aq = Species("m-Toluic-Acid(aq)", None, ["C", "H", "O"], 0.13614792, 0.0, PhaseType.AQUEOUS)
    Malonate = Species("Malonate", None, ["C", "H", "O"], 0.10204558, -2.0, PhaseType.AQUEOUS)
    Malonic_Acid_aq = Species("Malonic-Acid(aq)", None, ["C", "H", "O"], 0.10406146, 0.0, PhaseType.AQUEOUS)
    Methanamine_aq = Species("Methanamine(aq)", None, ["C", "H", "N"], 0.0310571, 0.0, PhaseType.AQUEOUS)
    Methanol_aq = Species("Methanol(aq)", None, ["C", "H", "O"], 0.03204186, 0.0, PhaseType.AQUEOUS)
    Methionine_aq = Species("Methionine(aq)", None, ["C", "H", "O", "N", "S"], 0.14921134, 0.0, PhaseType.AQUEOUS)
    n_Butane_aq = Species("n-Butane(aq)", None, ["C", "H"], 0.0581222, 0.0, PhaseType.AQUEOUS)
    n_Butylbenzene_aq = Species("n-Butylbenzene(aq)", None, ["C", "H"], 0.13421816, 0.0, PhaseType.AQUEOUS)
    n_Heptane_aq = Species("n-Heptane(aq)", None, ["C", "H"], 0.10020193999999999, 0.0, PhaseType.AQUEOUS)
    n_Heptylbenzene_aq = Species("n-Heptylbenzene(aq)", None, ["C", "H"], 0.17629789999999998, 0.0, PhaseType.AQUEOUS)
    n_Hexane_aq = Species("n-Hexane(aq)", None, ["C", "H"], 0.08617535999999999, 0.0, PhaseType.AQUEOUS)
    n_Hexylbenzene_aq = Species("n-Hexylbenzene(aq)", None, ["C", "H"], 0.16227132, 0.0, PhaseType.AQUEOUS)
    n_Octane_aq = Species("n-Octane(aq)", None, ["C", "H"], 0.11422852, 0.0, PhaseType.AQUEOUS)
    n_Octylbenzene_aq = Species("n-Octylbenzene(aq)", None, ["C", "H"], 0.19032448, 0.0, PhaseType.AQUEOUS)
    n_Pentane_aq = Species("n-Pentane(aq)", None, ["C", "H"], 0.07214878, 0.0, PhaseType.AQUEOUS)
    n_Pentylbenzene_aq = Species("n-Pentylbenzene(aq)", None, ["C", "H"], 0.14824474, 0.0, PhaseType.AQUEOUS)
    n_Propylbenzene_aq = Species("n-Propylbenzene(aq)", None, ["C", "H"], 0.12019157999999999, 0.0, PhaseType.AQUEOUS)
    Nonanoate = Species("Nonanoate", None, ["C", "H", "O"], 0.15723008, -1.0, PhaseType.AQUEOUS)
    Nonanoic_Acid_aq = Species("Nonanoic-Acid(aq)", None, ["C", "H", "O"], 0.15823801999999998, 0.0, PhaseType.AQUEOUS)
    o_Toluate = Species("o-Toluate", None, ["C", "H", "O"], 0.13513998, -1.0, PhaseType.AQUEOUS)
    o_Toluic_Acid_aq = Species("o-Toluic-Acid(aq)", None, ["C", "H", "O"], 0.13614792, 0.0, PhaseType.AQUEOUS)
    Octanoate = Species("Octanoate", None, ["C", "H", "O"], 0.14320349999999998, -1.0, PhaseType.AQUEOUS)
    Octanoic_Acid_aq = Species("Octanoic-Acid(aq)", None, ["C", "H", "O"], 0.14421144, 0.0, PhaseType.AQUEOUS)
    Oxalate = Species("Oxalate", None, ["C", "O"], 0.088019, -2.0, PhaseType.AQUEOUS)
    Oxalic_Acid_aq = Species("Oxalic-Acid(aq)", None, ["C", "H", "O"], 0.09003488, 0.0, PhaseType.AQUEOUS)
    p_Toluate = Species("p-Toluate", None, ["C", "H", "O"], 0.13513998, -1.0, PhaseType.AQUEOUS)
    p_Toluic_Acid_aq = Species("p-Toluic-Acid(aq)", None, ["C", "H", "O"], 0.13614792, 0.0, PhaseType.AQUEOUS)
    Phenol_aq = Species("Phenol(aq)", None, ["C", "H", "O"], 0.09411123999999998, 0.0, PhaseType.AQUEOUS)
    Phenylalanine_aq = Species("Phenylalanine(aq)", None, ["C", "H", "O", "N"], 0.16518914, 0.0, PhaseType.AQUEOUS)
    Pimelate = Species("Pimelate", None, ["C", "H", "O"], 0.1581519, -2.0, PhaseType.AQUEOUS)
    Pimelic_Acid_aq = Species("Pimelic-Acid(aq)", None, ["C", "H", "O"], 0.16016777999999998, 0.0, PhaseType.AQUEOUS)
    Propane_aq = Species("Propane(aq)", None, ["C", "H"], 0.044095619999999995, 0.0, PhaseType.AQUEOUS)
    Sebacate = Species("Sebacate", None, ["C", "H", "O"], 0.20023164, -2.0, PhaseType.AQUEOUS)
    Sebacic_Acid_aq = Species("Sebacic-Acid(aq)", None, ["C", "H", "O"], 0.20224752000000001, 0.0, PhaseType.AQUEOUS)
    Serine_aq = Species("Serine(aq)", None, ["C", "H", "O", "N"], 0.10509258, 0.0, PhaseType.AQUEOUS)
    Suberate = Species("Suberate", None, ["C", "H", "O"], 0.17217848, -2.0, PhaseType.AQUEOUS)
    Suberic_Acid_aq = Species("Suberic-Acid(aq)", None, ["C", "H", "O"], 0.17419436, 0.0, PhaseType.AQUEOUS)
    Succinate = Species("Succinate", None, ["C", "H", "O"], 0.11607216000000001, -2.0, PhaseType.AQUEOUS)
    Succinic_Acid_aq = Species("Succinic-Acid(aq)", None, ["C", "H", "O"], 0.11808804, 0.0, PhaseType.AQUEOUS)
    Threonine_aq = Species("Threonine(aq)", None, ["C", "H", "O", "N"], 0.11911916, 0.0, PhaseType.AQUEOUS)
    Toluene_aq = Species("Toluene(aq)", None, ["C", "H"], 0.09213842, 0.0, PhaseType.AQUEOUS)
    Tryptophan_aq = Species("Tryptophan(aq)", None, ["C", "H", "O", "N"], 0.20422517999999998, 0.0, PhaseType.AQUEOUS)
    Tyrosine_aq = Species("Tyrosine(aq)", None, ["C", "H", "O", "N"], 0.18118854, 0.0, PhaseType.AQUEOUS)
    Undecanoate = Species("Undecanoate", None, ["C", "H", "O"], 0.18528324, -1.0, PhaseType.AQUEOUS)
    Undecanoic_Acid_aq = Species("Undecanoic-Acid(aq)", None, ["C", "H", "O"], 0.18629118, 0.0, PhaseType.AQUEOUS)
    Urea_aq = Species("Urea(aq)", None, ["H", "N", "C", "O"], 0.06005526, 0.0, PhaseType.AQUEOUS)
    Valine_aq = Species("Valine(aq)", None, ["C", "H", "O", "N"], 0.11714634, 0.0, PhaseType.AQUEOUS)
    Acetaldehyde_aq = Species("Acetaldehyde(aq)", None, ["C", "H", "O"], 0.04405256, 0.0, PhaseType.AQUEOUS)
    Butanal_aq = Species("Butanal(aq)", None, ["C", "H", "O"], 0.07210572, 0.0, PhaseType.AQUEOUS)
    Decanal_aq = Species("Decanal(aq)", None, ["C", "H", "O"], 0.1562652, 0.0, PhaseType.AQUEOUS)
    Formaldehyde_aq = Species("Formaldehyde(aq)", None, ["C", "H", "O"], 0.03002598, 0.0, PhaseType.AQUEOUS)
    Heptanal_aq = Species("Heptanal(aq)", None, ["C", "H", "O"], 0.11418545999999999, 0.0, PhaseType.AQUEOUS)
    Hexanal_aq = Species("Hexanal(aq)", None, ["C", "H", "O"], 0.10015887999999999, 0.0, PhaseType.AQUEOUS)
    Nonanal_aq = Species("Nonanal(aq)", None, ["C", "H", "O"], 0.14223861999999998, 0.0, PhaseType.AQUEOUS)
    Octanal_aq = Species("Octanal(aq)", None, ["C", "H", "O"], 0.12821204, 0.0, PhaseType.AQUEOUS)
    Pentanal_aq = Species("Pentanal(aq)", None, ["C", "H", "O"], 0.0861323, 0.0, PhaseType.AQUEOUS)
    Propanal_aq = Species("Propanal(aq)", None, ["C", "H", "O"], 0.05807914, 0.0, PhaseType.AQUEOUS)
    HCN_aq = Species("HCN(aq)", None, ["H", "C", "N"], 0.027025340000000002, 0.0, PhaseType.AQUEOUS)
    CN_minus = Species("CN-", None, ["C", "N"], 0.0260174, -1.0, PhaseType.AQUEOUS)
    OCN_minus = Species("OCN-", None, ["O", "C", "N"], 0.0420168, -1.0, PhaseType.AQUEOUS)
    SCN_minus = Species("SCN-", None, ["S", "C", "N"], 0.058082400000000006, -1.0, PhaseType.AQUEOUS)
    SeCN_minus = Species("SeCN-", None, ["Se", "C", "N"], 0.1049774, -1.0, PhaseType.AQUEOUS)
    Bi_Ac_plus2 = Species("Bi(Ac)+2", None, ["Bi", "C", "H", "O"], 0.2680244, 2.0, PhaseType.AQUEOUS)
    Bi_Ac_2_plus = Species("Bi(Ac)2+", None, ["Bi", "C", "H", "O"], 0.32706842, 1.0, PhaseType.AQUEOUS)
    Bi_Ac_3_aq = Species("Bi(Ac)3(aq)", None, ["Bi", "C", "H", "O"], 0.38611244, 0.0, PhaseType.AQUEOUS)
    Dy_Ac_plus2 = Species("Dy(Ac)+2", None, ["Dy", "C", "H", "O"], 0.22154402, 2.0, PhaseType.AQUEOUS)
    Dy_Ac_2_plus = Species("Dy(Ac)2+", None, ["Dy", "C", "H", "O"], 0.28058804, 1.0, PhaseType.AQUEOUS)
    Dy_Ac_3_aq = Species("Dy(Ac)3(aq)", None, ["Dy", "C", "H", "O"], 0.33963206, 0.0, PhaseType.AQUEOUS)
    Ho_Ac_plus2 = Species("Ho(Ac)+2", None, ["Ho", "C", "H", "O"], 0.22397434, 2.0, PhaseType.AQUEOUS)
    Ho_Ac_2_plus = Species("Ho(Ac)2+", None, ["Ho", "C", "H", "O"], 0.28301835999999997, 1.0, PhaseType.AQUEOUS)
    Ho_Ac_3_aq = Species("Ho(Ac)3(aq)", None, ["Ho", "C", "H", "O"], 0.34206238, 0.0, PhaseType.AQUEOUS)
    Er_Ac_plus2 = Species("Er(Ac)+2", None, ["Er", "C", "H", "O"], 0.22630302, 2.0, PhaseType.AQUEOUS)
    Er_Ac_2_plus = Species("Er(Ac)2+", None, ["Er", "C", "H", "O"], 0.28534704, 1.0, PhaseType.AQUEOUS)
    Er_Ac_3_aq = Species("Er(Ac)3(aq)", None, ["Er", "C", "H", "O"], 0.34439105999999997, 0.0, PhaseType.AQUEOUS)
    Tm_Ac_plus2 = Species("Tm(Ac)+2", None, ["Tm", "C", "H", "O"], 0.22797823, 2.0, PhaseType.AQUEOUS)
    Tm_Ac_2_plus = Species("Tm(Ac)2+", None, ["Tm", "C", "H", "O"], 0.28702225, 1.0, PhaseType.AQUEOUS)
    Tm_Ac_3_aq = Species("Tm(Ac)3(aq)", None, ["Tm", "C", "H", "O"], 0.34606627, 0.0, PhaseType.AQUEOUS)
    Be_Ac_plus = Species("Be(Ac)+", None, ["Be", "C", "H", "O"], 0.06805620200000001, 1.0, PhaseType.AQUEOUS)
    Be_Ac_2_aq = Species("Be(Ac)2(aq)", None, ["Be", "C", "H", "O"], 0.12710022199999998, 0.0, PhaseType.AQUEOUS)
    Ra_Ac_plus = Species("Ra(Ac)+", None, ["Ra", "C", "H", "O"], 0.28504402, 1.0, PhaseType.AQUEOUS)
    Ra_Ac_2_aq = Species("Ra(Ac)2(aq)", None, ["Ra", "C", "H", "O"], 0.34408804000000004, 0.0, PhaseType.AQUEOUS)
    Au_Ac_aq = Species("Au(Ac)(aq)", None, ["Au", "C", "H", "O"], 0.25601057, 0.0, PhaseType.AQUEOUS)
    Au_Ac_2_minus = Species("Au(Ac)2-", None, ["Au", "C", "H", "O"], 0.31505458999999997, -1.0, PhaseType.AQUEOUS)
    Li_Ac_aq = Species("Li(Ac)(aq)", None, ["Li", "C", "H", "O"], 0.06598502, 0.0, PhaseType.AQUEOUS)
    Li_Ac_2_minus = Species("Li(Ac)2-", None, ["Li", "C", "H", "O"], 0.12502904, -1.0, PhaseType.AQUEOUS)
    Na_Ac_aq = Species("Na(Ac)(aq)", None, ["Na", "C", "H", "O"], 0.08203379, 0.0, PhaseType.AQUEOUS)
    Na_Ac_2_minus = Species("Na(Ac)2-", None, ["Na", "C", "H", "O"], 0.14107780999999997, -1.0, PhaseType.AQUEOUS)
    K_Ac_aq = Species("K(Ac)(aq)", None, ["K", "C", "H", "O"], 0.09814232, 0.0, PhaseType.AQUEOUS)
    K_Ac_2_minus = Species("K(Ac)2-", None, ["K", "C", "H", "O"], 0.15718633999999998, -1.0, PhaseType.AQUEOUS)
    Mg_Ac_plus = Species("Mg(Ac)+", None, ["Mg", "C", "H", "O"], 0.08334902, 1.0, PhaseType.AQUEOUS)
    Mg_Ac_2_aq = Species("Mg(Ac)2(aq)", None, ["Mg", "C", "H", "O"], 0.14239303999999997, 0.0, PhaseType.AQUEOUS)
    Sr_Ac_plus = Species("Sr(Ac)+", None, ["Sr", "C", "H", "O"], 0.14666402, 1.0, PhaseType.AQUEOUS)
    Sr_Ac_2_aq = Species("Sr(Ac)2(aq)", None, ["Sr", "C", "H", "O"], 0.20570803999999998, 0.0, PhaseType.AQUEOUS)
    Ba_Ac_plus = Species("Ba(Ac)+", None, ["Ba", "C", "H", "O"], 0.19637102, 1.0, PhaseType.AQUEOUS)
    Ba_Ac_2_aq = Species("Ba(Ac)2(aq)", None, ["Ba", "C", "H", "O"], 0.25541504, 0.0, PhaseType.AQUEOUS)
    Cu_Ac_aq = Species("Cu(Ac)(aq)", None, ["Cu", "C", "H", "O"], 0.12259002, 0.0, PhaseType.AQUEOUS)
    Cu_Ac_2_minus = Species("Cu(Ac)2-", None, ["Cu", "C", "H", "O"], 0.18163404, -1.0, PhaseType.AQUEOUS)
    Rb_Ac_aq = Species("Rb(Ac)(aq)", None, ["Rb", "C", "H", "O"], 0.14451181999999999, 0.0, PhaseType.AQUEOUS)
    Rb_Ac_2_minus = Species("Rb(Ac)2-", None, ["Rb", "C", "H", "O"], 0.20355584, -1.0, PhaseType.AQUEOUS)
    Tl_Ac_aq = Species("Tl(Ac)(aq)", None, ["Tl", "C", "H", "O"], 0.26342732, 0.0, PhaseType.AQUEOUS)
    Tl_Ac_2_minus = Species("Tl(Ac)2-", None, ["Tl", "C", "H", "O"], 0.32247134, -1.0, PhaseType.AQUEOUS)
    Cs_Ac_aq = Species("Cs(Ac)(aq)", None, ["Cs", "C", "H", "O"], 0.19194947, 0.0, PhaseType.AQUEOUS)
    Cs_Ac_2_minus = Species("Cs(Ac)2-", None, ["Cs", "C", "H", "O"], 0.25099349, -1.0, PhaseType.AQUEOUS)
    Pb_Ac_plus = Species("Pb(Ac)+", None, ["Pb", "C", "H", "O"], 0.26624402, 1.0, PhaseType.AQUEOUS)
    Pb_Ac_2_aq = Species("Pb(Ac)2(aq)", None, ["Pb", "C", "H", "O"], 0.32528804, 0.0, PhaseType.AQUEOUS)
    Mn_Ac_plus = Species("Mn(Ac)+", None, ["Mn", "C", "H", "O"], 0.11398206999999999, 1.0, PhaseType.AQUEOUS)
    Mn_Ac_2_aq = Species("Mn(Ac)2(aq)", None, ["Mn", "C", "H", "O"], 0.17302609000000002, 0.0, PhaseType.AQUEOUS)
    Mn_Ac_3_minus = Species("Mn(Ac)3-", None, ["Mn", "C", "H", "O"], 0.23207011, -1.0, PhaseType.AQUEOUS)
    Co_Ac_plus = Species("Co(Ac)+", None, ["Co", "C", "H", "O"], 0.11797722, 1.0, PhaseType.AQUEOUS)
    Co_Ac_2_aq = Species("Co(Ac)2(aq)", None, ["Co", "C", "H", "O"], 0.17702123999999997, 0.0, PhaseType.AQUEOUS)
    Co_Ac_3_minus = Species("Co(Ac)3-", None, ["Co", "C", "H", "O"], 0.23606526, -1.0, PhaseType.AQUEOUS)
    Ni_Ac_plus = Species("Ni(Ac)+", None, ["Ni", "C", "H", "O"], 0.11773742000000001, 1.0, PhaseType.AQUEOUS)
    Ni_Ac_2_aq = Species("Ni(Ac)2(aq)", None, ["Ni", "C", "H", "O"], 0.17678144, 0.0, PhaseType.AQUEOUS)
    Ni_Ac_3_minus = Species("Ni(Ac)3-", None, ["Ni", "C", "H", "O"], 0.23582546000000001, -1.0, PhaseType.AQUEOUS)
    Cu_Ac_plus = Species("Cu(Ac)+", None, ["Cu", "C", "H", "O"], 0.12259002, 1.0, PhaseType.AQUEOUS)
    Cu_Ac_2_aq = Species("Cu(Ac)2(aq)", None, ["Cu", "C", "H", "O"], 0.18163404, 0.0, PhaseType.AQUEOUS)
    Cu_Ac_3_minus = Species("Cu(Ac)3-", None, ["Cu", "C", "H", "O"], 0.24067806000000003, -1.0, PhaseType.AQUEOUS)
    NH4_Ac_aq = Species("NH4(Ac)(aq)", None, ["N", "C", "H", "O"], 0.07708248, 0.0, PhaseType.AQUEOUS)
    NH4_Ac_2_minus = Species("NH4(Ac)2-", None, ["N", "C", "H", "O"], 0.13612649999999998, -1.0, PhaseType.AQUEOUS)
    UO2_Ac_plus = Species("UO2(Ac)+", None, ["U", "C", "H", "O"], 0.32907173, 1.0, PhaseType.AQUEOUS)
    UO2_Ac_2_aq = Species("UO2(Ac)2(aq)", None, ["U", "C", "H", "O"], 0.38811575, 0.0, PhaseType.AQUEOUS)
    UO2_Ac_3_minus = Species("UO2(Ac)3-", None, ["U", "C", "H", "O"], 0.44715976999999996, -1.0, PhaseType.AQUEOUS)
    Ag_Ac_aq = Species("Ag(Ac)(aq)", None, ["Ag", "C", "H", "O"], 0.16691222, 0.0, PhaseType.AQUEOUS)
    Ag_Ac_2_minus = Species("Ag(Ac)2-", None, ["Ag", "C", "H", "O"], 0.22595623999999997, -1.0, PhaseType.AQUEOUS)
    Cd_Ac_plus = Species("Cd(Ac)+", None, ["Cd", "C", "H", "O"], 0.17145502, 1.0, PhaseType.AQUEOUS)
    Cd_Ac_2_aq = Species("Cd(Ac)2(aq)", None, ["Cd", "C", "H", "O"], 0.23049904, 0.0, PhaseType.AQUEOUS)
    Cd_Ac_3_minus = Species("Cd(Ac)3-", None, ["Cd", "C", "H", "O"], 0.28954306, -1.0, PhaseType.AQUEOUS)
    Hg_Ac_plus = Species("Hg(Ac)+", None, ["Hg", "C", "H", "O"], 0.25963402, 1.0, PhaseType.AQUEOUS)
    Hg_Ac_2_aq = Species("Hg(Ac)2(aq)", None, ["Hg", "C", "H", "O"], 0.31867804, 0.0, PhaseType.AQUEOUS)
    Hg_Ac_3_minus = Species("Hg(Ac)3-", None, ["Hg", "C", "H", "O"], 0.37772205999999997, -1.0, PhaseType.AQUEOUS)
    Sc_Ac_plus2 = Species("Sc(Ac)+2", None, ["Sc", "C", "H", "O"], 0.10399992999999999, 2.0, PhaseType.AQUEOUS)
    Sc_Ac_2_plus = Species("Sc(Ac)2+", None, ["Sc", "C", "H", "O"], 0.16304395, 1.0, PhaseType.AQUEOUS)
    Sc_Ac_3_aq = Species("Sc(Ac)3(aq)", None, ["Sc", "C", "H", "O"], 0.22208797, 0.0, PhaseType.AQUEOUS)
    U_Ac_plus2 = Species("U(Ac)+2", None, ["U", "C", "H", "O"], 0.29707293, 2.0, PhaseType.AQUEOUS)
    U_Ac_2_plus = Species("U(Ac)2+", None, ["U", "C", "H", "O"], 0.35611695, 1.0, PhaseType.AQUEOUS)
    U_Ac_3_aq = Species("U(Ac)3(aq)", None, ["U", "C", "H", "O"], 0.41516096999999996, 0.0, PhaseType.AQUEOUS)
    Pr_Ac_plus2 = Species("Pr(Ac)+2", None, ["Pr", "C", "H", "O"], 0.19995167, 2.0, PhaseType.AQUEOUS)
    Pr_Ac_2_plus = Species("Pr(Ac)2+", None, ["Pr", "C", "H", "O"], 0.25899569, 1.0, PhaseType.AQUEOUS)
    Pr_Ac_3_aq = Species("Pr(Ac)3(aq)", None, ["Pr", "C", "H", "O"], 0.31803971, 0.0, PhaseType.AQUEOUS)
    La_Ac_plus2 = Species("La(Ac)+2", None, ["La", "C", "H", "O"], 0.19794952, 2.0, PhaseType.AQUEOUS)
    La_Ac_2_plus = Species("La(Ac)2+", None, ["La", "C", "H", "O"], 0.25699353999999996, 1.0, PhaseType.AQUEOUS)
    La_Ac_3_aq = Species("La(Ac)3(aq)", None, ["La", "C", "H", "O"], 0.31603756, 0.0, PhaseType.AQUEOUS)
    Nd_Ac_plus2 = Species("Nd(Ac)+2", None, ["Nd", "C", "H", "O"], 0.20328402, 2.0, PhaseType.AQUEOUS)
    Nd_Ac_2_plus = Species("Nd(Ac)2+", None, ["Nd", "C", "H", "O"], 0.26232804, 1.0, PhaseType.AQUEOUS)
    Nd_Ac_3_aq = Species("Nd(Ac)3(aq)", None, ["Nd", "C", "H", "O"], 0.32137206, 0.0, PhaseType.AQUEOUS)
    Ce_Ac_plus2 = Species("Ce(Ac)+2", None, ["Ce", "C", "H", "O"], 0.19916002, 2.0, PhaseType.AQUEOUS)
    Ce_Ac_2_plus = Species("Ce(Ac)2+", None, ["Ce", "C", "H", "O"], 0.25820403999999997, 1.0, PhaseType.AQUEOUS)
    Ce_Ac_3_aq = Species("Ce(Ac)3(aq)", None, ["Ce", "C", "H", "O"], 0.31724806, 0.0, PhaseType.AQUEOUS)
    Gd_Ac_plus2 = Species("Gd(Ac)+2", None, ["Gd", "C", "H", "O"], 0.21629402, 2.0, PhaseType.AQUEOUS)
    Gd_Ac_2_plus = Species("Gd(Ac)2+", None, ["Gd", "C", "H", "O"], 0.27533804, 1.0, PhaseType.AQUEOUS)
    Gd_Ac_3_aq = Species("Gd(Ac)3(aq)", None, ["Gd", "C", "H", "O"], 0.33438206000000004, 0.0, PhaseType.AQUEOUS)
    Sm_Ac_plus2 = Species("Sm(Ac)+2", None, ["Sm", "C", "H", "O"], 0.20940402, 2.0, PhaseType.AQUEOUS)
    Sm_Ac_2_plus = Species("Sm(Ac)2+", None, ["Sm", "C", "H", "O"], 0.26844804, 1.0, PhaseType.AQUEOUS)
    Sm_Ac_3_aq = Species("Sm(Ac)3(aq)", None, ["Sm", "C", "H", "O"], 0.32749206, 0.0, PhaseType.AQUEOUS)
    Yb_Ac_plus2 = Species("Yb(Ac)+2", None, ["Yb", "C", "H", "O"], 0.23208402, 2.0, PhaseType.AQUEOUS)
    Yb_Ac_2_plus = Species("Yb(Ac)2+", None, ["Yb", "C", "H", "O"], 0.29112804, 1.0, PhaseType.AQUEOUS)
    Yb_Ac_3_aq = Species("Yb(Ac)3(aq)", None, ["Yb", "C", "H", "O"], 0.35017206, 0.0, PhaseType.AQUEOUS)
    Eu_Ac_plus2 = Species("Eu(Ac)+2", None, ["Eu", "C", "H", "O"], 0.21100802, 2.0, PhaseType.AQUEOUS)
    Eu_Ac_2_plus = Species("Eu(Ac)2+", None, ["Eu", "C", "H", "O"], 0.27005204, 1.0, PhaseType.AQUEOUS)
    Eu_Ac_3_aq = Species("Eu(Ac)3(aq)", None, ["Eu", "C", "H", "O"], 0.32909606, 0.0, PhaseType.AQUEOUS)
    Y_Ac_plus2 = Species("Y(Ac)+2", None, ["Y", "C", "H", "O"], 0.14794986999999998, 2.0, PhaseType.AQUEOUS)
    Y_Ac_2_plus = Species("Y(Ac)2+", None, ["Y", "C", "H", "O"], 0.20699389, 1.0, PhaseType.AQUEOUS)
    Y_Ac_3_aq = Species("Y(Ac)3(aq)", None, ["Y", "C", "H", "O"], 0.26603791, 0.0, PhaseType.AQUEOUS)
    Lu_Ac_plus2 = Species("Lu(Ac)+2", None, ["Lu", "C", "H", "O"], 0.23401102000000001, 2.0, PhaseType.AQUEOUS)
    Lu_Ac_2_plus = Species("Lu(Ac)2+", None, ["Lu", "C", "H", "O"], 0.29305504, 1.0, PhaseType.AQUEOUS)
    Lu_Ac_3_aq = Species("Lu(Ac)3(aq)", None, ["Lu", "C", "H", "O"], 0.35209906, 0.0, PhaseType.AQUEOUS)
    Tb_Ac_plus2 = Species("Tb(Ac)+2", None, ["Tb", "C", "H", "O"], 0.21796936, 2.0, PhaseType.AQUEOUS)
    Tb_Ac_2_plus = Species("Tb(Ac)2+", None, ["Tb", "C", "H", "O"], 0.27701338, 1.0, PhaseType.AQUEOUS)
    Tb_Ac_3_aq = Species("Tb(Ac)3(aq)", None, ["Tb", "C", "H", "O"], 0.3360574, 0.0, PhaseType.AQUEOUS)
    Pb_Ac_3_minus = Species("Pb(Ac)3-", None, ["Pb", "C", "H", "O"], 0.38433206, -1.0, PhaseType.AQUEOUS)
    Fe_Ac_plus = Species("Fe(Ac)+", None, ["Fe", "C", "H", "O"], 0.11488902000000001, 1.0, PhaseType.AQUEOUS)
    Fe_Ac_2_aq = Species("Fe(Ac)2(aq)", None, ["Fe", "C", "H", "O"], 0.17393303999999998, 0.0, PhaseType.AQUEOUS)
    Zn_Ac_plus = Species("Zn(Ac)+", None, ["Zn", "C", "H", "O"], 0.12445302, 1.0, PhaseType.AQUEOUS)
    Zn_Ac_2_aq = Species("Zn(Ac)2(aq)", None, ["Zn", "C", "H", "O"], 0.18349704, 0.0, PhaseType.AQUEOUS)
    Zn_Ac_3_minus = Species("Zn(Ac)3-", None, ["Zn", "C", "H", "O"], 0.24254106, -1.0, PhaseType.AQUEOUS)
    Ca_Ac_plus = Species("Ca(Ac)+", None, ["Ca", "C", "H", "O"], 0.09912202, 1.0, PhaseType.AQUEOUS)
    Ca_Ac_2_aq = Species("Ca(Ac)2(aq)", None, ["Ca", "C", "H", "O"], 0.15816604, 0.0, PhaseType.AQUEOUS)
    Al_Ac_plus2 = Species("Al(Ac)+2", None, ["Al", "C", "H", "O"], 0.086025558, 2.0, PhaseType.AQUEOUS)
    Al_Ac_2_plus = Species("Al(Ac)2+", None, ["Al", "C", "H", "O"], 0.14506957799999998, 1.0, PhaseType.AQUEOUS)
    Al_Ac_3_aq = Species("Al(Ac)3(aq)", None, ["Al", "C", "H", "O"], 0.204113598, 0.0, PhaseType.AQUEOUS)
    Lactate = Species("Lactate", None, ["C", "H", "O"], 0.08907000000000001, -1.0, PhaseType.AQUEOUS)
    Lactic_Acid_aq = Species("Lactic-Acid(aq)", None, ["C", "H", "O"], 0.09007794, 0.0, PhaseType.AQUEOUS)
    Li_Lac_aq = Species("Li(Lac)(aq)", None, ["Li", "C", "H", "O"], 0.09601100000000001, 0.0, PhaseType.AQUEOUS)
    Mg_Lac_plus = Species("Mg(Lac)+", None, ["Mg", "C", "H", "O"], 0.113375, 1.0, PhaseType.AQUEOUS)
    Mg_Lac_2_aq = Species("Mg(Lac)2(aq)", None, ["Mg", "C", "H", "O"], 0.20244499999999999, 0.0, PhaseType.AQUEOUS)
    Ca_Lac_plus = Species("Ca(Lac)+", None, ["Ca", "C", "H", "O"], 0.12914799999999999, 1.0, PhaseType.AQUEOUS)
    Ca_Lac_2_aq = Species("Ca(Lac)2(aq)", None, ["Ca", "C", "H", "O"], 0.21821800000000002, 0.0, PhaseType.AQUEOUS)
    Sr_Lac_plus = Species("Sr(Lac)+", None, ["Sr", "C", "H", "O"], 0.17669, 1.0, PhaseType.AQUEOUS)
    Sr_Lac_2_aq = Species("Sr(Lac)2(aq)", None, ["Sr", "C", "H", "O"], 0.26576, 0.0, PhaseType.AQUEOUS)
    Ba_Lac_plus = Species("Ba(Lac)+", None, ["Ba", "C", "H", "O"], 0.22639700000000001, 1.0, PhaseType.AQUEOUS)
    Ba_Lac_2_aq = Species("Ba(Lac)2(aq)", None, ["Ba", "C", "H", "O"], 0.315467, 0.0, PhaseType.AQUEOUS)
    Mn_Lac_plus = Species("Mn(Lac)+", None, ["Mn", "C", "H", "O"], 0.14400805, 1.0, PhaseType.AQUEOUS)
    Mn_Lac_2_aq = Species("Mn(Lac)2(aq)", None, ["Mn", "C", "H", "O"], 0.23307804999999998, 0.0, PhaseType.AQUEOUS)
    Co_Lac_plus = Species("Co(Lac)+", None, ["Co", "C", "H", "O"], 0.1480032, 1.0, PhaseType.AQUEOUS)
    Co_Lac_2_aq = Species("Co(Lac)2(aq)", None, ["Co", "C", "H", "O"], 0.23707319999999998, 0.0, PhaseType.AQUEOUS)
    Ni_Lac_plus = Species("Ni(Lac)+", None, ["Ni", "C", "H", "O"], 0.1477634, 1.0, PhaseType.AQUEOUS)
    Ni_Lac_2_aq = Species("Ni(Lac)2(aq)", None, ["Ni", "C", "H", "O"], 0.2368334, 0.0, PhaseType.AQUEOUS)
    Cu_Lac_plus = Species("Cu(Lac)+", None, ["Cu", "C", "H", "O"], 0.152616, 1.0, PhaseType.AQUEOUS)
    Cu_Lac_2_aq = Species("Cu(Lac)2(aq)", None, ["Cu", "C", "H", "O"], 0.241686, 0.0, PhaseType.AQUEOUS)
    Zn_Lac_plus = Species("Zn(Lac)+", None, ["Zn", "C", "H", "O"], 0.15447899999999998, 1.0, PhaseType.AQUEOUS)
    Zn_Lac_2_aq = Species("Zn(Lac)2(aq)", None, ["Zn", "C", "H", "O"], 0.243549, 0.0, PhaseType.AQUEOUS)
    Cd_Lac_plus = Species("Cd(Lac)+", None, ["Cd", "C", "H", "O"], 0.20148100000000002, 1.0, PhaseType.AQUEOUS)
    Cd_Lac_2_aq = Species("Cd(Lac)2(aq)", None, ["Cd", "C", "H", "O"], 0.290551, 0.0, PhaseType.AQUEOUS)
    La_Lac_plus2 = Species("La(Lac)+2", None, ["La", "C", "H", "O"], 0.2279755, 2.0, PhaseType.AQUEOUS)
    Lu_Lac_plus2 = Species("Lu(Lac)+2", None, ["Lu", "C", "H", "O"], 0.264037, 2.0, PhaseType.AQUEOUS)
    Na_Lac_aq = Species("Na(Lac)(aq)", None, ["Na", "C", "H", "O"], 0.11205977, 0.0, PhaseType.AQUEOUS)
    Na_Lac_2_minus = Species("Na(Lac)2-", None, ["Na", "C", "H", "O"], 0.20112976999999999, -1.0, PhaseType.AQUEOUS)
    K_Lac_aq = Species("K(Lac)(aq)", None, ["K", "C", "H", "O"], 0.1281683, 0.0, PhaseType.AQUEOUS)
    K_Lac_2_minus = Species("K(Lac)2-", None, ["K", "C", "H", "O"], 0.2172383, -1.0, PhaseType.AQUEOUS)
    Pb_Lac_plus = Species("Pb(Lac)+", None, ["Pb", "C", "H", "O"], 0.29627000000000003, 1.0, PhaseType.AQUEOUS)
    Pb_Lac_2_aq = Species("Pb(Lac)2(aq)", None, ["Pb", "C", "H", "O"], 0.38534, 0.0, PhaseType.AQUEOUS)
    Fe_Lac_plus = Species("Fe(Lac)+", None, ["Fe", "C", "H", "O"], 0.144915, 1.0, PhaseType.AQUEOUS)
    Fe_Lac_2_aq = Species("Fe(Lac)2(aq)", None, ["Fe", "C", "H", "O"], 0.233985, 0.0, PhaseType.AQUEOUS)
    Eu_Lac_plus = Species("Eu(Lac)+", None, ["Eu", "C", "H", "O"], 0.24103400000000003, 1.0, PhaseType.AQUEOUS)
    Eu_Lac_2_aq = Species("Eu(Lac)2(aq)", None, ["Eu", "C", "H", "O"], 0.33010399999999995, 0.0, PhaseType.AQUEOUS)
    Glycolic_Acid_aq = Species("Glycolic-Acid(aq)", None, ["C", "H", "O"], 0.07605136, 0.0, PhaseType.AQUEOUS)
    Glycolate = Species("Glycolate", None, ["C", "H", "O"], 0.07504342, -1.0, PhaseType.AQUEOUS)
    Li_Glyc_aq = Species("Li(Glyc)(aq)", None, ["Li", "C", "H", "O"], 0.08198442, 0.0, PhaseType.AQUEOUS)
    Mg_Glyc_plus = Species("Mg(Glyc)+", None, ["Mg", "C", "H", "O"], 0.09934842, 1.0, PhaseType.AQUEOUS)
    Mg_Glyc_2_aq = Species("Mg(Glyc)2(aq)", None, ["Mg", "C", "H", "O"], 0.17439184, 0.0, PhaseType.AQUEOUS)
    Ca_Glyc_plus = Species("Ca(Glyc)+", None, ["Ca", "C", "H", "O"], 0.11512142, 1.0, PhaseType.AQUEOUS)
    Ca_Glyc_2_aq = Species("Ca(Glyc)2(aq)", None, ["Ca", "C", "H", "O"], 0.19016484, 0.0, PhaseType.AQUEOUS)
    Sr_Glyc_plus = Species("Sr(Glyc)+", None, ["Sr", "C", "H", "O"], 0.16266342, 1.0, PhaseType.AQUEOUS)
    Sr_Glyc_2_aq = Species("Sr(Glyc)2(aq)", None, ["Sr", "C", "H", "O"], 0.23770684, 0.0, PhaseType.AQUEOUS)
    Ba_Glyc_plus = Species("Ba(Glyc)+", None, ["Ba", "C", "H", "O"], 0.21237042, 1.0, PhaseType.AQUEOUS)
    Ba_Glyc_2_aq = Species("Ba(Glyc)2(aq)", None, ["Ba", "C", "H", "O"], 0.28741384000000003, 0.0, PhaseType.AQUEOUS)
    Mn_Glyc_plus = Species("Mn(Glyc)+", None, ["Mn", "C", "H", "O"], 0.12998147, 1.0, PhaseType.AQUEOUS)
    Mn_Glyc_2_aq = Species("Mn(Glyc)2(aq)", None, ["Mn", "C", "H", "O"], 0.20502489000000002, 0.0, PhaseType.AQUEOUS)
    Co_Glyc_plus = Species("Co(Glyc)+", None, ["Co", "C", "H", "O"], 0.13397662, 1.0, PhaseType.AQUEOUS)
    Co_Glyc_2_aq = Species("Co(Glyc)2(aq)", None, ["Co", "C", "H", "O"], 0.20902004, 0.0, PhaseType.AQUEOUS)
    Ni_Glyc_plus = Species("Ni(Glyc)+", None, ["Ni", "C", "H", "O"], 0.13373682, 1.0, PhaseType.AQUEOUS)
    Ni_Glyc_2_aq = Species("Ni(Glyc)2(aq)", None, ["Ni", "C", "H", "O"], 0.20878024, 0.0, PhaseType.AQUEOUS)
    Cu_Glyc_plus = Species("Cu(Glyc)+", None, ["Cu", "C", "H", "O"], 0.13858942000000002, 1.0, PhaseType.AQUEOUS)
    Cu_Glyc_2_aq = Species("Cu(Glyc)2(aq)", None, ["Cu", "C", "H", "O"], 0.21363284000000002, 0.0, PhaseType.AQUEOUS)
    Zn_Glyc_plus = Species("Zn(Glyc)+", None, ["Zn", "C", "H", "O"], 0.14045242, 1.0, PhaseType.AQUEOUS)
    Zn_Glyc_2_aq = Species("Zn(Glyc)2(aq)", None, ["Zn", "C", "H", "O"], 0.21549584, 0.0, PhaseType.AQUEOUS)
    Cd_Glyc_plus = Species("Cd(Glyc)+", None, ["Cd", "C", "H", "O"], 0.18745442, 1.0, PhaseType.AQUEOUS)
    Cd_Glyc_2_aq = Species("Cd(Glyc)2(aq)", None, ["Cd", "C", "H", "O"], 0.26249784, 0.0, PhaseType.AQUEOUS)
    Eu_Glyc_plus = Species("Eu(Glyc)+", None, ["Eu", "C", "H", "O"], 0.22700742000000002, 1.0, PhaseType.AQUEOUS)
    Eu_Glyc_2_aq = Species("Eu(Glyc)2(aq)", None, ["Eu", "C", "H", "O"], 0.30205084, 0.0, PhaseType.AQUEOUS)
    Na_Glyc_aq = Species("Na(Glyc)(aq)", None, ["Na", "C", "H", "O"], 0.09803319, 0.0, PhaseType.AQUEOUS)
    Na_Glyc_2_minus = Species("Na(Glyc)2-", None, ["Na", "C", "H", "O"], 0.17307661, -1.0, PhaseType.AQUEOUS)
    K_Glyc_aq = Species("K(Glyc)(aq)", None, ["K", "C", "H", "O"], 0.11414172, 0.0, PhaseType.AQUEOUS)
    K_Glyc_2_minus = Species("K(Glyc)2-", None, ["K", "C", "H", "O"], 0.18918514, -1.0, PhaseType.AQUEOUS)
    Pb_Glyc_plus = Species("Pb(Glyc)+", None, ["Pb", "C", "H", "O"], 0.28224342, 1.0, PhaseType.AQUEOUS)
    Pb_Glyc_2_aq = Species("Pb(Glyc)2(aq)", None, ["Pb", "C", "H", "O"], 0.35728684, 0.0, PhaseType.AQUEOUS)
    Fe_Glyc_plus = Species("Fe(Glyc)+", None, ["Fe", "C", "H", "O"], 0.13088842, 1.0, PhaseType.AQUEOUS)
    Fe_Glyc_2_aq = Species("Fe(Glyc)2(aq)", None, ["Fe", "C", "H", "O"], 0.20593184, 0.0, PhaseType.AQUEOUS)
    Alanine_aq = Species("Alanine(aq)", None, ["C", "H", "O", "N"], 0.08909318, 0.0, PhaseType.AQUEOUS)
    Alanate = Species("Alanate", None, ["C", "H", "O", "N"], 0.08808524, -1.0, PhaseType.AQUEOUS)
    Cd_Alan_plus = Species("Cd(Alan)+", None, ["Cd", "C", "H", "O", "N"], 0.20049624, 1.0, PhaseType.AQUEOUS)
    Cd_Alan_2_aq = Species("Cd(Alan)2(aq)", None, ["Cd", "C", "H", "N", "O"], 0.28858148, 0.0, PhaseType.AQUEOUS)
    Ca_Alan_plus = Species("Ca(Alan)+", None, ["Ca", "C", "H", "O", "N"], 0.12816324, 1.0, PhaseType.AQUEOUS)
    Ca_Alan_2_aq = Species("Ca(Alan)2(aq)", None, ["Ca", "C", "H", "N", "O"], 0.21624848000000002, 0.0,
                           PhaseType.AQUEOUS)
    Pb_Alan_plus = Species("Pb(Alan)+", None, ["Pb", "C", "H", "O", "N"], 0.29528524, 1.0, PhaseType.AQUEOUS)
    Pb_Alan_2_aq = Species("Pb(Alan)2(aq)", None, ["Pb", "C", "H", "N", "O"], 0.38337047999999996, 0.0,
                           PhaseType.AQUEOUS)
    Mg_Alan_plus = Species("Mg(Alan)+", None, ["Mg", "C", "H", "N", "O"], 0.11239024, 1.0, PhaseType.AQUEOUS)
    Mg_Alan_2_aq = Species("Mg(Alan)2(aq)", None, ["Mg", "C", "H", "N", "O"], 0.20047547999999998, 0.0,
                           PhaseType.AQUEOUS)
    Sr_Alan_plus = Species("Sr(Alan)+", None, ["Sr", "C", "H", "N", "O"], 0.17570524, 1.0, PhaseType.AQUEOUS)
    Sr_Alan_2_aq = Species("Sr(Alan)2(aq)", None, ["Sr", "C", "H", "N", "O"], 0.26379048, 0.0, PhaseType.AQUEOUS)
    Mn_Alan_plus = Species("Mn(Alan)+", None, ["Mn", "C", "H", "N", "O"], 0.14302329, 1.0, PhaseType.AQUEOUS)
    Mn_Alan_2_aq = Species("Mn(Alan)2(aq)", None, ["Mn", "C", "H", "N", "O"], 0.23110852999999998, 0.0,
                           PhaseType.AQUEOUS)
    Co_Alan_plus = Species("Co(Alan)+", None, ["Co", "C", "H", "N", "O"], 0.14701844, 1.0, PhaseType.AQUEOUS)
    Co_Alan_2_aq = Species("Co(Alan)2(aq)", None, ["Co", "C", "H", "N", "O"], 0.23510367999999998, 0.0,
                           PhaseType.AQUEOUS)
    Ni_Alan_plus = Species("Ni(Alan)+", None, ["Ni", "C", "H", "N", "O"], 0.14677864, 1.0, PhaseType.AQUEOUS)
    Ni_Alan_2_aq = Species("Ni(Alan)2(aq)", None, ["Ni", "C", "H", "N", "O"], 0.23486388000000002, 0.0,
                           PhaseType.AQUEOUS)
    Cu_Alan_plus = Species("Cu(Alan)+", None, ["Cu", "C", "H", "N", "O"], 0.15163124, 1.0, PhaseType.AQUEOUS)
    Cu_Alan_2_aq = Species("Cu(Alan)2(aq)", None, ["Cu", "C", "H", "N", "O"], 0.23971648, 0.0, PhaseType.AQUEOUS)
    Zn_Alan_plus = Species("Zn(Alan)+", None, ["Zn", "C", "H", "N", "O"], 0.15349424, 1.0, PhaseType.AQUEOUS)
    Zn_Alan_2_aq = Species("Zn(Alan)2(aq)", None, ["Zn", "C", "H", "N", "O"], 0.27357828, 0.0, PhaseType.AQUEOUS)
    Ba_Alan_plus = Species("Ba(Alan)+", None, ["Ba", "C", "H", "N", "O"], 0.22541223999999999, 1.0, PhaseType.AQUEOUS)
    Ba_Alan_2_aq = Species("Ba(Alan)2(aq)", None, ["Ba", "C", "H", "N", "O"], 0.31349748, 0.0, PhaseType.AQUEOUS)
    Fe_Alan_plus = Species("Fe(Alan)+", None, ["Fe", "C", "H", "N", "O"], 0.14393024, 1.0, PhaseType.AQUEOUS)
    Fe_Alan_2_aq = Species("Fe(Alan)2(aq)", None, ["Fe", "C", "H", "N", "O"], 0.23201548, 0.0, PhaseType.AQUEOUS)
    Eu_Alan_plus = Species("Eu(Alan)+", None, ["Eu", "C", "H", "N", "O"], 0.24004924, 1.0, PhaseType.AQUEOUS)
    Eu_Alan_2_aq = Species("Eu(Alan)2(aq)", None, ["Eu", "C", "H", "N", "O"], 0.32813448, 0.0, PhaseType.AQUEOUS)
    Glycine_aq = Species("Glycine(aq)", None, ["C", "H", "O", "N"], 0.0750666, 0.0, PhaseType.AQUEOUS)
    Glycinate = Species("Glycinate", None, ["C", "H", "O", "N"], 0.07405866, -1.0, PhaseType.AQUEOUS)
    Cd_Gly_plus = Species("Cd(Gly)+", None, ["Cd", "C", "H", "O", "N"], 0.18646966, 1.0, PhaseType.AQUEOUS)
    Cd_Gly_2_aq = Species("Cd(Gly)2(aq)", None, ["Cd", "C", "H", "N", "O"], 0.26052832, 0.0, PhaseType.AQUEOUS)
    Ca_Gly_plus = Species("Ca(Gly)+", None, ["Ca", "C", "H", "O", "N"], 0.11413665999999999, 1.0, PhaseType.AQUEOUS)
    Ca_Gly_2_aq = Species("Ca(Gly)2(aq)", None, ["Ca", "C", "H", "N", "O"], 0.18819532, 0.0, PhaseType.AQUEOUS)
    Sr_Gly_plus = Species("Sr(Gly)+", None, ["Sr", "C", "H", "N", "O"], 0.16167866, 1.0, PhaseType.AQUEOUS)
    Sr_Gly_2_aq = Species("Sr(Gly)2(aq)", None, ["Sr", "C", "H", "N", "O"], 0.23573731999999997, 0.0, PhaseType.AQUEOUS)
    Mn_Gly_plus = Species("Mn(Gly)+", None, ["Mn", "C", "H", "N", "O"], 0.12899671, 1.0, PhaseType.AQUEOUS)
    Mn_Gly_2_aq = Species("Mn(Gly)2(aq)", None, ["Mn", "C", "H", "N", "O"], 0.20305537, 0.0, PhaseType.AQUEOUS)
    Fe_Gly_plus = Species("Fe(Gly)+", None, ["Fe", "C", "H", "N", "O"], 0.12990366, 1.0, PhaseType.AQUEOUS)
    Fe_Gly_2_aq = Species("Fe(Gly)2(aq)", None, ["Fe", "C", "H", "N", "O"], 0.20396232000000003, 0.0, PhaseType.AQUEOUS)
    Co_Gly_plus = Species("Co(Gly)+", None, ["Co", "C", "H", "N", "O"], 0.13299186, 1.0, PhaseType.AQUEOUS)
    Co_Gly_2_aq = Species("Co(Gly)2(aq)", None, ["Co", "C", "H", "N", "O"], 0.20705052000000002, 0.0, PhaseType.AQUEOUS)
    Pb_Gly_plus = Species("Pb(Gly)+", None, ["Pb", "C", "H", "O", "N"], 0.28125866, 1.0, PhaseType.AQUEOUS)
    Pb_Gly_2_aq = Species("Pb(Gly)2(aq)", None, ["Pb", "C", "H", "N", "O"], 0.35531732, 0.0, PhaseType.AQUEOUS)
    Mg_Gly_plus = Species("Mg(Gly)+", None, ["Mg", "C", "H", "N", "O"], 0.09836365999999999, 1.0, PhaseType.AQUEOUS)
    Mg_Gly_2_aq = Species("Mg(Gly)2(aq)", None, ["Mg", "C", "H", "N", "O"], 0.17242232000000002, 0.0, PhaseType.AQUEOUS)
    Ni_Gly_plus = Species("Ni(Gly)+", None, ["Ni", "C", "H", "N", "O"], 0.13275206, 1.0, PhaseType.AQUEOUS)
    Ni_Gly_2_aq = Species("Ni(Gly)2(aq)", None, ["Ni", "C", "H", "N", "O"], 0.20681072, 0.0, PhaseType.AQUEOUS)
    Cu_Gly_plus = Species("Cu(Gly)+", None, ["Cu", "C", "H", "N", "O"], 0.13760466, 1.0, PhaseType.AQUEOUS)
    Cu_Gly_2_aq = Species("Cu(Gly)2(aq)", None, ["Cu", "C", "H", "N", "O"], 0.21166332, 0.0, PhaseType.AQUEOUS)
    Zn_Gly_plus = Species("Zn(Gly)+", None, ["Zn", "C", "H", "N", "O"], 0.13946766, 1.0, PhaseType.AQUEOUS)
    Zn_Gly_2_aq = Species("Zn(Gly)2(aq)", None, ["Zn", "C", "H", "N", "O"], 0.21352632, 0.0, PhaseType.AQUEOUS)
    Eu_Gly_plus = Species("Eu(Gly)+", None, ["Eu", "C", "H", "N", "O"], 0.22602266, 1.0, PhaseType.AQUEOUS)
    Eu_Gly_2_aq = Species("Eu(Gly)2(aq)", None, ["Eu", "C", "H", "N", "O"], 0.30008132, 0.0, PhaseType.AQUEOUS)
    Ba_Gly_plus = Species("Ba(Gly)+", None, ["Ba", "C", "H", "N", "O"], 0.21138566, 1.0, PhaseType.AQUEOUS)
    Ba_Gly_2_aq = Species("Ba(Gly)2(aq)", None, ["Ba", "C", "H", "N", "O"], 0.28544432, 0.0, PhaseType.AQUEOUS)
    Formic_Acid_aq = Species("Formic-Acid(aq)", None, ["C", "H", "O"], 0.04602538, 0.0, PhaseType.AQUEOUS)
    Formate = Species("Formate", None, ["H", "C", "O"], 0.04501744, -1.0, PhaseType.AQUEOUS)
    Mg_For_plus = Species("Mg(For)+", None, ["Mg", "C", "H", "O"], 0.06932244, 1.0, PhaseType.AQUEOUS)
    Mg_For_2_aq = Species("Mg(For)2(aq)", None, ["Mg", "C", "H", "O"], 0.11433988, 0.0, PhaseType.AQUEOUS)
    Ca_For_plus = Species("Ca(For)+", None, ["Ca", "C", "H", "O"], 0.08509544, 1.0, PhaseType.AQUEOUS)
    Ca_For_2_aq = Species("Ca(For)2(aq)", None, ["Ca", "C", "H", "O"], 0.13011288, 0.0, PhaseType.AQUEOUS)
    Sr_For_plus = Species("Sr(For)+", None, ["Sr", "C", "H", "O"], 0.13263744, 1.0, PhaseType.AQUEOUS)
    Sr_For_2_aq = Species("Sr(For)2(aq)", None, ["Sr", "C", "H", "O"], 0.17765488000000002, 0.0, PhaseType.AQUEOUS)
    Ba_For_plus = Species("Ba(For)+", None, ["Ba", "C", "H", "O"], 0.18234444000000002, 1.0, PhaseType.AQUEOUS)
    Ba_For_2_aq = Species("Ba(For)2(aq)", None, ["Ba", "C", "H", "O"], 0.22736188000000002, 0.0, PhaseType.AQUEOUS)
    Cu_For_plus = Species("Cu(For)+", None, ["Cu", "C", "H", "O"], 0.10856344000000001, 1.0, PhaseType.AQUEOUS)
    Cu_For_2_aq = Species("Cu(For)2(aq)", None, ["Cu", "C", "H", "O"], 0.15358088, 0.0, PhaseType.AQUEOUS)
    Cd_For_plus = Species("Cd(For)+", None, ["Cd", "C", "H", "O"], 0.15742844, 1.0, PhaseType.AQUEOUS)
    Cd_For_2_aq = Species("Cd(For)2(aq)", None, ["Cd", "C", "H", "O"], 0.20244588000000002, 0.0, PhaseType.AQUEOUS)
    Na_For_aq = Species("Na(For)(aq)", None, ["Na", "C", "H", "O"], 0.06800721, 0.0, PhaseType.AQUEOUS)
    Na_For_2_minus = Species("Na(For)2-", None, ["Na", "C", "H", "O"], 0.11302465, -1.0, PhaseType.AQUEOUS)
    K_For_aq = Species("K(For)(aq)", None, ["K", "C", "H", "O"], 0.08411574, 0.0, PhaseType.AQUEOUS)
    K_For_2_minus = Species("K(For)2-", None, ["K", "C", "H", "O"], 0.12913318000000001, -1.0, PhaseType.AQUEOUS)
    La_For_plus2 = Species("La(For)+2", None, ["La", "C", "H", "O"], 0.18392294, 2.0, PhaseType.AQUEOUS)
    La_For_2_plus = Species("La(For)2+", None, ["La", "C", "H", "O"], 0.22894038, 1.0, PhaseType.AQUEOUS)
    Eu_For_plus = Species("Eu(For)+", None, ["Eu", "C", "H", "O"], 0.19698143999999998, 1.0, PhaseType.AQUEOUS)
    Eu_For_2_aq = Species("Eu(For)2(aq)", None, ["Eu", "C", "H", "O"], 0.24199887999999997, 0.0, PhaseType.AQUEOUS)
    U_For_plus2 = Species("U(For)+2", None, ["U", "C", "H", "O"], 0.28304635, 2.0, PhaseType.AQUEOUS)
    U_For_2_plus = Species("U(For)2+", None, ["U", "C", "H", "O"], 0.32806379, 1.0, PhaseType.AQUEOUS)
    Eu_For_plus2 = Species("Eu(For)+2", None, ["Eu", "C", "H", "O"], 0.19698143999999998, 2.0, PhaseType.AQUEOUS)
    Eu_For_2_plus = Species("Eu(For)2+", None, ["Eu", "C", "H", "O"], 0.24199887999999997, 1.0, PhaseType.AQUEOUS)
    Gd_For_plus2 = Species("Gd(For)+2", None, ["Gd", "C", "H", "O"], 0.20226744, 2.0, PhaseType.AQUEOUS)
    Gd_For_2_plus = Species("Gd(For)2+", None, ["Gd", "C", "H", "O"], 0.24728487999999998, 1.0, PhaseType.AQUEOUS)
    Yb_For_plus2 = Species("Yb(For)+2", None, ["Yb", "C", "H", "O"], 0.21805744000000002, 2.0, PhaseType.AQUEOUS)
    Yb_For_2_plus = Species("Yb(For)2+", None, ["Yb", "C", "H", "O"], 0.26307488, 1.0, PhaseType.AQUEOUS)
    Pb_For_plus = Species("Pb(For)+", None, ["Pb", "C", "H", "O"], 0.25221744, 1.0, PhaseType.AQUEOUS)
    Pb_For_2_aq = Species("Pb(For)2(aq)", None, ["Pb", "C", "H", "O"], 0.29723488, 0.0, PhaseType.AQUEOUS)
    Mn_For_plus = Species("Mn(For)+", None, ["Mn", "C", "H", "O"], 0.09995549000000001, 1.0, PhaseType.AQUEOUS)
    Mn_For_2_aq = Species("Mn(For)2(aq)", None, ["Mn", "C", "H", "O"], 0.14497293, 0.0, PhaseType.AQUEOUS)
    Co_For_plus = Species("Co(For)+", None, ["Co", "C", "H", "O"], 0.10395064000000001, 1.0, PhaseType.AQUEOUS)
    Co_For_2_aq = Species("Co(For)2(aq)", None, ["Co", "C", "H", "O"], 0.14896808, 0.0, PhaseType.AQUEOUS)
    Ni_For_plus = Species("Ni(For)+", None, ["Ni", "C", "H", "O"], 0.10371084, 1.0, PhaseType.AQUEOUS)
    Ni_For_2_aq = Species("Ni(For)2(aq)", None, ["Ni", "C", "H", "O"], 0.14872828, 0.0, PhaseType.AQUEOUS)
    Zn_For_plus = Species("Zn(For)+", None, ["Zn", "C", "H", "O"], 0.11042643999999999, 1.0, PhaseType.AQUEOUS)
    Zn_For_2_aq = Species("Zn(For)2(aq)", None, ["Zn", "C", "H", "O"], 0.15544387999999998, 0.0, PhaseType.AQUEOUS)
    Fe_For_plus = Species("Fe(For)+", None, ["Fe", "C", "H", "O"], 0.10086244, 1.0, PhaseType.AQUEOUS)
    Fe_For_2_aq = Species("Fe(For)2(aq)", None, ["Fe", "C", "H", "O"], 0.14587988000000002, 0.0, PhaseType.AQUEOUS)
    Propanoic_Acid_aq = Species("Propanoic-Acid(aq)", None, ["C", "H", "O"], 0.07407854, 0.0, PhaseType.AQUEOUS)
    Propanoate = Species("Propanoate", None, ["C", "H", "O"], 0.0730706, -1.0, PhaseType.AQUEOUS)
    Mg_Prop_plus = Species("Mg(Prop)+", None, ["Mg", "C", "H", "O"], 0.0973756, 1.0, PhaseType.AQUEOUS)
    Mg_Prop_2_aq = Species("Mg(Prop)2(aq)", None, ["Mg", "C", "H", "O"], 0.1704462, 0.0, PhaseType.AQUEOUS)
    Ca_Prop_plus = Species("Ca(Prop)+", None, ["Ca", "C", "H", "O"], 0.11314859999999999, 1.0, PhaseType.AQUEOUS)
    Ca_Prop_2_aq = Species("Ca(Prop)2(aq)", None, ["Ca", "C", "H", "O"], 0.1862192, 0.0, PhaseType.AQUEOUS)
    Sr_Prop_plus = Species("Sr(Prop)+", None, ["Sr", "C", "H", "O"], 0.1606906, 1.0, PhaseType.AQUEOUS)
    Sr_Prop_2_aq = Species("Sr(Prop)2(aq)", None, ["Sr", "C", "H", "O"], 0.2337612, 0.0, PhaseType.AQUEOUS)
    Ba_Prop_plus = Species("Ba(Prop)+", None, ["Ba", "C", "H", "O"], 0.2103976, 1.0, PhaseType.AQUEOUS)
    Ba_Prop_2_aq = Species("Ba(Prop)2(aq)", None, ["Ba", "C", "H", "O"], 0.2834682, 0.0, PhaseType.AQUEOUS)
    Eu_Prop_plus = Species("Eu(Prop)+", None, ["Eu", "C", "H", "O"], 0.2250346, 1.0, PhaseType.AQUEOUS)
    Eu_Prop_2_aq = Species("Eu(Prop)2(aq)", None, ["Eu", "C", "H", "O"], 0.29810519999999996, 0.0, PhaseType.AQUEOUS)
    Cu_Prop_plus = Species("Cu(Prop)+", None, ["Cu", "C", "H", "O"], 0.1366166, 1.0, PhaseType.AQUEOUS)
    Cu_Prop_2_aq = Species("Cu(Prop)2(aq)", None, ["Cu", "C", "H", "O"], 0.20968720000000002, 0.0, PhaseType.AQUEOUS)
    Cd_Prop_plus = Species("Cd(Prop)+", None, ["Cd", "C", "H", "O"], 0.1854816, 1.0, PhaseType.AQUEOUS)
    Cd_Prop_2_aq = Species("Cd(Prop)2(aq)", None, ["Cd", "C", "H", "O"], 0.2585522, 0.0, PhaseType.AQUEOUS)
    Pb_Prop_plus = Species("Pb(Prop)+", None, ["Pb", "C", "H", "O"], 0.28027060000000004, 1.0, PhaseType.AQUEOUS)
    Pb_Prop_2_aq = Species("Pb(Prop)2(aq)", None, ["Pb", "C", "H", "O"], 0.35334119999999997, 0.0, PhaseType.AQUEOUS)
    Na_Prop_aq = Species("Na(Prop)(aq)", None, ["Na", "C", "H", "O"], 0.09606037, 0.0, PhaseType.AQUEOUS)
    Na_Prop_2_minus = Species("Na(Prop)2-", None, ["Na", "C", "H", "O"], 0.16913097, -1.0, PhaseType.AQUEOUS)
    K_Prop_aq = Species("K(Prop)(aq)", None, ["K", "C", "H", "O"], 0.11216889999999999, 0.0, PhaseType.AQUEOUS)
    K_Prop_2_minus = Species("K(Prop)2-", None, ["K", "C", "H", "O"], 0.1852395, -1.0, PhaseType.AQUEOUS)
    La_Prop_plus2 = Species("La(Prop)+2", None, ["La", "C", "H", "O"], 0.21197609999999997, 2.0, PhaseType.AQUEOUS)
    La_Prop_2_plus = Species("La(Prop)2+", None, ["La", "C", "H", "O"], 0.2850467, 1.0, PhaseType.AQUEOUS)
    Eu_Prop_plus2 = Species("Eu(Prop)+2", None, ["Eu", "C", "H", "O"], 0.2250346, 2.0, PhaseType.AQUEOUS)
    Eu_Prop_2_plus = Species("Eu(Prop)2+", None, ["Eu", "C", "H", "O"], 0.29810519999999996, 1.0, PhaseType.AQUEOUS)
    Gd_Prop_plus2 = Species("Gd(Prop)+2", None, ["Gd", "C", "H", "O"], 0.23032060000000001, 2.0, PhaseType.AQUEOUS)
    Gd_Prop_2_plus = Species("Gd(Prop)2+", None, ["Gd", "C", "H", "O"], 0.30339119999999997, 1.0, PhaseType.AQUEOUS)
    Yb_Prop_plus2 = Species("Yb(Prop)+2", None, ["Yb", "C", "H", "O"], 0.24611059999999998, 2.0, PhaseType.AQUEOUS)
    Yb_Prop_2_plus = Species("Yb(Prop)2+", None, ["Yb", "C", "H", "O"], 0.3191812, 1.0, PhaseType.AQUEOUS)
    U_Prop_plus2 = Species("U(Prop)+2", None, ["U", "C", "H", "O"], 0.31109950999999997, 2.0, PhaseType.AQUEOUS)
    U_Prop_2_plus = Species("U(Prop)2+", None, ["U", "C", "H", "O"], 0.38417011, 1.0, PhaseType.AQUEOUS)
    Co_Prop_plus = Species("Co(Prop)+", None, ["Co", "C", "H", "O"], 0.1320038, 1.0, PhaseType.AQUEOUS)
    Co_Prop_2_aq = Species("Co(Prop)2(aq)", None, ["Co", "C", "H", "O"], 0.2050744, 0.0, PhaseType.AQUEOUS)
    Ni_Prop_plus = Species("Ni(Prop)+", None, ["Ni", "C", "H", "O"], 0.131764, 1.0, PhaseType.AQUEOUS)
    Ni_Prop_2_aq = Species("Ni(Prop)2(aq)", None, ["Ni", "C", "H", "O"], 0.20483459999999998, 0.0, PhaseType.AQUEOUS)
    Zn_Prop_plus = Species("Zn(Prop)+", None, ["Zn", "C", "H", "O"], 0.13847959999999998, 1.0, PhaseType.AQUEOUS)
    Zn_Prop_2_aq = Species("Zn(Prop)2(aq)", None, ["Zn", "C", "H", "O"], 0.21155019999999997, 0.0, PhaseType.AQUEOUS)
    Fe_Prop_plus = Species("Fe(Prop)+", None, ["Fe", "C", "H", "O"], 0.1289156, 1.0, PhaseType.AQUEOUS)
    Fe_Prop_2_aq = Species("Fe(Prop)2(aq)", None, ["Fe", "C", "H", "O"], 0.2019862, 0.0, PhaseType.AQUEOUS)
    Mn_Prop_plus = Species("Mn(Prop)+", None, ["Mn", "C", "H", "O"], 0.12800865, 1.0, PhaseType.AQUEOUS)
    Mn_Prop_2_aq = Species("Mn(Prop)2(aq)", None, ["Mn", "C", "H", "O"], 0.20107925, 0.0, PhaseType.AQUEOUS)
    Butanoic_Acid_aq = Species("Butanoic-Acid(aq)", None, ["C", "H", "O"], 0.08810512, 0.0, PhaseType.AQUEOUS)
    Butanoate = Species("Butanoate", None, ["C", "H", "O"], 0.08709718, -1.0, PhaseType.AQUEOUS)
    U_But_plus2 = Species("U(But)+2", None, ["U", "C", "H", "O"], 0.32512609, 2.0, PhaseType.AQUEOUS)
    U_But_2_plus = Species("U(But)2+", None, ["U", "C", "H", "O"], 0.41222327000000003, 1.0, PhaseType.AQUEOUS)
    Eu_But_plus = Species("Eu(But)+", None, ["Eu", "C", "H", "O"], 0.23906117999999998, 1.0, PhaseType.AQUEOUS)
    Eu_But_2_aq = Species("Eu(But)2(aq)", None, ["Eu", "C", "H", "O"], 0.32615836, 0.0, PhaseType.AQUEOUS)
    Mg_But_plus = Species("Mg(But)+", None, ["Mg", "C", "H", "O"], 0.11140217999999999, 1.0, PhaseType.AQUEOUS)
    Ca_But_plus = Species("Ca(But)+", None, ["Ca", "C", "H", "O"], 0.12717518, 1.0, PhaseType.AQUEOUS)
    Ca_But_2_aq = Species("Ca(But)2(aq)", None, ["Ca", "C", "H", "O"], 0.21427236, 0.0, PhaseType.AQUEOUS)
    Sr_But_plus = Species("Sr(But)+", None, ["Sr", "C", "H", "O"], 0.17471718, 1.0, PhaseType.AQUEOUS)
    Sr_But_2_aq = Species("Sr(But)2(aq)", None, ["Sr", "C", "H", "O"], 0.26181436, 0.0, PhaseType.AQUEOUS)
    Ba_But_plus = Species("Ba(But)+", None, ["Ba", "C", "H", "O"], 0.22442418, 1.0, PhaseType.AQUEOUS)
    Ba_But_2_aq = Species("Ba(But)2(aq)", None, ["Ba", "C", "H", "O"], 0.31152136, 0.0, PhaseType.AQUEOUS)
    Cu_But_plus = Species("Cu(But)+", None, ["Cu", "C", "H", "O"], 0.15064318000000002, 1.0, PhaseType.AQUEOUS)
    Cu_But_2_aq = Species("Cu(But)2(aq)", None, ["Cu", "C", "H", "O"], 0.23774035999999998, 0.0, PhaseType.AQUEOUS)
    Cd_But_plus = Species("Cd(But)+", None, ["Cd", "C", "H", "O"], 0.19950817999999998, 1.0, PhaseType.AQUEOUS)
    Cd_But_2_aq = Species("Cd(But)2(aq)", None, ["Cd", "C", "H", "O"], 0.28660536, 0.0, PhaseType.AQUEOUS)
    Na_But_aq = Species("Na(But)(aq)", None, ["Na", "C", "H", "O"], 0.11008694999999999, 0.0, PhaseType.AQUEOUS)
    Na_But_2_minus = Species("Na(But)2-", None, ["Na", "C", "H", "O"], 0.19718413, -1.0, PhaseType.AQUEOUS)
    K_But_aq = Species("K(But)(aq)", None, ["K", "C", "H", "O"], 0.12619548, 0.0, PhaseType.AQUEOUS)
    K_But_2_minus = Species("K(But)2-", None, ["K", "C", "H", "O"], 0.21329266000000002, -1.0, PhaseType.AQUEOUS)
    La_But_plus2 = Species("La(But)+2", None, ["La", "C", "H", "O"], 0.22600267999999998, 2.0, PhaseType.AQUEOUS)
    La_But_2_plus = Species("La(But)2+", None, ["La", "C", "H", "O"], 0.31309986, 1.0, PhaseType.AQUEOUS)
    Eu_But_plus2 = Species("Eu(But)+2", None, ["Eu", "C", "H", "O"], 0.23906117999999998, 2.0, PhaseType.AQUEOUS)
    Eu_But_2_plus = Species("Eu(But)2+", None, ["Eu", "C", "H", "O"], 0.32615836, 1.0, PhaseType.AQUEOUS)
    Gd_But_plus2 = Species("Gd(But)+2", None, ["Gd", "C", "H", "O"], 0.24434718, 2.0, PhaseType.AQUEOUS)
    Gd_But_2_plus = Species("Gd(But)2+", None, ["Gd", "C", "H", "O"], 0.33144436, 1.0, PhaseType.AQUEOUS)
    Yb_But_plus2 = Species("Yb(But)+2", None, ["Yb", "C", "H", "O"], 0.26013718, 2.0, PhaseType.AQUEOUS)
    Yb_But_2_plus = Species("Yb(But)2+", None, ["Yb", "C", "H", "O"], 0.34723435999999996, 1.0, PhaseType.AQUEOUS)
    Pb_But_plus = Species("Pb(But)+", None, ["Pb", "C", "H", "O"], 0.29429718, 1.0, PhaseType.AQUEOUS)
    Pb_But_2_aq = Species("Pb(But)2(aq)", None, ["Pb", "C", "H", "O"], 0.38139436, 0.0, PhaseType.AQUEOUS)
    Mn_But_plus = Species("Mn(But)+", None, ["Mn", "C", "H", "O"], 0.14203523, 1.0, PhaseType.AQUEOUS)
    Mn_But_2_aq = Species("Mn(But)2(aq)", None, ["Mn", "C", "H", "O"], 0.22913241, 0.0, PhaseType.AQUEOUS)
    Ni_But_plus = Species("Ni(But)+", None, ["Ni", "C", "H", "O"], 0.14579058, 1.0, PhaseType.AQUEOUS)
    Ni_But_2_aq = Species("Ni(But)2(aq)", None, ["Ni", "C", "H", "O"], 0.23288776, 0.0, PhaseType.AQUEOUS)
    Zn_But_plus = Species("Zn(But)+", None, ["Zn", "C", "H", "O"], 0.15250618, 1.0, PhaseType.AQUEOUS)
    Zn_But_2_aq = Species("Zn(But)2(aq)", None, ["Zn", "C", "H", "O"], 0.23960336, 0.0, PhaseType.AQUEOUS)
    Fe_But_plus = Species("Fe(But)+", None, ["Fe", "C", "H", "O"], 0.14294218, 1.0, PhaseType.AQUEOUS)
    Fe_But_2_aq = Species("Fe(But)2(aq)", None, ["Fe", "C", "H", "O"], 0.23003936000000003, 0.0, PhaseType.AQUEOUS)
    Co_But_plus = Species("Co(But)+", None, ["Co", "C", "H", "O"], 0.14603038, 1.0, PhaseType.AQUEOUS)
    Co_But_2_aq = Species("Co(But)2(aq)", None, ["Co", "C", "H", "O"], 0.23312756, 0.0, PhaseType.AQUEOUS)
    Pentanoic_Acid_aq = Species("Pentanoic-Acid(aq)", None, ["C", "H", "O"], 0.10213169999999999, 0.0, PhaseType.AQUEOUS)
    Pentanoate = Species("Pentanoate", None, ["C", "H", "O"], 0.10112376000000001, -1.0, PhaseType.AQUEOUS)
    Ca_Pent_plus = Species("Ca(Pent)+", None, ["Ca", "C", "H", "O"], 0.14120176, 1.0, PhaseType.AQUEOUS)
    Ca_Pent_2_aq = Species("Ca(Pent)2(aq)", None, ["Ca", "C", "H", "O"], 0.24232552000000002, 0.0, PhaseType.AQUEOUS)
    Sr_Pent_plus = Species("Sr(Pent)+", None, ["Sr", "C", "H", "O"], 0.18874376, 1.0, PhaseType.AQUEOUS)
    Sr_Pent_2_aq = Species("Sr(Pent)2(aq)", None, ["Sr", "C", "H", "O"], 0.28986752, 0.0, PhaseType.AQUEOUS)
    Ba_Pent_plus = Species("Ba(Pent)+", None, ["Ba", "C", "H", "O"], 0.23845076, 1.0, PhaseType.AQUEOUS)
    Ba_Pent_2_aq = Species("Ba(Pent)2(aq)", None, ["Ba", "C", "H", "O"], 0.33957452, 0.0, PhaseType.AQUEOUS)
    Cu_Pent_plus = Species("Cu(Pent)+", None, ["Cu", "C", "H", "O"], 0.16466976, 1.0, PhaseType.AQUEOUS)
    Cu_Pent_2_aq = Species("Cu(Pent)2(aq)", None, ["Cu", "C", "H", "O"], 0.26579352, 0.0, PhaseType.AQUEOUS)
    Na_Pent_aq = Species("Na(Pent)(aq)", None, ["Na", "C", "H", "O"], 0.12411353, 0.0, PhaseType.AQUEOUS)
    Na_Pent_2_minus = Species("Na(Pent)2-", None, ["Na", "C", "H", "O"], 0.22523728999999998, -1.0, PhaseType.AQUEOUS)
    K_Pent_aq = Species("K(Pent)(aq)", None, ["K", "C", "H", "O"], 0.14022206, 0.0, PhaseType.AQUEOUS)
    K_Pent_2_minus = Species("K(Pent)2-", None, ["K", "C", "H", "O"], 0.24134582, -1.0, PhaseType.AQUEOUS)
    La_Pent_plus2 = Species("La(Pent)+2", None, ["La", "C", "H", "O"], 0.24002926, 2.0, PhaseType.AQUEOUS)
    La_Pent_2_plus = Species("La(Pent)2+", None, ["La", "C", "H", "O"], 0.34115302, 1.0, PhaseType.AQUEOUS)
    Eu_Pent_plus2 = Species("Eu(Pent)+2", None, ["Eu", "C", "H", "O"], 0.25308776, 2.0, PhaseType.AQUEOUS)
    Eu_Pent_2_plus = Species("Eu(Pent)2+", None, ["Eu", "C", "H", "O"], 0.35421151999999995, 1.0, PhaseType.AQUEOUS)
    U_Pent_plus2 = Species("U(Pent)+2", None, ["U", "C", "H", "O"], 0.33915267, 2.0, PhaseType.AQUEOUS)
    Eu_Pent_plus = Species("Eu(Pent)+", None, ["Eu", "C", "H", "O"], 0.25308776, 1.0, PhaseType.AQUEOUS)
    Gd_Pent_plus2 = Species("Gd(Pent)+2", None, ["Gd", "C", "H", "O"], 0.25837376, 2.0, PhaseType.AQUEOUS)
    Gd_Pent_2_plus = Species("Gd(Pent)2+", None, ["Gd", "C", "H", "O"], 0.35949751999999996, 1.0, PhaseType.AQUEOUS)
    Yb_Pent_plus2 = Species("Yb(Pent)+2", None, ["Yb", "C", "H", "O"], 0.27416376000000003, 2.0, PhaseType.AQUEOUS)
    Yb_Pent_2_plus = Species("Yb(Pent)2+", None, ["Yb", "C", "H", "O"], 0.37528752, 1.0, PhaseType.AQUEOUS)
    Mg_Pent_plus = Species("Mg(Pent)+", None, ["Mg", "C", "H", "O"], 0.12542876, 1.0, PhaseType.AQUEOUS)
    Mg_Pent_2_aq = Species("Mg(Pent)2(aq)", None, ["Mg", "C", "H", "O"], 0.22655251999999998, 0.0, PhaseType.AQUEOUS)
    Pb_Pent_plus = Species("Pb(Pent)+", None, ["Pb", "C", "H", "O"], 0.30832375999999995, 1.0, PhaseType.AQUEOUS)
    Pb_Pent_2_aq = Species("Pb(Pent)2(aq)", None, ["Pb", "C", "H", "O"], 0.40944752, 0.0, PhaseType.AQUEOUS)
    Co_Pent_plus = Species("Co(Pent)+", None, ["Co", "C", "H", "O"], 0.16005696, 1.0, PhaseType.AQUEOUS)
    Co_Pent_2_aq = Species("Co(Pent)2(aq)", None, ["Co", "C", "H", "O"], 0.26118072, 0.0, PhaseType.AQUEOUS)
    Ni_Pent_plus = Species("Ni(Pent)+", None, ["Ni", "C", "H", "O"], 0.15981715999999999, 1.0, PhaseType.AQUEOUS)
    Ni_Pent_2_aq = Species("Ni(Pent)2(aq)", None, ["Ni", "C", "H", "O"], 0.26094092, 0.0, PhaseType.AQUEOUS)
    Zn_Pent_plus = Species("Zn(Pent)+", None, ["Zn", "C", "H", "O"], 0.16653275999999997, 1.0, PhaseType.AQUEOUS)
    Zn_Pent_2_aq = Species("Zn(Pent)2(aq)", None, ["Zn", "C", "H", "O"], 0.26765652, 0.0, PhaseType.AQUEOUS)
    Cd_Pent_plus = Species("Cd(Pent)+", None, ["Cd", "C", "H", "O"], 0.21353476, 1.0, PhaseType.AQUEOUS)
    Cd_Pent_2_aq = Species("Cd(Pent)2(aq)", None, ["Cd", "C", "H", "O"], 0.31465852, 0.0, PhaseType.AQUEOUS)
    Fe_Pent_plus = Species("Fe(Pent)+", None, ["Fe", "C", "H", "O"], 0.15696875999999998, 1.0, PhaseType.AQUEOUS)
    Fe_Pent_2_aq = Species("Fe(Pent)2(aq)", None, ["Fe", "C", "H", "O"], 0.25809252, 0.0, PhaseType.AQUEOUS)
    Mn_Pent_plus = Species("Mn(Pent)+", None, ["Mn", "C", "H", "O"], 0.15606181, 1.0, PhaseType.AQUEOUS)
    Mn_Pent_2_aq = Species("Mn(Pent)2(aq)", None, ["Mn", "C", "H", "O"], 0.25718557, 0.0, PhaseType.AQUEOUS)
    Mg_But_2_aq = Species("Mg(But)2(aq)", None, ["Mg", "C", "H", "O"], 0.19849936, 0.0, PhaseType.AQUEOUS)
    H4SiO4_aq = Species("H4SiO4(aq)", None, ["Si", "O", "H"], 0.09611486, 0.0, PhaseType.AQUEOUS)

    # reaktoro elements
    H = Species("H", None, ["H"], 0.001007940, +0, PhaseType.ELEMENT)
    He = Species("He", None, ["He"], 0.004002602, +0, PhaseType.ELEMENT)
    Li = Species("Li", None, ["Li"], 0.006941000, +0, PhaseType.ELEMENT)
    Be = Species("Be", None, ["Be"], 0.009012182, +0, PhaseType.ELEMENT)
    B = Species("B", None, ["B"], 0.010811000, +0, PhaseType.ELEMENT)
    C = Species("C", None, ["C"], 0.012010700, +0, PhaseType.ELEMENT)
    N = Species("N", None, ["N"], 0.014006700, +0, PhaseType.ELEMENT)
    O = Species("O", None, ["O"], 0.015999400, +0, PhaseType.ELEMENT)
    F = Species("F", None, ["F"], 0.018998403, +0, PhaseType.ELEMENT)
    Ne = Species("Ne", None, ["Ne"], 0.020179700, +0, PhaseType.ELEMENT)
    Na = Species("Na", None, ["Na"], 0.022989770, +0, PhaseType.ELEMENT)
    Mg = Species("Mg", None, ["Mg"], 0.024305000, +0, PhaseType.ELEMENT)
    Al = Species("Al", None, ["Al"], 0.026981538, +0, PhaseType.ELEMENT)
    Si = Species("Si", None, ["Si"], 0.028085500, +0, PhaseType.ELEMENT)
    P = Species("P", None, ["P"], 0.030973761, +0, PhaseType.ELEMENT)
    S = Species("S", None, ["S"], 0.032065000, +0, PhaseType.ELEMENT)
    Cl = Species("Cl", None, ["Cl"], 0.035453000, +0, PhaseType.ELEMENT)
    K = Species("K", None, ["K"], 0.039098300, +0, PhaseType.ELEMENT)
    Ar = Species("Ar", None, ["Ar"], 0.039948000, +0, PhaseType.ELEMENT)
    Ca = Species("Ca", None, ["Ca"], 0.040078000, +0, PhaseType.ELEMENT)
    Sc = Species("Sc", None, ["Sc"], 0.044955910, +0, PhaseType.ELEMENT)
    Ti = Species("Ti", None, ["Ti"], 0.047867000, +0, PhaseType.ELEMENT)
    V = Species("V", None, ["V"], 0.050941500, +0, PhaseType.ELEMENT)
    Cr = Species("Cr", None, ["Cr"], 0.051996100, +0, PhaseType.ELEMENT)
    Mn = Species("Mn", None, ["Mn"], 0.054938050, +0, PhaseType.ELEMENT)
    Fe = Species("Fe", None, ["Fe"], 0.055845000, +0, PhaseType.ELEMENT)
    Ni = Species("Ni", None, ["Ni"], 0.058693400, +0, PhaseType.ELEMENT)
    Co = Species("Co", None, ["Co"], 0.058933200, +0, PhaseType.ELEMENT)
    Cu = Species("Cu", None, ["Cu"], 0.063546000, +0, PhaseType.ELEMENT)
    Zn = Species("Zn", None, ["Zn"], 0.065409000, +0, PhaseType.ELEMENT)
    Ga = Species("Ga", None, ["Ga"], 0.069723000, +0, PhaseType.ELEMENT)
    Ge = Species("Ge", None, ["Ge"], 0.072640000, +0, PhaseType.ELEMENT)
    As = Species("As", None, ["As"], 0.074921600, +0, PhaseType.ELEMENT)
    Se = Species("Se", None, ["Se"], 0.078960000, +0, PhaseType.ELEMENT)
    Br = Species("Br", None, ["Br"], 0.079904000, +0, PhaseType.ELEMENT)
    Kr = Species("Kr", None, ["Kr"], 0.083798000, +0, PhaseType.ELEMENT)
    Rb = Species("Rb", None, ["Rb"], 0.085467800, +0, PhaseType.ELEMENT)
    Sr = Species("Sr", None, ["Sr"], 0.087620000, +0, PhaseType.ELEMENT)
    Y = Species("Y", None, ["Y"], 0.088905850, +0, PhaseType.ELEMENT)
    Zr = Species("Zr", None, ["Zr"], 0.091224000, +0, PhaseType.ELEMENT)
    Nb = Species("Nb", None, ["Nb"], 0.092906380, +0, PhaseType.ELEMENT)
    Mo = Species("Mo", None, ["Mo"], 0.095940000, +0, PhaseType.ELEMENT)
    Tc = Species("Tc", None, ["Tc"], 0.098000000, +0, PhaseType.ELEMENT)
    Ru = Species("Ru", None, ["Ru"], 0.101070000, +0, PhaseType.ELEMENT)
    Rh = Species("Rh", None, ["Rh"], 0.102905500, +0, PhaseType.ELEMENT)
    Pd = Species("Pd", None, ["Pd"], 0.106420000, +0, PhaseType.ELEMENT)
    Ag = Species("Ag", None, ["Ag"], 0.107868200, +0, PhaseType.ELEMENT)
    Cd = Species("Cd", None, ["Cd"], 0.112411000, +0, PhaseType.ELEMENT)
    In = Species("In", None, ["In"], 0.114818000, +0, PhaseType.ELEMENT)
    Sn = Species("Sn", None, ["Sn"], 0.118710000, +0, PhaseType.ELEMENT)
    Sb = Species("Sb", None, ["Sb"], 0.121760000, +0, PhaseType.ELEMENT)
    I = Species("I", None, ["I"], 0.126904470, +0, PhaseType.ELEMENT)
    Te = Species("Te", None, ["Te"], 0.127600000, +0, PhaseType.ELEMENT)
    Xe = Species("Xe", None, ["Xe"], 0.131293000, +0, PhaseType.ELEMENT)
    Cs = Species("Cs", None, ["Cs"], 0.132905450, +0, PhaseType.ELEMENT)
    Ba = Species("Ba", None, ["Ba"], 0.137327000, +0, PhaseType.ELEMENT)
    La = Species("La", None, ["La"], 0.138905500, +0, PhaseType.ELEMENT)
    Ce = Species("Ce", None, ["Ce"], 0.140116000, +0, PhaseType.ELEMENT)
    Pr = Species("Pr", None, ["Pr"], 0.140907650, +0, PhaseType.ELEMENT)
    Nd = Species("Nd", None, ["Nd"], 0.144240000, +0, PhaseType.ELEMENT)
    Pm = Species("Pm", None, ["Pm"], 0.145000000, +0, PhaseType.ELEMENT)
    Sm = Species("Sm", None, ["Sm"], 0.150360000, +0, PhaseType.ELEMENT)
    Eu = Species("Eu", None, ["Eu"], 0.151964000, +0, PhaseType.ELEMENT)
    Gd = Species("Gd", None, ["Gd"], 0.157250000, +0, PhaseType.ELEMENT)
    Tb = Species("Tb", None, ["Tb"], 0.158925340, +0, PhaseType.ELEMENT)
    Dy = Species("Dy", None, ["Dy"], 0.162500000, +0, PhaseType.ELEMENT)
    Ho = Species("Ho", None, ["Ho"], 0.164930320, +0, PhaseType.ELEMENT)
    Er = Species("Er", None, ["Er"], 0.167259000, +0, PhaseType.ELEMENT)
    Tm = Species("Tm", None, ["Tm"], 0.168934210, +0, PhaseType.ELEMENT)
    Yb = Species("Yb", None, ["Yb"], 0.173040000, +0, PhaseType.ELEMENT)
    Lu = Species("Lu", None, ["Lu"], 0.174967000, +0, PhaseType.ELEMENT)
    Hf = Species("Hf", None, ["Hf"], 0.178490000, +0, PhaseType.ELEMENT)
    Ta = Species("Ta", None, ["Ta"], 0.180947900, +0, PhaseType.ELEMENT)
    W = Species("W", None, ["W"], 0.183840000, +0, PhaseType.ELEMENT)
    Re = Species("Re", None, ["Re"], 0.186207000, +0, PhaseType.ELEMENT)
    Os = Species("Os", None, ["Os"], 0.190230000, +0, PhaseType.ELEMENT)
    Ir = Species("Ir", None, ["Ir"], 0.192217000, +0, PhaseType.ELEMENT)
    Pt = Species("Pt", None, ["Pt"], 0.195078000, +0, PhaseType.ELEMENT)
    Au = Species("Au", None, ["Au"], 0.196966550, +0, PhaseType.ELEMENT)
    Hg = Species("Hg", None, ["Hg"], 0.200590000, +0, PhaseType.ELEMENT)
    Tl = Species("Tl", None, ["Tl"], 0.204383300, +0, PhaseType.ELEMENT)
    Pb = Species("Pb", None, ["Pb"], 0.207200000, +0, PhaseType.ELEMENT)
    Bi = Species("Bi", None, ["Bi"], 0.208980380, +0, PhaseType.ELEMENT)
    Po = Species("Po", None, ["Po"], 0.209000000, +0, PhaseType.ELEMENT)
    At = Species("At", None, ["At"], 0.210000000, +0, PhaseType.ELEMENT)
    Rn = Species("Rn", None, ["Rn"], 0.222000000, +0, PhaseType.ELEMENT)
    Fr = Species("Fr", None, ["Fr"], 0.223000000, +0, PhaseType.ELEMENT)
    Ra = Species("Ra", None, ["Ra"], 0.226000000, +0, PhaseType.ELEMENT)
    Ac = Species("Ac", None, ["Ac"], 0.227000000, +0, PhaseType.ELEMENT)
    Pa = Species("Pa", None, ["Pa"], 0.231035880, +0, PhaseType.ELEMENT)
    Th = Species("Th", None, ["Th"], 0.232038100, +0, PhaseType.ELEMENT)
    Np = Species("Np", None, ["Np"], 0.237000000, +0, PhaseType.ELEMENT)
    U = Species("U", None, ["U"], 0.238028910, +0, PhaseType.ELEMENT)
    Am = Species("Am", None, ["Am"], 0.243000000, +0, PhaseType.ELEMENT)
    Pu = Species("Pu", None, ["Pu"], 0.244000000, +0, PhaseType.ELEMENT)
    Bk = Species("Bk", None, ["Bk"], 0.247000000, +0, PhaseType.ELEMENT)
    Cm = Species("Cm", None, ["Cm"], 0.247000000, +0, PhaseType.ELEMENT)
    Cf = Species("Cf", None, ["Cf"], 0.251000000, +0, PhaseType.ELEMENT)
    Es = Species("Es", None, ["Es"], 0.252000000, +0, PhaseType.ELEMENT)
    Fm = Species("Fm", None, ["Fm"], 0.257000000, +0, PhaseType.ELEMENT)
    Md = Species("Md", None, ["Md"], 0.258000000, +0, PhaseType.ELEMENT)
    No = Species("No", None, ["No"], 0.259000000, +0, PhaseType.ELEMENT)
    Rf = Species("Rf", None, ["Rf"], 0.261000000, +0, PhaseType.ELEMENT)
    Lr = Species("Lr", None, ["Lr"], 0.262000000, +0, PhaseType.ELEMENT)


class LookUp:
    """
    The LookUp class provides an easy way to convert from a Reaktoro or CoolProp species name to the Component object.

    Attributes
    ----------
    reaktoroToComp : Dict
        a dictionary to translate Reaktoro species names into a Component object
    coolpropToComp : Dict
        a dictionary to translate CoolProp species names into a Component object

    # TODO should I add the elements to the look up Dicts??
    """

    reaktoroToComp = {
        "H2O(g)": Comp.STEAM,
        "H2O(aq)": Comp.WATER,
        "H2(g)": Comp.HYDROGEN,
        "O2(g)": Comp.OXYGEN,
        "NH3": Comp.AMMONIA,
        "NH3(g)": Comp.AMMONIA_g,
        "CO2(g)": Comp.CARBONDIOXIDE,
        "N2(g)": Comp.NITROGEN,
        "H2S(g)": Comp.H2S,
        "He(g)": Comp.HELIUM,
        "Ar(g)": Comp.ARGON,
        "CH4(g)": Comp.METHANE,
        "C2H4(g)": Comp.C2H4_g,
        "SO2(g)": Comp.SO2_g,
        "Kr(g)": Comp.Kr_g,
        "Ne(g)": Comp.Ne_g,
        "Xe(g)": Comp.Xe_g,
        "Almandine": Comp.Almandine,
        "Andradite": Comp.Andradite,
        "Grossular": Comp.Grossular,
        "Knorringite": Comp.Knorringite,
        "Majorite": Comp.Majorite,
        "Pyrope": Comp.Pyrope,
        "Spessartine": Comp.Spessartine,
        "Clinohumite": Comp.Clinohumite,
        "Fayalite": Comp.Fayalite,
        "Forsterite": Comp.Forsterite,
        "Monticellite": Comp.Monticellite,
        "Tephroite": Comp.Tephroite,
        "Andalusite": Comp.Andalusite,
        "Kyanite": Comp.Kyanite,
        "Al-Mullite": Comp.Al_Mullite,
        "Si-Mullite": Comp.Si_Mullite,
        "Fe-Chloritoid": Comp.Fe_Chloritoid,
        "Mg-Chloritoid": Comp.Mg_Chloritoid,
        "Mn-Chloritoid": Comp.Mn_Chloritoid,
        "Fe-Staurolite": Comp.Fe_Staurolite,
        "Mg-Staurolite": Comp.Mg_Staurolite,
        "Mn-Staurolite": Comp.Mn_Staurolite,
        "Hydroxy-Topaz": Comp.Hydroxy_Topaz,
        "Akermanite": Comp.Akermanite,
        "Julgoldite-FeFe": Comp.Julgoldite_FeFe,
        "Merwinite": Comp.Merwinite,
        "Pumpellyite-FeAl": Comp.Pumpellyite_FeAl,
        "Pumpellyite-MgAl": Comp.Pumpellyite_MgAl,
        "Rankinite": Comp.Rankinite,
        "Spurrite": Comp.Spurrite,
        "Tilleyite": Comp.Tilleyite,
        "Zircon": Comp.Zircon,
        "Clinozoisite": Comp.Clinozoisite,
        "Epidote,ordered": Comp.Epidote_ordered,
        "Fe-Epidote": Comp.Fe_Epidote,
        "Lawsonite": Comp.Lawsonite,
        "Piemontite,ordered": Comp.Piemontite_ordered,
        "Zoisite": Comp.Zoisite,
        "Vesuvianite": Comp.Vesuvianite,
        "Fe-Osumilite": Comp.Fe_Osumilite,
        "Osumilite,1": Comp.Osumilite_1,
        "Osumilite,2": Comp.Osumilite_2,
        "Fe-Akimotoite": Comp.Fe_Akimotoite,
        "Akimotoite": Comp.Akimotoite,
        "CaSi-Titanite": Comp.CaSi_Titanite,
        "Al-Perovskite": Comp.Al_Perovskite,
        "Ca-Perovskite": Comp.Ca_Perovskite,
        "Fe-Perovskite": Comp.Fe_Perovskite,
        "Mg-Perovskite": Comp.Mg_Perovskite,
        "Phasea": Comp.Phasea,
        "Fe-Ringwoodite": Comp.Fe_Ringwoodite,
        "Mg-Ringwoodite": Comp.Mg_Ringwoodite,
        "Fe-Wadsleyite": Comp.Fe_Wadsleyite,
        "Mg-Wadsleyite": Comp.Mg_Wadsleyite,
        "Acmite": Comp.Acmite,
        "Ca-Eskola-Pyroxene": Comp.Ca_Eskola_Pyroxene,
        "Clino-Enstatite": Comp.Clino_Enstatite,
        "Hi-P-Clinoenstatite": Comp.Hi_P_Clinoenstatite,
        "Diopside": Comp.Diopside,
        "Enstatite": Comp.Enstatite,
        "Ferrosilite": Comp.Ferrosilite,
        "Hedenbergite": Comp.Hedenbergite,
        "Jadeite": Comp.Jadeite,
        "Kosmochlor": Comp.Kosmochlor,
        "Mg-Tschermaks-Px": Comp.Mg_Tschermaks_Px,
        "Protoenstatite": Comp.Protoenstatite,
        "Pseudowollastonite": Comp.Pseudowollastonite,
        "Pyroxmangite": Comp.Pyroxmangite,
        "Rhodonite": Comp.Rhodonite,
        "Walstromite": Comp.Walstromite,
        "Wollastonite": Comp.Wollastonite,
        "Anthophyllite": Comp.Anthophyllite,
        "Fe-Anthophyllite": Comp.Fe_Anthophyllite,
        "Cummingtonite": Comp.Cummingtonite,
        "Ferroactinolite": Comp.Ferroactinolite,
        "Ferroglaucophane": Comp.Ferroglaucophane,
        "Glaucophane": Comp.Glaucophane,
        "Grunerite": Comp.Grunerite,
        "Pargasite": Comp.Pargasite,
        "Riebeckite": Comp.Riebeckite,
        "Tremolite": Comp.Tremolite,
        "Tschermakite": Comp.Tschermakite,
        "Deerite": Comp.Deerite,
        "Ferrocarpholite": Comp.Ferrocarpholite,
        "Magnesiocarpholite": Comp.Magnesiocarpholite,
        "Fe-Sapphirine,221": Comp.Fe_Sapphirine_221,
        "Sapphirine,221": Comp.Sapphirine_221,
        "Sapphirine,351": Comp.Sapphirine_351,
        "Annite": Comp.Annite,
        "Celadonite": Comp.Celadonite,
        "Ferroceladonite": Comp.Ferroceladonite,
        "Eastonite": Comp.Eastonite,
        "Margarite": Comp.Margarite,
        "Mn-Biotite": Comp.Mn_Biotite,
        "Muscovite": Comp.Muscovite,
        "Sodaphlogopite": Comp.Sodaphlogopite,
        "Paragonite": Comp.Paragonite,
        "Phlogopite": Comp.Phlogopite,
        "Al-Free-Chlorite": Comp.Al_Free_Chlorite,
        "Amesite,14A": Comp.Amesite_14A,
        "Clinochlore,ordered": Comp.Clinochlore_ordered,
        "Daphnite": Comp.Daphnite,
        "Mn-Chlorite": Comp.Mn_Chlorite,
        "Ferrosudoite": Comp.Ferrosudoite,
        "Sudoite": Comp.Sudoite,
        "Antigorite": Comp.Antigorite,
        "Chrysotile": Comp.Chrysotile,
        "Ferrotalc": Comp.Ferrotalc,
        "Greenalite": Comp.Greenalite,
        "Kaolinite": Comp.Kaolinite,
        "Lizardite": Comp.Lizardite,
        "Minnesotaite": Comp.Minnesotaite,
        "Mg-Minnesotaite": Comp.Mg_Minnesotaite,
        "Prehnite": Comp.Prehnite,
        "PRL-Talc": Comp.PRL_Talc,
        "Pyrophyllite": Comp.Pyrophyllite,
        "Ferrostilpnomelane": Comp.Ferrostilpnomelane,
        "Mg-Stilpnomelane": Comp.Mg_Stilpnomelane,
        "Talc": Comp.Talc,
        "Tschermak-Talc": Comp.Tschermak_Talc,
        "Ferri-Prehnite": Comp.Ferri_Prehnite,
        "Albite,high": Comp.Albite_high,
        "Analcite": Comp.Analcite,
        "Carnegieite,high": Comp.Carnegieite_high,
        "Carnegieite,low": Comp.Carnegieite_low,
        "K-Cymrite": Comp.K_Cymrite,
        "Kalsilite": Comp.Kalsilite,
        "Microcline": Comp.Microcline,
        "Coesite": Comp.Coesite,
        "Cristobalite,high": Comp.Cristobalite_high,
        "Stishovite": Comp.Stishovite,
        "Tridymite,high": Comp.Tridymite_high,
        "Heulandite": Comp.Heulandite,
        "Hollandite": Comp.Hollandite,
        "Laumontite": Comp.Laumontite,
        "Meionite": Comp.Meionite,
        "Sodalite": Comp.Sodalite,
        "Stilbite": Comp.Stilbite,
        "Si-Wadeite": Comp.Si_Wadeite,
        "Wairakite": Comp.Wairakite,
        "Baddeleyite": Comp.Baddeleyite,
        "Bixbyite": Comp.Bixbyite,
        "Corundum": Comp.Corundum,
        "Cuprite": Comp.Cuprite,
        "Eskolaite": Comp.Eskolaite,
        "Geikielite": Comp.Geikielite,
        "Lime": Comp.Lime,
        "Manganosite": Comp.Manganosite,
        "MgSi-Corundum": Comp.MgSi_Corundum,
        "Periclase": Comp.Periclase,
        "Ferropericlase": Comp.Ferropericlase,
        "Pyrophanite": Comp.Pyrophanite,
        "Rutile": Comp.Rutile,
        "Tenorite": Comp.Tenorite,
        "Ulvospinel": Comp.Ulvospinel,
        "Brucite": Comp.Brucite,
        "Diaspore": Comp.Diaspore,
        "Goethite": Comp.Goethite,
        "Magnesite": Comp.Magnesite,
        "Rhodochrosite": Comp.Rhodochrosite,
        "Siderite": Comp.Siderite,
        "Anhydrite": Comp.Anhydrite,
        "Halite": Comp.Halite,
        "Pyrite": Comp.Pyrite,
        "Sylvite": Comp.Sylvite,
        "Copper": Comp.Copper,
        "Diamond": Comp.Diamond,
        "Graphite": Comp.Graphite,
        "Sulphur": Comp.Sulphur,
        "Gibbsite": Comp.Gibbsite,
        "Boehmite": Comp.Boehmite,
        "Fluorphlogopite": Comp.Fluorphlogopite,
        "Hydroxyapatite": Comp.Hydroxyapatite,
        "Fluorapatite": Comp.Fluorapatite,
        "Chlorapatite": Comp.Chlorapatite,
        "Arsenic": Comp.Arsenic,
        "Arsenolite": Comp.Arsenolite,
        "Claudetite": Comp.Claudetite,
        "As2O5(s)": Comp.As2O5_s,
        "Realgar,alpha": Comp.Realgar_alpha,
        "Realgar,beta": Comp.Realgar_beta,
        "Orpiment": Comp.Orpiment,
        "Orpiment(am)": Comp.Orpiment_am,
        "Arsenopyrite": Comp.Arsenopyrite,
        "Scorodite": Comp.Scorodite,
        "Ferric-As(am)": Comp.Ferric_As_am,
        "Barium-As": Comp.Barium_As,
        "Barium-H-As": Comp.Barium_H_As,
        "a-GaOOH": Comp.a_GaOOH,
        "Dawsonite": Comp.Dawsonite,
        "Sapphirine,793": Comp.Sapphirine_793,
        "Fe-Sapphirine,793": Comp.Fe_Sapphirine_793,
        "Gedrite": Comp.Gedrite,
        "Beidellite-Ca": Comp.Beidellite_Ca,
        "Beidellite-H": Comp.Beidellite_H,
        "Beidellite-K": Comp.Beidellite_K,
        "Beidellite-Mg": Comp.Beidellite_Mg,
        "Beidellite-Na": Comp.Beidellite_Na,
        "Montmorillonite-Ca": Comp.Montmorillonite_Ca,
        "Montmorillonite-K": Comp.Montmorillonite_K,
        "Montmorillonite-Mg": Comp.Montmorillonite_Mg,
        "Montmorillonite-Na": Comp.Montmorillonite_Na,
        "Nontronite-Ca": Comp.Nontronite_Ca,
        "Nontronite-Mg": Comp.Nontronite_Mg,
        "Nontronite-H": Comp.Nontronite_H,
        "Nontronite-K": Comp.Nontronite_K,
        "Nontronite-Na": Comp.Nontronite_Na,
        "Saponite-Mg": Comp.Saponite_Mg,
        "Illite": Comp.Illite,
        "Dolomite,disordered": Comp.Dolomite_disordered,
        "Dolomite,ordered": Comp.Dolomite_ordered,
        "Galena": Comp.Galena,
        "Barite": Comp.Barite,
        "Fluorite": Comp.Fluorite,
        "Celestite": Comp.Celestite,
        "Anglesite": Comp.Anglesite,
        "Chalcedony": Comp.Chalcedony,
        "SiO2(a)": Comp.SiO2_a,
        "Larnite": Comp.Larnite,
        "Sphene": Comp.Sphene,
        "Quartz": Comp.Quartz,
        "Nepheline": Comp.Nepheline,
        "Hematite": Comp.Hematite,
        "Nickel-Oxide": Comp.Nickel_Oxide,
        "Ilmenite": Comp.Ilmenite,
        "Magnetite": Comp.Magnetite,
        "Magnesioferrite": Comp.Magnesioferrite,
        "Calcite": Comp.Calcite,
        "Aragonite": Comp.Aragonite,
        "Pyrrhotite,trot": Comp.Pyrrhotite_trot,
        "Troilite": Comp.Troilite,
        "Troilite,low": Comp.Troilite_low,
        "Pyrrhotite,trov": Comp.Pyrrhotite_trov,
        "Iron": Comp.Iron,
        "Nickel": Comp.Nickel,
        "Sillimanite": Comp.Sillimanite,
        "Gehlenite": Comp.Gehlenite,
        "Cordierite": Comp.Cordierite,
        "Hydrous-Cordierite": Comp.Hydrous_Cordierite,
        "Fe-Cordierite": Comp.Fe_Cordierite,
        "Mn-Cordierite": Comp.Mn_Cordierite,
        "Ca-Tschermaks-Px": Comp.Ca_Tschermaks_Px,
        "Albite": Comp.Albite,
        "Sanidine": Comp.Sanidine,
        "Anorthite": Comp.Anorthite,
        "Leucite": Comp.Leucite,
        "Spinel": Comp.Spinel,
        "Hercynite": Comp.Hercynite,
        "Picrochromite": Comp.Picrochromite,
        "Dolomite": Comp.Dolomite,
        "Ankerite": Comp.Ankerite,
        "CO(g)": Comp.CO_g,
        "S2(g)": Comp.S2_g,
        "Phenol(g)": Comp.Phenol_g,
        "o-Cresol(g)": Comp.o_Cresol_g,
        "m-Cresol(g)": Comp.m_Cresol_g,
        "p-Cresol(g)": Comp.p_Cresol_g,
        "Ethylene(g)": Comp.Ethylene_g,
        "Rn(g)": Comp.Rn_g,
        "NO(g)": Comp.NO_g,
        "N2O(g)": Comp.N2O_g,
        "Ag(CO3)-": Comp.Ag_CO3_minus,
        "Ag(CO3)2-3": Comp.Ag_CO3_2_minus3,
        "Ag+": Comp.Ag_plus,
        "Ag+2": Comp.Ag_plus2,
        "AgCl(aq)": Comp.AgCl_aq,
        "AgCl2-": Comp.AgCl2_minus,
        "AgCl3-2": Comp.AgCl3_minus2,
        "AgCl4-3": Comp.AgCl4_minus3,
        "AgOH(aq)": Comp.AgOH_aq,
        "AgO-": Comp.AgO_minus,
        "AgNO3(aq)": Comp.AgNO3_aq,
        "AlOH+2": Comp.AlOH_plus2,
        "Al+3": Comp.Al_plus3,
        "AlH3SiO4+2": Comp.AlH3SiO4_plus2,
        "Al(OH)3(aq)": Comp.Al_OH_3_aq,
        "Al(OH)4-": Comp.Al_OH_4_minus,
        "Al(OH)2+": Comp.Al_OH_2_plus,
        "Au+": Comp.Au_plus,
        "Au+3": Comp.Au_plus3,
        "B(OH)3(aq)": Comp.B_OH_3_aq,
        "BF4-": Comp.BF4_minus,
        "BO2-": Comp.BO2_minus,
        "Ba(HCO3)+": Comp.Ba_HCO3_plus,
        "Ba+2": Comp.Ba_plus2,
        "BaCl+": Comp.BaCl_plus,
        "BaOH+": Comp.BaOH_plus,
        "Be+2": Comp.Be_plus2,
        "BeOH+": Comp.BeOH_plus,
        "BeO(aq)": Comp.BeO_aq,
        "HBeO2-": Comp.HBeO2_minus,
        "BeO2-2": Comp.BeO2_minus2,
        "Br-": Comp.Br_minus,
        "Br3-": Comp.Br3_minus,
        "HBrO(aq)": Comp.HBrO_aq,
        "BrO-": Comp.BrO_minus,
        "BrO3-": Comp.BrO3_minus,
        "BrO4-": Comp.BrO4_minus,
        "CaOH+": Comp.CaOH_plus,
        "Ce+4": Comp.Ce_plus4,
        "CO(aq)": Comp.CO_aq,
        "CO2(aq)": Comp.CO2_aq,
        "CO3-2": Comp.CO3_minus2,
        "Ca(HCO3)+": Comp.Ca_HCO3_plus,
        "Ca+2": Comp.Ca_plus2,
        "CaCl+": Comp.CaCl_plus,
        "CaCl2(aq)": Comp.CaCl2_aq,
        "CaF+": Comp.CaF_plus,
        "CaSO4(aq)": Comp.CaSO4_aq,
        "Cd+2": Comp.Cd_plus2,
        "CdOH+": Comp.CdOH_plus,
        "CdO(aq)": Comp.CdO_aq,
        "HCdO2-": Comp.HCdO2_minus,
        "CdO2-2": Comp.CdO2_minus2,
        "Ce+2": Comp.Ce_plus2,
        "Ce+3": Comp.Ce_plus3,
        "Cl-": Comp.Cl_minus,
        "HClO(aq)": Comp.HClO_aq,
        "ClO-": Comp.ClO_minus,
        "ClO2-": Comp.ClO2_minus,
        "ClO3-": Comp.ClO3_minus,
        "ClO4-": Comp.ClO4_minus,
        "Co+2": Comp.Co_plus2,
        "Co+3": Comp.Co_plus3,
        "CoOH+": Comp.CoOH_plus,
        "CoO(aq)": Comp.CoO_aq,
        "HCoO2-": Comp.HCoO2_minus,
        "CoO2-2": Comp.CoO2_minus2,
        "CoOH+2": Comp.CoOH_plus2,
        "Cr2O7-2": Comp.Cr2O7_minus2,
        "CrO4-2": Comp.CrO4_minus2,
        "Cs+": Comp.Cs_plus,
        "CsBr(aq)": Comp.CsBr_aq,
        "CsCl(aq)": Comp.CsCl_aq,
        "CsI(aq)": Comp.CsI_aq,
        "CsOH(aq)": Comp.CsOH_aq,
        "Cu+": Comp.Cu_plus,
        "Cu+2": Comp.Cu_plus2,
        "CuOH+": Comp.CuOH_plus,
        "CuO(aq)": Comp.CuO_aq,
        "HCuO2-": Comp.HCuO2_minus,
        "CuO2-2": Comp.CuO2_minus2,
        "Dy+2": Comp.Dy_plus2,
        "Dy+3": Comp.Dy_plus3,
        "Dy+4": Comp.Dy_plus4,
        "Er+2": Comp.Er_plus2,
        "Er+3": Comp.Er_plus3,
        "Er+4": Comp.Er_plus4,
        "Eu+2": Comp.Eu_plus2,
        "Eu+3": Comp.Eu_plus3,
        "Eu+4": Comp.Eu_plus4,
        "F-": Comp.F_minus,
        "Fe+2": Comp.Fe_plus2,
        "Fe+3": Comp.Fe_plus3,
        "FeCl+": Comp.FeCl_plus,
        "FeCl2(aq)": Comp.FeCl2_aq,
        "FeOH+2": Comp.FeOH_plus2,
        "FeOH+": Comp.FeOH_plus,
        "FeO+": Comp.FeO_plus,
        "FeO(aq)": Comp.FeO_aq,
        "HFeO2-": Comp.HFeO2_minus,
        "HFeO2(aq)": Comp.HFeO2_aq,
        "FeO2-": Comp.FeO2_minus,
        "Ga+3": Comp.Ga_plus3,
        "GaOH+2": Comp.GaOH_plus2,
        "GaO+": Comp.GaO_plus,
        "HGaO2(aq)": Comp.HGaO2_aq,
        "GaO2-": Comp.GaO2_minus,
        "Gd+2": Comp.Gd_plus2,
        "Gd+3": Comp.Gd_plus3,
        "Gd+4": Comp.Gd_plus4,
        "H+": Comp.H_plus,
        "H2(aq)": Comp.H2_aq,
        "NaH2AsO4(aq)": Comp.NaH2AsO4_aq,
        "KH2AsO4(aq)": Comp.KH2AsO4_aq,
        "MgH2AsO4+": Comp.MgH2AsO4_plus,
        "CaH2AsO4+": Comp.CaH2AsO4_plus,
        "SrH2AsO4+": Comp.SrH2AsO4_plus,
        "MnH2AsO4+": Comp.MnH2AsO4_plus,
        "FeH2AsO4+": Comp.FeH2AsO4_plus,
        "CoH2AsO4+": Comp.CoH2AsO4_plus,
        "NiH2AsO4+": Comp.NiH2AsO4_plus,
        "CuH2AsO4+": Comp.CuH2AsO4_plus,
        "ZnH2AsO4+": Comp.ZnH2AsO4_plus,
        "PbH2AsO4+": Comp.PbH2AsO4_plus,
        "AlH2AsO4+2": Comp.AlH2AsO4_plus2,
        "FeH2AsO4+2": Comp.FeH2AsO4_plus2,
        "NaHAsO4-": Comp.NaHAsO4_minus,
        "KHAsO4-": Comp.KHAsO4_minus,
        "MgHAsO4(aq)": Comp.MgHAsO4_aq,
        "CaHAsO4(aq)": Comp.CaHAsO4_aq,
        "SrHAsO4(aq)": Comp.SrHAsO4_aq,
        "MnHAsO4(aq)": Comp.MnHAsO4_aq,
        "FeHAsO4(aq)": Comp.FeHAsO4_aq,
        "CoHAsO4(aq)": Comp.CoHAsO4_aq,
        "NiHAsO4(aq)": Comp.NiHAsO4_aq,
        "CuHAsO4(aq)": Comp.CuHAsO4_aq,
        "ZnHAsO4(aq)": Comp.ZnHAsO4_aq,
        "PbHAsO4(aq)": Comp.PbHAsO4_aq,
        "AlHAsO4+": Comp.AlHAsO4_plus,
        "FeHAsO4+": Comp.FeHAsO4_plus,
        "NaAsO4-2": Comp.NaAsO4_minus2,
        "KAsO4-2": Comp.KAsO4_minus2,
        "MgAsO4-": Comp.MgAsO4_minus,
        "CaAsO4-": Comp.CaAsO4_minus,
        "SrAsO4-": Comp.SrAsO4_minus,
        "MnAsO4-": Comp.MnAsO4_minus,
        "FeAsO4-": Comp.FeAsO4_minus,
        "CoAsO4-": Comp.CoAsO4_minus,
        "NiAsO4-": Comp.NiAsO4_minus,
        "CuAsO4-": Comp.CuAsO4_minus,
        "ZnAsO4-": Comp.ZnAsO4_minus,
        "PbAsO4-": Comp.PbAsO4_minus,
        "AlAsO4(aq)": Comp.AlAsO4_aq,
        "FeAsO4(aq)": Comp.FeAsO4_aq,
        "NaH2AsO3(aq)": Comp.NaH2AsO3_aq,
        "AgH2AsO3(aq)": Comp.AgH2AsO3_aq,
        "MgH2AsO3+": Comp.MgH2AsO3_plus,
        "CaH2AsO3+": Comp.CaH2AsO3_plus,
        "SrH2AsO3+": Comp.SrH2AsO3_plus,
        "BaH2AsO3+": Comp.BaH2AsO3_plus,
        "CuH2AsO3+": Comp.CuH2AsO3_plus,
        "PbH2AsO3+": Comp.PbH2AsO3_plus,
        "AlH2AsO3+2": Comp.AlH2AsO3_plus2,
        "FeH2AsO3+2": Comp.FeH2AsO3_plus2,
        "H2P2O7-2": Comp.H2P2O7_minus2,
        "H2PO4-": Comp.H2PO4_minus,
        "H2S(aq)": Comp.H2S_aq,
        "H3VO4(aq)": Comp.H3VO4_aq,
        "H2VO4-": Comp.H2VO4_minus,
        "H3P2O7-": Comp.H3P2O7_minus,
        "H3PO4(aq)": Comp.H3PO4_aq,
        "HCO3-": Comp.HCO3_minus,
        "HCrO4-": Comp.HCrO4_minus,
        "HF(aq)": Comp.HF_aq,
        "HF2-": Comp.HF2_minus,
        "HNO3(aq)": Comp.HNO3_aq,
        "HO2-": Comp.HO2_minus,
        "HPO4-2": Comp.HPO4_minus2,
        "HS-": Comp.HS_minus,
        "HSO3-": Comp.HSO3_minus,
        "HSO4-": Comp.HSO4_minus,
        "HSO5-": Comp.HSO5_minus,
        "HSe-": Comp.HSe_minus,
        "H2SeO3(aq)": Comp.H2SeO3_aq,
        "HSeO3-": Comp.HSeO3_minus,
        "HSeO4-": Comp.HSeO4_minus,
        "HSiO3-": Comp.HSiO3_minus,
        "HVO4-2": Comp.HVO4_minus2,
        "He(aq)": Comp.He_aq,
        "Hg+2": Comp.Hg_plus2,
        "HgOH+": Comp.HgOH_plus,
        "HgO(aq)": Comp.HgO_aq,
        "HHgO2-": Comp.HHgO2_minus,
        "Hg2+2": Comp.Hg2_plus2,
        "Ho+2": Comp.Ho_plus2,
        "Ho+3": Comp.Ho_plus3,
        "Ho+4": Comp.Ho_plus4,
        "I-": Comp.I_minus,
        "I3-": Comp.I3_minus,
        "HIO(aq)": Comp.HIO_aq,
        "IO-": Comp.IO_minus,
        "IO3-": Comp.IO3_minus,
        "IO4-": Comp.IO4_minus,
        "In+3": Comp.In_plus3,
        "InOH+2": Comp.InOH_plus2,
        "InO+": Comp.InO_plus,
        "HInO2(aq)": Comp.HInO2_aq,
        "InO2-": Comp.InO2_minus,
        "K+": Comp.K_plus,
        "KBr(aq)": Comp.KBr_aq,
        "KCl(aq)": Comp.KCl_aq,
        "KAlO2(aq)": Comp.KAlO2_aq,
        "KhSO4(aq)": Comp.KhSO4_aq,
        "KI(aq)": Comp.KI_aq,
        "KOH(aq)": Comp.KOH_aq,
        "KSO4-": Comp.KSO4_minus,
        "Kr(aq)": Comp.Kr_aq,
        "La+3": Comp.La_plus3,
        "Li+": Comp.Li_plus,
        "LiCl(aq)": Comp.LiCl_aq,
        "LiOH(aq)": Comp.LiOH_aq,
        "Lu+3": Comp.Lu_plus3,
        "Lu+4": Comp.Lu_plus4,
        "Mg(HCO3)+": Comp.Mg_HCO3_plus,
        "Mg+2": Comp.Mg_plus2,
        "MgCl+": Comp.MgCl_plus,
        "MgF+": Comp.MgF_plus,
        "MgOH+": Comp.MgOH_plus,
        "Mn+2": Comp.Mn_plus2,
        "Mn+3": Comp.Mn_plus3,
        "MnCl+": Comp.MnCl_plus,
        "MnOH+": Comp.MnOH_plus,
        "MnO(aq)": Comp.MnO_aq,
        "HMnO2-": Comp.HMnO2_minus,
        "MnO2-2": Comp.MnO2_minus2,
        "MnO4-": Comp.MnO4_minus,
        "MnO4-2": Comp.MnO4_minus2,
        "MnSO4(aq)": Comp.MnSO4_aq,
        "HMoO4-": Comp.HMoO4_minus,
        "MoO4-2": Comp.MoO4_minus2,
        "N2(aq)": Comp.N2_aq,
        "NH3(aq)": Comp.NH3_aq,
        "NH4+": Comp.NH4_plus,
        "NO2-": Comp.NO2_minus,
        "NO3-": Comp.NO3_minus,
        "Na+": Comp.Na_plus,
        "NaAl(OH)4(aq)": Comp.NaAl_OH_4_aq,
        "NaBr(aq)": Comp.NaBr_aq,
        "NaCl(aq)": Comp.NaCl_aq,
        "NaF(aq)": Comp.NaF_aq,
        "NaHSiO3(aq)": Comp.NaHSiO3_aq,
        "NaI(aq)": Comp.NaI_aq,
        "NaOH(aq)": Comp.NaOH_aq,
        "Nd+2": Comp.Nd_plus2,
        "Nd+3": Comp.Nd_plus3,
        "Nd+4": Comp.Nd_plus4,
        "Ne(aq)": Comp.Ne_aq,
        "Ni+2": Comp.Ni_plus2,
        "NiCl+": Comp.NiCl_plus,
        "NiOH+": Comp.NiOH_plus,
        "NiO(aq)": Comp.NiO_aq,
        "HNiO2-": Comp.HNiO2_minus,
        "NiO2-2": Comp.NiO2_minus2,
        "O2(aq)": Comp.O2_aq,
        "OH-": Comp.OH_minus,
        "PO4-3": Comp.PO4_minus3,
        "Pb+2": Comp.Pb_plus2,
        "PbCl+": Comp.PbCl_plus,
        "PbCl2(aq)": Comp.PbCl2_aq,
        "PbCl3-": Comp.PbCl3_minus,
        "PbCl4-2": Comp.PbCl4_minus2,
        "PbOH+": Comp.PbOH_plus,
        "PbO(aq)": Comp.PbO_aq,
        "HPbO2-": Comp.HPbO2_minus,
        "Pd(OH)+": Comp.Pd_OH_plus,
        "PdSO4(aq)": Comp.PdSO4_aq,
        "Pd(SO4)2-2": Comp.Pd_SO4_2_minus2,
        "Pd(SO4)3-4": Comp.Pd_SO4_3_minus4,
        "Pd+2": Comp.Pd_plus2,
        "PdCl+": Comp.PdCl_plus,
        "PdCl2(aq)": Comp.PdCl2_aq,
        "PdCl3-": Comp.PdCl3_minus,
        "PdCl4-2": Comp.PdCl4_minus2,
        "PdO(aq)": Comp.PdO_aq,
        "Pr+2": Comp.Pr_plus2,
        "Pr+3": Comp.Pr_plus3,
        "Pr+4": Comp.Pr_plus4,
        "Pt(OH)+": Comp.Pt_OH_plus,
        "PtSO4(aq)": Comp.PtSO4_aq,
        "Pt(SO4)2-2": Comp.Pt_SO4_2_minus2,
        "Pt(SO4)3-4": Comp.Pt_SO4_3_minus4,
        "Pt+2": Comp.Pt_plus2,
        "PtCl+": Comp.PtCl_plus,
        "PtCl2(aq)": Comp.PtCl2_aq,
        "PtCl3-": Comp.PtCl3_minus,
        "PtCl4-2": Comp.PtCl4_minus2,
        "PtO(aq)": Comp.PtO_aq,
        "Ra+2": Comp.Ra_plus2,
        "Rb+": Comp.Rb_plus,
        "RbBr(aq)": Comp.RbBr_aq,
        "RbCl(aq)": Comp.RbCl_aq,
        "RbF(aq)": Comp.RbF_aq,
        "RbI(aq)": Comp.RbI_aq,
        "RbOH(aq)": Comp.RbOH_aq,
        "ReO4-": Comp.ReO4_minus,
        "Rh(OH)+": Comp.Rh_OH_plus,
        "Rh(OH)+2": Comp.Rh_OH_plus2,
        "RhSO4(aq)": Comp.RhSO4_aq,
        "Rh(SO4)+": Comp.Rh_SO4_plus,
        "Rh(SO4)2-": Comp.Rh_SO4_2_minus,
        "Rh(SO4)2-2": Comp.Rh_SO4_2_minus2,
        "Rh(SO4)3-3": Comp.Rh_SO4_3_minus3,
        "Rh(SO4)3-4": Comp.Rh_SO4_3_minus4,
        "Rh+2": Comp.Rh_plus2,
        "Rh+3": Comp.Rh_plus3,
        "RhCl+": Comp.RhCl_plus,
        "RhCl+2": Comp.RhCl_plus2,
        "RhCl2(aq)": Comp.RhCl2_aq,
        "RhCl2+": Comp.RhCl2_plus,
        "RhCl3(aq)": Comp.RhCl3_aq,
        "RhCl3-": Comp.RhCl3_minus,
        "RhCl4-": Comp.RhCl4_minus,
        "RhCl4-2": Comp.RhCl4_minus2,
        "RhO(aq)": Comp.RhO_aq,
        "RhO+": Comp.RhO_plus,
        "Rn(aq)": Comp.Rn_aq,
        "Ru(OH)+": Comp.Ru_OH_plus,
        "Ru(OH)+2": Comp.Ru_OH_plus2,
        "RuO4-2": Comp.RuO4_minus2,
        "RuSO4(aq)": Comp.RuSO4_aq,
        "Ru(SO4)+": Comp.Ru_SO4_plus,
        "Ru(SO4)2-": Comp.Ru_SO4_2_minus,
        "Ru(SO4)2-2": Comp.Ru_SO4_2_minus2,
        "Ru(SO4)3-3": Comp.Ru_SO4_3_minus3,
        "Ru(SO4)3-4": Comp.Ru_SO4_3_minus4,
        "Ru+2": Comp.Ru_plus2,
        "Ru+3": Comp.Ru_plus3,
        "RuCl+": Comp.RuCl_plus,
        "RuCl+2": Comp.RuCl_plus2,
        "RuCl2(aq)": Comp.RuCl2_aq,
        "RuCl2+": Comp.RuCl2_plus,
        "RuCl3(aq)": Comp.RuCl3_aq,
        "RuCl3-": Comp.RuCl3_minus,
        "RuCl4-": Comp.RuCl4_minus,
        "RuCl4-2": Comp.RuCl4_minus2,
        "RuCl5-2": Comp.RuCl5_minus2,
        "RuCl6-3": Comp.RuCl6_minus3,
        "RuO(aq)": Comp.RuO_aq,
        "RuO+": Comp.RuO_plus,
        "S2-2": Comp.S2_minus2,
        "S2O3-2": Comp.S2O3_minus2,
        "HS2O3-": Comp.HS2O3_minus,
        "H2S2O3(aq)": Comp.H2S2O3_aq,
        "S2O4-2": Comp.S2O4_minus2,
        "HS2O4-": Comp.HS2O4_minus,
        "H2S2O4(aq)": Comp.H2S2O4_aq,
        "S2O5-2": Comp.S2O5_minus2,
        "S2O6-2": Comp.S2O6_minus2,
        "S2O8-2": Comp.S2O8_minus2,
        "S3-2": Comp.S3_minus2,
        "S3O6-2": Comp.S3O6_minus2,
        "S4-2": Comp.S4_minus2,
        "S4O6-2": Comp.S4O6_minus2,
        "S5-2": Comp.S5_minus2,
        "S5O6-2": Comp.S5O6_minus2,
        "SO2(aq)": Comp.SO2_aq,
        "SO3-2": Comp.SO3_minus2,
        "SO4-2": Comp.SO4_minus2,
        "Sc+3": Comp.Sc_plus3,
        "ScOH+2": Comp.ScOH_plus2,
        "ScO+": Comp.ScO_plus,
        "HScO2(aq)": Comp.HScO2_aq,
        "ScO2-": Comp.ScO2_minus,
        "SeO3-2": Comp.SeO3_minus2,
        "SeO4-2": Comp.SeO4_minus2,
        "SiF6-2": Comp.SiF6_minus2,
        "SiO2(aq)": Comp.SiO2_aq,
        "Sm+2": Comp.Sm_plus2,
        "Sm+3": Comp.Sm_plus3,
        "Sm+4": Comp.Sm_plus4,
        "Sn+2": Comp.Sn_plus2,
        "SnO(aq)": Comp.SnO_aq,
        "SnOH+": Comp.SnOH_plus,
        "HSnO2-": Comp.HSnO2_minus,
        "Sr(HCO3)+": Comp.Sr_HCO3_plus,
        "Sr+2": Comp.Sr_plus2,
        "SrCl+": Comp.SrCl_plus,
        "SrF+": Comp.SrF_plus,
        "SrOH+": Comp.SrOH_plus,
        "Tb+2": Comp.Tb_plus2,
        "Tb+3": Comp.Tb_plus3,
        "Tb+4": Comp.Tb_plus4,
        "Th+4": Comp.Th_plus4,
        "Tl+": Comp.Tl_plus,
        "Tl+3": Comp.Tl_plus3,
        "TlOH(aq)": Comp.TlOH_aq,
        "TlOH+2": Comp.TlOH_plus2,
        "TlO+": Comp.TlO_plus,
        "HTlO2(aq)": Comp.HTlO2_aq,
        "TlO2-": Comp.TlO2_minus,
        "Tm+2": Comp.Tm_plus2,
        "Tm+3": Comp.Tm_plus3,
        "Tm+4": Comp.Tm_plus4,
        "U+3": Comp.U_plus3,
        "U+4": Comp.U_plus4,
        "UO2+": Comp.UO2_plus,
        "UO2+2": Comp.UO2_plus2,
        "VO+": Comp.VO_plus,
        "VO+2": Comp.VO_plus2,
        "VOH+": Comp.VOH_plus,
        "VOH+2": Comp.VOH_plus2,
        "VO2+": Comp.VO2_plus,
        "Vooh+": Comp.Vooh_plus,
        "WO4-2": Comp.WO4_minus2,
        "HWO4-": Comp.HWO4_minus,
        "Xe(aq)": Comp.Xe_aq,
        "Y+3": Comp.Y_plus3,
        "YOH+2": Comp.YOH_plus2,
        "YO+": Comp.YO_plus,
        "HYO2(aq)": Comp.HYO2_aq,
        "YO2-": Comp.YO2_minus,
        "Yb+2": Comp.Yb_plus2,
        "Yb+3": Comp.Yb_plus3,
        "Yb+4": Comp.Yb_plus4,
        "Zn+2": Comp.Zn_plus2,
        "ZnCl+": Comp.ZnCl_plus,
        "ZnCl2(aq)": Comp.ZnCl2_aq,
        "ZnCl3-": Comp.ZnCl3_minus,
        "ZnOH+": Comp.ZnOH_plus,
        "ZnO(aq)": Comp.ZnO_aq,
        "HZnO2-": Comp.HZnO2_minus,
        "ZnO2-2": Comp.ZnO2_minus2,
        "U(OH)+2": Comp.U_OH_plus2,
        "UO+": Comp.UO_plus,
        "HUO2(aq)": Comp.HUO2_aq,
        "U(OH)+3": Comp.U_OH_plus3,
        "UO+2": Comp.UO_plus2,
        "HUO2+": Comp.HUO2_plus,
        "UO2(aq)": Comp.UO2_aq,
        "HUO3-": Comp.HUO3_minus,
        "UO2OH(aq)": Comp.UO2OH_aq,
        "UO3-": Comp.UO3_minus,
        "UO2OH+": Comp.UO2OH_plus,
        "UO3(aq)": Comp.UO3_aq,
        "HUO4-": Comp.HUO4_minus,
        "UO4-2": Comp.UO4_minus2,
        "Fr+": Comp.Fr_plus,
        "HNO2(aq)": Comp.HNO2_aq,
        "H2N2O2(aq)": Comp.H2N2O2_aq,
        "HN2O2-": Comp.HN2O2_minus,
        "N2O2-2": Comp.N2O2_minus2,
        "N2H5+": Comp.N2H5_plus,
        "N2H6+2": Comp.N2H6_plus2,
        "H3PO2(aq)": Comp.H3PO2_aq,
        "H2PO2-": Comp.H2PO2_minus,
        "H3PO3(aq)": Comp.H3PO3_aq,
        "H2PO3-": Comp.H2PO3_minus,
        "HPO3-2": Comp.HPO3_minus2,
        "P2O7-4": Comp.P2O7_minus4,
        "HP2O7-3": Comp.HP2O7_minus3,
        "H4P2O7(aq)": Comp.H4P2O7_aq,
        "AsO4-3": Comp.AsO4_minus3,
        "H3AsO4(aq)": Comp.H3AsO4_aq,
        "H2AsO4-": Comp.H2AsO4_minus,
        "HAsO4-2": Comp.HAsO4_minus2,
        "HAsO2(aq)": Comp.HAsO2_aq,
        "H2AsO3-": Comp.H2AsO3_minus,
        "HAsO3-2": Comp.HAsO3_minus2,
        "AsO3-3": Comp.AsO3_minus3,
        "As3S4(HS)2-": Comp.As3S4_HS_2_minus,
        "HSbO2(aq)": Comp.HSbO2_aq,
        "SbO2-": Comp.SbO2_minus,
        "Bi+3": Comp.Bi_plus3,
        "BiO+": Comp.BiO_plus,
        "BiOH+2": Comp.BiOH_plus2,
        "HBiO2(aq)": Comp.HBiO2_aq,
        "BiO2-": Comp.BiO2_minus,
        "H2O2(aq)": Comp.H2O2_aq,
        "HClO2(aq)": Comp.HClO2_aq,
        "HIO3(aq)": Comp.HIO3_aq,
        "V+2": Comp.V_plus2,
        "V+3": Comp.V_plus3,
        "VO4-3": Comp.VO4_minus3,
        "Cr+2": Comp.Cr_plus2,
        "Cr+3": Comp.Cr_plus3,
        "CrOH+2": Comp.CrOH_plus2,
        "CrO+": Comp.CrO_plus,
        "HCrO2(aq)": Comp.HCrO2_aq,
        "CrO2-": Comp.CrO2_minus,
        "Zr+4": Comp.Zr_plus4,
        "Zr(OH)+3": Comp.Zr_OH_plus3,
        "ZrO+2": Comp.ZrO_plus2,
        "HZrO2+": Comp.HZrO2_plus,
        "ZrO2(aq)": Comp.ZrO2_aq,
        "HZrO3-": Comp.HZrO3_minus,
        "HNbO3(aq)": Comp.HNbO3_aq,
        "NbO3-": Comp.NbO3_minus,
        "TcO4-": Comp.TcO4_minus,
        "Pm+2": Comp.Pm_plus2,
        "Pm+3": Comp.Pm_plus3,
        "Pm+4": Comp.Pm_plus4,
        "Hf+4": Comp.Hf_plus4,
        "HfOH+3": Comp.HfOH_plus3,
        "HfO+2": Comp.HfO_plus2,
        "HHfO2+": Comp.HHfO2_plus,
        "HfO2(aq)": Comp.HfO2_aq,
        "HHfO3-": Comp.HHfO3_minus,
        "La+2": Comp.La_plus2,
        "LaCO3+": Comp.LaCO3_plus,
        "LaHCO3+2": Comp.LaHCO3_plus2,
        "LaOH+2": Comp.LaOH_plus2,
        "LaO+": Comp.LaO_plus,
        "LaO2H(aq)": Comp.LaO2H_aq,
        "LaO2-": Comp.LaO2_minus,
        "LaCl+2": Comp.LaCl_plus2,
        "LaCl2+": Comp.LaCl2_plus,
        "LaCl3(aq)": Comp.LaCl3_aq,
        "LaCl4-": Comp.LaCl4_minus,
        "LaNO3+2": Comp.LaNO3_plus2,
        "LaF+2": Comp.LaF_plus2,
        "LaF2+": Comp.LaF2_plus,
        "LaF3(aq)": Comp.LaF3_aq,
        "LaF4-": Comp.LaF4_minus,
        "LaH2PO4+2": Comp.LaH2PO4_plus2,
        "LaSO4+": Comp.LaSO4_plus,
        "CeCO3+": Comp.CeCO3_plus,
        "CeHCO3+2": Comp.CeHCO3_plus2,
        "CeOH+2": Comp.CeOH_plus2,
        "CeO+": Comp.CeO_plus,
        "CeO2H(aq)": Comp.CeO2H_aq,
        "CeO2-": Comp.CeO2_minus,
        "CeCl+2": Comp.CeCl_plus2,
        "CeCl2+": Comp.CeCl2_plus,
        "CeCl3(aq)": Comp.CeCl3_aq,
        "CeCl4-": Comp.CeCl4_minus,
        "CeH2PO4+2": Comp.CeH2PO4_plus2,
        "CeNO3+2": Comp.CeNO3_plus2,
        "CeF+2": Comp.CeF_plus2,
        "CeF2+": Comp.CeF2_plus,
        "CeF3(aq)": Comp.CeF3_aq,
        "CeF4-": Comp.CeF4_minus,
        "CeBr+2": Comp.CeBr_plus2,
        "CeIO3+2": Comp.CeIO3_plus2,
        "CeClO4+2": Comp.CeClO4_plus2,
        "CeSO4+": Comp.CeSO4_plus,
        "PrCO3+": Comp.PrCO3_plus,
        "PrHCO3+2": Comp.PrHCO3_plus2,
        "PrCl+2": Comp.PrCl_plus2,
        "PrCl2+": Comp.PrCl2_plus,
        "PrCl3(aq)": Comp.PrCl3_aq,
        "PrCl4-": Comp.PrCl4_minus,
        "PrH2PO4+2": Comp.PrH2PO4_plus2,
        "PrNO3+2": Comp.PrNO3_plus2,
        "PrF+2": Comp.PrF_plus2,
        "PrF2+": Comp.PrF2_plus,
        "PrF3(aq)": Comp.PrF3_aq,
        "PrF4-": Comp.PrF4_minus,
        "PrOH+2": Comp.PrOH_plus2,
        "PrO+": Comp.PrO_plus,
        "PrO2H(aq)": Comp.PrO2H_aq,
        "PrO2-": Comp.PrO2_minus,
        "PrSO4+": Comp.PrSO4_plus,
        "NdCO3+": Comp.NdCO3_plus,
        "NdHCO3+2": Comp.NdHCO3_plus2,
        "NdOH+2": Comp.NdOH_plus2,
        "NdO+": Comp.NdO_plus,
        "NdO2H(aq)": Comp.NdO2H_aq,
        "NdO2-": Comp.NdO2_minus,
        "NdCl+2": Comp.NdCl_plus2,
        "NdCl2+": Comp.NdCl2_plus,
        "NdCl3(aq)": Comp.NdCl3_aq,
        "NdCl4-": Comp.NdCl4_minus,
        "NdH2PO4+2": Comp.NdH2PO4_plus2,
        "NdNO3+2": Comp.NdNO3_plus2,
        "NdF+2": Comp.NdF_plus2,
        "NdF2+": Comp.NdF2_plus,
        "NdF3(aq)": Comp.NdF3_aq,
        "NdF4-": Comp.NdF4_minus,
        "NdSO4+": Comp.NdSO4_plus,
        "SmCO3+": Comp.SmCO3_plus,
        "SmOH+2": Comp.SmOH_plus2,
        "SmO+": Comp.SmO_plus,
        "SmO2H(aq)": Comp.SmO2H_aq,
        "SmO2-": Comp.SmO2_minus,
        "SmHCO3+2": Comp.SmHCO3_plus2,
        "SmCl+2": Comp.SmCl_plus2,
        "SmCl2+": Comp.SmCl2_plus,
        "SmCl3(aq)": Comp.SmCl3_aq,
        "SmCl4-": Comp.SmCl4_minus,
        "SmH2PO4+2": Comp.SmH2PO4_plus2,
        "SmNO3+2": Comp.SmNO3_plus2,
        "SmF+2": Comp.SmF_plus2,
        "SmF2+": Comp.SmF2_plus,
        "SmF3(aq)": Comp.SmF3_aq,
        "SmF4-": Comp.SmF4_minus,
        "SmSO4+": Comp.SmSO4_plus,
        "EuCO3+": Comp.EuCO3_plus,
        "EuOH+2": Comp.EuOH_plus2,
        "EuO+": Comp.EuO_plus,
        "EuO2H(aq)": Comp.EuO2H_aq,
        "EuO2-": Comp.EuO2_minus,
        "EuHCO3+2": Comp.EuHCO3_plus2,
        "EuCl+2": Comp.EuCl_plus2,
        "EuCl2+": Comp.EuCl2_plus,
        "EuCl3(aq)": Comp.EuCl3_aq,
        "EuCl4-": Comp.EuCl4_minus,
        "EuF+": Comp.EuF_plus,
        "EuF2(aq)": Comp.EuF2_aq,
        "EuF3-": Comp.EuF3_minus,
        "EuF4-2": Comp.EuF4_minus2,
        "EuCl+": Comp.EuCl_plus,
        "EuCl2(aq)": Comp.EuCl2_aq,
        "EuCl3-": Comp.EuCl3_minus,
        "EuCl4-2": Comp.EuCl4_minus2,
        "EuH2PO4+2": Comp.EuH2PO4_plus2,
        "EuNO3+2": Comp.EuNO3_plus2,
        "EuF+2": Comp.EuF_plus2,
        "EuF2+": Comp.EuF2_plus,
        "EuF3(aq)": Comp.EuF3_aq,
        "EuF4-": Comp.EuF4_minus,
        "EuSO4+": Comp.EuSO4_plus,
        "GdCO3+": Comp.GdCO3_plus,
        "GdOH+2": Comp.GdOH_plus2,
        "GdO+": Comp.GdO_plus,
        "GdO2H(aq)": Comp.GdO2H_aq,
        "GdO2-": Comp.GdO2_minus,
        "GdHCO3+2": Comp.GdHCO3_plus2,
        "GdCl+2": Comp.GdCl_plus2,
        "GdCl2+": Comp.GdCl2_plus,
        "GdCl3(aq)": Comp.GdCl3_aq,
        "GdCl4-": Comp.GdCl4_minus,
        "GdH2PO4+2": Comp.GdH2PO4_plus2,
        "GdNO3+2": Comp.GdNO3_plus2,
        "GdF+2": Comp.GdF_plus2,
        "GdF2+": Comp.GdF2_plus,
        "GdF3(aq)": Comp.GdF3_aq,
        "GdF4-": Comp.GdF4_minus,
        "GdSO4+": Comp.GdSO4_plus,
        "TbCO3+": Comp.TbCO3_plus,
        "TbOH+2": Comp.TbOH_plus2,
        "TbO+": Comp.TbO_plus,
        "TbO2H(aq)": Comp.TbO2H_aq,
        "TbO2-": Comp.TbO2_minus,
        "TbHCO3+2": Comp.TbHCO3_plus2,
        "TbCl+2": Comp.TbCl_plus2,
        "TbCl2+": Comp.TbCl2_plus,
        "TbCl3(aq)": Comp.TbCl3_aq,
        "TbCl4-": Comp.TbCl4_minus,
        "TbH2PO4+2": Comp.TbH2PO4_plus2,
        "TbNO3+2": Comp.TbNO3_plus2,
        "TbF+2": Comp.TbF_plus2,
        "TbF2+": Comp.TbF2_plus,
        "TbF3(aq)": Comp.TbF3_aq,
        "TbF4-": Comp.TbF4_minus,
        "TbSO4+": Comp.TbSO4_plus,
        "DyCO3+": Comp.DyCO3_plus,
        "DyHCO3+2": Comp.DyHCO3_plus2,
        "DyCl+2": Comp.DyCl_plus2,
        "DyCl2+": Comp.DyCl2_plus,
        "DyCl3(aq)": Comp.DyCl3_aq,
        "DyCl4-": Comp.DyCl4_minus,
        "DyH2PO4+2": Comp.DyH2PO4_plus2,
        "DyNO3+2": Comp.DyNO3_plus2,
        "DyF+2": Comp.DyF_plus2,
        "DyF2+": Comp.DyF2_plus,
        "DyF3(aq)": Comp.DyF3_aq,
        "DyF4-": Comp.DyF4_minus,
        "DyOH+2": Comp.DyOH_plus2,
        "DyO+": Comp.DyO_plus,
        "DyO2H(aq)": Comp.DyO2H_aq,
        "DyO2-": Comp.DyO2_minus,
        "DySO4+": Comp.DySO4_plus,
        "HoCO3+": Comp.HoCO3_plus,
        "HoHCO3+2": Comp.HoHCO3_plus2,
        "HoCl+2": Comp.HoCl_plus2,
        "HoCl2+": Comp.HoCl2_plus,
        "HoCl3(aq)": Comp.HoCl3_aq,
        "HoCl4-": Comp.HoCl4_minus,
        "HoH2PO4+2": Comp.HoH2PO4_plus2,
        "HoNO3+2": Comp.HoNO3_plus2,
        "HoF+2": Comp.HoF_plus2,
        "HoF2+": Comp.HoF2_plus,
        "HoF3(aq)": Comp.HoF3_aq,
        "HoF4-": Comp.HoF4_minus,
        "HoOH+2": Comp.HoOH_plus2,
        "HoO+": Comp.HoO_plus,
        "HoO2H(aq)": Comp.HoO2H_aq,
        "HoO2-": Comp.HoO2_minus,
        "HoSO4+": Comp.HoSO4_plus,
        "ErCO3+": Comp.ErCO3_plus,
        "ErHCO3+2": Comp.ErHCO3_plus2,
        "ErCl+2": Comp.ErCl_plus2,
        "ErCl2+": Comp.ErCl2_plus,
        "ErCl3(aq)": Comp.ErCl3_aq,
        "ErCl4-": Comp.ErCl4_minus,
        "ErH2PO4+2": Comp.ErH2PO4_plus2,
        "ErNO3+2": Comp.ErNO3_plus2,
        "ErF+2": Comp.ErF_plus2,
        "ErF2+": Comp.ErF2_plus,
        "ErF3(aq)": Comp.ErF3_aq,
        "ErF4-": Comp.ErF4_minus,
        "ErOH+2": Comp.ErOH_plus2,
        "ErO+": Comp.ErO_plus,
        "ErO2H(aq)": Comp.ErO2H_aq,
        "ErO2-": Comp.ErO2_minus,
        "ErSO4+": Comp.ErSO4_plus,
        "TmCO3+": Comp.TmCO3_plus,
        "TmHCO3+2": Comp.TmHCO3_plus2,
        "TmCl+2": Comp.TmCl_plus2,
        "TmCl2+": Comp.TmCl2_plus,
        "TmCl3(aq)": Comp.TmCl3_aq,
        "TmCl4-": Comp.TmCl4_minus,
        "TmH2PO4+2": Comp.TmH2PO4_plus2,
        "TmNO3+2": Comp.TmNO3_plus2,
        "TmF+2": Comp.TmF_plus2,
        "TmF2+": Comp.TmF2_plus,
        "TmF3(aq)": Comp.TmF3_aq,
        "TmF4-": Comp.TmF4_minus,
        "TmOH+2": Comp.TmOH_plus2,
        "TmO+": Comp.TmO_plus,
        "TmO2H(aq)": Comp.TmO2H_aq,
        "TmO2-": Comp.TmO2_minus,
        "TmSO4+": Comp.TmSO4_plus,
        "YbCO3+": Comp.YbCO3_plus,
        "YbOH+2": Comp.YbOH_plus2,
        "YbO+": Comp.YbO_plus,
        "YbO2H(aq)": Comp.YbO2H_aq,
        "YbO2-": Comp.YbO2_minus,
        "YbHCO3+2": Comp.YbHCO3_plus2,
        "YbCl+2": Comp.YbCl_plus2,
        "YbCl2+": Comp.YbCl2_plus,
        "YbCl3(aq)": Comp.YbCl3_aq,
        "YbCl4-": Comp.YbCl4_minus,
        "YbH2PO4+2": Comp.YbH2PO4_plus2,
        "YbNO3+2": Comp.YbNO3_plus2,
        "YbF+2": Comp.YbF_plus2,
        "YbF2+": Comp.YbF2_plus,
        "YbF3(aq)": Comp.YbF3_aq,
        "YbF4-": Comp.YbF4_minus,
        "YbSO4+": Comp.YbSO4_plus,
        "LuCO3+": Comp.LuCO3_plus,
        "LuOH+2": Comp.LuOH_plus2,
        "LuO+": Comp.LuO_plus,
        "LuO2H(aq)": Comp.LuO2H_aq,
        "LuO2-": Comp.LuO2_minus,
        "LuHCO3+2": Comp.LuHCO3_plus2,
        "LuCl+2": Comp.LuCl_plus2,
        "LuCl2+": Comp.LuCl2_plus,
        "LuCl3(aq)": Comp.LuCl3_aq,
        "LuCl4-": Comp.LuCl4_minus,
        "LuH2PO4+2": Comp.LuH2PO4_plus2,
        "LuNO3+2": Comp.LuNO3_plus2,
        "LuF+2": Comp.LuF_plus2,
        "LuF2+": Comp.LuF2_plus,
        "LuF3(aq)": Comp.LuF3_aq,
        "LuF4-": Comp.LuF4_minus,
        "LuSO4+": Comp.LuSO4_plus,
        "NaSO4-": Comp.NaSO4_minus,
        "MgSO4(aq)": Comp.MgSO4_aq,
        "HCl(aq)": Comp.HCl_aq,
        "MgCO3(aq)": Comp.MgCO3_aq,
        "CaCO3(aq)": Comp.CaCO3_aq,
        "SrCO3(aq)": Comp.SrCO3_aq,
        "BaCO3(aq)": Comp.BaCO3_aq,
        "BeCl+": Comp.BeCl_plus,
        "BeCl2(aq)": Comp.BeCl2_aq,
        "FeCl+2": Comp.FeCl_plus2,
        "CoCl+": Comp.CoCl_plus,
        "CuCl(aq)": Comp.CuCl_aq,
        "CuCl2-": Comp.CuCl2_minus,
        "CuCl3-2": Comp.CuCl3_minus2,
        "CuCl+": Comp.CuCl_plus,
        "CuCl2(aq)": Comp.CuCl2_aq,
        "CuCl3-": Comp.CuCl3_minus,
        "CuCl4-2": Comp.CuCl4_minus2,
        "CdCl+": Comp.CdCl_plus,
        "CdCl2(aq)": Comp.CdCl2_aq,
        "CdCl3-": Comp.CdCl3_minus,
        "CdCl4-2": Comp.CdCl4_minus2,
        "TlCl(aq)": Comp.TlCl_aq,
        "TlCl+2": Comp.TlCl_plus2,
        "AuCl(aq)": Comp.AuCl_aq,
        "AuCl2-": Comp.AuCl2_minus,
        "AuCl3-2": Comp.AuCl3_minus2,
        "AuCl4-": Comp.AuCl4_minus,
        "HgCl+": Comp.HgCl_plus,
        "HgCl2(aq)": Comp.HgCl2_aq,
        "HgCl3-": Comp.HgCl3_minus,
        "HgCl4-2": Comp.HgCl4_minus2,
        "InCl+2": Comp.InCl_plus2,
        "BeF+": Comp.BeF_plus,
        "BeF2(aq)": Comp.BeF2_aq,
        "BeF3-": Comp.BeF3_minus,
        "BeF4-2": Comp.BeF4_minus2,
        "MnF+": Comp.MnF_plus,
        "FeF+": Comp.FeF_plus,
        "FeF+2": Comp.FeF_plus2,
        "CoF+": Comp.CoF_plus,
        "NiF+": Comp.NiF_plus,
        "CuF+": Comp.CuF_plus,
        "ZnF+": Comp.ZnF_plus,
        "AgF(aq)": Comp.AgF_aq,
        "CdF+": Comp.CdF_plus,
        "CdF2(aq)": Comp.CdF2_aq,
        "BaF+": Comp.BaF_plus,
        "TlF(aq)": Comp.TlF_aq,
        "HgF+": Comp.HgF_plus,
        "InF+2": Comp.InF_plus2,
        "PbF+": Comp.PbF_plus,
        "PbF2(aq)": Comp.PbF2_aq,
        "Ag(HS)2-": Comp.Ag_HS_2_minus,
        "Au(HS)2-": Comp.Au_HS_2_minus,
        "Pb(HS)2(aq)": Comp.Pb_HS_2_aq,
        "Pb(HS)3-": Comp.Pb_HS_3_minus,
        "Mg(HSiO3)+": Comp.Mg_HSiO3_plus,
        "Ca(HSiO3)+": Comp.Ca_HSiO3_plus,
        "AlF+2": Comp.AlF_plus2,
        "AlF2+": Comp.AlF2_plus,
        "AlF3(aq)": Comp.AlF3_aq,
        "AlF4-": Comp.AlF4_minus,
        "Al(OH)2F2-": Comp.Al_OH_2F2_minus,
        "Al(OH)2F(aq)": Comp.Al_OH_2F_aq,
        "Al(OH)F2(aq)": Comp.Al_OH_F2_aq,
        "AlSO4+": Comp.AlSO4_plus,
        "NaAl(OH)3F(aq)": Comp.NaAl_OH_3F_aq,
        "NaAl(OH)2F2(aq)": Comp.NaAl_OH_2F2_aq,
        "CH4(aq)": Comp.CH4_aq,
        "H-Acetate(aq)": Comp.H_Acetate_aq,
        "Acetate-": Comp.Acetate_minus,
        "1-Butanamine(aq)": Comp._1_Butanamine_aq,
        "1-Butanol(aq)": Comp._1_Butanol_aq,
        "1-Butene(aq)": Comp._1_Butene_aq,
        "1-Butyne(aq)": Comp._1_Butyne_aq,
        "1-Heptanamine(aq)": Comp._1_Heptanamine_aq,
        "1-Heptanol(aq)": Comp._1_Heptanol_aq,
        "1-Heptene(aq)": Comp._1_Heptene_aq,
        "1-Heptyne(aq)": Comp._1_Heptyne_aq,
        "1-Hexanamine(aq)": Comp._1_Hexanamine_aq,
        "1-Hexanol(aq)": Comp._1_Hexanol_aq,
        "1-Hexene(aq)": Comp._1_Hexene_aq,
        "1-Hexyne(aq)": Comp._1_Hexyne_aq,
        "1-Octanamine(aq)": Comp._1_Octanamine_aq,
        "1-Octanol(aq)": Comp._1_Octanol_aq,
        "1-Octene(aq)": Comp._1_Octene_aq,
        "1-Octyne(aq)": Comp._1_Octyne_aq,
        "1-Pentanamine(aq)": Comp._1_Pentanamine_aq,
        "1-Pentanol(aq)": Comp._1_Pentanol_aq,
        "1-Pentene(aq)": Comp._1_Pentene_aq,
        "1-Pentyne(aq)": Comp._1_Pentyne_aq,
        "1-Propanamine(aq)": Comp._1_Propanamine_aq,
        "1-Propanol(aq)": Comp._1_Propanol_aq,
        "1-Propene(aq)": Comp._1_Propene_aq,
        "1-Propyne(aq)": Comp._1_Propyne_aq,
        "2-Butanone(aq)": Comp._2_Butanone_aq,
        "2-Heptanone(aq)": Comp._2_Heptanone_aq,
        "2-Hexanone(aq)": Comp._2_Hexanone_aq,
        "2-Hydroxybutanoate": Comp._2_Hydroxybutanoate,
        "2-Hydroxybutanoic(aq)": Comp._2_Hydroxybutanoic_aq,
        "2-Hydroxydecanoate": Comp._2_Hydroxydecanoate,
        "2-Hydroxydecanoic(aq)": Comp._2_Hydroxydecanoic_aq,
        "2-Hydroxyheptanoic": Comp._2_Hydroxyheptanoic,
        "2-Hydroxyhexanoate": Comp._2_Hydroxyhexanoate,
        "2-Hydroxyhexanoic(aq)": Comp._2_Hydroxyhexanoic_aq,
        "2-Hydroxynonanoate": Comp._2_Hydroxynonanoate,
        "2-Hydroxynonanoic(aq)": Comp._2_Hydroxynonanoic_aq,
        "2-Hydroxyoctanoate": Comp._2_Hydroxyoctanoate,
        "2-Hydroxyoctanoic(aq)": Comp._2_Hydroxyoctanoic_aq,
        "2-Hydroxypentanoic": Comp._2_Hydroxypentanoic,
        "2-Octanone(aq)": Comp._2_Octanone_aq,
        "2-Pentanone(aq)": Comp._2_Pentanone_aq,
        "A-Aminobutyric(aq)": Comp.A_Aminobutyric_aq,
        "Acetamide(aq)": Comp.Acetamide_aq,
        "Acetone(aq)": Comp.Acetone_aq,
        "Adipate": Comp.Adipate,
        "Adipic-Acid(aq)": Comp.Adipic_Acid_aq,
        "Alanylglycine(aq)": Comp.Alanylglycine_aq,
        "Asparagine(aq)": Comp.Asparagine_aq,
        "Aspartic-Acid(aq)": Comp.Aspartic_Acid_aq,
        "Azelaic-Acid(aq)": Comp.Azelaic_Acid_aq,
        "Azelate": Comp.Azelate,
        "Benzene(aq)": Comp.Benzene_aq,
        "Benzoate": Comp.Benzoate,
        "Benzoic-Acid(aq)": Comp.Benzoic_Acid_aq,
        "o-Cresol(aq)": Comp.o_Cresol_aq,
        "m-Cresol(aq)": Comp.m_Cresol_aq,
        "p-Cresol(aq)": Comp.p_Cresol_aq,
        "Decanoate": Comp.Decanoate,
        "Decanoic-Acid(aq)": Comp.Decanoic_Acid_aq,
        "2,3-DMP(aq)": Comp._2_3_DMP_aq,
        "2,4-DMP(aq)": Comp._2_4_DMP_aq,
        "2,5-DMP(aq)": Comp._2_5_DMP_aq,
        "2,6-DMP(aq)": Comp._2_6_DMP_aq,
        "3,4-DMP(aq)": Comp._3_4_DMP_aq,
        "3,5-DMP(aq)": Comp._3_5_DMP_aq,
        "Dodecanoate": Comp.Dodecanoate,
        "Dodecanoic-Acid(aq)": Comp.Dodecanoic_Acid_aq,
        "Ethanamine(aq)": Comp.Ethanamine_aq,
        "Ethane(aq)": Comp.Ethane_aq,
        "Ethanol(aq)": Comp.Ethanol_aq,
        "Ethylacetate(aq)": Comp.Ethylacetate_aq,
        "Ethylbenzene(aq)": Comp.Ethylbenzene_aq,
        "Ethylene(aq)": Comp.Ethylene_aq,
        "Ethyne(aq)": Comp.Ethyne_aq,
        "Glutamic-Acid(aq)": Comp.Glutamic_Acid_aq,
        "Glutamine(aq)": Comp.Glutamine_aq,
        "Glutarate": Comp.Glutarate,
        "Glutaric-Acid(aq)": Comp.Glutaric_Acid_aq,
        "Diglycine(aq)": Comp.Diglycine_aq,
        "H-Adipate": Comp.H_Adipate,
        "H-Azelate": Comp.H_Azelate,
        "H-Glutarate": Comp.H_Glutarate,
        "H-Malonate": Comp.H_Malonate,
        "H-Oxalate": Comp.H_Oxalate,
        "H-Pimelate": Comp.H_Pimelate,
        "H-Sebacate": Comp.H_Sebacate,
        "H-Suberate": Comp.H_Suberate,
        "H-Succinate": Comp.H_Succinate,
        "Heptanoate": Comp.Heptanoate,
        "Heptanoic-Acid(aq)": Comp.Heptanoic_Acid_aq,
        "Hexanoate": Comp.Hexanoate,
        "Hexanoic-Acid(aq)": Comp.Hexanoic_Acid_aq,
        "Isoleucine(aq)": Comp.Isoleucine_aq,
        "Leucine(aq)": Comp.Leucine_aq,
        "m-Toluate": Comp.m_Toluate,
        "m-Toluic-Acid(aq)": Comp.m_Toluic_Acid_aq,
        "Malonate": Comp.Malonate,
        "Malonic-Acid(aq)": Comp.Malonic_Acid_aq,
        "Methanamine(aq)": Comp.Methanamine_aq,
        "Methanol(aq)": Comp.Methanol_aq,
        "Methionine(aq)": Comp.Methionine_aq,
        "n-Butane(aq)": Comp.n_Butane_aq,
        "n-Butylbenzene(aq)": Comp.n_Butylbenzene_aq,
        "n-Heptane(aq)": Comp.n_Heptane_aq,
        "n-Heptylbenzene(aq)": Comp.n_Heptylbenzene_aq,
        "n-Hexane(aq)": Comp.n_Hexane_aq,
        "n-Hexylbenzene(aq)": Comp.n_Hexylbenzene_aq,
        "n-Octane(aq)": Comp.n_Octane_aq,
        "n-Octylbenzene(aq)": Comp.n_Octylbenzene_aq,
        "n-Pentane(aq)": Comp.n_Pentane_aq,
        "n-Pentylbenzene(aq)": Comp.n_Pentylbenzene_aq,
        "n-Propylbenzene(aq)": Comp.n_Propylbenzene_aq,
        "Nonanoate": Comp.Nonanoate,
        "Nonanoic-Acid(aq)": Comp.Nonanoic_Acid_aq,
        "o-Toluate": Comp.o_Toluate,
        "o-Toluic-Acid(aq)": Comp.o_Toluic_Acid_aq,
        "Octanoate": Comp.Octanoate,
        "Octanoic-Acid(aq)": Comp.Octanoic_Acid_aq,
        "Oxalate": Comp.Oxalate,
        "Oxalic-Acid(aq)": Comp.Oxalic_Acid_aq,
        "p-Toluate": Comp.p_Toluate,
        "p-Toluic-Acid(aq)": Comp.p_Toluic_Acid_aq,
        "Phenol(aq)": Comp.Phenol_aq,
        "Phenylalanine(aq)": Comp.Phenylalanine_aq,
        "Pimelate": Comp.Pimelate,
        "Pimelic-Acid(aq)": Comp.Pimelic_Acid_aq,
        "Propane(aq)": Comp.Propane_aq,
        "Sebacate": Comp.Sebacate,
        "Sebacic-Acid(aq)": Comp.Sebacic_Acid_aq,
        "Serine(aq)": Comp.Serine_aq,
        "Suberate": Comp.Suberate,
        "Suberic-Acid(aq)": Comp.Suberic_Acid_aq,
        "Succinate": Comp.Succinate,
        "Succinic-Acid(aq)": Comp.Succinic_Acid_aq,
        "Threonine(aq)": Comp.Threonine_aq,
        "Toluene(aq)": Comp.Toluene_aq,
        "Tryptophan(aq)": Comp.Tryptophan_aq,
        "Tyrosine(aq)": Comp.Tyrosine_aq,
        "Undecanoate": Comp.Undecanoate,
        "Undecanoic-Acid(aq)": Comp.Undecanoic_Acid_aq,
        "Urea(aq)": Comp.Urea_aq,
        "Valine(aq)": Comp.Valine_aq,
        "Acetaldehyde(aq)": Comp.Acetaldehyde_aq,
        "Butanal(aq)": Comp.Butanal_aq,
        "Decanal(aq)": Comp.Decanal_aq,
        "Formaldehyde(aq)": Comp.Formaldehyde_aq,
        "Heptanal(aq)": Comp.Heptanal_aq,
        "Hexanal(aq)": Comp.Hexanal_aq,
        "Nonanal(aq)": Comp.Nonanal_aq,
        "Octanal(aq)": Comp.Octanal_aq,
        "Pentanal(aq)": Comp.Pentanal_aq,
        "Propanal(aq)": Comp.Propanal_aq,
        "HCN(aq)": Comp.HCN_aq,
        "CN-": Comp.CN_minus,
        "OCN-": Comp.OCN_minus,
        "SCN-": Comp.SCN_minus,
        "SeCN-": Comp.SeCN_minus,
        "Bi(Ac)+2": Comp.Bi_Ac_plus2,
        "Bi(Ac)2+": Comp.Bi_Ac_2_plus,
        "Bi(Ac)3(aq)": Comp.Bi_Ac_3_aq,
        "Dy(Ac)+2": Comp.Dy_Ac_plus2,
        "Dy(Ac)2+": Comp.Dy_Ac_2_plus,
        "Dy(Ac)3(aq)": Comp.Dy_Ac_3_aq,
        "Ho(Ac)+2": Comp.Ho_Ac_plus2,
        "Ho(Ac)2+": Comp.Ho_Ac_2_plus,
        "Ho(Ac)3(aq)": Comp.Ho_Ac_3_aq,
        "Er(Ac)+2": Comp.Er_Ac_plus2,
        "Er(Ac)2+": Comp.Er_Ac_2_plus,
        "Er(Ac)3(aq)": Comp.Er_Ac_3_aq,
        "Tm(Ac)+2": Comp.Tm_Ac_plus2,
        "Tm(Ac)2+": Comp.Tm_Ac_2_plus,
        "Tm(Ac)3(aq)": Comp.Tm_Ac_3_aq,
        "Be(Ac)+": Comp.Be_Ac_plus,
        "Be(Ac)2(aq)": Comp.Be_Ac_2_aq,
        "Ra(Ac)+": Comp.Ra_Ac_plus,
        "Ra(Ac)2(aq)": Comp.Ra_Ac_2_aq,
        "Au(Ac)(aq)": Comp.Au_Ac_aq,
        "Au(Ac)2-": Comp.Au_Ac_2_minus,
        "Li(Ac)(aq)": Comp.Li_Ac_aq,
        "Li(Ac)2-": Comp.Li_Ac_2_minus,
        "Na(Ac)(aq)": Comp.Na_Ac_aq,
        "Na(Ac)2-": Comp.Na_Ac_2_minus,
        "K(Ac)(aq)": Comp.K_Ac_aq,
        "K(Ac)2-": Comp.K_Ac_2_minus,
        "Mg(Ac)+": Comp.Mg_Ac_plus,
        "Mg(Ac)2(aq)": Comp.Mg_Ac_2_aq,
        "Sr(Ac)+": Comp.Sr_Ac_plus,
        "Sr(Ac)2(aq)": Comp.Sr_Ac_2_aq,
        "Ba(Ac)+": Comp.Ba_Ac_plus,
        "Ba(Ac)2(aq)": Comp.Ba_Ac_2_aq,
        "Cu(Ac)(aq)": Comp.Cu_Ac_aq,
        "Cu(Ac)2-": Comp.Cu_Ac_2_minus,
        "Rb(Ac)(aq)": Comp.Rb_Ac_aq,
        "Rb(Ac)2-": Comp.Rb_Ac_2_minus,
        "Tl(Ac)(aq)": Comp.Tl_Ac_aq,
        "Tl(Ac)2-": Comp.Tl_Ac_2_minus,
        "Cs(Ac)(aq)": Comp.Cs_Ac_aq,
        "Cs(Ac)2-": Comp.Cs_Ac_2_minus,
        "Pb(Ac)+": Comp.Pb_Ac_plus,
        "Pb(Ac)2(aq)": Comp.Pb_Ac_2_aq,
        "Mn(Ac)+": Comp.Mn_Ac_plus,
        "Mn(Ac)2(aq)": Comp.Mn_Ac_2_aq,
        "Mn(Ac)3-": Comp.Mn_Ac_3_minus,
        "Co(Ac)+": Comp.Co_Ac_plus,
        "Co(Ac)2(aq)": Comp.Co_Ac_2_aq,
        "Co(Ac)3-": Comp.Co_Ac_3_minus,
        "Ni(Ac)+": Comp.Ni_Ac_plus,
        "Ni(Ac)2(aq)": Comp.Ni_Ac_2_aq,
        "Ni(Ac)3-": Comp.Ni_Ac_3_minus,
        "Cu(Ac)+": Comp.Cu_Ac_plus,
        "Cu(Ac)2(aq)": Comp.Cu_Ac_2_aq,
        "Cu(Ac)3-": Comp.Cu_Ac_3_minus,
        "NH4(Ac)(aq)": Comp.NH4_Ac_aq,
        "NH4(Ac)2-": Comp.NH4_Ac_2_minus,
        "UO2(Ac)+": Comp.UO2_Ac_plus,
        "UO2(Ac)2(aq)": Comp.UO2_Ac_2_aq,
        "UO2(Ac)3-": Comp.UO2_Ac_3_minus,
        "Ag(Ac)(aq)": Comp.Ag_Ac_aq,
        "Ag(Ac)2-": Comp.Ag_Ac_2_minus,
        "Cd(Ac)+": Comp.Cd_Ac_plus,
        "Cd(Ac)2(aq)": Comp.Cd_Ac_2_aq,
        "Cd(Ac)3-": Comp.Cd_Ac_3_minus,
        "Hg(Ac)+": Comp.Hg_Ac_plus,
        "Hg(Ac)2(aq)": Comp.Hg_Ac_2_aq,
        "Hg(Ac)3-": Comp.Hg_Ac_3_minus,
        "Sc(Ac)+2": Comp.Sc_Ac_plus2,
        "Sc(Ac)2+": Comp.Sc_Ac_2_plus,
        "Sc(Ac)3(aq)": Comp.Sc_Ac_3_aq,
        "U(Ac)+2": Comp.U_Ac_plus2,
        "U(Ac)2+": Comp.U_Ac_2_plus,
        "U(Ac)3(aq)": Comp.U_Ac_3_aq,
        "Pr(Ac)+2": Comp.Pr_Ac_plus2,
        "Pr(Ac)2+": Comp.Pr_Ac_2_plus,
        "Pr(Ac)3(aq)": Comp.Pr_Ac_3_aq,
        "La(Ac)+2": Comp.La_Ac_plus2,
        "La(Ac)2+": Comp.La_Ac_2_plus,
        "La(Ac)3(aq)": Comp.La_Ac_3_aq,
        "Nd(Ac)+2": Comp.Nd_Ac_plus2,
        "Nd(Ac)2+": Comp.Nd_Ac_2_plus,
        "Nd(Ac)3(aq)": Comp.Nd_Ac_3_aq,
        "Ce(Ac)+2": Comp.Ce_Ac_plus2,
        "Ce(Ac)2+": Comp.Ce_Ac_2_plus,
        "Ce(Ac)3(aq)": Comp.Ce_Ac_3_aq,
        "Gd(Ac)+2": Comp.Gd_Ac_plus2,
        "Gd(Ac)2+": Comp.Gd_Ac_2_plus,
        "Gd(Ac)3(aq)": Comp.Gd_Ac_3_aq,
        "Sm(Ac)+2": Comp.Sm_Ac_plus2,
        "Sm(Ac)2+": Comp.Sm_Ac_2_plus,
        "Sm(Ac)3(aq)": Comp.Sm_Ac_3_aq,
        "Yb(Ac)+2": Comp.Yb_Ac_plus2,
        "Yb(Ac)2+": Comp.Yb_Ac_2_plus,
        "Yb(Ac)3(aq)": Comp.Yb_Ac_3_aq,
        "Eu(Ac)+2": Comp.Eu_Ac_plus2,
        "Eu(Ac)2+": Comp.Eu_Ac_2_plus,
        "Eu(Ac)3(aq)": Comp.Eu_Ac_3_aq,
        "Y(Ac)+2": Comp.Y_Ac_plus2,
        "Y(Ac)2+": Comp.Y_Ac_2_plus,
        "Y(Ac)3(aq)": Comp.Y_Ac_3_aq,
        "Lu(Ac)+2": Comp.Lu_Ac_plus2,
        "Lu(Ac)2+": Comp.Lu_Ac_2_plus,
        "Lu(Ac)3(aq)": Comp.Lu_Ac_3_aq,
        "Tb(Ac)+2": Comp.Tb_Ac_plus2,
        "Tb(Ac)2+": Comp.Tb_Ac_2_plus,
        "Tb(Ac)3(aq)": Comp.Tb_Ac_3_aq,
        "Pb(Ac)3-": Comp.Pb_Ac_3_minus,
        "Fe(Ac)+": Comp.Fe_Ac_plus,
        "Fe(Ac)2(aq)": Comp.Fe_Ac_2_aq,
        "Zn(Ac)+": Comp.Zn_Ac_plus,
        "Zn(Ac)2(aq)": Comp.Zn_Ac_2_aq,
        "Zn(Ac)3-": Comp.Zn_Ac_3_minus,
        "Ca(Ac)+": Comp.Ca_Ac_plus,
        "Ca(Ac)2(aq)": Comp.Ca_Ac_2_aq,
        "Al(Ac)+2": Comp.Al_Ac_plus2,
        "Al(Ac)2+": Comp.Al_Ac_2_plus,
        "Al(Ac)3(aq)": Comp.Al_Ac_3_aq,
        "Lactate": Comp.Lactate,
        "Lactic-Acid(aq)": Comp.Lactic_Acid_aq,
        "Li(Lac)(aq)": Comp.Li_Lac_aq,
        "Mg(Lac)+": Comp.Mg_Lac_plus,
        "Mg(Lac)2(aq)": Comp.Mg_Lac_2_aq,
        "Ca(Lac)+": Comp.Ca_Lac_plus,
        "Ca(Lac)2(aq)": Comp.Ca_Lac_2_aq,
        "Sr(Lac)+": Comp.Sr_Lac_plus,
        "Sr(Lac)2(aq)": Comp.Sr_Lac_2_aq,
        "Ba(Lac)+": Comp.Ba_Lac_plus,
        "Ba(Lac)2(aq)": Comp.Ba_Lac_2_aq,
        "Mn(Lac)+": Comp.Mn_Lac_plus,
        "Mn(Lac)2(aq)": Comp.Mn_Lac_2_aq,
        "Co(Lac)+": Comp.Co_Lac_plus,
        "Co(Lac)2(aq)": Comp.Co_Lac_2_aq,
        "Ni(Lac)+": Comp.Ni_Lac_plus,
        "Ni(Lac)2(aq)": Comp.Ni_Lac_2_aq,
        "Cu(Lac)+": Comp.Cu_Lac_plus,
        "Cu(Lac)2(aq)": Comp.Cu_Lac_2_aq,
        "Zn(Lac)+": Comp.Zn_Lac_plus,
        "Zn(Lac)2(aq)": Comp.Zn_Lac_2_aq,
        "Cd(Lac)+": Comp.Cd_Lac_plus,
        "Cd(Lac)2(aq)": Comp.Cd_Lac_2_aq,
        "La(Lac)+2": Comp.La_Lac_plus2,
        "Lu(Lac)+2": Comp.Lu_Lac_plus2,
        "Na(Lac)(aq)": Comp.Na_Lac_aq,
        "Na(Lac)2-": Comp.Na_Lac_2_minus,
        "K(Lac)(aq)": Comp.K_Lac_aq,
        "K(Lac)2-": Comp.K_Lac_2_minus,
        "Pb(Lac)+": Comp.Pb_Lac_plus,
        "Pb(Lac)2(aq)": Comp.Pb_Lac_2_aq,
        "Fe(Lac)+": Comp.Fe_Lac_plus,
        "Fe(Lac)2(aq)": Comp.Fe_Lac_2_aq,
        "Eu(Lac)+": Comp.Eu_Lac_plus,
        "Eu(Lac)2(aq)": Comp.Eu_Lac_2_aq,
        "Glycolic-Acid(aq)": Comp.Glycolic_Acid_aq,
        "Glycolate": Comp.Glycolate,
        "Li(Glyc)(aq)": Comp.Li_Glyc_aq,
        "Mg(Glyc)+": Comp.Mg_Glyc_plus,
        "Mg(Glyc)2(aq)": Comp.Mg_Glyc_2_aq,
        "Ca(Glyc)+": Comp.Ca_Glyc_plus,
        "Ca(Glyc)2(aq)": Comp.Ca_Glyc_2_aq,
        "Sr(Glyc)+": Comp.Sr_Glyc_plus,
        "Sr(Glyc)2(aq)": Comp.Sr_Glyc_2_aq,
        "Ba(Glyc)+": Comp.Ba_Glyc_plus,
        "Ba(Glyc)2(aq)": Comp.Ba_Glyc_2_aq,
        "Mn(Glyc)+": Comp.Mn_Glyc_plus,
        "Mn(Glyc)2(aq)": Comp.Mn_Glyc_2_aq,
        "Co(Glyc)+": Comp.Co_Glyc_plus,
        "Co(Glyc)2(aq)": Comp.Co_Glyc_2_aq,
        "Ni(Glyc)+": Comp.Ni_Glyc_plus,
        "Ni(Glyc)2(aq)": Comp.Ni_Glyc_2_aq,
        "Cu(Glyc)+": Comp.Cu_Glyc_plus,
        "Cu(Glyc)2(aq)": Comp.Cu_Glyc_2_aq,
        "Zn(Glyc)+": Comp.Zn_Glyc_plus,
        "Zn(Glyc)2(aq)": Comp.Zn_Glyc_2_aq,
        "Cd(Glyc)+": Comp.Cd_Glyc_plus,
        "Cd(Glyc)2(aq)": Comp.Cd_Glyc_2_aq,
        "Eu(Glyc)+": Comp.Eu_Glyc_plus,
        "Eu(Glyc)2(aq)": Comp.Eu_Glyc_2_aq,
        "Na(Glyc)(aq)": Comp.Na_Glyc_aq,
        "Na(Glyc)2-": Comp.Na_Glyc_2_minus,
        "K(Glyc)(aq)": Comp.K_Glyc_aq,
        "K(Glyc)2-": Comp.K_Glyc_2_minus,
        "Pb(Glyc)+": Comp.Pb_Glyc_plus,
        "Pb(Glyc)2(aq)": Comp.Pb_Glyc_2_aq,
        "Fe(Glyc)+": Comp.Fe_Glyc_plus,
        "Fe(Glyc)2(aq)": Comp.Fe_Glyc_2_aq,
        "Alanine(aq)": Comp.Alanine_aq,
        "Alanate": Comp.Alanate,
        "Cd(Alan)+": Comp.Cd_Alan_plus,
        "Cd(Alan)2(aq)": Comp.Cd_Alan_2_aq,
        "Ca(Alan)+": Comp.Ca_Alan_plus,
        "Ca(Alan)2(aq)": Comp.Ca_Alan_2_aq,
        "Pb(Alan)+": Comp.Pb_Alan_plus,
        "Pb(Alan)2(aq)": Comp.Pb_Alan_2_aq,
        "Mg(Alan)+": Comp.Mg_Alan_plus,
        "Mg(Alan)2(aq)": Comp.Mg_Alan_2_aq,
        "Sr(Alan)+": Comp.Sr_Alan_plus,
        "Sr(Alan)2(aq)": Comp.Sr_Alan_2_aq,
        "Mn(Alan)+": Comp.Mn_Alan_plus,
        "Mn(Alan)2(aq)": Comp.Mn_Alan_2_aq,
        "Co(Alan)+": Comp.Co_Alan_plus,
        "Co(Alan)2(aq)": Comp.Co_Alan_2_aq,
        "Ni(Alan)+": Comp.Ni_Alan_plus,
        "Ni(Alan)2(aq)": Comp.Ni_Alan_2_aq,
        "Cu(Alan)+": Comp.Cu_Alan_plus,
        "Cu(Alan)2(aq)": Comp.Cu_Alan_2_aq,
        "Zn(Alan)+": Comp.Zn_Alan_plus,
        "Zn(Alan)2(aq)": Comp.Zn_Alan_2_aq,
        "Ba(Alan)+": Comp.Ba_Alan_plus,
        "Ba(Alan)2(aq)": Comp.Ba_Alan_2_aq,
        "Fe(Alan)+": Comp.Fe_Alan_plus,
        "Fe(Alan)2(aq)": Comp.Fe_Alan_2_aq,
        "Eu(Alan)+": Comp.Eu_Alan_plus,
        "Eu(Alan)2(aq)": Comp.Eu_Alan_2_aq,
        "Glycine(aq)": Comp.Glycine_aq,
        "Glycinate": Comp.Glycinate,
        "Cd(Gly)+": Comp.Cd_Gly_plus,
        "Cd(Gly)2(aq)": Comp.Cd_Gly_2_aq,
        "Ca(Gly)+": Comp.Ca_Gly_plus,
        "Ca(Gly)2(aq)": Comp.Ca_Gly_2_aq,
        "Sr(Gly)+": Comp.Sr_Gly_plus,
        "Sr(Gly)2(aq)": Comp.Sr_Gly_2_aq,
        "Mn(Gly)+": Comp.Mn_Gly_plus,
        "Mn(Gly)2(aq)": Comp.Mn_Gly_2_aq,
        "Fe(Gly)+": Comp.Fe_Gly_plus,
        "Fe(Gly)2(aq)": Comp.Fe_Gly_2_aq,
        "Co(Gly)+": Comp.Co_Gly_plus,
        "Co(Gly)2(aq)": Comp.Co_Gly_2_aq,
        "Pb(Gly)+": Comp.Pb_Gly_plus,
        "Pb(Gly)2(aq)": Comp.Pb_Gly_2_aq,
        "Mg(Gly)+": Comp.Mg_Gly_plus,
        "Mg(Gly)2(aq)": Comp.Mg_Gly_2_aq,
        "Ni(Gly)+": Comp.Ni_Gly_plus,
        "Ni(Gly)2(aq)": Comp.Ni_Gly_2_aq,
        "Cu(Gly)+": Comp.Cu_Gly_plus,
        "Cu(Gly)2(aq)": Comp.Cu_Gly_2_aq,
        "Zn(Gly)+": Comp.Zn_Gly_plus,
        "Zn(Gly)2(aq)": Comp.Zn_Gly_2_aq,
        "Eu(Gly)+": Comp.Eu_Gly_plus,
        "Eu(Gly)2(aq)": Comp.Eu_Gly_2_aq,
        "Ba(Gly)+": Comp.Ba_Gly_plus,
        "Ba(Gly)2(aq)": Comp.Ba_Gly_2_aq,
        "Formic-Acid(aq)": Comp.Formic_Acid_aq,
        "Formate": Comp.Formate,
        "Mg(For)+": Comp.Mg_For_plus,
        "Mg(For)2(aq)": Comp.Mg_For_2_aq,
        "Ca(For)+": Comp.Ca_For_plus,
        "Ca(For)2(aq)": Comp.Ca_For_2_aq,
        "Sr(For)+": Comp.Sr_For_plus,
        "Sr(For)2(aq)": Comp.Sr_For_2_aq,
        "Ba(For)+": Comp.Ba_For_plus,
        "Ba(For)2(aq)": Comp.Ba_For_2_aq,
        "Cu(For)+": Comp.Cu_For_plus,
        "Cu(For)2(aq)": Comp.Cu_For_2_aq,
        "Cd(For)+": Comp.Cd_For_plus,
        "Cd(For)2(aq)": Comp.Cd_For_2_aq,
        "Na(For)(aq)": Comp.Na_For_aq,
        "Na(For)2-": Comp.Na_For_2_minus,
        "K(For)(aq)": Comp.K_For_aq,
        "K(For)2-": Comp.K_For_2_minus,
        "La(For)+2": Comp.La_For_plus2,
        "La(For)2+": Comp.La_For_2_plus,
        "Eu(For)+": Comp.Eu_For_plus,
        "Eu(For)2(aq)": Comp.Eu_For_2_aq,
        "U(For)+2": Comp.U_For_plus2,
        "U(For)2+": Comp.U_For_2_plus,
        "Eu(For)+2": Comp.Eu_For_plus2,
        "Eu(For)2+": Comp.Eu_For_2_plus,
        "Gd(For)+2": Comp.Gd_For_plus2,
        "Gd(For)2+": Comp.Gd_For_2_plus,
        "Yb(For)+2": Comp.Yb_For_plus2,
        "Yb(For)2+": Comp.Yb_For_2_plus,
        "Pb(For)+": Comp.Pb_For_plus,
        "Pb(For)2(aq)": Comp.Pb_For_2_aq,
        "Mn(For)+": Comp.Mn_For_plus,
        "Mn(For)2(aq)": Comp.Mn_For_2_aq,
        "Co(For)+": Comp.Co_For_plus,
        "Co(For)2(aq)": Comp.Co_For_2_aq,
        "Ni(For)+": Comp.Ni_For_plus,
        "Ni(For)2(aq)": Comp.Ni_For_2_aq,
        "Zn(For)+": Comp.Zn_For_plus,
        "Zn(For)2(aq)": Comp.Zn_For_2_aq,
        "Fe(For)+": Comp.Fe_For_plus,
        "Fe(For)2(aq)": Comp.Fe_For_2_aq,
        "Propanoic-Acid(aq)": Comp.Propanoic_Acid_aq,
        "Propanoate": Comp.Propanoate,
        "Mg(Prop)+": Comp.Mg_Prop_plus,
        "Mg(Prop)2(aq)": Comp.Mg_Prop_2_aq,
        "Ca(Prop)+": Comp.Ca_Prop_plus,
        "Ca(Prop)2(aq)": Comp.Ca_Prop_2_aq,
        "Sr(Prop)+": Comp.Sr_Prop_plus,
        "Sr(Prop)2(aq)": Comp.Sr_Prop_2_aq,
        "Ba(Prop)+": Comp.Ba_Prop_plus,
        "Ba(Prop)2(aq)": Comp.Ba_Prop_2_aq,
        "Eu(Prop)+": Comp.Eu_Prop_plus,
        "Eu(Prop)2(aq)": Comp.Eu_Prop_2_aq,
        "Cu(Prop)+": Comp.Cu_Prop_plus,
        "Cu(Prop)2(aq)": Comp.Cu_Prop_2_aq,
        "Cd(Prop)+": Comp.Cd_Prop_plus,
        "Cd(Prop)2(aq)": Comp.Cd_Prop_2_aq,
        "Pb(Prop)+": Comp.Pb_Prop_plus,
        "Pb(Prop)2(aq)": Comp.Pb_Prop_2_aq,
        "Na(Prop)(aq)": Comp.Na_Prop_aq,
        "Na(Prop)2-": Comp.Na_Prop_2_minus,
        "K(Prop)(aq)": Comp.K_Prop_aq,
        "K(Prop)2-": Comp.K_Prop_2_minus,
        "La(Prop)+2": Comp.La_Prop_plus2,
        "La(Prop)2+": Comp.La_Prop_2_plus,
        "Eu(Prop)+2": Comp.Eu_Prop_plus2,
        "Eu(Prop)2+": Comp.Eu_Prop_2_plus,
        "Gd(Prop)+2": Comp.Gd_Prop_plus2,
        "Gd(Prop)2+": Comp.Gd_Prop_2_plus,
        "Yb(Prop)+2": Comp.Yb_Prop_plus2,
        "Yb(Prop)2+": Comp.Yb_Prop_2_plus,
        "U(Prop)+2": Comp.U_Prop_plus2,
        "U(Prop)2+": Comp.U_Prop_2_plus,
        "Co(Prop)+": Comp.Co_Prop_plus,
        "Co(Prop)2(aq)": Comp.Co_Prop_2_aq,
        "Ni(Prop)+": Comp.Ni_Prop_plus,
        "Ni(Prop)2(aq)": Comp.Ni_Prop_2_aq,
        "Zn(Prop)+": Comp.Zn_Prop_plus,
        "Zn(Prop)2(aq)": Comp.Zn_Prop_2_aq,
        "Fe(Prop)+": Comp.Fe_Prop_plus,
        "Fe(Prop)2(aq)": Comp.Fe_Prop_2_aq,
        "Mn(Prop)+": Comp.Mn_Prop_plus,
        "Mn(Prop)2(aq)": Comp.Mn_Prop_2_aq,
        "Butanoic-Acid(aq)": Comp.Butanoic_Acid_aq,
        "Butanoate": Comp.Butanoate,
        "U(But)+2": Comp.U_But_plus2,
        "U(But)2+": Comp.U_But_2_plus,
        "Eu(But)+": Comp.Eu_But_plus,
        "Eu(But)2(aq)": Comp.Eu_But_2_aq,
        "Mg(But)+": Comp.Mg_But_plus,
        "Ca(But)+": Comp.Ca_But_plus,
        "Ca(But)2(aq)": Comp.Ca_But_2_aq,
        "Sr(But)+": Comp.Sr_But_plus,
        "Sr(But)2(aq)": Comp.Sr_But_2_aq,
        "Ba(But)+": Comp.Ba_But_plus,
        "Ba(But)2(aq)": Comp.Ba_But_2_aq,
        "Cu(But)+": Comp.Cu_But_plus,
        "Cu(But)2(aq)": Comp.Cu_But_2_aq,
        "Cd(But)+": Comp.Cd_But_plus,
        "Cd(But)2(aq)": Comp.Cd_But_2_aq,
        "Na(But)(aq)": Comp.Na_But_aq,
        "Na(But)2-": Comp.Na_But_2_minus,
        "K(But)(aq)": Comp.K_But_aq,
        "K(But)2-": Comp.K_But_2_minus,
        "La(But)+2": Comp.La_But_plus2,
        "La(But)2+": Comp.La_But_2_plus,
        "Eu(But)+2": Comp.Eu_But_plus2,
        "Eu(But)2+": Comp.Eu_But_2_plus,
        "Gd(But)+2": Comp.Gd_But_plus2,
        "Gd(But)2+": Comp.Gd_But_2_plus,
        "Yb(But)+2": Comp.Yb_But_plus2,
        "Yb(But)2+": Comp.Yb_But_2_plus,
        "Pb(But)+": Comp.Pb_But_plus,
        "Pb(But)2(aq)": Comp.Pb_But_2_aq,
        "Mn(But)+": Comp.Mn_But_plus,
        "Mn(But)2(aq)": Comp.Mn_But_2_aq,
        "Ni(But)+": Comp.Ni_But_plus,
        "Ni(But)2(aq)": Comp.Ni_But_2_aq,
        "Zn(But)+": Comp.Zn_But_plus,
        "Zn(But)2(aq)": Comp.Zn_But_2_aq,
        "Fe(But)+": Comp.Fe_But_plus,
        "Fe(But)2(aq)": Comp.Fe_But_2_aq,
        "Co(But)+": Comp.Co_But_plus,
        "Co(But)2(aq)": Comp.Co_But_2_aq,
        "Pentanoic-Acid(aq)": Comp.Pentanoic_Acid_aq,
        "Pentanoate": Comp.Pentanoate,
        "Ca(Pent)+": Comp.Ca_Pent_plus,
        "Ca(Pent)2(aq)": Comp.Ca_Pent_2_aq,
        "Sr(Pent)+": Comp.Sr_Pent_plus,
        "Sr(Pent)2(aq)": Comp.Sr_Pent_2_aq,
        "Ba(Pent)+": Comp.Ba_Pent_plus,
        "Ba(Pent)2(aq)": Comp.Ba_Pent_2_aq,
        "Cu(Pent)+": Comp.Cu_Pent_plus,
        "Cu(Pent)2(aq)": Comp.Cu_Pent_2_aq,
        "Na(Pent)(aq)": Comp.Na_Pent_aq,
        "Na(Pent)2-": Comp.Na_Pent_2_minus,
        "K(Pent)(aq)": Comp.K_Pent_aq,
        "K(Pent)2-": Comp.K_Pent_2_minus,
        "La(Pent)+2": Comp.La_Pent_plus2,
        "La(Pent)2+": Comp.La_Pent_2_plus,
        "Eu(Pent)+2": Comp.Eu_Pent_plus2,
        "Eu(Pent)2+": Comp.Eu_Pent_2_plus,
        "U(Pent)+2": Comp.U_Pent_plus2,
        "Eu(Pent)+": Comp.Eu_Pent_plus,
        "Gd(Pent)+2": Comp.Gd_Pent_plus2,
        "Gd(Pent)2+": Comp.Gd_Pent_2_plus,
        "Yb(Pent)+2": Comp.Yb_Pent_plus2,
        "Yb(Pent)2+": Comp.Yb_Pent_2_plus,
        "Mg(Pent)+": Comp.Mg_Pent_plus,
        "Mg(Pent)2(aq)": Comp.Mg_Pent_2_aq,
        "Pb(Pent)+": Comp.Pb_Pent_plus,
        "Pb(Pent)2(aq)": Comp.Pb_Pent_2_aq,
        "Co(Pent)+": Comp.Co_Pent_plus,
        "Co(Pent)2(aq)": Comp.Co_Pent_2_aq,
        "Ni(Pent)+": Comp.Ni_Pent_plus,
        "Ni(Pent)2(aq)": Comp.Ni_Pent_2_aq,
        "Zn(Pent)+": Comp.Zn_Pent_plus,
        "Zn(Pent)2(aq)": Comp.Zn_Pent_2_aq,
        "Cd(Pent)+": Comp.Cd_Pent_plus,
        "Cd(Pent)2(aq)": Comp.Cd_Pent_2_aq,
        "Fe(Pent)+": Comp.Fe_Pent_plus,
        "Fe(Pent)2(aq)": Comp.Fe_Pent_2_aq,
        "Mn(Pent)+": Comp.Mn_Pent_plus,
        "Mn(Pent)2(aq)": Comp.Mn_Pent_2_aq,
        "Mg(But)2(aq)": Comp.Mg_But_2_aq,
        "H4SiO4(aq)": Comp.H4SiO4_aq,
    }

    coolpropToComp = {
        "Water": Comp.WATER,
        "Hydrogen": Comp.HYDROGEN,
        "Oxygen": Comp.OXYGEN,
        "Ammonia": Comp.AMMONIA,
        "CarbonDioxide": Comp.CARBONDIOXIDE,
        "Nitrogen": Comp.NITROGEN,
        "HydrogenSulfide": Comp.H2S,
        "Helium": Comp.HELIUM,
        "Argon": Comp.ARGON,
        "Methane": Comp.METHANE,
        "Ethylene": Comp.C2H4_g,
        "SulfurDioxide": Comp.SO2_g,
        "Krypton": Comp.Kr_g,
        "Neon": Comp.Ne_g,
        "Xenon": Comp.Xe_g,}

    def withReaktoroName(self, name: str) -> Comp:
        """
        Translate the Reaktoro species name into a Comp object

        Parameters
        ----------
        name : str
            the Reaktoro species name

        Returns
        -------
        Comp
            a Comp object of the Reaktoro species
        """
        return self.reaktoroToComp[name]

    def withCoolPropName(self, name: str) -> Comp:
        """
        Translate the CoolProp species name into a Comp object

        Parameters
        ----------
        name : str
            the CoolProp species name

        Returns
        -------
        Comp
            a Comp object of the CoolProp species
        """
        return self.coolpropToComp[name]

    def generate(self):

        # this could do with a bit more work... not sure if it actually works as intended

        self.reaktoroToComp = {}
        self.coolpropToComp = {}

        for i in Comp:

            if i.value.alias["RKT"] is not None:
                self.reaktoroToComp[i.value.alias["RKT"]] = i
            if i.value.alias["CP"] is not None:
                self.coolpropToComp[i.value.alias["CP"]] = i

        return self


# this is for generating the LookUp Dictionary
# test = LookUp().generate()
#
# txt = ""
# for i in test.reaktoroToComp:
#     txt += "\"" + i + "\": Comp." + test.reaktoroToComp[i].name + ",\n"
#
#
# print(txt)
