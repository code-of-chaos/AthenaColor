# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.models.Color.ColorTupleConversion import cmyk_to_rgb,hsv_to_rgb,hsl_to_rgb
from AthenaColor.Functions.ANSIsequences import ColorSequence
from AthenaColor.data.HtmlColors import HtmlColorObjects
from AthenaColor.Color.ColorSystem import RGB, RGBA, HEX, HEXA, HSV, HSL, CMYK

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "RgbControlled"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlled:
    __slots__ = (
        "param_code",
        "Maroon","DarkRed","Brown","Firebrick","Crimson","Red","Tomato","Coral","IndianRed","LightCoral","DarkSalmon",
        "Salmon","LightSalmon","OrangeRed","DarkOrange","Orange","Gold","DarkGoldenRod","GoldenRod","PaleGoldenRod",
        "DarkKhaki","Khaki","Olive","Yellow","YellowGreen","DarkOliveGreen","OliveDrab","LawnGreen","Chartreuse",
        "GreenYellow","DarkGreen","Green","ForestGreen","Lime","LimeGreen","LightGreen","PaleGreen","DarkSeaGreen",
        "MediumSpringGreen","SpringGreen","SeaGreen","MediumAquaMarine","MediumSeaGreen","LightSeaGreen","DarkSlateGray",
        "Teal","DarkCyan","Aqua","Cyan","LightCyan","DarkTurquoise","Turquoise","MediumTurquoise","PaleTurquoise",
        "AquaMarine","PowderBlue","CadetBlue","SteelBlue","CornFlowerBlue","DeepSkyBlue","DodgerBlue","LightBlue",
        "SkyBlue","LightSkyBlue","MidnightBlue","Navy","DarkBlue","MediumBlue","Blue","RoyalBlue","BlueViolet","Indigo",
        "DarkSlateBlue","SlateBlue","MediumSlateBlue","MediumPurple","DarkMagenta","DarkViolet","DarkOrchid","MediumOrchid",
        "Purple","Thistle","Plum","Violet","Magenta","Orchid","MediumVioletRed","PaleVioletRed","DeepPink","HotPink",
        "LightPink", "Pink", "AntiqueWhite", "Beige", "Bisque", "BlanchedAlmond", "Wheat", "CornSilk", "LemonChiffon",
        "LightGoldenRodYellow", "LightYellow", "SaddleBrown", "Sienna", "Chocolate", "Peru", "SandyBrown", "BurlyWood", "Tan",
        "RosyBrown", "Moccasin", "NavajoWhite", "PeachPuff", "MistyRose", "LavenderBlush", "Linen", "OldLace", "PapayaWhip",
        "WeaShell", "MintCream", "SlateGray", "LightSlateGray", "LightSteelBlue", "Lavender", "FloralWhite", "AliceBlue",
        "GhostWhite", "Honeydew", "Ivory", "Azure", "Snow", "Black", "DimGray", "Gray", "DarkGray", "Silver", "LightGray"
        , "Gainsboro", "WhiteSmoke", "White",
    )
    def __init__(self, param_code:str):
        self.param_code = param_code
        self.Maroon              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Maroon)}")
        self.DarkRed             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkRed)}")
        self.Brown               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Brown)}")
        self.Firebrick           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Firebrick)}")
        self.Crimson             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Crimson)}")
        self.Red                 = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Red)}")
        self.Tomato              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Tomato)}")
        self.Coral               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Coral)}")
        self.IndianRed           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.IndianRed)}")
        self.LightCoral          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightCoral)}")
        self.DarkSalmon          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkSalmon)}")
        self.Salmon              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Salmon)}")
        self.LightSalmon         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightSalmon)}")
        self.OrangeRed           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.OrangeRed)}")
        self.DarkOrange          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkOrange)}")
        self.Orange              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Orange)}")
        self.Gold                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Gold)}")
        self.DarkGoldenRod       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkGoldenRod)}")
        self.GoldenRod           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.GoldenRod)}")
        self.PaleGoldenRod       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PaleGoldenRod)}")
        self.DarkKhaki           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkKhaki)}")
        self.Khaki               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Khaki)}")
        self.Olive               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Olive)}")
        self.Yellow              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Yellow)}")
        self.YellowGreen         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.YellowGreen)}")
        self.DarkOliveGreen      = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkOliveGreen)}")
        self.OliveDrab           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.OliveDrab)}")
        self.LawnGreen           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LawnGreen)}")
        self.Chartreuse          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Chartreuse)}")
        self.GreenYellow         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.GreenYellow)}")
        self.DarkGreen           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkGreen)}")
        self.Green               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Green)}")
        self.ForestGreen         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.ForestGreen)}")
        self.Lime                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Lime)}")
        self.LimeGreen           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LimeGreen)}")
        self.LightGreen          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightGreen)}")
        self.PaleGreen           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PaleGreen)}")
        self.DarkSeaGreen        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkSeaGreen)}")
        self.MediumSpringGreen   = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumSpringGreen)}")
        self.SpringGreen         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SpringGreen)}")
        self.SeaGreen            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SeaGreen)}")
        self.MediumAquaMarine    = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumAquaMarine)}")
        self.MediumSeaGreen      = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumSeaGreen)}")
        self.LightSeaGreen       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightSeaGreen)}")
        self.DarkSlateGray       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkSlateGray)}")
        self.Teal                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Teal)}")
        self.DarkCyan            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkCyan)}")
        self.Aqua                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Aqua)}")
        self.Cyan                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Cyan)}")
        self.LightCyan           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightCyan)}")
        self.DarkTurquoise       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkTurquoise)}")
        self.Turquoise           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Turquoise)}")
        self.MediumTurquoise     = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumTurquoise)}")
        self.PaleTurquoise       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PaleTurquoise)}")
        self.AquaMarine          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.AquaMarine)}")
        self.PowderBlue          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PowderBlue)}")
        self.CadetBlue           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.CadetBlue)}")
        self.SteelBlue           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SteelBlue)}")
        self.CornFlowerBlue      = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.CornFlowerBlue)}")
        self.DeepSkyBlue         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DeepSkyBlue)}")
        self.DodgerBlue          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DodgerBlue)}")
        self.LightBlue           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightBlue)}")
        self.SkyBlue             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SkyBlue)}")
        self.LightSkyBlue        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightSkyBlue)}")
        self.MidnightBlue        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MidnightBlue)}")
        self.Navy                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Navy)}")
        self.DarkBlue            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkBlue)}")
        self.MediumBlue          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumBlue)}")
        self.Blue                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Blue)}")
        self.RoyalBlue           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.RoyalBlue)}")
        self.BlueViolet          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.BlueViolet)}")
        self.Indigo              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Indigo)}")
        self.DarkSlateBlue       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkSlateBlue)}")
        self.SlateBlue           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SlateBlue)}")
        self.MediumSlateBlue     = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumSlateBlue)}")
        self.MediumPurple        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumPurple)}")
        self.DarkMagenta         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkMagenta)}")
        self.DarkViolet          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkViolet)}")
        self.DarkOrchid          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkOrchid)}")
        self.MediumOrchid        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumOrchid)}")
        self.Purple              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Purple)}")
        self.Thistle             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Thistle)}")
        self.Plum                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Plum)}")
        self.Violet              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Violet)}")
        self.Magenta             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Magenta)}")
        self.Orchid              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Orchid)}")
        self.MediumVioletRed     = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MediumVioletRed)}")
        self.PaleVioletRed       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PaleVioletRed)}")
        self.DeepPink            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DeepPink)}")
        self.HotPink             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.HotPink)}")
        self.LightPink           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightPink)}")
        self.Pink                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Pink)}")
        self.AntiqueWhite        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.AntiqueWhite)}")
        self.Beige               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Beige)}")
        self.Bisque              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Bisque)}")
        self.BlanchedAlmond      = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.BlanchedAlmond)}")
        self.Wheat               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Wheat)}")
        self.CornSilk            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.CornSilk)}")
        self.LemonChiffon        = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LemonChiffon)}")
        self.LightGoldenRodYellow= ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightGoldenRodYellow)}")
        self.LightYellow         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightYellow)}")
        self.SaddleBrown         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SaddleBrown)}")
        self.Sienna              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Sienna)}")
        self.Chocolate           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Chocolate)}")
        self.Peru                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Peru)}")
        self.SandyBrown          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SandyBrown)}")
        self.BurlyWood           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.BurlyWood)}")
        self.Tan                 = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Tan)}")
        self.RosyBrown           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.RosyBrown)}")
        self.Moccasin            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Moccasin)}")
        self.NavajoWhite         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.NavajoWhite)}")
        self.PeachPuff           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PeachPuff)}")
        self.MistyRose           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MistyRose)}")
        self.LavenderBlush       = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LavenderBlush)}")
        self.Linen               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Linen)}")
        self.OldLace             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.OldLace)}")
        self.PapayaWhip          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.PapayaWhip)}")
        self.WeaShell            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.WeaShell)}")
        self.MintCream           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.MintCream)}")
        self.SlateGray           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.SlateGray)}")
        self.LightSlateGray      = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightSlateGray)}")
        self.LightSteelBlue      = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightSteelBlue)}")
        self.Lavender            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Lavender)}")
        self.FloralWhite         = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.FloralWhite)}")
        self.AliceBlue           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.AliceBlue)}")
        self.GhostWhite          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.GhostWhite)}")
        self.Honeydew            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Honeydew)}")
        self.Ivory               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Ivory)}")
        self.Azure               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Azure)}")
        self.Snow                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Snow)}")
        self.Black               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Black)}")
        self.DimGray             = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DimGray)}")
        self.Gray                = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Gray)}")
        self.DarkGray            = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.DarkGray)}")
        self.Silver              = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Silver)}")
        self.LightGray           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.LightGray)}")
        self.Gainsboro           = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.Gainsboro)}")
        self.WhiteSmoke          = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.WhiteSmoke)}")
        self.White               = ColorSequence(f"{self.param_code}{str(HtmlColorObjects.White)}")

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> str:
        if isinstance(color, (RGB,RGBA,HEX,HEXA)):
            return ColorSequence(f"{self.param_code}{color.r};{color.g};{color.b}")
        elif isinstance(color,HSL):
            r,g,b = hsl_to_rgb(color.h,color.s,color.l)
            return ColorSequence(f"{self.param_code}{r};{g};{b}")
        elif isinstance(color,HSV):
            r,g,b = hsv_to_rgb(color.h,color.s,color.v)
            return ColorSequence(f"{self.param_code}{r};{g};{b}")
        elif isinstance(color,CMYK):
            r,g,b = cmyk_to_rgb(color.c,color.m,color.y,color.k)
            return ColorSequence(f"{self.param_code}{r};{g};{b}")
        else:
            raise ValueError