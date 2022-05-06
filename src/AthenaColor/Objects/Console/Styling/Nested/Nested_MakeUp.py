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
sep_ = " "

class StyleNest:
    @staticmethod
    def Reset(*obj,sep=sep_):                      return NCSNO(obj,0,sep)
    @staticmethod
    def Bold(*obj,sep=sep_):                       return NCS(obj,1,22,sep)
    @staticmethod
    def NoBold(*obj,sep=sep_):                     return NCSNO(obj,22,sep)
    @staticmethod
    def Dim(*obj,sep=sep_):                        return NCS(obj,2,22,sep)
    @staticmethod
    def NoDim(*obj,sep=sep_):                      return NCSNO(obj,22,sep)
    @staticmethod
    def Italic(*obj,sep=sep_):                     return NCS(obj,3,23,sep)
    @staticmethod
    def NoItalic(*obj,sep=sep_):                   return NCSNO(obj,23,sep)
    @staticmethod
    def Underline(*obj,sep=sep_):                  return NCS(obj,4,24,sep)
    @staticmethod
    def NoUnderline(*obj,sep=sep_):                return NCSNO(obj,24,sep)
    @staticmethod
    def BlinkSlow(*obj,sep=sep_):                  return NCS(obj,5,25,sep)
    @staticmethod
    def NoBlinkSlow(*obj,sep=sep_):                return NCSNO(obj,25,sep)
    @staticmethod
    def BlinkRapid(*obj,sep=sep_):                 return NCS(obj,6,25,sep)
    @staticmethod
    def NoBlinkRapid(*obj,sep=sep_):               return NCSNO(obj,25,sep)
    @staticmethod
    def Reversed(*obj,sep=sep_):                   return NCS(obj,7,27,sep)
    @staticmethod
    def NoReversed(*obj,sep=sep_):                 return NCSNO(obj,27,sep)
    @staticmethod
    def Conceal(*obj,sep=sep_):                    return NCS(obj,8,28,sep)
    @staticmethod
    def NoConceal(*obj,sep=sep_):                  return NCSNO(obj,28,sep)
    @staticmethod
    def Crossed(*obj,sep=sep_):                    return NCS(obj,9,29,sep)
    @staticmethod
    def NoCrossed(*obj,sep=sep_):                  return NCSNO(obj,29,sep)
    @staticmethod
    def FontPrimary(*obj,sep=sep_):                return NCS(obj,10,10,sep)
    @staticmethod
    def FontSecond1(*obj,sep=sep_):                return NCS(obj,11,10,sep)
    @staticmethod
    def FontSecond2(*obj,sep=sep_):                return NCS(obj,12,10,sep)
    @staticmethod
    def FontSecond3(*obj,sep=sep_):                return NCS(obj,13,10,sep)
    @staticmethod
    def FontSecond4(*obj,sep=sep_):                return NCS(obj,14,10,sep)
    @staticmethod
    def FontSecond5(*obj,sep=sep_):                return NCS(obj,15,10,sep)
    @staticmethod
    def FontSecond6(*obj,sep=sep_):                return NCS(obj,16,10,sep)
    @staticmethod
    def FontSecond8(*obj,sep=sep_):                return NCS(obj,17,10,sep)
    @staticmethod
    def FontSecond9(*obj,sep=sep_):                return NCS(obj,18,10,sep)
    @staticmethod
    def FontSecond10(*obj,sep=sep_):               return NCS(obj,19,10,sep)
    @staticmethod
    def NoFont(*obj,sep=sep_):                     return NCSNO(obj,10,sep)
    @staticmethod
    def Fraktur(*obj,sep=sep_):                    return NCSNO(obj,20,sep)
    @staticmethod
    def UnderlineDouble(*obj,sep=sep_):            return NCS(obj,21,24,sep)
    @staticmethod
    def NoUnderlineDouble(*obj,sep=sep_):          return NCSNO(obj,24,sep)
    @staticmethod
    def PropSpacing(*obj,sep=sep_):                return NCS(obj,26,26,sep)
    @staticmethod
    def NoPropSpacing(*obj,sep=sep_):              return NCSNO(obj,26,sep)
    @staticmethod
    def NoForeground(*obj,sep=sep_):               return NCSNO(obj,39,sep)
    @staticmethod
    def NoBackground(*obj,sep=sep_):               return NCSNO(obj,49,sep)
    @staticmethod
    def Frame(*obj,sep=sep_):                      return NCS(obj,51,54,sep)
    @staticmethod
    def NoFrame(*obj,sep=sep_):                    return NCSNO(obj,54,sep)
    @staticmethod
    def Circle(*obj,sep=sep_):                     return NCS(obj,52,54,sep)
    @staticmethod
    def NoCircle(*obj,sep=sep_):                   return NCSNO(obj,54,sep)
    @staticmethod
    def OverLine(*obj,sep=sep_):                   return NCS(obj,53,55,sep)
    @staticmethod
    def NoOverLine(*obj,sep=sep_):                 return NCSNO(obj,55,sep)
    @staticmethod
    def UnderColourDefault(*obj,sep=sep_):         return NCSNO(obj,59,sep)
    @staticmethod
    def IdeogramUnderLine(*obj,sep=sep_):          return NCS(obj,60,65,sep)
    @staticmethod
    def IdeogramUnderLineDouble(*obj,sep=sep_):    return NCS(obj,61,65,sep)
    @staticmethod
    def IdeogramOverLine(*obj,sep=sep_):           return NCS(obj,62,65,sep)
    @staticmethod
    def IdeogramOverLineDouble(*obj,sep=sep_):     return NCS(obj,63,65,sep)
    @staticmethod
    def IdeogramStress(*obj,sep=sep_):             return NCS(obj,64,65,sep)
    @staticmethod
    def NoIdeogram(*obj,sep=sep_):                 return NCSNO(obj,65,sep)
    @staticmethod
    def SuperScript(*obj,sep=sep_):                return NCS(obj,73,75,sep)
    @staticmethod
    def SubScript(*obj,sep=sep_):                  return NCS(obj,74,75,sep)
    @staticmethod
    def NoScript(*obj,sep=sep_):                   return NCSNO(obj,75,sep)

