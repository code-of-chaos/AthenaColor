# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects.ColorSystems import RGB
from AthenaColor.Functions.AnsiSquences import ColorSequence
import AthenaColor.Data.HtmlColors as HtmlColors

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlled:
    param_code:str
    def __init__(self, param_code:str):
        self.param_code = param_code

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:RGB) -> str:
        return ColorSequence(self.param_code + str(color))

    def rgb(self, r:int,g:int,b:int) -> str:
        return ColorSequence(self.param_code + str(RGB(r, g, b)))

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def Maroon              (self): return self.custom(HtmlColors.Maroon)
    @property
    def DarkRed             (self): return self.custom(HtmlColors.DarkRed)
    @property
    def Brown               (self): return self.custom(HtmlColors.Brown)
    @property
    def Firebrick           (self): return self.custom(HtmlColors.Firebrick)
    @property
    def Crimson             (self): return self.custom(HtmlColors.Crimson)
    @property
    def Red                 (self): return self.custom(HtmlColors.Red)
    @property
    def Tomato              (self): return self.custom(HtmlColors.Tomato)
    @property
    def Coral               (self): return self.custom(HtmlColors.Coral)
    @property
    def IndianRed           (self): return self.custom(HtmlColors.IndianRed)
    @property
    def LightCoral          (self): return self.custom(HtmlColors.LightCoral)
    @property
    def DarkSalmon          (self): return self.custom(HtmlColors.DarkSalmon)
    @property
    def Salmon              (self): return self.custom(HtmlColors.Salmon)
    @property
    def LightSalmon         (self): return self.custom(HtmlColors.LightSalmon)
    @property
    def OrangeRed           (self): return self.custom(HtmlColors.OrangeRed)
    @property
    def DarkOrange          (self): return self.custom(HtmlColors.DarkOrange)
    @property
    def Orange              (self): return self.custom(HtmlColors.Orange)
    @property
    def Gold                (self): return self.custom(HtmlColors.Gold)
    @property
    def DarkGoldenRod       (self): return self.custom(HtmlColors.DarkGoldenRod)
    @property
    def GoldenRod           (self): return self.custom(HtmlColors.GoldenRod)
    @property
    def PaleGoldenRod       (self): return self.custom(HtmlColors.PaleGoldenRod)
    @property
    def DarkKhaki           (self): return self.custom(HtmlColors.DarkKhaki)
    @property
    def Khaki               (self): return self.custom(HtmlColors.Khaki)
    @property
    def Olive               (self): return self.custom(HtmlColors.Olive)
    @property
    def Yellow              (self): return self.custom(HtmlColors.Yellow)
    @property
    def YellowGreen         (self): return self.custom(HtmlColors.YellowGreen)
    @property
    def DarkOliveGreen      (self): return self.custom(HtmlColors.DarkOliveGreen)
    @property
    def OliveDrab           (self): return self.custom(HtmlColors.OliveDrab)
    @property
    def LawnGreen           (self): return self.custom(HtmlColors.LawnGreen)
    @property
    def Chartreuse          (self): return self.custom(HtmlColors.Chartreuse)
    @property
    def GreenYellow         (self): return self.custom(HtmlColors.GreenYellow)
    @property
    def DarkGreen           (self): return self.custom(HtmlColors.DarkGreen)
    @property
    def Green               (self): return self.custom(HtmlColors.Green)
    @property
    def ForestGreen         (self): return self.custom(HtmlColors.ForestGreen)
    @property
    def Lime                (self): return self.custom(HtmlColors.Lime)
    @property
    def LimeGreen           (self): return self.custom(HtmlColors.LimeGreen)
    @property
    def LightGreen          (self): return self.custom(HtmlColors.LightGreen)
    @property
    def PaleGreen           (self): return self.custom(HtmlColors.PaleGreen)
    @property
    def DarkSeaGreen        (self): return self.custom(HtmlColors.DarkSeaGreen)
    @property
    def MediumSpringGreen   (self): return self.custom(HtmlColors.MediumSpringGreen)
    @property
    def SpringGreen         (self): return self.custom(HtmlColors.SpringGreen)
    @property
    def SeaGreen            (self): return self.custom(HtmlColors.SeaGreen)
    @property
    def MediumAquaMarine    (self): return self.custom(HtmlColors.MediumAquaMarine)
    @property
    def MediumSeaGreen      (self): return self.custom(HtmlColors.MediumSeaGreen)
    @property
    def LightSeaGreen       (self): return self.custom(HtmlColors.LightSeaGreen)
    @property
    def DarkSlateGray       (self): return self.custom(HtmlColors.DarkSlateGray)
    @property
    def Teal                (self): return self.custom(HtmlColors.Teal)
    @property
    def DarkCyan            (self): return self.custom(HtmlColors.DarkCyan)
    @property
    def Aqua                (self): return self.custom(HtmlColors.Aqua)
    @property
    def Cyan                (self): return self.custom(HtmlColors.Cyan)
    @property
    def LightCyan           (self): return self.custom(HtmlColors.LightCyan)
    @property
    def DarkTurquoise       (self): return self.custom(HtmlColors.DarkTurquoise)
    @property
    def Turquoise           (self): return self.custom(HtmlColors.Turquoise)
    @property
    def MediumTurquoise     (self): return self.custom(HtmlColors.MediumTurquoise)
    @property
    def PaleTurquoise       (self): return self.custom(HtmlColors.PaleTurquoise)
    @property
    def AquaMarine          (self): return self.custom(HtmlColors.AquaMarine)
    @property
    def PowderBlue          (self): return self.custom(HtmlColors.PowderBlue)
    @property
    def CadetBlue           (self): return self.custom(HtmlColors.CadetBlue)
    @property
    def SteelBlue           (self): return self.custom(HtmlColors.SteelBlue)
    @property
    def CornFlowerBlue      (self): return self.custom(HtmlColors.CornFlowerBlue)
    @property
    def DeepSkyBlue         (self): return self.custom(HtmlColors.DeepSkyBlue)
    @property
    def DodgerBlue          (self): return self.custom(HtmlColors.DodgerBlue)
    @property
    def LightBlue           (self): return self.custom(HtmlColors.LightBlue)
    @property
    def SkyBlue             (self): return self.custom(HtmlColors.SkyBlue)
    @property
    def LightSkyBlue        (self): return self.custom(HtmlColors.LightSkyBlue)
    @property
    def MidnightBlue        (self): return self.custom(HtmlColors.MidnightBlue)
    @property
    def Navy                (self): return self.custom(HtmlColors.Navy)
    @property
    def DarkBlue            (self): return self.custom(HtmlColors.DarkBlue)
    @property
    def MediumBlue          (self): return self.custom(HtmlColors.MediumBlue)
    @property
    def Blue                (self): return self.custom(HtmlColors.Blue)
    @property
    def RoyalBlue           (self): return self.custom(HtmlColors.RoyalBlue)
    @property
    def BlueViolet          (self): return self.custom(HtmlColors.BlueViolet)
    @property
    def Indigo              (self): return self.custom(HtmlColors.Indigo)
    @property
    def DarkSlateBlue       (self): return self.custom(HtmlColors.DarkSlateBlue)
    @property
    def SlateBlue           (self): return self.custom(HtmlColors.SlateBlue)
    @property
    def MediumSlateBlue     (self): return self.custom(HtmlColors.MediumSlateBlue)
    @property
    def MediumPurple        (self): return self.custom(HtmlColors.MediumPurple)
    @property
    def DarkMagenta         (self): return self.custom(HtmlColors.DarkMagenta)
    @property
    def DarkViolet          (self): return self.custom(HtmlColors.DarkViolet)
    @property
    def DarkOrchid          (self): return self.custom(HtmlColors.DarkOrchid)
    @property
    def MediumOrchid        (self): return self.custom(HtmlColors.MediumOrchid)
    @property
    def Purple              (self): return self.custom(HtmlColors.Purple)
    @property
    def Thistle             (self): return self.custom(HtmlColors.Thistle)
    @property
    def Plum                (self): return self.custom(HtmlColors.Plum)
    @property
    def Violet              (self): return self.custom(HtmlColors.Violet)
    @property
    def Magenta             (self): return self.custom(HtmlColors.Magenta)
    @property
    def Orchid              (self): return self.custom(HtmlColors.Orchid)
    @property
    def MediumVioletRed     (self): return self.custom(HtmlColors.MediumVioletRed)
    @property
    def PaleVioletRed       (self): return self.custom(HtmlColors.PaleVioletRed)
    @property
    def DeepPink            (self): return self.custom(HtmlColors.DeepPink)
    @property
    def HotPink             (self): return self.custom(HtmlColors.HotPink)
    @property
    def LightPink           (self): return self.custom(HtmlColors.LightPink)
    @property
    def Pink                (self): return self.custom(HtmlColors.Pink)
    @property
    def AntiqueWhite        (self): return self.custom(HtmlColors.AntiqueWhite)
    @property
    def Beige               (self): return self.custom(HtmlColors.Beige)
    @property
    def Bisque              (self): return self.custom(HtmlColors.Bisque)
    @property
    def BlanchedAlmond      (self): return self.custom(HtmlColors.BlanchedAlmond)
    @property
    def Wheat               (self): return self.custom(HtmlColors.Wheat)
    @property
    def CornSilk            (self): return self.custom(HtmlColors.CornSilk)
    @property
    def LemonChiffon        (self): return self.custom(HtmlColors.LemonChiffon)
    @property
    def LightGoldenRodYellow(self): return self.custom(HtmlColors.LightGoldenRodYellow)
    @property
    def LightYellow         (self): return self.custom(HtmlColors.LightYellow)
    @property
    def SaddleBrown         (self): return self.custom(HtmlColors.SaddleBrown)
    @property
    def Sienna              (self): return self.custom(HtmlColors.Sienna)
    @property
    def Chocolate           (self): return self.custom(HtmlColors.Chocolate)
    @property
    def Peru                (self): return self.custom(HtmlColors.Peru)
    @property
    def SandyBrown          (self): return self.custom(HtmlColors.SandyBrown)
    @property
    def BurlyWood           (self): return self.custom(HtmlColors.BurlyWood)
    @property
    def Tan                 (self): return self.custom(HtmlColors.Tan)
    @property
    def RosyBrown           (self): return self.custom(HtmlColors.RosyBrown)
    @property
    def Moccasin            (self): return self.custom(HtmlColors.Moccasin)
    @property
    def NavajoWhite         (self): return self.custom(HtmlColors.NavajoWhite)
    @property
    def PeachPuff           (self): return self.custom(HtmlColors.PeachPuff)
    @property
    def MistyRose           (self): return self.custom(HtmlColors.MistyRose)
    @property
    def LavenderBlush       (self): return self.custom(HtmlColors.LavenderBlush)
    @property
    def Linen               (self): return self.custom(HtmlColors.Linen)
    @property
    def OldLace             (self): return self.custom(HtmlColors.OldLace)
    @property
    def PapayaWhip          (self): return self.custom(HtmlColors.PapayaWhip)
    @property
    def WeaShell            (self): return self.custom(HtmlColors.WeaShell)
    @property
    def MintCream           (self): return self.custom(HtmlColors.MintCream)
    @property
    def SlateGray           (self): return self.custom(HtmlColors.SlateGray)
    @property
    def LightSlateGray      (self): return self.custom(HtmlColors.LightSlateGray)
    @property
    def LightSteelBlue      (self): return self.custom(HtmlColors.LightSteelBlue)
    @property
    def Lavender            (self): return self.custom(HtmlColors.Lavender)
    @property
    def FloralWhite         (self): return self.custom(HtmlColors.FloralWhite)
    @property
    def AliceBlue           (self): return self.custom(HtmlColors.AliceBlue)
    @property
    def GhostWhite          (self): return self.custom(HtmlColors.GhostWhite)
    @property
    def Honeydew            (self): return self.custom(HtmlColors.Honeydew)
    @property
    def Ivory               (self): return self.custom(HtmlColors.Ivory)
    @property
    def Azure               (self): return self.custom(HtmlColors.Azure)
    @property
    def Snow                (self): return self.custom(HtmlColors.Snow)
    @property
    def Black               (self): return self.custom(HtmlColors.Black)
    @property
    def DimGray             (self): return self.custom(HtmlColors.DimGray)
    @property
    def Gray                (self): return self.custom(HtmlColors.Gray)
    @property
    def DarkGray            (self): return self.custom(HtmlColors.DarkGray)
    @property
    def Silver              (self): return self.custom(HtmlColors.Silver)
    @property
    def LightGray           (self): return self.custom(HtmlColors.LightGray)
    @property
    def Gainsboro           (self): return self.custom(HtmlColors.Gainsboro)
    @property
    def WhiteSmoke          (self): return self.custom(HtmlColors.WhiteSmoke)
    @property
    def White               (self): return self.custom(HtmlColors.White)