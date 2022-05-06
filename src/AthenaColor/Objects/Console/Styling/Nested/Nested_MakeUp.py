# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Functions.ANSIsquences import NestedColorSequence,NestedColorSequence_NoReset

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "StyleNest", "BasicNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - StyleNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence            # Done for slight speed increase
NCSNO = NestedColorSequence_NoReset  # Done for slight speed increase

class StyleNest:
    @staticmethod
    def Reset(*obj, sep=" "):                      return NCSNO(obj,  control_code=0, sep=sep)
    @staticmethod
    def Bold(*obj, sep=" "):                       return NCS(obj,  control_code=1, reset_code=22, sep=sep)
    @staticmethod
    def NoBold(*obj, sep=" "):                     return NCSNO(obj,  control_code=22, sep=sep)
    @staticmethod
    def Dim(*obj, sep=" "):                        return NCS(obj,  control_code=2, reset_code=22, sep=sep)
    @staticmethod
    def NoDim(*obj, sep=" "):                      return NCSNO(obj,  control_code=22, sep=sep)
    @staticmethod
    def Italic(*obj, sep=" "):                     return NCS(obj,  control_code=3, reset_code=23, sep=sep)
    @staticmethod
    def NoItalic(*obj, sep=" "):                   return NCSNO(obj,  control_code=23, sep=sep)
    @staticmethod
    def Underline(*obj, sep=" "):                  return NCS(obj,  control_code=4, reset_code=24, sep=sep)
    @staticmethod
    def NoUnderline(*obj, sep=" "):                return NCSNO(obj,  control_code=24, sep=sep)
    @staticmethod
    def BlinkSlow(*obj, sep=" "):                  return NCS(obj,  control_code=5, reset_code=25, sep=sep)
    @staticmethod
    def NoBlinkSlow(*obj, sep=" "):                return NCSNO(obj,  control_code=25, sep=sep)
    @staticmethod
    def BlinkRapid(*obj, sep=" "):                 return NCS(obj,  control_code=6, reset_code=25, sep=sep)
    @staticmethod
    def NoBlinkRapid(*obj, sep=" "):               return NCSNO(obj,  control_code=25, sep=sep)
    @staticmethod
    def Reversed(*obj, sep=" "):                   return NCS(obj,  control_code=7, reset_code=27, sep=sep)
    @staticmethod
    def NoReversed(*obj, sep=" "):                 return NCSNO(obj,  control_code=27, sep=sep)
    @staticmethod
    def Conceal(*obj, sep=" "):                    return NCS(obj,  control_code=8, reset_code=28, sep=sep)
    @staticmethod
    def NoConceal(*obj, sep=" "):                  return NCSNO(obj,  control_code=28, sep=sep)
    @staticmethod
    def Crossed(*obj, sep=" "):                    return NCS(obj,  control_code=9, reset_code=29, sep=sep)
    @staticmethod
    def NoCrossed(*obj, sep=" "):                  return NCSNO(obj,  control_code=29, sep=sep)
    @staticmethod
    def FontPrimary(*obj, sep=" "):                return NCS(obj,  control_code=10, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond1(*obj, sep=" "):                return NCS(obj,  control_code=11, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond2(*obj, sep=" "):                return NCS(obj,  control_code=12, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond3(*obj, sep=" "):                return NCS(obj,  control_code=13, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond4(*obj, sep=" "):                return NCS(obj,  control_code=14, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond5(*obj, sep=" "):                return NCS(obj,  control_code=15, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond6(*obj, sep=" "):                return NCS(obj,  control_code=16, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond8(*obj, sep=" "):                return NCS(obj,  control_code=17, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond9(*obj, sep=" "):                return NCS(obj,  control_code=18, reset_code=10, sep=sep)
    @staticmethod
    def FontSecond10(*obj, sep=" "):               return NCS(obj,  control_code=19, reset_code=10, sep=sep)
    @staticmethod
    def NoFont(*obj, sep=" "):                     return NCSNO(obj,  control_code=10, sep=sep)
    @staticmethod
    def Fraktur(*obj, sep=" "):                    return NCSNO(obj,  control_code=20, sep=sep)
    @staticmethod
    def UnderlineDouble(*obj, sep=" "):            return NCS(obj,  control_code=21, reset_code=24, sep=sep)
    @staticmethod
    def NoUnderlineDouble(*obj, sep=" "):          return NCSNO(obj,  control_code=24, sep=sep)
    @staticmethod
    def PropSpacing(*obj, sep=" "):                return NCS(obj,  control_code=26, reset_code=26, sep=sep)
    @staticmethod
    def NoPropSpacing(*obj, sep=" "):              return NCSNO(obj,  control_code=26, sep=sep)
    @staticmethod
    def NoForeground(*obj, sep=" "):               return NCSNO(obj,  control_code=39, sep=sep)
    @staticmethod
    def NoBackground(*obj, sep=" "):               return NCSNO(obj,  control_code=49, sep=sep)
    @staticmethod
    def Frame(*obj, sep=" "):                      return NCS(obj,  control_code=51, reset_code=54, sep=sep)
    @staticmethod
    def NoFrame(*obj, sep=" "):                    return NCSNO(obj,  control_code=54, sep=sep)
    @staticmethod
    def Circle(*obj, sep=" "):                     return NCS(obj,  control_code=52, reset_code=54, sep=sep)
    @staticmethod
    def NoCircle(*obj, sep=" "):                   return NCSNO(obj,  control_code=54, sep=sep)
    @staticmethod
    def OverLine(*obj, sep=" "):                   return NCS(obj,  control_code=53, reset_code=55, sep=sep)
    @staticmethod
    def NoOverLine(*obj, sep=" "):                 return NCSNO(obj,  control_code=55, sep=sep)
    @staticmethod
    def UnderColourDefault(*obj, sep=" "):         return NCSNO(obj,  control_code=59, sep=sep)
    @staticmethod
    def IdeogramUnderLine(*obj, sep=" "):          return NCS(obj,  control_code=60, reset_code=65, sep=sep)
    @staticmethod
    def IdeogramUnderLineDouble(*obj, sep=" "):    return NCS(obj,  control_code=61, reset_code=65, sep=sep)
    @staticmethod
    def IdeogramOverLine(*obj, sep=" "):           return NCS(obj,  control_code=62, reset_code=65, sep=sep)
    @staticmethod
    def IdeogramOverLineDouble(*obj, sep=" "):     return NCS(obj,  control_code=63, reset_code=65, sep=sep)
    @staticmethod
    def IdeogramStress(*obj, sep=" "):             return NCS(obj,  control_code=64, reset_code=65, sep=sep)
    @staticmethod
    def NoIdeogram(*obj, sep=" "):                 return NCSNO(obj,  control_code=65, sep=sep)
    @staticmethod
    def SuperScript(*obj, sep=" "):                return NCS(obj,  control_code=73, reset_code=75, sep=sep)
    @staticmethod
    def SubScript(*obj, sep=" "):                  return NCS(obj,  control_code=74, reset_code=75, sep=sep)
    @staticmethod
    def NoScript(*obj, sep=" "):                   return NCSNO(obj,  control_code=75, sep=sep)

# ----------------------------------------------------------------------------------------------------------------------
# - BasicNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class BasicNest:
    class Fore:
        @staticmethod
        def Black(*obj, sep=" "):           return NCS(obj, 30, 39, sep=sep)
        @staticmethod
        def Red(*obj, sep=" "):             return NCS(obj, 31, 39, sep=sep)
        @staticmethod
        def Green(*obj, sep=" "):           return NCS(obj, 32, 39, sep=sep)
        @staticmethod
        def Yellow(*obj, sep=" "):          return NCS(obj, 33, 39, sep=sep)
        @staticmethod
        def Blue(*obj, sep=" "):            return NCS(obj, 34, 39, sep=sep)
        @staticmethod
        def Magenta(*obj, sep=" "):         return NCS(obj, 35, 39, sep=sep)
        @staticmethod
        def Cyan(*obj, sep=" "):            return NCS(obj, 36, 39, sep=sep)
        @staticmethod
        def White(*obj, sep=" "):           return NCS(obj, 37, 39, sep=sep)
        @staticmethod
        def BrightBlack(*obj, sep=" "):     return NCS(obj, 90, 39, sep=sep)
        @staticmethod
        def BrightRed(*obj, sep=" "):       return NCS(obj, 91, 39, sep=sep)
        @staticmethod
        def BrightGreen(*obj, sep=" "):     return NCS(obj, 92, 39, sep=sep)
        @staticmethod
        def BrightYellow(*obj, sep=" "):    return NCS(obj, 93, 39, sep=sep)
        @staticmethod
        def BrightBlue(*obj, sep=" "):      return NCS(obj, 94, 39, sep=sep)
        @staticmethod
        def BrightMagenta(*obj, sep=" "):   return NCS(obj, 95, 39, sep=sep)
        @staticmethod
        def BrightCyan(*obj, sep=" "):      return NCS(obj, 96, 39, sep=sep)
        @staticmethod
        def BrightWhite(*obj, sep=" "):     return NCS(obj, 97, 39, sep=sep)

    class Back:
        @staticmethod
        def Black(*obj, sep=" "):           return NCS(obj, 40, 49, sep=sep)
        @staticmethod
        def Red(*obj, sep=" "):             return NCS(obj, 41, 49, sep=sep)
        @staticmethod
        def Green(*obj, sep=" "):           return NCS(obj, 42, 49, sep=sep)
        @staticmethod
        def Yellow(*obj, sep=" "):          return NCS(obj, 43, 49, sep=sep)
        @staticmethod
        def Blue(*obj, sep=" "):            return NCS(obj, 44, 49, sep=sep)
        @staticmethod
        def Magenta(*obj, sep=" "):         return NCS(obj, 45, 49, sep=sep)
        @staticmethod
        def Cyan(*obj, sep=" "):            return NCS(obj, 46, 49, sep=sep)
        @staticmethod
        def White(*obj, sep=" "):           return NCS(obj, 47, 49, sep=sep)
        @staticmethod
        def BrightBlack(*obj, sep=" "):     return NCS(obj, 100, 49, sep=sep)
        @staticmethod
        def BrightRed(*obj, sep=" "):       return NCS(obj, 101, 49, sep=sep)
        @staticmethod
        def BrightGreen(*obj, sep=" "):     return NCS(obj, 102, 49, sep=sep)
        @staticmethod
        def BrightYellow(*obj, sep=" "):    return NCS(obj, 103, 49, sep=sep)
        @staticmethod
        def BrightBlue(*obj, sep=" "):      return NCS(obj, 104, 49, sep=sep)
        @staticmethod
        def BrightMagenta(*obj, sep=" "):   return NCS(obj, 105, 49, sep=sep)
        @staticmethod
        def BrightCyan(*obj, sep=" "):      return NCS(obj, 106, 49, sep=sep)
        @staticmethod
        def BrightWhite(*obj, sep=" "):     return NCS(obj, 107, 49, sep=sep)