# ----------------------------------------------------------------------------------------------------------------------
# - BasicNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class BasicNest:
    class Fore:
        @staticmethod
        def Black(*obj,sep=sep_):           return NCS(obj, 30, 39,sep)
        @staticmethod
        def Red(*obj,sep=sep_):             return NCS(obj, 31, 39,sep)
        @staticmethod
        def Green(*obj,sep=sep_):           return NCS(obj, 32, 39,sep)
        @staticmethod
        def Yellow(*obj,sep=sep_):          return NCS(obj, 33, 39,sep)
        @staticmethod
        def Blue(*obj,sep=sep_):            return NCS(obj, 34, 39,sep)
        @staticmethod
        def Magenta(*obj,sep=sep_):         return NCS(obj, 35, 39,sep)
        @staticmethod
        def Cyan(*obj,sep=sep_):            return NCS(obj, 36, 39,sep)
        @staticmethod
        def White(*obj,sep=sep_):           return NCS(obj, 37, 39,sep)
        @staticmethod
        def BrightBlack(*obj,sep=sep_):     return NCS(obj, 90, 39,sep)
        @staticmethod
        def BrightRed(*obj,sep=sep_):       return NCS(obj, 91, 39,sep)
        @staticmethod
        def BrightGreen(*obj,sep=sep_):     return NCS(obj, 92, 39,sep)
        @staticmethod
        def BrightYellow(*obj,sep=sep_):    return NCS(obj, 93, 39,sep)
        @staticmethod
        def BrightBlue(*obj,sep=sep_):      return NCS(obj, 94, 39,sep)
        @staticmethod
        def BrightMagenta(*obj,sep=sep_):   return NCS(obj, 95, 39,sep)
        @staticmethod
        def BrightCyan(*obj,sep=sep_):      return NCS(obj, 96, 39,sep)
        @staticmethod
        def BrightWhite(*obj,sep=sep_):     return NCS(obj, 97, 39,sep)

    class Back:
        @staticmethod
        def Black(*obj,sep=sep_):           return NCS(obj, 40, 49,sep)
        @staticmethod
        def Red(*obj,sep=sep_):             return NCS(obj, 41, 49,sep)
        @staticmethod
        def Green(*obj,sep=sep_):           return NCS(obj, 42, 49,sep)
        @staticmethod
        def Yellow(*obj,sep=sep_):          return NCS(obj, 43, 49,sep)
        @staticmethod
        def Blue(*obj,sep=sep_):            return NCS(obj, 44, 49,sep)
        @staticmethod
        def Magenta(*obj,sep=sep_):         return NCS(obj, 45, 49,sep)
        @staticmethod
        def Cyan(*obj,sep=sep_):            return NCS(obj, 46, 49,sep)
        @staticmethod
        def White(*obj,sep=sep_):           return NCS(obj, 47, 49,sep)
        @staticmethod
        def BrightBlack(*obj,sep=sep_):     return NCS(obj, 100, 49,sep)
        @staticmethod
        def BrightRed(*obj,sep=sep_):       return NCS(obj, 101, 49,sep)
        @staticmethod
        def BrightGreen(*obj,sep=sep_):     return NCS(obj, 102, 49,sep)
        @staticmethod
        def BrightYellow(*obj,sep=sep_):    return NCS(obj, 103, 49,sep)
        @staticmethod
        def BrightBlue(*obj,sep=sep_):      return NCS(obj, 104, 49,sep)
        @staticmethod
        def BrightMagenta(*obj,sep=sep_):   return NCS(obj, 105, 49,sep)
        @staticmethod
        def BrightCyan(*obj,sep=sep_):      return NCS(obj, 106, 49,sep)
        @staticmethod
        def BrightWhite(*obj,sep=sep_):     return NCS(obj, 107, 49,sep)