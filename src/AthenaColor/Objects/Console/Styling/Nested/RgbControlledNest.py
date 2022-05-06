# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX, NormalizeRgb
from AthenaColor.Functions.ANSIsquences import NestedColorSequence
from AthenaColor.Data.HtmlColors import HtmlColorStr as HC
from AthenaColor.Functions.General import StrictType

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "RgbControlledNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence # Done for slight speed increase

class RgbControlledNest:
    def __init__(self, param_code:str,reset_code:int):
        self._param_code:str = StrictType(param_code, str)
        self._reset:int = StrictType(reset_code, int)

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self,*obj, color:RGB|HEX, **kwargs) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        color = StrictType(color,(RGB,HEX))
        return NestedColorSequence(
            *obj,
            control_code=f"{self._param_code}{color.r};{color.g};{color.b}",
            reset_code=self._reset,
            **kwargs
        )

    def rgb(self,*obj, r:int,g:int,b:int, **kwargs) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        r,g,b =  NormalizeRgb(r, g, b)
        return NestedColorSequence(
            *obj,
            control_code=f"{self._param_code}{r};{g};{b}",
            reset_code=self._reset,
            **kwargs
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    # No partial methods, as this was increase the speed impact 2-fold
    def Maroon(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Maroon}",reset_code=self._reset,**kwargs)
    def DarkRed(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.DarkRed}",reset_code=self._reset,**kwargs)
    def Brown(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Brown}",reset_code=self._reset,**kwargs)
    def Firebrick(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.Firebrick}",reset_code=self._reset,**kwargs)
    def Crimson(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.Crimson}",reset_code=self._reset,**kwargs)
    def Red(self, *obj, **kwargs):                 return NCS(*obj,control_code=f"{self._param_code}{HC.Red}",reset_code=self._reset,**kwargs)
    def Tomato(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Tomato}",reset_code=self._reset,**kwargs)
    def Coral(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Coral}",reset_code=self._reset,**kwargs)
    def IndianRed(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.IndianRed}",reset_code=self._reset,**kwargs)
    def LightCoral(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.LightCoral}",reset_code=self._reset,**kwargs)
    def DarkSalmon(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.DarkSalmon}",reset_code=self._reset,**kwargs)
    def Salmon(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Salmon}",reset_code=self._reset,**kwargs)
    def LightSalmon(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.LightSalmon}",reset_code=self._reset,**kwargs)
    def OrangeRed(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.OrangeRed}",reset_code=self._reset,**kwargs)
    def DarkOrange(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.DarkOrange}",reset_code=self._reset,**kwargs)
    def Orange(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Orange}",reset_code=self._reset,**kwargs)
    def Gold(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Gold}",reset_code=self._reset,**kwargs)
    def DarkGoldenRod(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.DarkGoldenRod}",reset_code=self._reset,**kwargs)
    def GoldenRod(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.GoldenRod}",reset_code=self._reset,**kwargs)
    def PaleGoldenRod(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.PaleGoldenRod}",reset_code=self._reset,**kwargs)
    def DarkKhaki(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.DarkKhaki}",reset_code=self._reset,**kwargs)
    def Khaki(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Khaki}",reset_code=self._reset,**kwargs)
    def Olive(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Olive}",reset_code=self._reset,**kwargs)
    def Yellow(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Yellow}",reset_code=self._reset,**kwargs)
    def YellowGreen(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.YellowGreen}",reset_code=self._reset,**kwargs)
    def DarkOliveGreen(self, *obj, **kwargs):      return NCS(*obj,control_code=f"{self._param_code}{HC.DarkOliveGreen}",reset_code=self._reset,**kwargs)
    def OliveDrab(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.OliveDrab}",reset_code=self._reset,**kwargs)
    def LawnGreen(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.LawnGreen}",reset_code=self._reset,**kwargs)
    def Chartreuse(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.Chartreuse}",reset_code=self._reset,**kwargs)
    def GreenYellow(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.GreenYellow}",reset_code=self._reset,**kwargs)
    def DarkGreen(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.DarkGreen}",reset_code=self._reset,**kwargs)
    def Green(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Green}",reset_code=self._reset,**kwargs)
    def ForestGreen(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.ForestGreen}",reset_code=self._reset,**kwargs)
    def Lime(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Lime}",reset_code=self._reset,**kwargs)
    def LimeGreen(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.LimeGreen}",reset_code=self._reset,**kwargs)
    def LightGreen(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.LightGreen}",reset_code=self._reset,**kwargs)
    def PaleGreen(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.PaleGreen}",reset_code=self._reset,**kwargs)
    def DarkSeaGreen(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.DarkSeaGreen}",reset_code=self._reset,**kwargs)
    def MediumSpringGreen(self, *obj, **kwargs):   return NCS(*obj,control_code=f"{self._param_code}{HC.MediumSpringGreen}",reset_code=self._reset,**kwargs)
    def SpringGreen(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.SpringGreen}",reset_code=self._reset,**kwargs)
    def SeaGreen(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.SeaGreen}",reset_code=self._reset,**kwargs)
    def MediumAquaMarine(self, *obj, **kwargs):    return NCS(*obj,control_code=f"{self._param_code}{HC.MediumAquaMarine}",reset_code=self._reset,**kwargs)
    def MediumSeaGreen(self, *obj, **kwargs):      return NCS(*obj,control_code=f"{self._param_code}{HC.MediumSeaGreen}",reset_code=self._reset,**kwargs)
    def LightSeaGreen(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.LightSeaGreen}",reset_code=self._reset,**kwargs)
    def DarkSlateGray(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.DarkSlateGray}",reset_code=self._reset,**kwargs)
    def Teal(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Teal}",reset_code=self._reset,**kwargs)
    def DarkCyan(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.DarkCyan}",reset_code=self._reset,**kwargs)
    def Aqua(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Aqua}",reset_code=self._reset,**kwargs)
    def Cyan(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Cyan}",reset_code=self._reset,**kwargs)
    def LightCyan(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.LightCyan}",reset_code=self._reset,**kwargs)
    def DarkTurquoise(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.DarkTurquoise}",reset_code=self._reset,**kwargs)
    def Turquoise(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.Turquoise}",reset_code=self._reset,**kwargs)
    def MediumTurquoise(self, *obj, **kwargs):     return NCS(*obj,control_code=f"{self._param_code}{HC.MediumTurquoise}",reset_code=self._reset,**kwargs)
    def PaleTurquoise(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.PaleTurquoise}",reset_code=self._reset,**kwargs)
    def AquaMarine(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.AquaMarine}",reset_code=self._reset,**kwargs)
    def PowderBlue(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.PowderBlue}",reset_code=self._reset,**kwargs)
    def CadetBlue(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.CadetBlue}",reset_code=self._reset,**kwargs)
    def SteelBlue(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.SteelBlue}",reset_code=self._reset,**kwargs)
    def CornFlowerBlue(self, *obj, **kwargs):      return NCS(*obj,control_code=f"{self._param_code}{HC.CornFlowerBlue}",reset_code=self._reset,**kwargs)
    def DeepSkyBlue(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.DeepSkyBlue}",reset_code=self._reset,**kwargs)
    def DodgerBlue(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.DodgerBlue}",reset_code=self._reset,**kwargs)
    def LightBlue(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.LightBlue}",reset_code=self._reset,**kwargs)
    def SkyBlue(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.SkyBlue}",reset_code=self._reset,**kwargs)
    def LightSkyBlue(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.LightSkyBlue}",reset_code=self._reset,**kwargs)
    def MidnightBlue(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.MidnightBlue}",reset_code=self._reset,**kwargs)
    def Navy(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Navy}",reset_code=self._reset,**kwargs)
    def DarkBlue(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.DarkBlue}",reset_code=self._reset,**kwargs)
    def MediumBlue(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.MediumBlue}",reset_code=self._reset,**kwargs)
    def Blue(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Blue}",reset_code=self._reset,**kwargs)
    def RoyalBlue(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.RoyalBlue}",reset_code=self._reset,**kwargs)
    def BlueViolet(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.BlueViolet}",reset_code=self._reset,**kwargs)
    def Indigo(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Indigo}",reset_code=self._reset,**kwargs)
    def DarkSlateBlue(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.DarkSlateBlue}",reset_code=self._reset,**kwargs)
    def SlateBlue(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.SlateBlue}",reset_code=self._reset,**kwargs)
    def MediumSlateBlue(self, *obj, **kwargs):     return NCS(*obj,control_code=f"{self._param_code}{HC.MediumSlateBlue}",reset_code=self._reset,**kwargs)
    def MediumPurple(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.MediumPurple}",reset_code=self._reset,**kwargs)
    def DarkMagenta(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.DarkMagenta}",reset_code=self._reset,**kwargs)
    def DarkViolet(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.DarkViolet}",reset_code=self._reset,**kwargs)
    def DarkOrchid(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.DarkOrchid}",reset_code=self._reset,**kwargs)
    def MediumOrchid(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.MediumOrchid}",reset_code=self._reset,**kwargs)
    def Purple(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Purple}",reset_code=self._reset,**kwargs)
    def Thistle(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.Thistle}",reset_code=self._reset,**kwargs)
    def Plum(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Plum}",reset_code=self._reset,**kwargs)
    def Violet(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Violet}",reset_code=self._reset,**kwargs)
    def Magenta(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.Magenta}",reset_code=self._reset,**kwargs)
    def Orchid(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Orchid}",reset_code=self._reset,**kwargs)
    def MediumVioletRed(self, *obj, **kwargs):     return NCS(*obj,control_code=f"{self._param_code}{HC.MediumVioletRed}",reset_code=self._reset,**kwargs)
    def PaleVioletRed(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.PaleVioletRed}",reset_code=self._reset,**kwargs)
    def DeepPink(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.DeepPink}",reset_code=self._reset,**kwargs)
    def HotPink(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.HotPink}",reset_code=self._reset,**kwargs)
    def LightPink(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.LightPink}",reset_code=self._reset,**kwargs)
    def Pink(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Pink}",reset_code=self._reset,**kwargs)
    def AntiqueWhite(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.AntiqueWhite}",reset_code=self._reset,**kwargs)
    def Beige(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Beige}",reset_code=self._reset,**kwargs)
    def Bisque(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Bisque}",reset_code=self._reset,**kwargs)
    def BlanchedAlmond(self, *obj, **kwargs):      return NCS(*obj,control_code=f"{self._param_code}{HC.BlanchedAlmond}",reset_code=self._reset,**kwargs)
    def Wheat(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Wheat}",reset_code=self._reset,**kwargs)
    def CornSilk(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.CornSilk}",reset_code=self._reset,**kwargs)
    def LemonChiffon(self, *obj, **kwargs):        return NCS(*obj,control_code=f"{self._param_code}{HC.LemonChiffon}",reset_code=self._reset,**kwargs)
    def LightGoldenRodYellow(self, *obj, **kwargs):return NCS(*obj,control_code=f"{self._param_code}{HC.LightGoldenRodYellow}",reset_code=self._reset,**kwargs)
    def LightYellow(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.LightYellow}",reset_code=self._reset,**kwargs)
    def SaddleBrown(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.SaddleBrown}",reset_code=self._reset,**kwargs)
    def Sienna(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Sienna}",reset_code=self._reset,**kwargs)
    def Chocolate(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.Chocolate}",reset_code=self._reset,**kwargs)
    def Peru(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Peru}",reset_code=self._reset,**kwargs)
    def SandyBrown(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.SandyBrown}",reset_code=self._reset,**kwargs)
    def BurlyWood(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.BurlyWood}",reset_code=self._reset,**kwargs)
    def Tan(self, *obj, **kwargs):                 return NCS(*obj,control_code=f"{self._param_code}{HC.Tan}",reset_code=self._reset,**kwargs)
    def RosyBrown(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.RosyBrown}",reset_code=self._reset,**kwargs)
    def Moccasin(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.Moccasin}",reset_code=self._reset,**kwargs)
    def NavajoWhite(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.NavajoWhite}",reset_code=self._reset,**kwargs)
    def PeachPuff(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.PeachPuff}",reset_code=self._reset,**kwargs)
    def MistyRose(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.MistyRose}",reset_code=self._reset,**kwargs)
    def LavenderBlush(self, *obj, **kwargs):       return NCS(*obj,control_code=f"{self._param_code}{HC.LavenderBlush}",reset_code=self._reset,**kwargs)
    def Linen(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Linen}",reset_code=self._reset,**kwargs)
    def OldLace(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.OldLace}",reset_code=self._reset,**kwargs)
    def PapayaWhip(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.PapayaWhip}",reset_code=self._reset,**kwargs)
    def WeaShell(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.WeaShell}",reset_code=self._reset,**kwargs)
    def MintCream(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.MintCream}",reset_code=self._reset,**kwargs)
    def SlateGray(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.SlateGray}",reset_code=self._reset,**kwargs)
    def LightSlateGray(self, *obj, **kwargs):      return NCS(*obj,control_code=f"{self._param_code}{HC.LightSlateGray}",reset_code=self._reset,**kwargs)
    def LightSteelBlue(self, *obj, **kwargs):      return NCS(*obj,control_code=f"{self._param_code}{HC.LightSteelBlue}",reset_code=self._reset,**kwargs)
    def Lavender(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.Lavender}",reset_code=self._reset,**kwargs)
    def FloralWhite(self, *obj, **kwargs):         return NCS(*obj,control_code=f"{self._param_code}{HC.FloralWhite}",reset_code=self._reset,**kwargs)
    def AliceBlue(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.AliceBlue}",reset_code=self._reset,**kwargs)
    def GhostWhite(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.GhostWhite}",reset_code=self._reset,**kwargs)
    def Honeydew(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.Honeydew}",reset_code=self._reset,**kwargs)
    def Ivory(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Ivory}",reset_code=self._reset,**kwargs)
    def Azure(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Azure}",reset_code=self._reset,**kwargs)
    def Snow(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Snow}",reset_code=self._reset,**kwargs)
    def Black(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.Black}",reset_code=self._reset,**kwargs)
    def DimGray(self, *obj, **kwargs):             return NCS(*obj,control_code=f"{self._param_code}{HC.DimGray}",reset_code=self._reset,**kwargs)
    def Gray(self, *obj, **kwargs):                return NCS(*obj,control_code=f"{self._param_code}{HC.Gray}",reset_code=self._reset,**kwargs)
    def DarkGray(self, *obj, **kwargs):            return NCS(*obj,control_code=f"{self._param_code}{HC.DarkGray}",reset_code=self._reset,**kwargs)
    def Silver(self, *obj, **kwargs):              return NCS(*obj,control_code=f"{self._param_code}{HC.Silver}",reset_code=self._reset,**kwargs)
    def LightGray(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.LightGray}",reset_code=self._reset,**kwargs)
    def Gainsboro(self, *obj, **kwargs):           return NCS(*obj,control_code=f"{self._param_code}{HC.Gainsboro}",reset_code=self._reset,**kwargs)
    def WhiteSmoke(self, *obj, **kwargs):          return NCS(*obj,control_code=f"{self._param_code}{HC.WhiteSmoke}",reset_code=self._reset,**kwargs)
    def White(self, *obj, **kwargs):               return NCS(*obj,control_code=f"{self._param_code}{HC.White}",reset_code=self._reset,**kwargs)