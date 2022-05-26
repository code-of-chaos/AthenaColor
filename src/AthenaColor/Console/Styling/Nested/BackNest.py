# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Color.ColorSystem import RGB,HEX, NormalizeRgb
from AthenaColor.Functions.ANSIsequences import NestedColorSequence
from AthenaColor.Console.Styling.Inline.Bodies import Back
from AthenaColor.Console.Styling.Inline.Style import Style

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "BackNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence # Done for slight speed increase
sep_=" "

class BackNest:
    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def custom(*obj, color:RGB|HEX, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"\033[48;2;{';'.join(*color.export())}m",
            Style.NoForeground,
            sep=sep
        )

    @staticmethod
    def rgb(*obj, r:int,g:int,b:int, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"\033[48;2;{';'.join(*NormalizeRgb(r, g, b))}m",
            Style.NoForeground,
            sep=sep
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    # No partial methods, as this was increase the speed impact 2-fold
    @staticmethod
    def Maroon(*obj, sep=sep_):              return NCS(obj,Back.Maroon,Style.NoBackground,sep)
    @staticmethod
    def DarkRed(*obj, sep=sep_):             return NCS(obj,Back.DarkRed,Style.NoBackground,sep)
    @staticmethod
    def Brown(*obj, sep=sep_):               return NCS(obj,Back.Brown,Style.NoBackground,sep)
    @staticmethod
    def Firebrick(*obj, sep=sep_):           return NCS(obj,Back.Firebrick,Style.NoBackground,sep)
    @staticmethod
    def Crimson(*obj, sep=sep_):             return NCS(obj,Back.Crimson,Style.NoBackground,sep)
    @staticmethod
    def Red(*obj, sep=sep_):                 return NCS(obj,Back.Red,Style.NoBackground,sep)
    @staticmethod
    def Tomato(*obj, sep=sep_):              return NCS(obj,Back.Tomato,Style.NoBackground,sep)
    @staticmethod
    def Coral(*obj, sep=sep_):               return NCS(obj,Back.Coral,Style.NoBackground,sep)
    @staticmethod
    def IndianRed(*obj, sep=sep_):           return NCS(obj,Back.IndianRed,Style.NoBackground,sep)
    @staticmethod
    def LightCoral(*obj, sep=sep_):          return NCS(obj,Back.LightCoral,Style.NoBackground,sep)
    @staticmethod
    def DarkSalmon(*obj, sep=sep_):          return NCS(obj,Back.DarkSalmon,Style.NoBackground,sep)
    @staticmethod
    def Salmon(*obj, sep=sep_):              return NCS(obj,Back.Salmon,Style.NoBackground,sep)
    @staticmethod
    def LightSalmon(*obj, sep=sep_):         return NCS(obj,Back.LightSalmon,Style.NoBackground,sep)
    @staticmethod
    def OrangeRed(*obj, sep=sep_):           return NCS(obj,Back.OrangeRed,Style.NoBackground,sep)
    @staticmethod
    def DarkOrange(*obj, sep=sep_):          return NCS(obj,Back.DarkOrange,Style.NoBackground,sep)
    @staticmethod
    def Orange(*obj, sep=sep_):              return NCS(obj,Back.Orange,Style.NoBackground,sep)
    @staticmethod
    def Gold(*obj, sep=sep_):                return NCS(obj,Back.Gold,Style.NoBackground,sep)
    @staticmethod
    def DarkGoldenRod(*obj, sep=sep_):       return NCS(obj,Back.DarkGoldenRod,Style.NoBackground,sep)
    @staticmethod
    def GoldenRod(*obj, sep=sep_):           return NCS(obj,Back.GoldenRod,Style.NoBackground,sep)
    @staticmethod
    def PaleGoldenRod(*obj, sep=sep_):       return NCS(obj,Back.PaleGoldenRod,Style.NoBackground,sep)
    @staticmethod
    def DarkKhaki(*obj, sep=sep_):           return NCS(obj,Back.DarkKhaki,Style.NoBackground,sep)
    @staticmethod
    def Khaki(*obj, sep=sep_):               return NCS(obj,Back.Khaki,Style.NoBackground,sep)
    @staticmethod
    def Olive(*obj, sep=sep_):               return NCS(obj,Back.Olive,Style.NoBackground,sep)
    @staticmethod
    def Yellow(*obj, sep=sep_):              return NCS(obj,Back.Yellow,Style.NoBackground,sep)
    @staticmethod
    def YellowGreen(*obj, sep=sep_):         return NCS(obj,Back.YellowGreen,Style.NoBackground,sep)
    @staticmethod
    def DarkOliveGreen(*obj, sep=sep_):      return NCS(obj,Back.DarkOliveGreen,Style.NoBackground,sep)
    @staticmethod
    def OliveDrab(*obj, sep=sep_):           return NCS(obj,Back.OliveDrab,Style.NoBackground,sep)
    @staticmethod
    def LawnGreen(*obj, sep=sep_):           return NCS(obj,Back.LawnGreen,Style.NoBackground,sep)
    @staticmethod
    def Chartreuse(*obj, sep=sep_):          return NCS(obj,Back.Chartreuse,Style.NoBackground,sep)
    @staticmethod
    def GreenYellow(*obj, sep=sep_):         return NCS(obj,Back.GreenYellow,Style.NoBackground,sep)
    @staticmethod
    def DarkGreen(*obj, sep=sep_):           return NCS(obj,Back.DarkGreen,Style.NoBackground,sep)
    @staticmethod
    def Green(*obj, sep=sep_):               return NCS(obj,Back.Green,Style.NoBackground,sep)
    @staticmethod
    def ForestGreen(*obj, sep=sep_):         return NCS(obj,Back.ForestGreen,Style.NoBackground,sep)
    @staticmethod
    def Lime(*obj, sep=sep_):                return NCS(obj,Back.Lime,Style.NoBackground,sep)
    @staticmethod
    def LimeGreen(*obj, sep=sep_):           return NCS(obj,Back.LimeGreen,Style.NoBackground,sep)
    @staticmethod
    def LightGreen(*obj, sep=sep_):          return NCS(obj,Back.LightGreen,Style.NoBackground,sep)
    @staticmethod
    def PaleGreen(*obj, sep=sep_):           return NCS(obj,Back.PaleGreen,Style.NoBackground,sep)
    @staticmethod
    def DarkSeaGreen(*obj, sep=sep_):        return NCS(obj,Back.DarkSeaGreen,Style.NoBackground,sep)
    @staticmethod
    def MediumSpringGreen(*obj, sep=sep_):   return NCS(obj,Back.MediumSpringGreen,Style.NoBackground,sep)
    @staticmethod
    def SpringGreen(*obj, sep=sep_):         return NCS(obj,Back.SpringGreen,Style.NoBackground,sep)
    @staticmethod
    def SeaGreen(*obj, sep=sep_):            return NCS(obj,Back.SeaGreen,Style.NoBackground,sep)
    @staticmethod
    def MediumAquaMarine(*obj, sep=sep_):    return NCS(obj,Back.MediumAquaMarine,Style.NoBackground,sep)
    @staticmethod
    def MediumSeaGreen(*obj, sep=sep_):      return NCS(obj,Back.MediumSeaGreen,Style.NoBackground,sep)
    @staticmethod
    def LightSeaGreen(*obj, sep=sep_):       return NCS(obj,Back.LightSeaGreen,Style.NoBackground,sep)
    @staticmethod
    def DarkSlateGray(*obj, sep=sep_):       return NCS(obj,Back.DarkSlateGray,Style.NoBackground,sep)
    @staticmethod
    def Teal(*obj, sep=sep_):                return NCS(obj,Back.Teal,Style.NoBackground,sep)
    @staticmethod
    def DarkCyan(*obj, sep=sep_):            return NCS(obj,Back.DarkCyan,Style.NoBackground,sep)
    @staticmethod
    def Aqua(*obj, sep=sep_):                return NCS(obj,Back.Aqua,Style.NoBackground,sep)
    @staticmethod
    def Cyan(*obj, sep=sep_):                return NCS(obj,Back.Cyan,Style.NoBackground,sep)
    @staticmethod
    def LightCyan(*obj, sep=sep_):           return NCS(obj,Back.LightCyan,Style.NoBackground,sep)
    @staticmethod
    def DarkTurquoise(*obj, sep=sep_):       return NCS(obj,Back.DarkTurquoise,Style.NoBackground,sep)
    @staticmethod
    def Turquoise(*obj, sep=sep_):           return NCS(obj,Back.Turquoise,Style.NoBackground,sep)
    @staticmethod
    def MediumTurquoise(*obj, sep=sep_):     return NCS(obj,Back.MediumTurquoise,Style.NoBackground,sep)
    @staticmethod
    def PaleTurquoise(*obj, sep=sep_):       return NCS(obj,Back.PaleTurquoise,Style.NoBackground,sep)
    @staticmethod
    def AquaMarine(*obj, sep=sep_):          return NCS(obj,Back.AquaMarine,Style.NoBackground,sep)
    @staticmethod
    def PowderBlue(*obj, sep=sep_):          return NCS(obj,Back.PowderBlue,Style.NoBackground,sep)
    @staticmethod
    def CadetBlue(*obj, sep=sep_):           return NCS(obj,Back.CadetBlue,Style.NoBackground,sep)
    @staticmethod
    def SteelBlue(*obj, sep=sep_):           return NCS(obj,Back.SteelBlue,Style.NoBackground,sep)
    @staticmethod
    def CornFlowerBlue(*obj, sep=sep_):      return NCS(obj,Back.CornFlowerBlue,Style.NoBackground,sep)
    @staticmethod
    def DeepSkyBlue(*obj, sep=sep_):         return NCS(obj,Back.DeepSkyBlue,Style.NoBackground,sep)
    @staticmethod
    def DodgerBlue(*obj, sep=sep_):          return NCS(obj,Back.DodgerBlue,Style.NoBackground,sep)
    @staticmethod
    def LightBlue(*obj, sep=sep_):           return NCS(obj,Back.LightBlue,Style.NoBackground,sep)
    @staticmethod
    def SkyBlue(*obj, sep=sep_):             return NCS(obj,Back.SkyBlue,Style.NoBackground,sep)
    @staticmethod
    def LightSkyBlue(*obj, sep=sep_):        return NCS(obj,Back.LightSkyBlue,Style.NoBackground,sep)
    @staticmethod
    def MidnightBlue(*obj, sep=sep_):        return NCS(obj,Back.MidnightBlue,Style.NoBackground,sep)
    @staticmethod
    def Navy(*obj, sep=sep_):                return NCS(obj,Back.Navy,Style.NoBackground,sep)
    @staticmethod
    def DarkBlue(*obj, sep=sep_):            return NCS(obj,Back.DarkBlue,Style.NoBackground,sep)
    @staticmethod
    def MediumBlue(*obj, sep=sep_):          return NCS(obj,Back.MediumBlue,Style.NoBackground,sep)
    @staticmethod
    def Blue(*obj, sep=sep_):                return NCS(obj,Back.Blue,Style.NoBackground,sep)
    @staticmethod
    def RoyalBlue(*obj, sep=sep_):           return NCS(obj,Back.RoyalBlue,Style.NoBackground,sep)
    @staticmethod
    def BlueViolet(*obj, sep=sep_):          return NCS(obj,Back.BlueViolet,Style.NoBackground,sep)
    @staticmethod
    def Indigo(*obj, sep=sep_):              return NCS(obj,Back.Indigo,Style.NoBackground,sep)
    @staticmethod
    def DarkSlateBlue(*obj, sep=sep_):       return NCS(obj,Back.DarkSlateBlue,Style.NoBackground,sep)
    @staticmethod
    def SlateBlue(*obj, sep=sep_):           return NCS(obj,Back.SlateBlue,Style.NoBackground,sep)
    @staticmethod
    def MediumSlateBlue(*obj, sep=sep_):     return NCS(obj,Back.MediumSlateBlue,Style.NoBackground,sep)
    @staticmethod
    def MediumPurple(*obj, sep=sep_):        return NCS(obj,Back.MediumPurple,Style.NoBackground,sep)
    @staticmethod
    def DarkMagenta(*obj, sep=sep_):         return NCS(obj,Back.DarkMagenta,Style.NoBackground,sep)
    @staticmethod
    def DarkViolet(*obj, sep=sep_):          return NCS(obj,Back.DarkViolet,Style.NoBackground,sep)
    @staticmethod
    def DarkOrchid(*obj, sep=sep_):          return NCS(obj,Back.DarkOrchid,Style.NoBackground,sep)
    @staticmethod
    def MediumOrchid(*obj, sep=sep_):        return NCS(obj,Back.MediumOrchid,Style.NoBackground,sep)
    @staticmethod
    def Purple(*obj, sep=sep_):              return NCS(obj,Back.Purple,Style.NoBackground,sep)
    @staticmethod
    def Thistle(*obj, sep=sep_):             return NCS(obj,Back.Thistle,Style.NoBackground,sep)
    @staticmethod
    def Plum(*obj, sep=sep_):                return NCS(obj,Back.Plum,Style.NoBackground,sep)
    @staticmethod
    def Violet(*obj, sep=sep_):              return NCS(obj,Back.Violet,Style.NoBackground,sep)
    @staticmethod
    def Magenta(*obj, sep=sep_):             return NCS(obj,Back.Magenta,Style.NoBackground,sep)
    @staticmethod
    def Orchid(*obj, sep=sep_):              return NCS(obj,Back.Orchid,Style.NoBackground,sep)
    @staticmethod
    def MediumVioletRed(*obj, sep=sep_):     return NCS(obj,Back.MediumVioletRed,Style.NoBackground,sep)
    @staticmethod
    def PaleVioletRed(*obj, sep=sep_):       return NCS(obj,Back.PaleVioletRed,Style.NoBackground,sep)
    @staticmethod
    def DeepPink(*obj, sep=sep_):            return NCS(obj,Back.DeepPink,Style.NoBackground,sep)
    @staticmethod
    def HotPink(*obj, sep=sep_):             return NCS(obj,Back.HotPink,Style.NoBackground,sep)
    @staticmethod
    def LightPink(*obj, sep=sep_):           return NCS(obj,Back.LightPink,Style.NoBackground,sep)
    @staticmethod
    def Pink(*obj, sep=sep_):                return NCS(obj,Back.Pink,Style.NoBackground,sep)
    @staticmethod
    def AntiqueWhite(*obj, sep=sep_):        return NCS(obj,Back.AntiqueWhite,Style.NoBackground,sep)
    @staticmethod
    def Beige(*obj, sep=sep_):               return NCS(obj,Back.Beige,Style.NoBackground,sep)
    @staticmethod
    def Bisque(*obj, sep=sep_):              return NCS(obj,Back.Bisque,Style.NoBackground,sep)
    @staticmethod
    def BlanchedAlmond(*obj, sep=sep_):      return NCS(obj,Back.BlanchedAlmond,Style.NoBackground,sep)
    @staticmethod
    def Wheat(*obj, sep=sep_):               return NCS(obj,Back.Wheat,Style.NoBackground,sep)
    @staticmethod
    def CornSilk(*obj, sep=sep_):            return NCS(obj,Back.CornSilk,Style.NoBackground,sep)
    @staticmethod
    def LemonChiffon(*obj, sep=sep_):        return NCS(obj,Back.LemonChiffon,Style.NoBackground,sep)
    @staticmethod
    def LightGoldenRodYellow(*obj, sep=sep_):return NCS(obj,Back.LightGoldenRodYellow,Style.NoBackground,sep)
    @staticmethod
    def LightYellow(*obj, sep=sep_):         return NCS(obj,Back.LightYellow,Style.NoBackground,sep)
    @staticmethod
    def SaddleBrown(*obj, sep=sep_):         return NCS(obj,Back.SaddleBrown,Style.NoBackground,sep)
    @staticmethod
    def Sienna(*obj, sep=sep_):              return NCS(obj,Back.Sienna,Style.NoBackground,sep)
    @staticmethod
    def Chocolate(*obj, sep=sep_):           return NCS(obj,Back.Chocolate,Style.NoBackground,sep)
    @staticmethod
    def Peru(*obj, sep=sep_):                return NCS(obj,Back.Peru,Style.NoBackground,sep)
    @staticmethod
    def SandyBrown(*obj, sep=sep_):          return NCS(obj,Back.SandyBrown,Style.NoBackground,sep)
    @staticmethod
    def BurlyWood(*obj, sep=sep_):           return NCS(obj,Back.BurlyWood,Style.NoBackground,sep)
    @staticmethod
    def Tan(*obj, sep=sep_):                 return NCS(obj,Back.Tan,Style.NoBackground,sep)
    @staticmethod
    def RosyBrown(*obj, sep=sep_):           return NCS(obj,Back.RosyBrown,Style.NoBackground,sep)
    @staticmethod
    def Moccasin(*obj, sep=sep_):            return NCS(obj,Back.Moccasin,Style.NoBackground,sep)
    @staticmethod
    def NavajoWhite(*obj, sep=sep_):         return NCS(obj,Back.NavajoWhite,Style.NoBackground,sep)
    @staticmethod
    def PeachPuff(*obj, sep=sep_):           return NCS(obj,Back.PeachPuff,Style.NoBackground,sep)
    @staticmethod
    def MistyRose(*obj, sep=sep_):           return NCS(obj,Back.MistyRose,Style.NoBackground,sep)
    @staticmethod
    def LavenderBlush(*obj, sep=sep_):       return NCS(obj,Back.LavenderBlush,Style.NoBackground,sep)
    @staticmethod
    def Linen(*obj, sep=sep_):               return NCS(obj,Back.Linen,Style.NoBackground,sep)
    @staticmethod
    def OldLace(*obj, sep=sep_):             return NCS(obj,Back.OldLace,Style.NoBackground,sep)
    @staticmethod
    def PapayaWhip(*obj, sep=sep_):          return NCS(obj,Back.PapayaWhip,Style.NoBackground,sep)
    @staticmethod
    def WeaShell(*obj, sep=sep_):            return NCS(obj,Back.WeaShell,Style.NoBackground,sep)
    @staticmethod
    def MintCream(*obj, sep=sep_):           return NCS(obj,Back.MintCream,Style.NoBackground,sep)
    @staticmethod
    def SlateGray(*obj, sep=sep_):           return NCS(obj,Back.SlateGray,Style.NoBackground,sep)
    @staticmethod
    def LightSlateGray(*obj, sep=sep_):      return NCS(obj,Back.LightSlateGray,Style.NoBackground,sep)
    @staticmethod
    def LightSteelBlue(*obj, sep=sep_):      return NCS(obj,Back.LightSteelBlue,Style.NoBackground,sep)
    @staticmethod
    def Lavender(*obj, sep=sep_):            return NCS(obj,Back.Lavender,Style.NoBackground,sep)
    @staticmethod
    def FloralWhite(*obj, sep=sep_):         return NCS(obj,Back.FloralWhite,Style.NoBackground,sep)
    @staticmethod
    def AliceBlue(*obj, sep=sep_):           return NCS(obj,Back.AliceBlue,Style.NoBackground,sep)
    @staticmethod
    def GhostWhite(*obj, sep=sep_):          return NCS(obj,Back.GhostWhite,Style.NoBackground,sep)
    @staticmethod
    def Honeydew(*obj, sep=sep_):            return NCS(obj,Back.Honeydew,Style.NoBackground,sep)
    @staticmethod
    def Ivory(*obj, sep=sep_):               return NCS(obj,Back.Ivory,Style.NoBackground,sep)
    @staticmethod
    def Azure(*obj, sep=sep_):               return NCS(obj,Back.Azure,Style.NoBackground,sep)
    @staticmethod
    def Snow(*obj, sep=sep_):                return NCS(obj,Back.Snow,Style.NoBackground,sep)
    @staticmethod
    def Black(*obj, sep=sep_):               return NCS(obj,Back.Black,Style.NoBackground,sep)
    @staticmethod
    def DimGray(*obj, sep=sep_):             return NCS(obj,Back.DimGray,Style.NoBackground,sep)
    @staticmethod
    def Gray(*obj, sep=sep_):                return NCS(obj,Back.Gray,Style.NoBackground,sep)
    @staticmethod
    def DarkGray(*obj, sep=sep_):            return NCS(obj,Back.DarkGray,Style.NoBackground,sep)
    @staticmethod
    def Silver(*obj, sep=sep_):              return NCS(obj,Back.Silver,Style.NoBackground,sep)
    @staticmethod
    def LightGray(*obj, sep=sep_):           return NCS(obj,Back.LightGray,Style.NoBackground,sep)
    @staticmethod
    def Gainsboro(*obj, sep=sep_):           return NCS(obj,Back.Gainsboro,Style.NoBackground,sep)
    @staticmethod
    def WhiteSmoke(*obj, sep=sep_):          return NCS(obj,Back.WhiteSmoke,Style.NoBackground,sep)
    @staticmethod
    def White(*obj, sep=sep_):               return NCS(obj,Back.White,Style.NoBackground,sep)