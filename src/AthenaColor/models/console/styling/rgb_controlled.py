# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.models.color_system import RGB, RGBA, HEX, HEXA, HSV, HSL, CMYK
from AthenaColor.functions.color_tuple_conversion import cmyk_to_rgb,hsv_to_rgb,hsl_to_rgb
from AthenaColor.functions.ansi_sequences import color_sequence
from AthenaColor.data.colors_html import HtmlColorObjects

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
        self.Maroon              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Maroon)}")
        self.DarkRed             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkRed)}")
        self.Brown               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Brown)}")
        self.Firebrick           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Firebrick)}")
        self.Crimson             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Crimson)}")
        self.Red                 = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Red)}")
        self.Tomato              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Tomato)}")
        self.Coral               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Coral)}")
        self.IndianRed           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.IndianRed)}")
        self.LightCoral          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightCoral)}")
        self.DarkSalmon          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkSalmon)}")
        self.Salmon              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Salmon)}")
        self.LightSalmon         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightSalmon)}")
        self.OrangeRed           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.OrangeRed)}")
        self.DarkOrange          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkOrange)}")
        self.Orange              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Orange)}")
        self.Gold                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Gold)}")
        self.DarkGoldenRod       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkGoldenRod)}")
        self.GoldenRod           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.GoldenRod)}")
        self.PaleGoldenRod       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PaleGoldenRod)}")
        self.DarkKhaki           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkKhaki)}")
        self.Khaki               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Khaki)}")
        self.Olive               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Olive)}")
        self.Yellow              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Yellow)}")
        self.YellowGreen         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.YellowGreen)}")
        self.DarkOliveGreen      = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkOliveGreen)}")
        self.OliveDrab           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.OliveDrab)}")
        self.LawnGreen           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LawnGreen)}")
        self.Chartreuse          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Chartreuse)}")
        self.GreenYellow         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.GreenYellow)}")
        self.DarkGreen           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkGreen)}")
        self.Green               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Green)}")
        self.ForestGreen         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.ForestGreen)}")
        self.Lime                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Lime)}")
        self.LimeGreen           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LimeGreen)}")
        self.LightGreen          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightGreen)}")
        self.PaleGreen           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PaleGreen)}")
        self.DarkSeaGreen        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkSeaGreen)}")
        self.MediumSpringGreen   = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumSpringGreen)}")
        self.SpringGreen         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SpringGreen)}")
        self.SeaGreen            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SeaGreen)}")
        self.MediumAquaMarine    = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumAquaMarine)}")
        self.MediumSeaGreen      = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumSeaGreen)}")
        self.LightSeaGreen       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightSeaGreen)}")
        self.DarkSlateGray       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkSlateGray)}")
        self.Teal                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Teal)}")
        self.DarkCyan            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkCyan)}")
        self.Aqua                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Aqua)}")
        self.Cyan                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Cyan)}")
        self.LightCyan           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightCyan)}")
        self.DarkTurquoise       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkTurquoise)}")
        self.Turquoise           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Turquoise)}")
        self.MediumTurquoise     = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumTurquoise)}")
        self.PaleTurquoise       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PaleTurquoise)}")
        self.AquaMarine          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.AquaMarine)}")
        self.PowderBlue          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PowderBlue)}")
        self.CadetBlue           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.CadetBlue)}")
        self.SteelBlue           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SteelBlue)}")
        self.CornFlowerBlue      = color_sequence(f"{self.param_code}{str(HtmlColorObjects.CornFlowerBlue)}")
        self.DeepSkyBlue         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DeepSkyBlue)}")
        self.DodgerBlue          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DodgerBlue)}")
        self.LightBlue           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightBlue)}")
        self.SkyBlue             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SkyBlue)}")
        self.LightSkyBlue        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightSkyBlue)}")
        self.MidnightBlue        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MidnightBlue)}")
        self.Navy                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Navy)}")
        self.DarkBlue            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkBlue)}")
        self.MediumBlue          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumBlue)}")
        self.Blue                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Blue)}")
        self.RoyalBlue           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.RoyalBlue)}")
        self.BlueViolet          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.BlueViolet)}")
        self.Indigo              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Indigo)}")
        self.DarkSlateBlue       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkSlateBlue)}")
        self.SlateBlue           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SlateBlue)}")
        self.MediumSlateBlue     = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumSlateBlue)}")
        self.MediumPurple        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumPurple)}")
        self.DarkMagenta         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkMagenta)}")
        self.DarkViolet          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkViolet)}")
        self.DarkOrchid          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkOrchid)}")
        self.MediumOrchid        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumOrchid)}")
        self.Purple              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Purple)}")
        self.Thistle             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Thistle)}")
        self.Plum                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Plum)}")
        self.Violet              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Violet)}")
        self.Magenta             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Magenta)}")
        self.Orchid              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Orchid)}")
        self.MediumVioletRed     = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MediumVioletRed)}")
        self.PaleVioletRed       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PaleVioletRed)}")
        self.DeepPink            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DeepPink)}")
        self.HotPink             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.HotPink)}")
        self.LightPink           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightPink)}")
        self.Pink                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Pink)}")
        self.AntiqueWhite        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.AntiqueWhite)}")
        self.Beige               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Beige)}")
        self.Bisque              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Bisque)}")
        self.BlanchedAlmond      = color_sequence(f"{self.param_code}{str(HtmlColorObjects.BlanchedAlmond)}")
        self.Wheat               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Wheat)}")
        self.CornSilk            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.CornSilk)}")
        self.LemonChiffon        = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LemonChiffon)}")
        self.LightGoldenRodYellow= color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightGoldenRodYellow)}")
        self.LightYellow         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightYellow)}")
        self.SaddleBrown         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SaddleBrown)}")
        self.Sienna              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Sienna)}")
        self.Chocolate           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Chocolate)}")
        self.Peru                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Peru)}")
        self.SandyBrown          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SandyBrown)}")
        self.BurlyWood           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.BurlyWood)}")
        self.Tan                 = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Tan)}")
        self.RosyBrown           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.RosyBrown)}")
        self.Moccasin            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Moccasin)}")
        self.NavajoWhite         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.NavajoWhite)}")
        self.PeachPuff           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PeachPuff)}")
        self.MistyRose           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MistyRose)}")
        self.LavenderBlush       = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LavenderBlush)}")
        self.Linen               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Linen)}")
        self.OldLace             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.OldLace)}")
        self.PapayaWhip          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.PapayaWhip)}")
        self.WeaShell            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.WeaShell)}")
        self.MintCream           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.MintCream)}")
        self.SlateGray           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.SlateGray)}")
        self.LightSlateGray      = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightSlateGray)}")
        self.LightSteelBlue      = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightSteelBlue)}")
        self.Lavender            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Lavender)}")
        self.FloralWhite         = color_sequence(f"{self.param_code}{str(HtmlColorObjects.FloralWhite)}")
        self.AliceBlue           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.AliceBlue)}")
        self.GhostWhite          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.GhostWhite)}")
        self.Honeydew            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Honeydew)}")
        self.Ivory               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Ivory)}")
        self.Azure               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Azure)}")
        self.Snow                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Snow)}")
        self.Black               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Black)}")
        self.DimGray             = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DimGray)}")
        self.Gray                = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Gray)}")
        self.DarkGray            = color_sequence(f"{self.param_code}{str(HtmlColorObjects.DarkGray)}")
        self.Silver              = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Silver)}")
        self.LightGray           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.LightGray)}")
        self.Gainsboro           = color_sequence(f"{self.param_code}{str(HtmlColorObjects.Gainsboro)}")
        self.WhiteSmoke          = color_sequence(f"{self.param_code}{str(HtmlColorObjects.WhiteSmoke)}")
        self.White               = color_sequence(f"{self.param_code}{str(HtmlColorObjects.White)}")

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA) -> str:
        if isinstance(color, (RGB,RGBA,HEX,HEXA)):
            return color_sequence(f"{self.param_code}{color.r};{color.g};{color.b}")
        elif isinstance(color,HSL):
            r,g,b = hsl_to_rgb(color.h,color.s,color.l)
            return color_sequence(f"{self.param_code}{r};{g};{b}")
        elif isinstance(color,HSV):
            r,g,b = hsv_to_rgb(color.h,color.s,color.v)
            return color_sequence(f"{self.param_code}{r};{g};{b}")
        elif isinstance(color,CMYK):
            r,g,b = cmyk_to_rgb(color.c,color.m,color.y,color.k)
            return color_sequence(f"{self.param_code}{r};{g};{b}")
        else:
            raise ValueError