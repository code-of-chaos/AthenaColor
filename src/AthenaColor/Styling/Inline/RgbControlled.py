# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from ...Objects import (
    rgb,
    HtmlColors
)
from AthenaColor import init

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlled:
    param_code:str
    _sufix:str

    def __init__(self, param_code:str):
        self.param_code = param_code
        self._sufix =  "m"

    @property
    def prefix(self):
        return init.esc + self.param_code
    @property
    def sufix(self):
        return self._sufix

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:rgb):
      return f"{self.prefix}{color}{self.sufix}"

    def c(self,color:rgb): #synonim for cls.custom()
      return self.custom(color)

    def rgb(self, r:int,g:int,b:int):
      return f"{self.prefix}{rgb(r,g,b)}{self.sufix}"

    def _sequence(self,Color:rgb) -> str:
        return self.prefix + str(Color) + self.sufix

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def Maroon              (self): return self._sequence(HtmlColors.Maroon)
    @property
    def DarkRed             (self): return self._sequence(HtmlColors.DarkRed)
    @property
    def Brown               (self): return self._sequence(HtmlColors.Brown)
    @property
    def Firebrick           (self): return self._sequence(HtmlColors.Firebrick)
    @property
    def Crimson             (self): return self._sequence(HtmlColors.Crimson)
    @property
    def Red                 (self): return self._sequence(HtmlColors.Red)
    @property
    def Tomato              (self): return self._sequence(HtmlColors.Tomato)
    @property
    def Coral               (self): return self._sequence(HtmlColors.Coral)
    @property
    def IndianRed           (self): return self._sequence(HtmlColors.IndianRed)
    @property
    def LightCoral          (self): return self._sequence(HtmlColors.LightCoral)
    @property
    def DarkSalmon          (self): return self._sequence(HtmlColors.DarkSalmon)
    @property
    def Salmon              (self): return self._sequence(HtmlColors.Salmon)
    @property
    def LightSalmon         (self): return self._sequence(HtmlColors.LightSalmon)
    @property
    def OrangeRed           (self): return self._sequence(HtmlColors.OrangeRed)
    @property
    def DarkOrange          (self): return self._sequence(HtmlColors.DarkOrange)
    @property
    def Orange              (self): return self._sequence(HtmlColors.Orange)
    @property
    def Gold                (self): return self._sequence(HtmlColors.Gold)
    @property
    def DarkGoldenRod       (self): return self._sequence(HtmlColors.DarkGoldenRod)
    @property
    def GoldenRod           (self): return self._sequence(HtmlColors.GoldenRod)
    @property
    def PaleGoldenRod       (self): return self._sequence(HtmlColors.PaleGoldenRod)
    @property
    def DarkKhaki           (self): return self._sequence(HtmlColors.DarkKhaki)
    @property
    def Khaki               (self): return self._sequence(HtmlColors.Khaki)
    @property
    def Olive               (self): return self._sequence(HtmlColors.Olive)
    @property
    def Yellow              (self): return self._sequence(HtmlColors.Yellow)
    @property
    def YellowGreen         (self): return self._sequence(HtmlColors.YellowGreen)
    @property
    def DarkOliveGreen      (self): return self._sequence(HtmlColors.DarkOliveGreen)
    @property
    def OliveDrab           (self): return self._sequence(HtmlColors.OliveDrab)
    @property
    def LawnGreen           (self): return self._sequence(HtmlColors.LawnGreen)
    @property
    def Chartreuse          (self): return self._sequence(HtmlColors.Chartreuse)
    @property
    def GreenYellow         (self): return self._sequence(HtmlColors.GreenYellow)
    @property
    def DarkGreen           (self): return self._sequence(HtmlColors.DarkGreen)
    @property
    def Green               (self): return self._sequence(HtmlColors.Green)
    @property
    def ForestGreen         (self): return self._sequence(HtmlColors.ForestGreen)
    @property
    def Lime                (self): return self._sequence(HtmlColors.Lime)
    @property
    def LimeGreen           (self): return self._sequence(HtmlColors.LimeGreen)
    @property
    def LightGreen          (self): return self._sequence(HtmlColors.LightGreen)
    @property
    def PaleGreen           (self): return self._sequence(HtmlColors.PaleGreen)
    @property
    def DarkSeaGreen        (self): return self._sequence(HtmlColors.DarkSeaGreen)
    @property
    def MediumSpringGreen   (self): return self._sequence(HtmlColors.MediumSpringGreen)
    @property
    def SpringGreen         (self): return self._sequence(HtmlColors.SpringGreen)
    @property
    def SeaGreen            (self): return self._sequence(HtmlColors.SeaGreen)
    @property
    def MediumAquaMarine    (self): return self._sequence(HtmlColors.MediumAquaMarine)
    @property
    def MediumSeaGreen      (self): return self._sequence(HtmlColors.MediumSeaGreen)
    @property
    def LightSeaGreen       (self): return self._sequence(HtmlColors.LightSeaGreen)
    @property
    def DarkSlateGray       (self): return self._sequence(HtmlColors.DarkSlateGray)
    @property
    def Teal                (self): return self._sequence(HtmlColors.Teal)
    @property
    def DarkCyan            (self): return self._sequence(HtmlColors.DarkCyan)
    @property
    def Aqua                (self): return self._sequence(HtmlColors.Aqua)
    @property
    def Cyan                (self): return self._sequence(HtmlColors.Cyan)
    @property
    def LightCyan           (self): return self._sequence(HtmlColors.LightCyan)
    @property
    def DarkTurquoise       (self): return self._sequence(HtmlColors.DarkTurquoise)
    @property
    def Turquoise           (self): return self._sequence(HtmlColors.Turquoise)
    @property
    def MediumTurquoise     (self): return self._sequence(HtmlColors.MediumTurquoise)
    @property
    def PaleTurquoise       (self): return self._sequence(HtmlColors.PaleTurquoise)
    @property
    def AquaMarine          (self): return self._sequence(HtmlColors.AquaMarine)
    @property
    def PowderBlue          (self): return self._sequence(HtmlColors.PowderBlue)
    @property
    def CadetBlue           (self): return self._sequence(HtmlColors.CadetBlue)
    @property
    def SteelBlue           (self): return self._sequence(HtmlColors.SteelBlue)
    @property
    def CornFlowerBlue      (self): return self._sequence(HtmlColors.CornFlowerBlue)
    @property
    def DeepSkyBlue         (self): return self._sequence(HtmlColors.DeepSkyBlue)
    @property
    def DodgerBlue          (self): return self._sequence(HtmlColors.DodgerBlue)
    @property
    def LightBlue           (self): return self._sequence(HtmlColors.LightBlue)
    @property
    def SkyBlue             (self): return self._sequence(HtmlColors.SkyBlue)
    @property
    def LightSkyBlue        (self): return self._sequence(HtmlColors.LightSkyBlue)
    @property
    def MidnightBlue        (self): return self._sequence(HtmlColors.MidnightBlue)
    @property
    def Navy                (self): return self._sequence(HtmlColors.Navy)
    @property
    def DarkBlue            (self): return self._sequence(HtmlColors.DarkBlue)
    @property
    def MediumBlue          (self): return self._sequence(HtmlColors.MediumBlue)
    @property
    def Blue                (self): return self._sequence(HtmlColors.Blue)
    @property
    def RoyalBlue           (self): return self._sequence(HtmlColors.RoyalBlue)
    @property
    def BlueViolet          (self): return self._sequence(HtmlColors.BlueViolet)
    @property
    def Indigo              (self): return self._sequence(HtmlColors.Indigo)
    @property
    def DarkSlateBlue       (self): return self._sequence(HtmlColors.DarkSlateBlue)
    @property
    def SlateBlue           (self): return self._sequence(HtmlColors.SlateBlue)
    @property
    def MediumSlateBlue     (self): return self._sequence(HtmlColors.MediumSlateBlue)
    @property
    def MediumPurple        (self): return self._sequence(HtmlColors.MediumPurple)
    @property
    def DarkMagenta         (self): return self._sequence(HtmlColors.DarkMagenta)
    @property
    def DarkViolet          (self): return self._sequence(HtmlColors.DarkViolet)
    @property
    def DarkOrchid          (self): return self._sequence(HtmlColors.DarkOrchid)
    @property
    def MediumOrchid        (self): return self._sequence(HtmlColors.MediumOrchid)
    @property
    def Purple              (self): return self._sequence(HtmlColors.Purple)
    @property
    def Thistle             (self): return self._sequence(HtmlColors.Thistle)
    @property
    def Plum                (self): return self._sequence(HtmlColors.Plum)
    @property
    def Violet              (self): return self._sequence(HtmlColors.Violet)
    @property
    def Magenta             (self): return self._sequence(HtmlColors.Magenta)
    @property
    def Orchid              (self): return self._sequence(HtmlColors.Orchid)
    @property
    def MediumVioletRed     (self): return self._sequence(HtmlColors.MediumVioletRed)
    @property
    def PaleVioletRed       (self): return self._sequence(HtmlColors.PaleVioletRed)
    @property
    def DeepPink            (self): return self._sequence(HtmlColors.DeepPink)
    @property
    def HotPink             (self): return self._sequence(HtmlColors.HotPink)
    @property
    def LightPink           (self): return self._sequence(HtmlColors.LightPink)
    @property
    def Pink                (self): return self._sequence(HtmlColors.Pink)
    @property
    def AntiqueWhite        (self): return self._sequence(HtmlColors.AntiqueWhite)
    @property
    def Beige               (self): return self._sequence(HtmlColors.Beige)
    @property
    def Bisque              (self): return self._sequence(HtmlColors.Bisque)
    @property
    def BlanchedAlmond      (self): return self._sequence(HtmlColors.BlanchedAlmond)
    @property
    def Wheat               (self): return self._sequence(HtmlColors.Wheat)
    @property
    def CornSilk            (self): return self._sequence(HtmlColors.CornSilk)
    @property
    def LemonChiffon        (self): return self._sequence(HtmlColors.LemonChiffon)
    @property
    def LightGoldenRodYellow(self): return self._sequence(HtmlColors.LightGoldenRodYellow)
    @property
    def LightYellow         (self): return self._sequence(HtmlColors.LightYellow)
    @property
    def SaddleBrown         (self): return self._sequence(HtmlColors.SaddleBrown)
    @property
    def Sienna              (self): return self._sequence(HtmlColors.Sienna)
    @property
    def Chocolate           (self): return self._sequence(HtmlColors.Chocolate)
    @property
    def Peru                (self): return self._sequence(HtmlColors.Peru)
    @property
    def SandyBrown          (self): return self._sequence(HtmlColors.SandyBrown)
    @property
    def BurlyWood           (self): return self._sequence(HtmlColors.BurlyWood)
    @property
    def Tan                 (self): return self._sequence(HtmlColors.Tan)
    @property
    def RosyBrown           (self): return self._sequence(HtmlColors.RosyBrown)
    @property
    def Moccasin            (self): return self._sequence(HtmlColors.Moccasin)
    @property
    def NavajoWhite         (self): return self._sequence(HtmlColors.NavajoWhite)
    @property
    def PeachPuff           (self): return self._sequence(HtmlColors.PeachPuff)
    @property
    def MistyRose           (self): return self._sequence(HtmlColors.MistyRose)
    @property
    def LavenderBlush       (self): return self._sequence(HtmlColors.LavenderBlush)
    @property
    def Linen               (self): return self._sequence(HtmlColors.Linen)
    @property
    def OldLace             (self): return self._sequence(HtmlColors.OldLace)
    @property
    def PapayaWhip          (self): return self._sequence(HtmlColors.PapayaWhip)
    @property
    def WeaShell            (self): return self._sequence(HtmlColors.WeaShell)
    @property
    def MintCream           (self): return self._sequence(HtmlColors.MintCream)
    @property
    def SlateGray           (self): return self._sequence(HtmlColors.SlateGray)
    @property
    def LightSlateGray      (self): return self._sequence(HtmlColors.LightSlateGray)
    @property
    def LightSteelBlue      (self): return self._sequence(HtmlColors.LightSteelBlue)
    @property
    def Lavender            (self): return self._sequence(HtmlColors.Lavender)
    @property
    def FloralWhite         (self): return self._sequence(HtmlColors.FloralWhite)
    @property
    def AliceBlue           (self): return self._sequence(HtmlColors.AliceBlue)
    @property
    def GhostWhite          (self): return self._sequence(HtmlColors.GhostWhite)
    @property
    def Honeydew            (self): return self._sequence(HtmlColors.Honeydew)
    @property
    def Ivory               (self): return self._sequence(HtmlColors.Ivory)
    @property
    def Azure               (self): return self._sequence(HtmlColors.Azure)
    @property
    def Snow                (self): return self._sequence(HtmlColors.Snow)
    @property
    def Black               (self): return self._sequence(HtmlColors.Black)
    @property
    def DimGray             (self): return self._sequence(HtmlColors.DimGray)
    @property
    def Gray                (self): return self._sequence(HtmlColors.Gray)
    @property
    def DarkGray            (self): return self._sequence(HtmlColors.DarkGray)
    @property
    def Silver              (self): return self._sequence(HtmlColors.Silver)
    @property
    def LightGray           (self): return self._sequence(HtmlColors.LightGray)
    @property
    def Gainsboro           (self): return self._sequence(HtmlColors.Gainsboro)
    @property
    def WhiteSmoke          (self): return self._sequence(HtmlColors.WhiteSmoke)
    @property
    def White               (self): return self._sequence(HtmlColors.White)