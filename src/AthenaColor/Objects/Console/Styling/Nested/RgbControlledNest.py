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
    def Maroon(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Maroon}",reset_code=self._reset,sep=sep)
    def DarkRed(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.DarkRed}",reset_code=self._reset,sep=sep)
    def Brown(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Brown}",reset_code=self._reset,sep=sep)
    def Firebrick(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.Firebrick}",reset_code=self._reset,sep=sep)
    def Crimson(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.Crimson}",reset_code=self._reset,sep=sep)
    def Red(self, *obj, sep=" "):                 return NCS(obj,control_code=f"{self._param_code}{HC.Red}",reset_code=self._reset,sep=sep)
    def Tomato(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Tomato}",reset_code=self._reset,sep=sep)
    def Coral(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Coral}",reset_code=self._reset,sep=sep)
    def IndianRed(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.IndianRed}",reset_code=self._reset,sep=sep)
    def LightCoral(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.LightCoral}",reset_code=self._reset,sep=sep)
    def DarkSalmon(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.DarkSalmon}",reset_code=self._reset,sep=sep)
    def Salmon(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Salmon}",reset_code=self._reset,sep=sep)
    def LightSalmon(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.LightSalmon}",reset_code=self._reset,sep=sep)
    def OrangeRed(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.OrangeRed}",reset_code=self._reset,sep=sep)
    def DarkOrange(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.DarkOrange}",reset_code=self._reset,sep=sep)
    def Orange(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Orange}",reset_code=self._reset,sep=sep)
    def Gold(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Gold}",reset_code=self._reset,sep=sep)
    def DarkGoldenRod(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.DarkGoldenRod}",reset_code=self._reset,sep=sep)
    def GoldenRod(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.GoldenRod}",reset_code=self._reset,sep=sep)
    def PaleGoldenRod(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.PaleGoldenRod}",reset_code=self._reset,sep=sep)
    def DarkKhaki(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.DarkKhaki}",reset_code=self._reset,sep=sep)
    def Khaki(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Khaki}",reset_code=self._reset,sep=sep)
    def Olive(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Olive}",reset_code=self._reset,sep=sep)
    def Yellow(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Yellow}",reset_code=self._reset,sep=sep)
    def YellowGreen(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.YellowGreen}",reset_code=self._reset,sep=sep)
    def DarkOliveGreen(self, *obj, sep=" "):      return NCS(obj,control_code=f"{self._param_code}{HC.DarkOliveGreen}",reset_code=self._reset,sep=sep)
    def OliveDrab(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.OliveDrab}",reset_code=self._reset,sep=sep)
    def LawnGreen(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.LawnGreen}",reset_code=self._reset,sep=sep)
    def Chartreuse(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.Chartreuse}",reset_code=self._reset,sep=sep)
    def GreenYellow(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.GreenYellow}",reset_code=self._reset,sep=sep)
    def DarkGreen(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.DarkGreen}",reset_code=self._reset,sep=sep)
    def Green(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Green}",reset_code=self._reset,sep=sep)
    def ForestGreen(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.ForestGreen}",reset_code=self._reset,sep=sep)
    def Lime(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Lime}",reset_code=self._reset,sep=sep)
    def LimeGreen(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.LimeGreen}",reset_code=self._reset,sep=sep)
    def LightGreen(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.LightGreen}",reset_code=self._reset,sep=sep)
    def PaleGreen(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.PaleGreen}",reset_code=self._reset,sep=sep)
    def DarkSeaGreen(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.DarkSeaGreen}",reset_code=self._reset,sep=sep)
    def MediumSpringGreen(self, *obj, sep=" "):   return NCS(obj,control_code=f"{self._param_code}{HC.MediumSpringGreen}",reset_code=self._reset,sep=sep)
    def SpringGreen(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.SpringGreen}",reset_code=self._reset,sep=sep)
    def SeaGreen(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.SeaGreen}",reset_code=self._reset,sep=sep)
    def MediumAquaMarine(self, *obj, sep=" "):    return NCS(obj,control_code=f"{self._param_code}{HC.MediumAquaMarine}",reset_code=self._reset,sep=sep)
    def MediumSeaGreen(self, *obj, sep=" "):      return NCS(obj,control_code=f"{self._param_code}{HC.MediumSeaGreen}",reset_code=self._reset,sep=sep)
    def LightSeaGreen(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.LightSeaGreen}",reset_code=self._reset,sep=sep)
    def DarkSlateGray(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.DarkSlateGray}",reset_code=self._reset,sep=sep)
    def Teal(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Teal}",reset_code=self._reset,sep=sep)
    def DarkCyan(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.DarkCyan}",reset_code=self._reset,sep=sep)
    def Aqua(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Aqua}",reset_code=self._reset,sep=sep)
    def Cyan(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Cyan}",reset_code=self._reset,sep=sep)
    def LightCyan(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.LightCyan}",reset_code=self._reset,sep=sep)
    def DarkTurquoise(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.DarkTurquoise}",reset_code=self._reset,sep=sep)
    def Turquoise(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.Turquoise}",reset_code=self._reset,sep=sep)
    def MediumTurquoise(self, *obj, sep=" "):     return NCS(obj,control_code=f"{self._param_code}{HC.MediumTurquoise}",reset_code=self._reset,sep=sep)
    def PaleTurquoise(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.PaleTurquoise}",reset_code=self._reset,sep=sep)
    def AquaMarine(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.AquaMarine}",reset_code=self._reset,sep=sep)
    def PowderBlue(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.PowderBlue}",reset_code=self._reset,sep=sep)
    def CadetBlue(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.CadetBlue}",reset_code=self._reset,sep=sep)
    def SteelBlue(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.SteelBlue}",reset_code=self._reset,sep=sep)
    def CornFlowerBlue(self, *obj, sep=" "):      return NCS(obj,control_code=f"{self._param_code}{HC.CornFlowerBlue}",reset_code=self._reset,sep=sep)
    def DeepSkyBlue(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.DeepSkyBlue}",reset_code=self._reset,sep=sep)
    def DodgerBlue(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.DodgerBlue}",reset_code=self._reset,sep=sep)
    def LightBlue(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.LightBlue}",reset_code=self._reset,sep=sep)
    def SkyBlue(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.SkyBlue}",reset_code=self._reset,sep=sep)
    def LightSkyBlue(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.LightSkyBlue}",reset_code=self._reset,sep=sep)
    def MidnightBlue(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.MidnightBlue}",reset_code=self._reset,sep=sep)
    def Navy(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Navy}",reset_code=self._reset,sep=sep)
    def DarkBlue(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.DarkBlue}",reset_code=self._reset,sep=sep)
    def MediumBlue(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.MediumBlue}",reset_code=self._reset,sep=sep)
    def Blue(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Blue}",reset_code=self._reset,sep=sep)
    def RoyalBlue(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.RoyalBlue}",reset_code=self._reset,sep=sep)
    def BlueViolet(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.BlueViolet}",reset_code=self._reset,sep=sep)
    def Indigo(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Indigo}",reset_code=self._reset,sep=sep)
    def DarkSlateBlue(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.DarkSlateBlue}",reset_code=self._reset,sep=sep)
    def SlateBlue(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.SlateBlue}",reset_code=self._reset,sep=sep)
    def MediumSlateBlue(self, *obj, sep=" "):     return NCS(obj,control_code=f"{self._param_code}{HC.MediumSlateBlue}",reset_code=self._reset,sep=sep)
    def MediumPurple(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.MediumPurple}",reset_code=self._reset,sep=sep)
    def DarkMagenta(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.DarkMagenta}",reset_code=self._reset,sep=sep)
    def DarkViolet(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.DarkViolet}",reset_code=self._reset,sep=sep)
    def DarkOrchid(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.DarkOrchid}",reset_code=self._reset,sep=sep)
    def MediumOrchid(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.MediumOrchid}",reset_code=self._reset,sep=sep)
    def Purple(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Purple}",reset_code=self._reset,sep=sep)
    def Thistle(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.Thistle}",reset_code=self._reset,sep=sep)
    def Plum(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Plum}",reset_code=self._reset,sep=sep)
    def Violet(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Violet}",reset_code=self._reset,sep=sep)
    def Magenta(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.Magenta}",reset_code=self._reset,sep=sep)
    def Orchid(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Orchid}",reset_code=self._reset,sep=sep)
    def MediumVioletRed(self, *obj, sep=" "):     return NCS(obj,control_code=f"{self._param_code}{HC.MediumVioletRed}",reset_code=self._reset,sep=sep)
    def PaleVioletRed(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.PaleVioletRed}",reset_code=self._reset,sep=sep)
    def DeepPink(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.DeepPink}",reset_code=self._reset,sep=sep)
    def HotPink(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.HotPink}",reset_code=self._reset,sep=sep)
    def LightPink(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.LightPink}",reset_code=self._reset,sep=sep)
    def Pink(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Pink}",reset_code=self._reset,sep=sep)
    def AntiqueWhite(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.AntiqueWhite}",reset_code=self._reset,sep=sep)
    def Beige(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Beige}",reset_code=self._reset,sep=sep)
    def Bisque(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Bisque}",reset_code=self._reset,sep=sep)
    def BlanchedAlmond(self, *obj, sep=" "):      return NCS(obj,control_code=f"{self._param_code}{HC.BlanchedAlmond}",reset_code=self._reset,sep=sep)
    def Wheat(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Wheat}",reset_code=self._reset,sep=sep)
    def CornSilk(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.CornSilk}",reset_code=self._reset,sep=sep)
    def LemonChiffon(self, *obj, sep=" "):        return NCS(obj,control_code=f"{self._param_code}{HC.LemonChiffon}",reset_code=self._reset,sep=sep)
    def LightGoldenRodYellow(self, *obj, sep=" "):return NCS(obj,control_code=f"{self._param_code}{HC.LightGoldenRodYellow}",reset_code=self._reset,sep=sep)
    def LightYellow(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.LightYellow}",reset_code=self._reset,sep=sep)
    def SaddleBrown(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.SaddleBrown}",reset_code=self._reset,sep=sep)
    def Sienna(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Sienna}",reset_code=self._reset,sep=sep)
    def Chocolate(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.Chocolate}",reset_code=self._reset,sep=sep)
    def Peru(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Peru}",reset_code=self._reset,sep=sep)
    def SandyBrown(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.SandyBrown}",reset_code=self._reset,sep=sep)
    def BurlyWood(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.BurlyWood}",reset_code=self._reset,sep=sep)
    def Tan(self, *obj, sep=" "):                 return NCS(obj,control_code=f"{self._param_code}{HC.Tan}",reset_code=self._reset,sep=sep)
    def RosyBrown(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.RosyBrown}",reset_code=self._reset,sep=sep)
    def Moccasin(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.Moccasin}",reset_code=self._reset,sep=sep)
    def NavajoWhite(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.NavajoWhite}",reset_code=self._reset,sep=sep)
    def PeachPuff(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.PeachPuff}",reset_code=self._reset,sep=sep)
    def MistyRose(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.MistyRose}",reset_code=self._reset,sep=sep)
    def LavenderBlush(self, *obj, sep=" "):       return NCS(obj,control_code=f"{self._param_code}{HC.LavenderBlush}",reset_code=self._reset,sep=sep)
    def Linen(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Linen}",reset_code=self._reset,sep=sep)
    def OldLace(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.OldLace}",reset_code=self._reset,sep=sep)
    def PapayaWhip(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.PapayaWhip}",reset_code=self._reset,sep=sep)
    def WeaShell(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.WeaShell}",reset_code=self._reset,sep=sep)
    def MintCream(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.MintCream}",reset_code=self._reset,sep=sep)
    def SlateGray(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.SlateGray}",reset_code=self._reset,sep=sep)
    def LightSlateGray(self, *obj, sep=" "):      return NCS(obj,control_code=f"{self._param_code}{HC.LightSlateGray}",reset_code=self._reset,sep=sep)
    def LightSteelBlue(self, *obj, sep=" "):      return NCS(obj,control_code=f"{self._param_code}{HC.LightSteelBlue}",reset_code=self._reset,sep=sep)
    def Lavender(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.Lavender}",reset_code=self._reset,sep=sep)
    def FloralWhite(self, *obj, sep=" "):         return NCS(obj,control_code=f"{self._param_code}{HC.FloralWhite}",reset_code=self._reset,sep=sep)
    def AliceBlue(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.AliceBlue}",reset_code=self._reset,sep=sep)
    def GhostWhite(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.GhostWhite}",reset_code=self._reset,sep=sep)
    def Honeydew(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.Honeydew}",reset_code=self._reset,sep=sep)
    def Ivory(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Ivory}",reset_code=self._reset,sep=sep)
    def Azure(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Azure}",reset_code=self._reset,sep=sep)
    def Snow(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Snow}",reset_code=self._reset,sep=sep)
    def Black(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.Black}",reset_code=self._reset,sep=sep)
    def DimGray(self, *obj, sep=" "):             return NCS(obj,control_code=f"{self._param_code}{HC.DimGray}",reset_code=self._reset,sep=sep)
    def Gray(self, *obj, sep=" "):                return NCS(obj,control_code=f"{self._param_code}{HC.Gray}",reset_code=self._reset,sep=sep)
    def DarkGray(self, *obj, sep=" "):            return NCS(obj,control_code=f"{self._param_code}{HC.DarkGray}",reset_code=self._reset,sep=sep)
    def Silver(self, *obj, sep=" "):              return NCS(obj,control_code=f"{self._param_code}{HC.Silver}",reset_code=self._reset,sep=sep)
    def LightGray(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.LightGray}",reset_code=self._reset,sep=sep)
    def Gainsboro(self, *obj, sep=" "):           return NCS(obj,control_code=f"{self._param_code}{HC.Gainsboro}",reset_code=self._reset,sep=sep)
    def WhiteSmoke(self, *obj, sep=" "):          return NCS(obj,control_code=f"{self._param_code}{HC.WhiteSmoke}",reset_code=self._reset,sep=sep)
    def White(self, *obj, sep=" "):               return NCS(obj,control_code=f"{self._param_code}{HC.White}",reset_code=self._reset,sep=sep)