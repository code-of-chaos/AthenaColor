# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX, NormalizeRgb
from AthenaColor.Functions.ANSIsquences import NestedColorSequence
from AthenaColor.Objects.Console.Styling.Inline.Bodies import Underline
from AthenaColor.Objects.Console.Styling.Inline.Style import Style


# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "UnderlineNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence # Done for slight speed increase
sep_=" "

class UnderlineNest:
    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def custom(*obj, color:RGB|HEX, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"\033[58;2;{';'.join(*color.export())}m",
            Style.NoForeground,
            sep=sep
        )

    @staticmethod
    def rgb(*obj, r:int,g:int,b:int, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"\033[58;2;{';'.join(*NormalizeRgb(r, g, b))}m",
            Style.NoForeground,
            sep=sep
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    # No partial methods, as this was increase the speed impact 2-fold
    @staticmethod
    def Maroon( *obj, sep=sep_):             return NCS(obj,Underline.Maroon,Style.NoUnderline,sep)
    @staticmethod
    def DarkRed(*obj, sep=sep_):             return NCS(obj,Underline.DarkRed,Style.NoUnderline,sep)
    @staticmethod
    def Brown(*obj, sep=sep_):               return NCS(obj,Underline.Brown,Style.NoUnderline,sep)
    @staticmethod
    def Firebrick(*obj, sep=sep_):           return NCS(obj,Underline.Firebrick,Style.NoUnderline,sep)
    @staticmethod
    def Crimson(*obj, sep=sep_):             return NCS(obj,Underline.Crimson,Style.NoUnderline,sep)
    @staticmethod
    def Red(*obj, sep=sep_):                 return NCS(obj,Underline.Red,Style.NoUnderline,sep)
    @staticmethod
    def Tomato(*obj, sep=sep_):              return NCS(obj,Underline.Tomato,Style.NoUnderline,sep)
    @staticmethod
    def Coral(*obj, sep=sep_):               return NCS(obj,Underline.Coral,Style.NoUnderline,sep)
    @staticmethod
    def IndianRed(*obj, sep=sep_):           return NCS(obj,Underline.IndianRed,Style.NoUnderline,sep)
    @staticmethod
    def LightCoral(*obj, sep=sep_):          return NCS(obj,Underline.LightCoral,Style.NoUnderline,sep)
    @staticmethod
    def DarkSalmon(*obj, sep=sep_):          return NCS(obj,Underline.DarkSalmon,Style.NoUnderline,sep)
    @staticmethod
    def Salmon(*obj, sep=sep_):              return NCS(obj,Underline.Salmon,Style.NoUnderline,sep)
    @staticmethod
    def LightSalmon(*obj, sep=sep_):         return NCS(obj,Underline.LightSalmon,Style.NoUnderline,sep)
    @staticmethod
    def OrangeRed(*obj, sep=sep_):           return NCS(obj,Underline.OrangeRed,Style.NoUnderline,sep)
    @staticmethod
    def DarkOrange(*obj, sep=sep_):          return NCS(obj,Underline.DarkOrange,Style.NoUnderline,sep)
    @staticmethod
    def Orange(*obj, sep=sep_):              return NCS(obj,Underline.Orange,Style.NoUnderline,sep)
    @staticmethod
    def Gold(*obj, sep=sep_):                return NCS(obj,Underline.Gold,Style.NoUnderline,sep)
    @staticmethod
    def DarkGoldenRod(*obj, sep=sep_):       return NCS(obj,Underline.DarkGoldenRod,Style.NoUnderline,sep)
    @staticmethod
    def GoldenRod(*obj, sep=sep_):           return NCS(obj,Underline.GoldenRod,Style.NoUnderline,sep)
    @staticmethod
    def PaleGoldenRod(*obj, sep=sep_):       return NCS(obj,Underline.PaleGoldenRod,Style.NoUnderline,sep)
    @staticmethod
    def DarkKhaki(*obj, sep=sep_):           return NCS(obj,Underline.DarkKhaki,Style.NoUnderline,sep)
    @staticmethod
    def Khaki(*obj, sep=sep_):               return NCS(obj,Underline.Khaki,Style.NoUnderline,sep)
    @staticmethod
    def Olive(*obj, sep=sep_):               return NCS(obj,Underline.Olive,Style.NoUnderline,sep)
    @staticmethod
    def Yellow(*obj, sep=sep_):              return NCS(obj,Underline.Yellow,Style.NoUnderline,sep)
    @staticmethod
    def YellowGreen(*obj, sep=sep_):         return NCS(obj,Underline.YellowGreen,Style.NoUnderline,sep)
    @staticmethod
    def DarkOliveGreen(*obj, sep=sep_):      return NCS(obj,Underline.DarkOliveGreen,Style.NoUnderline,sep)
    @staticmethod
    def OliveDrab(*obj, sep=sep_):           return NCS(obj,Underline.OliveDrab,Style.NoUnderline,sep)
    @staticmethod
    def LawnGreen(*obj, sep=sep_):           return NCS(obj,Underline.LawnGreen,Style.NoUnderline,sep)
    @staticmethod
    def Chartreuse(*obj, sep=sep_):          return NCS(obj,Underline.Chartreuse,Style.NoUnderline,sep)
    @staticmethod
    def GreenYellow(*obj, sep=sep_):         return NCS(obj,Underline.GreenYellow,Style.NoUnderline,sep)
    @staticmethod
    def DarkGreen(*obj, sep=sep_):           return NCS(obj,Underline.DarkGreen,Style.NoUnderline,sep)
    @staticmethod
    def Green(*obj, sep=sep_):               return NCS(obj,Underline.Green,Style.NoUnderline,sep)
    @staticmethod
    def ForestGreen(*obj, sep=sep_):         return NCS(obj,Underline.ForestGreen,Style.NoUnderline,sep)
    @staticmethod
    def Lime(*obj, sep=sep_):                return NCS(obj,Underline.Lime,Style.NoUnderline,sep)
    @staticmethod
    def LimeGreen(*obj, sep=sep_):           return NCS(obj,Underline.LimeGreen,Style.NoUnderline,sep)
    @staticmethod
    def LightGreen(*obj, sep=sep_):          return NCS(obj,Underline.LightGreen,Style.NoUnderline,sep)
    @staticmethod
    def PaleGreen(*obj, sep=sep_):           return NCS(obj,Underline.PaleGreen,Style.NoUnderline,sep)
    @staticmethod
    def DarkSeaGreen(*obj, sep=sep_):        return NCS(obj,Underline.DarkSeaGreen,Style.NoUnderline,sep)
    @staticmethod
    def MediumSpringGreen(*obj, sep=sep_):   return NCS(obj,Underline.MediumSpringGreen,Style.NoUnderline,sep)
    @staticmethod
    def SpringGreen(*obj, sep=sep_):         return NCS(obj,Underline.SpringGreen,Style.NoUnderline,sep)
    @staticmethod
    def SeaGreen(*obj, sep=sep_):            return NCS(obj,Underline.SeaGreen,Style.NoUnderline,sep)
    @staticmethod
    def MediumAquaMarine(*obj, sep=sep_):    return NCS(obj,Underline.MediumAquaMarine,Style.NoUnderline,sep)
    @staticmethod
    def MediumSeaGreen(*obj, sep=sep_):      return NCS(obj,Underline.MediumSeaGreen,Style.NoUnderline,sep)
    @staticmethod
    def LightSeaGreen(*obj, sep=sep_):       return NCS(obj,Underline.LightSeaGreen,Style.NoUnderline,sep)
    @staticmethod
    def DarkSlateGray(*obj, sep=sep_):       return NCS(obj,Underline.DarkSlateGray,Style.NoUnderline,sep)
    @staticmethod
    def Teal(*obj, sep=sep_):                return NCS(obj,Underline.Teal,Style.NoUnderline,sep)
    @staticmethod
    def DarkCyan(*obj, sep=sep_):            return NCS(obj,Underline.DarkCyan,Style.NoUnderline,sep)
    @staticmethod
    def Aqua(*obj, sep=sep_):                return NCS(obj,Underline.Aqua,Style.NoUnderline,sep)
    @staticmethod
    def Cyan(*obj, sep=sep_):                return NCS(obj,Underline.Cyan,Style.NoUnderline,sep)
    @staticmethod
    def LightCyan(*obj, sep=sep_):           return NCS(obj,Underline.LightCyan,Style.NoUnderline,sep)
    @staticmethod
    def DarkTurquoise(*obj, sep=sep_):       return NCS(obj,Underline.DarkTurquoise,Style.NoUnderline,sep)
    @staticmethod
    def Turquoise(*obj, sep=sep_):           return NCS(obj,Underline.Turquoise,Style.NoUnderline,sep)
    @staticmethod
    def MediumTurquoise(*obj, sep=sep_):     return NCS(obj,Underline.MediumTurquoise,Style.NoUnderline,sep)
    @staticmethod
    def PaleTurquoise(*obj, sep=sep_):       return NCS(obj,Underline.PaleTurquoise,Style.NoUnderline,sep)
    @staticmethod
    def AquaMarine(*obj, sep=sep_):          return NCS(obj,Underline.AquaMarine,Style.NoUnderline,sep)
    @staticmethod
    def PowderBlue(*obj, sep=sep_):          return NCS(obj,Underline.PowderBlue,Style.NoUnderline,sep)
    @staticmethod
    def CadetBlue(*obj, sep=sep_):           return NCS(obj,Underline.CadetBlue,Style.NoUnderline,sep)
    @staticmethod
    def SteelBlue(*obj, sep=sep_):           return NCS(obj,Underline.SteelBlue,Style.NoUnderline,sep)
    @staticmethod
    def CornFlowerBlue(*obj, sep=sep_):      return NCS(obj,Underline.CornFlowerBlue,Style.NoUnderline,sep)
    @staticmethod
    def DeepSkyBlue(*obj, sep=sep_):         return NCS(obj,Underline.DeepSkyBlue,Style.NoUnderline,sep)
    @staticmethod
    def DodgerBlue(*obj, sep=sep_):          return NCS(obj,Underline.DodgerBlue,Style.NoUnderline,sep)
    @staticmethod
    def LightBlue(*obj, sep=sep_):           return NCS(obj,Underline.LightBlue,Style.NoUnderline,sep)
    @staticmethod
    def SkyBlue(*obj, sep=sep_):             return NCS(obj,Underline.SkyBlue,Style.NoUnderline,sep)
    @staticmethod
    def LightSkyBlue(*obj, sep=sep_):        return NCS(obj,Underline.LightSkyBlue,Style.NoUnderline,sep)
    @staticmethod
    def MidnightBlue(*obj, sep=sep_):        return NCS(obj,Underline.MidnightBlue,Style.NoUnderline,sep)
    @staticmethod
    def Navy(*obj, sep=sep_):                return NCS(obj,Underline.Navy,Style.NoUnderline,sep)
    @staticmethod
    def DarkBlue(*obj, sep=sep_):            return NCS(obj,Underline.DarkBlue,Style.NoUnderline,sep)
    @staticmethod
    def MediumBlue(*obj, sep=sep_):          return NCS(obj,Underline.MediumBlue,Style.NoUnderline,sep)
    @staticmethod
    def Blue(*obj, sep=sep_):                return NCS(obj,Underline.Blue,Style.NoUnderline,sep)
    @staticmethod
    def RoyalBlue(*obj, sep=sep_):           return NCS(obj,Underline.RoyalBlue,Style.NoUnderline,sep)
    @staticmethod
    def BlueViolet(*obj, sep=sep_):          return NCS(obj,Underline.BlueViolet,Style.NoUnderline,sep)
    @staticmethod
    def Indigo(*obj, sep=sep_):              return NCS(obj,Underline.Indigo,Style.NoUnderline,sep)
    @staticmethod
    def DarkSlateBlue(*obj, sep=sep_):       return NCS(obj,Underline.DarkSlateBlue,Style.NoUnderline,sep)
    @staticmethod
    def SlateBlue(*obj, sep=sep_):           return NCS(obj,Underline.SlateBlue,Style.NoUnderline,sep)
    @staticmethod
    def MediumSlateBlue(*obj, sep=sep_):     return NCS(obj,Underline.MediumSlateBlue,Style.NoUnderline,sep)
    @staticmethod
    def MediumPurple(*obj, sep=sep_):        return NCS(obj,Underline.MediumPurple,Style.NoUnderline,sep)
    @staticmethod
    def DarkMagenta(*obj, sep=sep_):         return NCS(obj,Underline.DarkMagenta,Style.NoUnderline,sep)
    @staticmethod
    def DarkViolet(*obj, sep=sep_):          return NCS(obj,Underline.DarkViolet,Style.NoUnderline,sep)
    @staticmethod
    def DarkOrchid(*obj, sep=sep_):          return NCS(obj,Underline.DarkOrchid,Style.NoUnderline,sep)
    @staticmethod
    def MediumOrchid(*obj, sep=sep_):        return NCS(obj,Underline.MediumOrchid,Style.NoUnderline,sep)
    @staticmethod
    def Purple(*obj, sep=sep_):              return NCS(obj,Underline.Purple,Style.NoUnderline,sep)
    @staticmethod
    def Thistle(*obj, sep=sep_):             return NCS(obj,Underline.Thistle,Style.NoUnderline,sep)
    @staticmethod
    def Plum(*obj, sep=sep_):                return NCS(obj,Underline.Plum,Style.NoUnderline,sep)
    @staticmethod
    def Violet(*obj, sep=sep_):              return NCS(obj,Underline.Violet,Style.NoUnderline,sep)
    @staticmethod
    def Magenta(*obj, sep=sep_):             return NCS(obj,Underline.Magenta,Style.NoUnderline,sep)
    @staticmethod
    def Orchid(*obj, sep=sep_):              return NCS(obj,Underline.Orchid,Style.NoUnderline,sep)
    @staticmethod
    def MediumVioletRed(*obj, sep=sep_):     return NCS(obj,Underline.MediumVioletRed,Style.NoUnderline,sep)
    @staticmethod
    def PaleVioletRed(*obj, sep=sep_):       return NCS(obj,Underline.PaleVioletRed,Style.NoUnderline,sep)
    @staticmethod
    def DeepPink(*obj, sep=sep_):            return NCS(obj,Underline.DeepPink,Style.NoUnderline,sep)
    @staticmethod
    def HotPink(*obj, sep=sep_):             return NCS(obj,Underline.HotPink,Style.NoUnderline,sep)
    @staticmethod
    def LightPink(*obj, sep=sep_):           return NCS(obj,Underline.LightPink,Style.NoUnderline,sep)
    @staticmethod
    def Pink(*obj, sep=sep_):                return NCS(obj,Underline.Pink,Style.NoUnderline,sep)
    @staticmethod
    def AntiqueWhite(*obj, sep=sep_):        return NCS(obj,Underline.AntiqueWhite,Style.NoUnderline,sep)
    @staticmethod
    def Beige(*obj, sep=sep_):               return NCS(obj,Underline.Beige,Style.NoUnderline,sep)
    @staticmethod
    def Bisque(*obj, sep=sep_):              return NCS(obj,Underline.Bisque,Style.NoUnderline,sep)
    @staticmethod
    def BlanchedAlmond(*obj, sep=sep_):      return NCS(obj,Underline.BlanchedAlmond,Style.NoUnderline,sep)
    @staticmethod
    def Wheat(*obj, sep=sep_):               return NCS(obj,Underline.Wheat,Style.NoUnderline,sep)
    @staticmethod
    def CornSilk(*obj, sep=sep_):            return NCS(obj,Underline.CornSilk,Style.NoUnderline,sep)
    @staticmethod
    def LemonChiffon(*obj, sep=sep_):        return NCS(obj,Underline.LemonChiffon,Style.NoUnderline,sep)
    @staticmethod
    def LightGoldenRodYellow(*obj, sep=sep_):return NCS(obj,Underline.LightGoldenRodYellow,Style.NoUnderline,sep)
    @staticmethod
    def LightYellow(*obj, sep=sep_):         return NCS(obj,Underline.LightYellow,Style.NoUnderline,sep)
    @staticmethod
    def SaddleBrown(*obj, sep=sep_):         return NCS(obj,Underline.SaddleBrown,Style.NoUnderline,sep)
    @staticmethod
    def Sienna(*obj, sep=sep_):              return NCS(obj,Underline.Sienna,Style.NoUnderline,sep)
    @staticmethod
    def Chocolate(*obj, sep=sep_):           return NCS(obj,Underline.Chocolate,Style.NoUnderline,sep)
    @staticmethod
    def Peru(*obj, sep=sep_):                return NCS(obj,Underline.Peru,Style.NoUnderline,sep)
    @staticmethod
    def SandyBrown(*obj, sep=sep_):          return NCS(obj,Underline.SandyBrown,Style.NoUnderline,sep)
    @staticmethod
    def BurlyWood(*obj, sep=sep_):           return NCS(obj,Underline.BurlyWood,Style.NoUnderline,sep)
    @staticmethod
    def Tan(*obj, sep=sep_):                 return NCS(obj,Underline.Tan,Style.NoUnderline,sep)
    @staticmethod
    def RosyBrown(*obj, sep=sep_):           return NCS(obj,Underline.RosyBrown,Style.NoUnderline,sep)
    @staticmethod
    def Moccasin(*obj, sep=sep_):            return NCS(obj,Underline.Moccasin,Style.NoUnderline,sep)
    @staticmethod
    def NavajoWhite(*obj, sep=sep_):         return NCS(obj,Underline.NavajoWhite,Style.NoUnderline,sep)
    @staticmethod
    def PeachPuff(*obj, sep=sep_):           return NCS(obj,Underline.PeachPuff,Style.NoUnderline,sep)
    @staticmethod
    def MistyRose(*obj, sep=sep_):           return NCS(obj,Underline.MistyRose,Style.NoUnderline,sep)
    @staticmethod
    def LavenderBlush(*obj, sep=sep_):       return NCS(obj,Underline.LavenderBlush,Style.NoUnderline,sep)
    @staticmethod
    def Linen(*obj, sep=sep_):               return NCS(obj,Underline.Linen,Style.NoUnderline,sep)
    @staticmethod
    def OldLace(*obj, sep=sep_):             return NCS(obj,Underline.OldLace,Style.NoUnderline,sep)
    @staticmethod
    def PapayaWhip(*obj, sep=sep_):          return NCS(obj,Underline.PapayaWhip,Style.NoUnderline,sep)
    @staticmethod
    def WeaShell(*obj, sep=sep_):            return NCS(obj,Underline.WeaShell,Style.NoUnderline,sep)
    @staticmethod
    def MintCream(*obj, sep=sep_):           return NCS(obj,Underline.MintCream,Style.NoUnderline,sep)
    @staticmethod
    def SlateGray(*obj, sep=sep_):           return NCS(obj,Underline.SlateGray,Style.NoUnderline,sep)
    @staticmethod
    def LightSlateGray(*obj, sep=sep_):      return NCS(obj,Underline.LightSlateGray,Style.NoUnderline,sep)
    @staticmethod
    def LightSteelBlue(*obj, sep=sep_):      return NCS(obj,Underline.LightSteelBlue,Style.NoUnderline,sep)
    @staticmethod
    def Lavender(*obj, sep=sep_):            return NCS(obj,Underline.Lavender,Style.NoUnderline,sep)
    @staticmethod
    def FloralWhite(*obj, sep=sep_):         return NCS(obj,Underline.FloralWhite,Style.NoUnderline,sep)
    @staticmethod
    def AliceBlue(*obj, sep=sep_):           return NCS(obj,Underline.AliceBlue,Style.NoUnderline,sep)
    @staticmethod
    def GhostWhite(*obj, sep=sep_):          return NCS(obj,Underline.GhostWhite,Style.NoUnderline,sep)
    @staticmethod
    def Honeydew(*obj, sep=sep_):            return NCS(obj,Underline.Honeydew,Style.NoUnderline,sep)
    @staticmethod
    def Ivory(*obj, sep=sep_):               return NCS(obj,Underline.Ivory,Style.NoUnderline,sep)
    @staticmethod
    def Azure(*obj, sep=sep_):               return NCS(obj,Underline.Azure,Style.NoUnderline,sep)
    @staticmethod
    def Snow(*obj, sep=sep_):                return NCS(obj,Underline.Snow,Style.NoUnderline,sep)
    @staticmethod
    def Black(*obj, sep=sep_):               return NCS(obj,Underline.Black,Style.NoUnderline,sep)
    @staticmethod
    def DimGray(*obj, sep=sep_):             return NCS(obj,Underline.DimGray,Style.NoUnderline,sep)
    @staticmethod
    def Gray(*obj, sep=sep_):                return NCS(obj,Underline.Gray,Style.NoUnderline,sep)
    @staticmethod
    def DarkGray(*obj, sep=sep_):            return NCS(obj,Underline.DarkGray,Style.NoUnderline,sep)
    @staticmethod
    def Silver(*obj, sep=sep_):              return NCS(obj,Underline.Silver,Style.NoUnderline,sep)
    @staticmethod
    def LightGray(*obj, sep=sep_):           return NCS(obj,Underline.LightGray,Style.NoUnderline,sep)
    @staticmethod
    def Gainsboro(*obj, sep=sep_):           return NCS(obj,Underline.Gainsboro,Style.NoUnderline,sep)
    @staticmethod
    def WhiteSmoke(*obj, sep=sep_):          return NCS(obj,Underline.WhiteSmoke,Style.NoUnderline,sep)
    @staticmethod
    def White(*obj, sep=sep_):               return NCS(obj,Underline.White,Style.NoUnderline,sep)