# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX, NormalizeRgb
from AthenaColor.Functions.ANSIsquences import NestedColorSequence
from AthenaColor.Objects.Console.Styling.Inline.Bodies import Fore
from AthenaColor.Objects.Console.Styling.Inline.Style import Style

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "ForeNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence # Done for slight speed increase
sep_=" "

class ForeNest:
    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def custom(*obj, color:RGB|HEX, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"\033[38;2;{';'.join(*color.export())}m",
            Style.NoForeground,
            sep=sep
        )

    @staticmethod
    def rgb(*obj, r:int,g:int,b:int, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"\033[38;2;{';'.join(*NormalizeRgb(r, g, b))}m",
            Style.NoForeground,
            sep=sep
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    # No partial methods, as this was increase the speed impact 2-fold
    @staticmethod
    def Maroon(*obj, sep=sep_):              return NCS(obj,Fore.Maroon,Style.NoForeground,sep)
    @staticmethod
    def DarkRed(*obj, sep=sep_):             return NCS(obj,Fore.DarkRed,Style.NoForeground,sep)
    @staticmethod
    def Brown(*obj, sep=sep_):               return NCS(obj,Fore.Brown,Style.NoForeground,sep)
    @staticmethod
    def Firebrick(*obj, sep=sep_):           return NCS(obj,Fore.Firebrick,Style.NoForeground,sep)
    @staticmethod
    def Crimson(*obj, sep=sep_):             return NCS(obj,Fore.Crimson,Style.NoForeground,sep)
    @staticmethod
    def Red(*obj, sep=sep_):                 return NCS(obj,Fore.Red,Style.NoForeground,sep)
    @staticmethod
    def Tomato(*obj, sep=sep_):              return NCS(obj,Fore.Tomato,Style.NoForeground,sep)
    @staticmethod
    def Coral(*obj, sep=sep_):               return NCS(obj,Fore.Coral,Style.NoForeground,sep)
    @staticmethod
    def IndianRed(*obj, sep=sep_):           return NCS(obj,Fore.IndianRed,Style.NoForeground,sep)
    @staticmethod
    def LightCoral(*obj, sep=sep_):          return NCS(obj,Fore.LightCoral,Style.NoForeground,sep)
    @staticmethod
    def DarkSalmon(*obj, sep=sep_):          return NCS(obj,Fore.DarkSalmon,Style.NoForeground,sep)
    @staticmethod
    def Salmon(*obj, sep=sep_):              return NCS(obj,Fore.Salmon,Style.NoForeground,sep)
    @staticmethod
    def LightSalmon(*obj, sep=sep_):         return NCS(obj,Fore.LightSalmon,Style.NoForeground,sep)
    @staticmethod
    def OrangeRed(*obj, sep=sep_):           return NCS(obj,Fore.OrangeRed,Style.NoForeground,sep)
    @staticmethod
    def DarkOrange(*obj, sep=sep_):          return NCS(obj,Fore.DarkOrange,Style.NoForeground,sep)
    @staticmethod
    def Orange(*obj, sep=sep_):              return NCS(obj,Fore.Orange,Style.NoForeground,sep)
    @staticmethod
    def Gold(*obj, sep=sep_):                return NCS(obj,Fore.Gold,Style.NoForeground,sep)
    @staticmethod
    def DarkGoldenRod(*obj, sep=sep_):       return NCS(obj,Fore.DarkGoldenRod,Style.NoForeground,sep)
    @staticmethod
    def GoldenRod(*obj, sep=sep_):           return NCS(obj,Fore.GoldenRod,Style.NoForeground,sep)
    @staticmethod
    def PaleGoldenRod(*obj, sep=sep_):       return NCS(obj,Fore.PaleGoldenRod,Style.NoForeground,sep)
    @staticmethod
    def DarkKhaki(*obj, sep=sep_):           return NCS(obj,Fore.DarkKhaki,Style.NoForeground,sep)
    @staticmethod
    def Khaki(*obj, sep=sep_):               return NCS(obj,Fore.Khaki,Style.NoForeground,sep)
    @staticmethod
    def Olive(*obj, sep=sep_):               return NCS(obj,Fore.Olive,Style.NoForeground,sep)
    @staticmethod
    def Yellow(*obj, sep=sep_):              return NCS(obj,Fore.Yellow,Style.NoForeground,sep)
    @staticmethod
    def YellowGreen(*obj, sep=sep_):         return NCS(obj,Fore.YellowGreen,Style.NoForeground,sep)
    @staticmethod
    def DarkOliveGreen(*obj, sep=sep_):      return NCS(obj,Fore.DarkOliveGreen,Style.NoForeground,sep)
    @staticmethod
    def OliveDrab(*obj, sep=sep_):           return NCS(obj,Fore.OliveDrab,Style.NoForeground,sep)
    @staticmethod
    def LawnGreen(*obj, sep=sep_):           return NCS(obj,Fore.LawnGreen,Style.NoForeground,sep)
    @staticmethod
    def Chartreuse(*obj, sep=sep_):          return NCS(obj,Fore.Chartreuse,Style.NoForeground,sep)
    @staticmethod
    def GreenYellow(*obj, sep=sep_):         return NCS(obj,Fore.GreenYellow,Style.NoForeground,sep)
    @staticmethod
    def DarkGreen(*obj, sep=sep_):           return NCS(obj,Fore.DarkGreen,Style.NoForeground,sep)
    @staticmethod
    def Green(*obj, sep=sep_):               return NCS(obj,Fore.Green,Style.NoForeground,sep)
    @staticmethod
    def ForestGreen(*obj, sep=sep_):         return NCS(obj,Fore.ForestGreen,Style.NoForeground,sep)
    @staticmethod
    def Lime(*obj, sep=sep_):                return NCS(obj,Fore.Lime,Style.NoForeground,sep)
    @staticmethod
    def LimeGreen(*obj, sep=sep_):           return NCS(obj,Fore.LimeGreen,Style.NoForeground,sep)
    @staticmethod
    def LightGreen(*obj, sep=sep_):          return NCS(obj,Fore.LightGreen,Style.NoForeground,sep)
    @staticmethod
    def PaleGreen(*obj, sep=sep_):           return NCS(obj,Fore.PaleGreen,Style.NoForeground,sep)
    @staticmethod
    def DarkSeaGreen(*obj, sep=sep_):        return NCS(obj,Fore.DarkSeaGreen,Style.NoForeground,sep)
    @staticmethod
    def MediumSpringGreen(*obj, sep=sep_):   return NCS(obj,Fore.MediumSpringGreen,Style.NoForeground,sep)
    @staticmethod
    def SpringGreen(*obj, sep=sep_):         return NCS(obj,Fore.SpringGreen,Style.NoForeground,sep)
    @staticmethod
    def SeaGreen(*obj, sep=sep_):            return NCS(obj,Fore.SeaGreen,Style.NoForeground,sep)
    @staticmethod
    def MediumAquaMarine(*obj, sep=sep_):    return NCS(obj,Fore.MediumAquaMarine,Style.NoForeground,sep)
    @staticmethod
    def MediumSeaGreen(*obj, sep=sep_):      return NCS(obj,Fore.MediumSeaGreen,Style.NoForeground,sep)
    @staticmethod
    def LightSeaGreen(*obj, sep=sep_):       return NCS(obj,Fore.LightSeaGreen,Style.NoForeground,sep)
    @staticmethod
    def DarkSlateGray(*obj, sep=sep_):       return NCS(obj,Fore.DarkSlateGray,Style.NoForeground,sep)
    @staticmethod
    def Teal(*obj, sep=sep_):                return NCS(obj,Fore.Teal,Style.NoForeground,sep)
    @staticmethod
    def DarkCyan(*obj, sep=sep_):            return NCS(obj,Fore.DarkCyan,Style.NoForeground,sep)
    @staticmethod
    def Aqua(*obj, sep=sep_):                return NCS(obj,Fore.Aqua,Style.NoForeground,sep)
    @staticmethod
    def Cyan(*obj, sep=sep_):                return NCS(obj,Fore.Cyan,Style.NoForeground,sep)
    @staticmethod
    def LightCyan(*obj, sep=sep_):           return NCS(obj,Fore.LightCyan,Style.NoForeground,sep)
    @staticmethod
    def DarkTurquoise(*obj, sep=sep_):       return NCS(obj,Fore.DarkTurquoise,Style.NoForeground,sep)
    @staticmethod
    def Turquoise(*obj, sep=sep_):           return NCS(obj,Fore.Turquoise,Style.NoForeground,sep)
    @staticmethod
    def MediumTurquoise(*obj, sep=sep_):     return NCS(obj,Fore.MediumTurquoise,Style.NoForeground,sep)
    @staticmethod
    def PaleTurquoise(*obj, sep=sep_):       return NCS(obj,Fore.PaleTurquoise,Style.NoForeground,sep)
    @staticmethod
    def AquaMarine(*obj, sep=sep_):          return NCS(obj,Fore.AquaMarine,Style.NoForeground,sep)
    @staticmethod
    def PowderBlue(*obj, sep=sep_):          return NCS(obj,Fore.PowderBlue,Style.NoForeground,sep)
    @staticmethod
    def CadetBlue(*obj, sep=sep_):           return NCS(obj,Fore.CadetBlue,Style.NoForeground,sep)
    @staticmethod
    def SteelBlue(*obj, sep=sep_):           return NCS(obj,Fore.SteelBlue,Style.NoForeground,sep)
    @staticmethod
    def CornFlowerBlue(*obj, sep=sep_):      return NCS(obj,Fore.CornFlowerBlue,Style.NoForeground,sep)
    @staticmethod
    def DeepSkyBlue(*obj, sep=sep_):         return NCS(obj,Fore.DeepSkyBlue,Style.NoForeground,sep)
    @staticmethod
    def DodgerBlue(*obj, sep=sep_):          return NCS(obj,Fore.DodgerBlue,Style.NoForeground,sep)
    @staticmethod
    def LightBlue(*obj, sep=sep_):           return NCS(obj,Fore.LightBlue,Style.NoForeground,sep)
    @staticmethod
    def SkyBlue(*obj, sep=sep_):             return NCS(obj,Fore.SkyBlue,Style.NoForeground,sep)
    @staticmethod
    def LightSkyBlue(*obj, sep=sep_):        return NCS(obj,Fore.LightSkyBlue,Style.NoForeground,sep)
    @staticmethod
    def MidnightBlue(*obj, sep=sep_):        return NCS(obj,Fore.MidnightBlue,Style.NoForeground,sep)
    @staticmethod
    def Navy(*obj, sep=sep_):                return NCS(obj,Fore.Navy,Style.NoForeground,sep)
    @staticmethod
    def DarkBlue(*obj, sep=sep_):            return NCS(obj,Fore.DarkBlue,Style.NoForeground,sep)
    @staticmethod
    def MediumBlue(*obj, sep=sep_):          return NCS(obj,Fore.MediumBlue,Style.NoForeground,sep)
    @staticmethod
    def Blue(*obj, sep=sep_):                return NCS(obj,Fore.Blue,Style.NoForeground,sep)
    @staticmethod
    def RoyalBlue(*obj, sep=sep_):           return NCS(obj,Fore.RoyalBlue,Style.NoForeground,sep)
    @staticmethod
    def BlueViolet(*obj, sep=sep_):          return NCS(obj,Fore.BlueViolet,Style.NoForeground,sep)
    @staticmethod
    def Indigo(*obj, sep=sep_):              return NCS(obj,Fore.Indigo,Style.NoForeground,sep)
    @staticmethod
    def DarkSlateBlue(*obj, sep=sep_):       return NCS(obj,Fore.DarkSlateBlue,Style.NoForeground,sep)
    @staticmethod
    def SlateBlue(*obj, sep=sep_):           return NCS(obj,Fore.SlateBlue,Style.NoForeground,sep)
    @staticmethod
    def MediumSlateBlue(*obj, sep=sep_):     return NCS(obj,Fore.MediumSlateBlue,Style.NoForeground,sep)
    @staticmethod
    def MediumPurple(*obj, sep=sep_):        return NCS(obj,Fore.MediumPurple,Style.NoForeground,sep)
    @staticmethod
    def DarkMagenta(*obj, sep=sep_):         return NCS(obj,Fore.DarkMagenta,Style.NoForeground,sep)
    @staticmethod
    def DarkViolet(*obj, sep=sep_):          return NCS(obj,Fore.DarkViolet,Style.NoForeground,sep)
    @staticmethod
    def DarkOrchid(*obj, sep=sep_):          return NCS(obj,Fore.DarkOrchid,Style.NoForeground,sep)
    @staticmethod
    def MediumOrchid(*obj, sep=sep_):        return NCS(obj,Fore.MediumOrchid,Style.NoForeground,sep)
    @staticmethod
    def Purple(*obj, sep=sep_):              return NCS(obj,Fore.Purple,Style.NoForeground,sep)
    @staticmethod
    def Thistle(*obj, sep=sep_):             return NCS(obj,Fore.Thistle,Style.NoForeground,sep)
    @staticmethod
    def Plum(*obj, sep=sep_):                return NCS(obj,Fore.Plum,Style.NoForeground,sep)
    @staticmethod
    def Violet(*obj, sep=sep_):              return NCS(obj,Fore.Violet,Style.NoForeground,sep)
    @staticmethod
    def Magenta(*obj, sep=sep_):             return NCS(obj,Fore.Magenta,Style.NoForeground,sep)
    @staticmethod
    def Orchid(*obj, sep=sep_):              return NCS(obj,Fore.Orchid,Style.NoForeground,sep)
    @staticmethod
    def MediumVioletRed(*obj, sep=sep_):     return NCS(obj,Fore.MediumVioletRed,Style.NoForeground,sep)
    @staticmethod
    def PaleVioletRed(*obj, sep=sep_):       return NCS(obj,Fore.PaleVioletRed,Style.NoForeground,sep)
    @staticmethod
    def DeepPink(*obj, sep=sep_):            return NCS(obj,Fore.DeepPink,Style.NoForeground,sep)
    @staticmethod
    def HotPink(*obj, sep=sep_):             return NCS(obj,Fore.HotPink,Style.NoForeground,sep)
    @staticmethod
    def LightPink(*obj, sep=sep_):           return NCS(obj,Fore.LightPink,Style.NoForeground,sep)
    @staticmethod
    def Pink(*obj, sep=sep_):                return NCS(obj,Fore.Pink,Style.NoForeground,sep)
    @staticmethod
    def AntiqueWhite(*obj, sep=sep_):        return NCS(obj,Fore.AntiqueWhite,Style.NoForeground,sep)
    @staticmethod
    def Beige(*obj, sep=sep_):               return NCS(obj,Fore.Beige,Style.NoForeground,sep)
    @staticmethod
    def Bisque(*obj, sep=sep_):              return NCS(obj,Fore.Bisque,Style.NoForeground,sep)
    @staticmethod
    def BlanchedAlmond(*obj, sep=sep_):      return NCS(obj,Fore.BlanchedAlmond,Style.NoForeground,sep)
    @staticmethod
    def Wheat(*obj, sep=sep_):               return NCS(obj,Fore.Wheat,Style.NoForeground,sep)
    @staticmethod
    def CornSilk(*obj, sep=sep_):            return NCS(obj,Fore.CornSilk,Style.NoForeground,sep)
    @staticmethod
    def LemonChiffon(*obj, sep=sep_):        return NCS(obj,Fore.LemonChiffon,Style.NoForeground,sep)
    @staticmethod
    def LightGoldenRodYellow(*obj, sep=sep_):return NCS(obj,Fore.LightGoldenRodYellow,Style.NoForeground,sep)
    @staticmethod
    def LightYellow(*obj, sep=sep_):         return NCS(obj,Fore.LightYellow,Style.NoForeground,sep)
    @staticmethod
    def SaddleBrown(*obj, sep=sep_):         return NCS(obj,Fore.SaddleBrown,Style.NoForeground,sep)
    @staticmethod
    def Sienna(*obj, sep=sep_):              return NCS(obj,Fore.Sienna,Style.NoForeground,sep)
    @staticmethod
    def Chocolate(*obj, sep=sep_):           return NCS(obj,Fore.Chocolate,Style.NoForeground,sep)
    @staticmethod
    def Peru(*obj, sep=sep_):                return NCS(obj,Fore.Peru,Style.NoForeground,sep)
    @staticmethod
    def SandyBrown(*obj, sep=sep_):          return NCS(obj,Fore.SandyBrown,Style.NoForeground,sep)
    @staticmethod
    def BurlyWood(*obj, sep=sep_):           return NCS(obj,Fore.BurlyWood,Style.NoForeground,sep)
    @staticmethod
    def Tan(*obj, sep=sep_):                 return NCS(obj,Fore.Tan,Style.NoForeground,sep)
    @staticmethod
    def RosyBrown(*obj, sep=sep_):           return NCS(obj,Fore.RosyBrown,Style.NoForeground,sep)
    @staticmethod
    def Moccasin(*obj, sep=sep_):            return NCS(obj,Fore.Moccasin,Style.NoForeground,sep)
    @staticmethod
    def NavajoWhite(*obj, sep=sep_):         return NCS(obj,Fore.NavajoWhite,Style.NoForeground,sep)
    @staticmethod
    def PeachPuff(*obj, sep=sep_):           return NCS(obj,Fore.PeachPuff,Style.NoForeground,sep)
    @staticmethod
    def MistyRose(*obj, sep=sep_):           return NCS(obj,Fore.MistyRose,Style.NoForeground,sep)
    @staticmethod
    def LavenderBlush(*obj, sep=sep_):       return NCS(obj,Fore.LavenderBlush,Style.NoForeground,sep)
    @staticmethod
    def Linen(*obj, sep=sep_):               return NCS(obj,Fore.Linen,Style.NoForeground,sep)
    @staticmethod
    def OldLace(*obj, sep=sep_):             return NCS(obj,Fore.OldLace,Style.NoForeground,sep)
    @staticmethod
    def PapayaWhip(*obj, sep=sep_):          return NCS(obj,Fore.PapayaWhip,Style.NoForeground,sep)
    @staticmethod
    def WeaShell(*obj, sep=sep_):            return NCS(obj,Fore.WeaShell,Style.NoForeground,sep)
    @staticmethod
    def MintCream(*obj, sep=sep_):           return NCS(obj,Fore.MintCream,Style.NoForeground,sep)
    @staticmethod
    def SlateGray(*obj, sep=sep_):           return NCS(obj,Fore.SlateGray,Style.NoForeground,sep)
    @staticmethod
    def LightSlateGray(*obj, sep=sep_):      return NCS(obj,Fore.LightSlateGray,Style.NoForeground,sep)
    @staticmethod
    def LightSteelBlue(*obj, sep=sep_):      return NCS(obj,Fore.LightSteelBlue,Style.NoForeground,sep)
    @staticmethod
    def Lavender(*obj, sep=sep_):            return NCS(obj,Fore.Lavender,Style.NoForeground,sep)
    @staticmethod
    def FloralWhite(*obj, sep=sep_):         return NCS(obj,Fore.FloralWhite,Style.NoForeground,sep)
    @staticmethod
    def AliceBlue(*obj, sep=sep_):           return NCS(obj,Fore.AliceBlue,Style.NoForeground,sep)
    @staticmethod
    def GhostWhite(*obj, sep=sep_):          return NCS(obj,Fore.GhostWhite,Style.NoForeground,sep)
    @staticmethod
    def Honeydew(*obj, sep=sep_):            return NCS(obj,Fore.Honeydew,Style.NoForeground,sep)
    @staticmethod
    def Ivory(*obj, sep=sep_):               return NCS(obj,Fore.Ivory,Style.NoForeground,sep)
    @staticmethod
    def Azure(*obj, sep=sep_):               return NCS(obj,Fore.Azure,Style.NoForeground,sep)
    @staticmethod
    def Snow(*obj, sep=sep_):                return NCS(obj,Fore.Snow,Style.NoForeground,sep)
    @staticmethod
    def Black(*obj, sep=sep_):               return NCS(obj,Fore.Black,Style.NoForeground,sep)
    @staticmethod
    def DimGray(*obj, sep=sep_):             return NCS(obj,Fore.DimGray,Style.NoForeground,sep)
    @staticmethod
    def Gray(*obj, sep=sep_):                return NCS(obj,Fore.Gray,Style.NoForeground,sep)
    @staticmethod
    def DarkGray(*obj, sep=sep_):            return NCS(obj,Fore.DarkGray,Style.NoForeground,sep)
    @staticmethod
    def Silver(*obj, sep=sep_):              return NCS(obj,Fore.Silver,Style.NoForeground,sep)
    @staticmethod
    def LightGray(*obj, sep=sep_):           return NCS(obj,Fore.LightGray,Style.NoForeground,sep)
    @staticmethod
    def Gainsboro(*obj, sep=sep_):           return NCS(obj,Fore.Gainsboro,Style.NoForeground,sep)
    @staticmethod
    def WhiteSmoke(*obj, sep=sep_):          return NCS(obj,Fore.WhiteSmoke,Style.NoForeground,sep)
    @staticmethod
    def White(*obj, sep=sep_):               return NCS(obj,Fore.White,Style.NoForeground,sep)