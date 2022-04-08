# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.v3_10.Objects.ColorSystems import (RGB,RGBA,HEX,HEXA,HSV,HSL,CMYK)
from AthenaColor.v3_10.Functions.ColorTupleConversion import cmyk_to_rgb,hsv_to_rgb,hsl_to_rgb
from AthenaColor.v3_10.Functions.AnsiSquences import ColorSequence
from AthenaColor.v3_10.Data.HtmlColors import HtmlColorTuples

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
    def custom(self, color:RGB|RGBA|HEX|HEXA|HSV|HSL|CMYK) -> str:
        match color:
            case RGB(r=r,g=g,b=b) | RGBA(r=r,g=g,b=b) | HEX(r=r,g=g,b=b) | HEXA(r=r,g=g,b=b):
                color_str = f"{r};{g};{b}"
            case HSL(h=h,s=s,l=l):
                r,g,b = hsl_to_rgb(h,s,l)
                color_str = f"{r};{g};{b}"
            case HSV(h=h,s=s,v=v):
                r,g,b = hsv_to_rgb(h,s,v)
                color_str = f"{r};{g};{b}"
            case CMYK(c=c,m=m,y=y,k=k):
                r,g,b = cmyk_to_rgb(c,m,y,k)
                color_str = f"{r};{g};{b}"
            case _:
                raise ValueError
        return ColorSequence(self.param_code + color_str)

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def Maroon              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Maroon))
    @property
    def DarkRed             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkRed))
    @property
    def Brown               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Brown))
    @property
    def Firebrick           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Firebrick))
    @property
    def Crimson             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Crimson))
    @property
    def Red                 (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Red))
    @property
    def Tomato              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Tomato))
    @property
    def Coral               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Coral))
    @property
    def IndianRed           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.IndianRed))
    @property
    def LightCoral          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightCoral))
    @property
    def DarkSalmon          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkSalmon))
    @property
    def Salmon              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Salmon))
    @property
    def LightSalmon         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightSalmon))
    @property
    def OrangeRed           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.OrangeRed))
    @property
    def DarkOrange          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkOrange))
    @property
    def Orange              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Orange))
    @property
    def Gold                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Gold))
    @property
    def DarkGoldenRod       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkGoldenRod))
    @property
    def GoldenRod           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.GoldenRod))
    @property
    def PaleGoldenRod       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PaleGoldenRod))
    @property
    def DarkKhaki           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkKhaki))
    @property
    def Khaki               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Khaki))
    @property
    def Olive               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Olive))
    @property
    def Yellow              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Yellow))
    @property
    def YellowGreen         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.YellowGreen))
    @property
    def DarkOliveGreen      (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkOliveGreen))
    @property
    def OliveDrab           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.OliveDrab))
    @property
    def LawnGreen           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LawnGreen))
    @property
    def Chartreuse          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Chartreuse))
    @property
    def GreenYellow         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.GreenYellow))
    @property
    def DarkGreen           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkGreen))
    @property
    def Green               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Green))
    @property
    def ForestGreen         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.ForestGreen))
    @property
    def Lime                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Lime))
    @property
    def LimeGreen           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LimeGreen))
    @property
    def LightGreen          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightGreen))
    @property
    def PaleGreen           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PaleGreen))
    @property
    def DarkSeaGreen        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkSeaGreen))
    @property
    def MediumSpringGreen   (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumSpringGreen))
    @property
    def SpringGreen         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SpringGreen))
    @property
    def SeaGreen            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SeaGreen))
    @property
    def MediumAquaMarine    (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumAquaMarine))
    @property
    def MediumSeaGreen      (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumSeaGreen))
    @property
    def LightSeaGreen       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightSeaGreen))
    @property
    def DarkSlateGray       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkSlateGray))
    @property
    def Teal                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Teal))
    @property
    def DarkCyan            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkCyan))
    @property
    def Aqua                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Aqua))
    @property
    def Cyan                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Cyan))
    @property
    def LightCyan           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightCyan))
    @property
    def DarkTurquoise       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkTurquoise))
    @property
    def Turquoise           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Turquoise))
    @property
    def MediumTurquoise     (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumTurquoise))
    @property
    def PaleTurquoise       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PaleTurquoise))
    @property
    def AquaMarine          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.AquaMarine))
    @property
    def PowderBlue          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PowderBlue))
    @property
    def CadetBlue           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.CadetBlue))
    @property
    def SteelBlue           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SteelBlue))
    @property
    def CornFlowerBlue      (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.CornFlowerBlue))
    @property
    def DeepSkyBlue         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DeepSkyBlue))
    @property
    def DodgerBlue          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DodgerBlue))
    @property
    def LightBlue           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightBlue))
    @property
    def SkyBlue             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SkyBlue))
    @property
    def LightSkyBlue        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightSkyBlue))
    @property
    def MidnightBlue        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MidnightBlue))
    @property
    def Navy                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Navy))
    @property
    def DarkBlue            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkBlue))
    @property
    def MediumBlue          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumBlue))
    @property
    def Blue                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Blue))
    @property
    def RoyalBlue           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.RoyalBlue))
    @property
    def BlueViolet          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.BlueViolet))
    @property
    def Indigo              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Indigo))
    @property
    def DarkSlateBlue       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkSlateBlue))
    @property
    def SlateBlue           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SlateBlue))
    @property
    def MediumSlateBlue     (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumSlateBlue))
    @property
    def MediumPurple        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumPurple))
    @property
    def DarkMagenta         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkMagenta))
    @property
    def DarkViolet          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkViolet))
    @property
    def DarkOrchid          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkOrchid))
    @property
    def MediumOrchid        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumOrchid))
    @property
    def Purple              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Purple))
    @property
    def Thistle             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Thistle))
    @property
    def Plum                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Plum))
    @property
    def Violet              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Violet))
    @property
    def Magenta             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Magenta))
    @property
    def Orchid              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Orchid))
    @property
    def MediumVioletRed     (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MediumVioletRed))
    @property
    def PaleVioletRed       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PaleVioletRed))
    @property
    def DeepPink            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DeepPink))
    @property
    def HotPink             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.HotPink))
    @property
    def LightPink           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightPink))
    @property
    def Pink                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Pink))
    @property
    def AntiqueWhite        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.AntiqueWhite))
    @property
    def Beige               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Beige))
    @property
    def Bisque              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Bisque))
    @property
    def BlanchedAlmond      (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.BlanchedAlmond))
    @property
    def Wheat               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Wheat))
    @property
    def CornSilk            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.CornSilk))
    @property
    def LemonChiffon        (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LemonChiffon))
    @property
    def LightGoldenRodYellow(self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightGoldenRodYellow))
    @property
    def LightYellow         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightYellow))
    @property
    def SaddleBrown         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SaddleBrown))
    @property
    def Sienna              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Sienna))
    @property
    def Chocolate           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Chocolate))
    @property
    def Peru                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Peru))
    @property
    def SandyBrown          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SandyBrown))
    @property
    def BurlyWood           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.BurlyWood))
    @property
    def Tan                 (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Tan))
    @property
    def RosyBrown           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.RosyBrown))
    @property
    def Moccasin            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Moccasin))
    @property
    def NavajoWhite         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.NavajoWhite))
    @property
    def PeachPuff           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PeachPuff))
    @property
    def MistyRose           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MistyRose))
    @property
    def LavenderBlush       (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LavenderBlush))
    @property
    def Linen               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Linen))
    @property
    def OldLace             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.OldLace))
    @property
    def PapayaWhip          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.PapayaWhip))
    @property
    def WeaShell            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.WeaShell))
    @property
    def MintCream           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.MintCream))
    @property
    def SlateGray           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.SlateGray))
    @property
    def LightSlateGray      (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightSlateGray))
    @property
    def LightSteelBlue      (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightSteelBlue))
    @property
    def Lavender            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Lavender))
    @property
    def FloralWhite         (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.FloralWhite))
    @property
    def AliceBlue           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.AliceBlue))
    @property
    def GhostWhite          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.GhostWhite))
    @property
    def Honeydew            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Honeydew))
    @property
    def Ivory               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Ivory))
    @property
    def Azure               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Azure))
    @property
    def Snow                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Snow))
    @property
    def Black               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Black))
    @property
    def DimGray             (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DimGray))
    @property
    def Gray                (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Gray))
    @property
    def DarkGray            (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.DarkGray))
    @property
    def Silver              (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Silver))
    @property
    def LightGray           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.LightGray))
    @property
    def Gainsboro           (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.Gainsboro))
    @property
    def WhiteSmoke          (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.WhiteSmoke))
    @property
    def White               (self): return ColorSequence(self.param_code + ";".join(HtmlColorTuples.White))