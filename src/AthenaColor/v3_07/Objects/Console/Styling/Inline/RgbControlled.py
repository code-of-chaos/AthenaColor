# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from typing import Union

# Custom Library

# Custom Packages
from AthenaColor.v3_07.Objects.ColorSystems import (RGB,RGBA,HEX,HEXA,HSV,HSL,CMYK)
from AthenaColor.v3_07.Functions.ColorTupleConversion import cmyk_to_rgb,hsv_to_rgb,hsl_to_rgb
from AthenaColor.v3_07.Functions.AnsiSquences import ColorSequence
from AthenaColor.v3_07.Data.HtmlColors import HtmlColorTuples

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Colors = Union[RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA]

class RgbControlled:
    param_code:str
    def __init__(self, param_code:str):
        self.param_code = param_code

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:Colors) -> str:
        if isinstance(color, (RGB,RGBA,HEX,HEXA)):
            color_str = f"{color.r};{color.g};{color.b}"
        elif isinstance(color,HSL):
            r,g,b = hsl_to_rgb(color.h,color.s,color.l)
            color_str = f"{r};{g};{b}"
        elif isinstance(color,HSV):
            r,g,b = hsv_to_rgb(color.h,color.s,color.v)
            color_str = f"{r};{g};{b}"
        elif isinstance(color,CMYK):
            r,g,b = cmyk_to_rgb(color.c,color.m,color.y,color.k)
            color_str = f"{r};{g};{b}"
        else:
            raise ValueError
        return ColorSequence(self.param_code + color_str)

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def Maroon              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Maroon))
    @property
    def DarkRed             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkRed))
    @property
    def Brown               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Brown))
    @property
    def Firebrick           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Firebrick))
    @property
    def Crimson             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Crimson))
    @property
    def Red                 (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Red))
    @property
    def Tomato              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Tomato))
    @property
    def Coral               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Coral))
    @property
    def IndianRed           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.IndianRed))
    @property
    def LightCoral          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightCoral))
    @property
    def DarkSalmon          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkSalmon))
    @property
    def Salmon              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Salmon))
    @property
    def LightSalmon         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightSalmon))
    @property
    def OrangeRed           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.OrangeRed))
    @property
    def DarkOrange          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkOrange))
    @property
    def Orange              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Orange))
    @property
    def Gold                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Gold))
    @property
    def DarkGoldenRod       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkGoldenRod))
    @property
    def GoldenRod           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.GoldenRod))
    @property
    def PaleGoldenRod       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PaleGoldenRod))
    @property
    def DarkKhaki           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkKhaki))
    @property
    def Khaki               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Khaki))
    @property
    def Olive               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Olive))
    @property
    def Yellow              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Yellow))
    @property
    def YellowGreen         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.YellowGreen))
    @property
    def DarkOliveGreen      (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkOliveGreen))
    @property
    def OliveDrab           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.OliveDrab))
    @property
    def LawnGreen           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LawnGreen))
    @property
    def Chartreuse          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Chartreuse))
    @property
    def GreenYellow         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.GreenYellow))
    @property
    def DarkGreen           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkGreen))
    @property
    def Green               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Green))
    @property
    def ForestGreen         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.ForestGreen))
    @property
    def Lime                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Lime))
    @property
    def LimeGreen           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LimeGreen))
    @property
    def LightGreen          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightGreen))
    @property
    def PaleGreen           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PaleGreen))
    @property
    def DarkSeaGreen        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkSeaGreen))
    @property
    def MediumSpringGreen   (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumSpringGreen))
    @property
    def SpringGreen         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SpringGreen))
    @property
    def SeaGreen            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SeaGreen))
    @property
    def MediumAquaMarine    (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumAquaMarine))
    @property
    def MediumSeaGreen      (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumSeaGreen))
    @property
    def LightSeaGreen       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightSeaGreen))
    @property
    def DarkSlateGray       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkSlateGray))
    @property
    def Teal                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Teal))
    @property
    def DarkCyan            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkCyan))
    @property
    def Aqua                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Aqua))
    @property
    def Cyan                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Cyan))
    @property
    def LightCyan           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightCyan))
    @property
    def DarkTurquoise       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkTurquoise))
    @property
    def Turquoise           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Turquoise))
    @property
    def MediumTurquoise     (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumTurquoise))
    @property
    def PaleTurquoise       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PaleTurquoise))
    @property
    def AquaMarine          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.AquaMarine))
    @property
    def PowderBlue          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PowderBlue))
    @property
    def CadetBlue           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.CadetBlue))
    @property
    def SteelBlue           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SteelBlue))
    @property
    def CornFlowerBlue      (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.CornFlowerBlue))
    @property
    def DeepSkyBlue         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DeepSkyBlue))
    @property
    def DodgerBlue          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DodgerBlue))
    @property
    def LightBlue           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightBlue))
    @property
    def SkyBlue             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SkyBlue))
    @property
    def LightSkyBlue        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightSkyBlue))
    @property
    def MidnightBlue        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MidnightBlue))
    @property
    def Navy                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Navy))
    @property
    def DarkBlue            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkBlue))
    @property
    def MediumBlue          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumBlue))
    @property
    def Blue                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Blue))
    @property
    def RoyalBlue           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.RoyalBlue))
    @property
    def BlueViolet          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.BlueViolet))
    @property
    def Indigo              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Indigo))
    @property
    def DarkSlateBlue       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkSlateBlue))
    @property
    def SlateBlue           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SlateBlue))
    @property
    def MediumSlateBlue     (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumSlateBlue))
    @property
    def MediumPurple        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumPurple))
    @property
    def DarkMagenta         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkMagenta))
    @property
    def DarkViolet          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkViolet))
    @property
    def DarkOrchid          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkOrchid))
    @property
    def MediumOrchid        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumOrchid))
    @property
    def Purple              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Purple))
    @property
    def Thistle             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Thistle))
    @property
    def Plum                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Plum))
    @property
    def Violet              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Violet))
    @property
    def Magenta             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Magenta))
    @property
    def Orchid              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Orchid))
    @property
    def MediumVioletRed     (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MediumVioletRed))
    @property
    def PaleVioletRed       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PaleVioletRed))
    @property
    def DeepPink            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DeepPink))
    @property
    def HotPink             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.HotPink))
    @property
    def LightPink           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightPink))
    @property
    def Pink                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Pink))
    @property
    def AntiqueWhite        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.AntiqueWhite))
    @property
    def Beige               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Beige))
    @property
    def Bisque              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Bisque))
    @property
    def BlanchedAlmond      (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.BlanchedAlmond))
    @property
    def Wheat               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Wheat))
    @property
    def CornSilk            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.CornSilk))
    @property
    def LemonChiffon        (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LemonChiffon))
    @property
    def LightGoldenRodYellow(self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightGoldenRodYellow))
    @property
    def LightYellow         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightYellow))
    @property
    def SaddleBrown         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SaddleBrown))
    @property
    def Sienna              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Sienna))
    @property
    def Chocolate           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Chocolate))
    @property
    def Peru                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Peru))
    @property
    def SandyBrown          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SandyBrown))
    @property
    def BurlyWood           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.BurlyWood))
    @property
    def Tan                 (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Tan))
    @property
    def RosyBrown           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.RosyBrown))
    @property
    def Moccasin            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Moccasin))
    @property
    def NavajoWhite         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.NavajoWhite))
    @property
    def PeachPuff           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PeachPuff))
    @property
    def MistyRose           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MistyRose))
    @property
    def LavenderBlush       (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LavenderBlush))
    @property
    def Linen               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Linen))
    @property
    def OldLace             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.OldLace))
    @property
    def PapayaWhip          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.PapayaWhip))
    @property
    def WeaShell            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.WeaShell))
    @property
    def MintCream           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.MintCream))
    @property
    def SlateGray           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.SlateGray))
    @property
    def LightSlateGray      (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightSlateGray))
    @property
    def LightSteelBlue      (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightSteelBlue))
    @property
    def Lavender            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Lavender))
    @property
    def FloralWhite         (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.FloralWhite))
    @property
    def AliceBlue           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.AliceBlue))
    @property
    def GhostWhite          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.GhostWhite))
    @property
    def Honeydew            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Honeydew))
    @property
    def Ivory               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Ivory))
    @property
    def Azure               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Azure))
    @property
    def Snow                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Snow))
    @property
    def Black               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Black))
    @property
    def DimGray             (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DimGray))
    @property
    def Gray                (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Gray))
    @property
    def DarkGray            (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.DarkGray))
    @property
    def Silver              (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Silver))
    @property
    def LightGray           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.LightGray))
    @property
    def Gainsboro           (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.Gainsboro))
    @property
    def WhiteSmoke          (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.WhiteSmoke))
    @property
    def White               (self): return ColorSequence(self.param_code + ";".join(str(c) for c in HtmlColorTuples.White))