# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.models.color_system import RGB,HEX, NormalizeRgb
from AthenaColor.functions.ansi_sequences import NestedColorSequence
from AthenaColor.models.console.styling.rgb_controlled import RgbControlled

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence # Done for slight speed increase
sep_=" "

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlledNested:
    _inline_class:RgbControlled
    _reset:str
    __slots__ = ["_inline_class", "_reset"]
    def __init__(self, inline_class:RgbControlled, reset:str):
        self._inline_class = inline_class
        self._reset = reset

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self,*obj, color:RGB|HEX, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"{self._inline_class.param_code}{';'.join(*color.export())}m",
            self._reset,
            sep=sep
        )

    def rgb(self, *obj, r:int,g:int,b:int, sep=sep_) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        return NestedColorSequence(
            obj,
            f"{self._inline_class.param_code}{';'.join(*NormalizeRgb(r, g, b))}m",
            self._reset,
            sep=sep
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    # No partial methods, as this was increase the speed impact 2-fold
    def Maroon(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Maroon,self._reset,sep)
    def DarkRed(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.DarkRed,self._reset,sep)
    def Brown(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Brown,self._reset,sep)
    def Firebrick(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.Firebrick,self._reset,sep)
    def Crimson(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.Crimson,self._reset,sep)
    def Red(self, *obj, sep=sep_):                 return NCS(obj,self._inline_class.Red,self._reset,sep)
    def Tomato(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Tomato,self._reset,sep)
    def Coral(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Coral,self._reset,sep)
    def IndianRed(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.IndianRed,self._reset,sep)
    def LightCoral(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.LightCoral,self._reset,sep)
    def DarkSalmon(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.DarkSalmon,self._reset,sep)
    def Salmon(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Salmon,self._reset,sep)
    def LightSalmon(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.LightSalmon,self._reset,sep)
    def OrangeRed(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.OrangeRed,self._reset,sep)
    def DarkOrange(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.DarkOrange,self._reset,sep)
    def Orange(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Orange,self._reset,sep)
    def Gold(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Gold,self._reset,sep)
    def DarkGoldenRod(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.DarkGoldenRod,self._reset,sep)
    def GoldenRod(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.GoldenRod,self._reset,sep)
    def PaleGoldenRod(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.PaleGoldenRod,self._reset,sep)
    def DarkKhaki(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.DarkKhaki,self._reset,sep)
    def Khaki(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Khaki,self._reset,sep)
    def Olive(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Olive,self._reset,sep)
    def Yellow(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Yellow,self._reset,sep)
    def YellowGreen(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.YellowGreen,self._reset,sep)
    def DarkOliveGreen(self, *obj, sep=sep_):      return NCS(obj,self._inline_class.DarkOliveGreen,self._reset,sep)
    def OliveDrab(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.OliveDrab,self._reset,sep)
    def LawnGreen(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.LawnGreen,self._reset,sep)
    def Chartreuse(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.Chartreuse,self._reset,sep)
    def GreenYellow(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.GreenYellow,self._reset,sep)
    def DarkGreen(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.DarkGreen,self._reset,sep)
    def Green(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Green,self._reset,sep)
    def ForestGreen(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.ForestGreen,self._reset,sep)
    def Lime(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Lime,self._reset,sep)
    def LimeGreen(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.LimeGreen,self._reset,sep)
    def LightGreen(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.LightGreen,self._reset,sep)
    def PaleGreen(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.PaleGreen,self._reset,sep)
    def DarkSeaGreen(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.DarkSeaGreen,self._reset,sep)
    def MediumSpringGreen(self, *obj, sep=sep_):   return NCS(obj,self._inline_class.MediumSpringGreen,self._reset,sep)
    def SpringGreen(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.SpringGreen,self._reset,sep)
    def SeaGreen(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.SeaGreen,self._reset,sep)
    def MediumAquaMarine(self, *obj, sep=sep_):    return NCS(obj,self._inline_class.MediumAquaMarine,self._reset,sep)
    def MediumSeaGreen(self, *obj, sep=sep_):      return NCS(obj,self._inline_class.MediumSeaGreen,self._reset,sep)
    def LightSeaGreen(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.LightSeaGreen,self._reset,sep)
    def DarkSlateGray(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.DarkSlateGray,self._reset,sep)
    def Teal(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Teal,self._reset,sep)
    def DarkCyan(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.DarkCyan,self._reset,sep)
    def Aqua(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Aqua,self._reset,sep)
    def Cyan(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Cyan,self._reset,sep)
    def LightCyan(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.LightCyan,self._reset,sep)
    def DarkTurquoise(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.DarkTurquoise,self._reset,sep)
    def Turquoise(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.Turquoise,self._reset,sep)
    def MediumTurquoise(self, *obj, sep=sep_):     return NCS(obj,self._inline_class.MediumTurquoise,self._reset,sep)
    def PaleTurquoise(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.PaleTurquoise,self._reset,sep)
    def AquaMarine(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.AquaMarine,self._reset,sep)
    def PowderBlue(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.PowderBlue,self._reset,sep)
    def CadetBlue(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.CadetBlue,self._reset,sep)
    def SteelBlue(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.SteelBlue,self._reset,sep)
    def CornFlowerBlue(self, *obj, sep=sep_):      return NCS(obj,self._inline_class.CornFlowerBlue,self._reset,sep)
    def DeepSkyBlue(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.DeepSkyBlue,self._reset,sep)
    def DodgerBlue(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.DodgerBlue,self._reset,sep)
    def LightBlue(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.LightBlue,self._reset,sep)
    def SkyBlue(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.SkyBlue,self._reset,sep)
    def LightSkyBlue(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.LightSkyBlue,self._reset,sep)
    def MidnightBlue(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.MidnightBlue,self._reset,sep)
    def Navy(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Navy,self._reset,sep)
    def DarkBlue(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.DarkBlue,self._reset,sep)
    def MediumBlue(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.MediumBlue,self._reset,sep)
    def Blue(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Blue,self._reset,sep)
    def RoyalBlue(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.RoyalBlue,self._reset,sep)
    def BlueViolet(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.BlueViolet,self._reset,sep)
    def Indigo(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Indigo,self._reset,sep)
    def DarkSlateBlue(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.DarkSlateBlue,self._reset,sep)
    def SlateBlue(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.SlateBlue,self._reset,sep)
    def MediumSlateBlue(self, *obj, sep=sep_):     return NCS(obj,self._inline_class.MediumSlateBlue,self._reset,sep)
    def MediumPurple(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.MediumPurple,self._reset,sep)
    def DarkMagenta(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.DarkMagenta,self._reset,sep)
    def DarkViolet(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.DarkViolet,self._reset,sep)
    def DarkOrchid(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.DarkOrchid,self._reset,sep)
    def MediumOrchid(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.MediumOrchid,self._reset,sep)
    def Purple(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Purple,self._reset,sep)
    def Thistle(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.Thistle,self._reset,sep)
    def Plum(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Plum,self._reset,sep)
    def Violet(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Violet,self._reset,sep)
    def Magenta(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.Magenta,self._reset,sep)
    def Orchid(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Orchid,self._reset,sep)
    def MediumVioletRed(self, *obj, sep=sep_):     return NCS(obj,self._inline_class.MediumVioletRed,self._reset,sep)
    def PaleVioletRed(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.PaleVioletRed,self._reset,sep)
    def DeepPink(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.DeepPink,self._reset,sep)
    def HotPink(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.HotPink,self._reset,sep)
    def LightPink(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.LightPink,self._reset,sep)
    def Pink(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Pink,self._reset,sep)
    def AntiqueWhite(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.AntiqueWhite,self._reset,sep)
    def Beige(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Beige,self._reset,sep)
    def Bisque(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Bisque,self._reset,sep)
    def BlanchedAlmond(self, *obj, sep=sep_):      return NCS(obj,self._inline_class.BlanchedAlmond,self._reset,sep)
    def Wheat(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Wheat,self._reset,sep)
    def CornSilk(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.CornSilk,self._reset,sep)
    def LemonChiffon(self, *obj, sep=sep_):        return NCS(obj,self._inline_class.LemonChiffon,self._reset,sep)
    def LightGoldenRodYellow(self, *obj, sep=sep_):return NCS(obj,self._inline_class.LightGoldenRodYellow,self._reset,sep)
    def LightYellow(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.LightYellow,self._reset,sep)
    def SaddleBrown(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.SaddleBrown,self._reset,sep)
    def Sienna(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Sienna,self._reset,sep)
    def Chocolate(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.Chocolate,self._reset,sep)
    def Peru(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Peru,self._reset,sep)
    def SandyBrown(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.SandyBrown,self._reset,sep)
    def BurlyWood(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.BurlyWood,self._reset,sep)
    def Tan(self, *obj, sep=sep_):                 return NCS(obj,self._inline_class.Tan,self._reset,sep)
    def RosyBrown(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.RosyBrown,self._reset,sep)
    def Moccasin(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.Moccasin,self._reset,sep)
    def NavajoWhite(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.NavajoWhite,self._reset,sep)
    def PeachPuff(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.PeachPuff,self._reset,sep)
    def MistyRose(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.MistyRose,self._reset,sep)
    def LavenderBlush(self, *obj, sep=sep_):       return NCS(obj,self._inline_class.LavenderBlush,self._reset,sep)
    def Linen(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Linen,self._reset,sep)
    def OldLace(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.OldLace,self._reset,sep)
    def PapayaWhip(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.PapayaWhip,self._reset,sep)
    def WeaShell(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.WeaShell,self._reset,sep)
    def MintCream(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.MintCream,self._reset,sep)
    def SlateGray(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.SlateGray,self._reset,sep)
    def LightSlateGray(self, *obj, sep=sep_):      return NCS(obj,self._inline_class.LightSlateGray,self._reset,sep)
    def LightSteelBlue(self, *obj, sep=sep_):      return NCS(obj,self._inline_class.LightSteelBlue,self._reset,sep)
    def Lavender(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.Lavender,self._reset,sep)
    def FloralWhite(self, *obj, sep=sep_):         return NCS(obj,self._inline_class.FloralWhite,self._reset,sep)
    def AliceBlue(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.AliceBlue,self._reset,sep)
    def GhostWhite(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.GhostWhite,self._reset,sep)
    def Honeydew(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.Honeydew,self._reset,sep)
    def Ivory(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Ivory,self._reset,sep)
    def Azure(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Azure,self._reset,sep)
    def Snow(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Snow,self._reset,sep)
    def Black(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.Black,self._reset,sep)
    def DimGray(self, *obj, sep=sep_):             return NCS(obj,self._inline_class.DimGray,self._reset,sep)
    def Gray(self, *obj, sep=sep_):                return NCS(obj,self._inline_class.Gray,self._reset,sep)
    def DarkGray(self, *obj, sep=sep_):            return NCS(obj,self._inline_class.DarkGray,self._reset,sep)
    def Silver(self, *obj, sep=sep_):              return NCS(obj,self._inline_class.Silver,self._reset,sep)
    def LightGray(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.LightGray,self._reset,sep)
    def Gainsboro(self, *obj, sep=sep_):           return NCS(obj,self._inline_class.Gainsboro,self._reset,sep)
    def WhiteSmoke(self, *obj, sep=sep_):          return NCS(obj,self._inline_class.WhiteSmoke,self._reset,sep)
    def White(self, *obj, sep=sep_):               return NCS(obj,self._inline_class.White,self._reset,sep)