# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from functools import partialmethod

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX, NormalizeRgb
from AthenaColor.Functions.ANSIsquences import NestedColorSequence
from AthenaColor.Data.HtmlColors import HtmlColorObjects as HtmlColors
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

    # same as custom, but without the Strict Type, as the defined colors are known colors,and are types as RGB values
    def _partialmethod(self,*obj, color:RGB|HEX, **kwargs) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
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
    Maroon              = partialmethod(_partialmethod, color=HtmlColors.Maroon)
    DarkRed             = partialmethod(_partialmethod, color=HtmlColors.DarkRed)
    Brown               = partialmethod(_partialmethod, color=HtmlColors.Brown)
    Firebrick           = partialmethod(_partialmethod, color=HtmlColors.Firebrick)
    Crimson             = partialmethod(_partialmethod, color=HtmlColors.Crimson)
    Red                 = partialmethod(_partialmethod, color=HtmlColors.Red)
    Tomato              = partialmethod(_partialmethod, color=HtmlColors.Tomato)
    Coral               = partialmethod(_partialmethod, color=HtmlColors.Coral)
    IndianRed           = partialmethod(_partialmethod, color=HtmlColors.IndianRed)
    LightCoral          = partialmethod(_partialmethod, color=HtmlColors.LightCoral)
    DarkSalmon          = partialmethod(_partialmethod, color=HtmlColors.DarkSalmon)
    Salmon              = partialmethod(_partialmethod, color=HtmlColors.Salmon)
    LightSalmon         = partialmethod(_partialmethod, color=HtmlColors.LightSalmon)
    OrangeRed           = partialmethod(_partialmethod, color=HtmlColors.OrangeRed)
    DarkOrange          = partialmethod(_partialmethod, color=HtmlColors.DarkOrange)
    Orange              = partialmethod(_partialmethod, color=HtmlColors.Orange)
    Gold                = partialmethod(_partialmethod, color=HtmlColors.Gold)
    DarkGoldenRod       = partialmethod(_partialmethod, color=HtmlColors.DarkGoldenRod)
    GoldenRod           = partialmethod(_partialmethod, color=HtmlColors.GoldenRod)
    PaleGoldenRod       = partialmethod(_partialmethod, color=HtmlColors.PaleGoldenRod)
    DarkKhaki           = partialmethod(_partialmethod, color=HtmlColors.DarkKhaki)
    Khaki               = partialmethod(_partialmethod, color=HtmlColors.Khaki)
    Olive               = partialmethod(_partialmethod, color=HtmlColors.Olive)
    Yellow              = partialmethod(_partialmethod, color=HtmlColors.Yellow)
    YellowGreen         = partialmethod(_partialmethod, color=HtmlColors.YellowGreen)
    DarkOliveGreen      = partialmethod(_partialmethod, color=HtmlColors.DarkOliveGreen)
    OliveDrab           = partialmethod(_partialmethod, color=HtmlColors.OliveDrab)
    LawnGreen           = partialmethod(_partialmethod, color=HtmlColors.LawnGreen)
    Chartreuse          = partialmethod(_partialmethod, color=HtmlColors.Chartreuse)
    GreenYellow         = partialmethod(_partialmethod, color=HtmlColors.GreenYellow)
    DarkGreen           = partialmethod(_partialmethod, color=HtmlColors.DarkGreen)
    Green               = partialmethod(_partialmethod, color=HtmlColors.Green)
    ForestGreen         = partialmethod(_partialmethod, color=HtmlColors.ForestGreen)
    Lime                = partialmethod(_partialmethod, color=HtmlColors.Lime)
    LimeGreen           = partialmethod(_partialmethod, color=HtmlColors.LimeGreen)
    LightGreen          = partialmethod(_partialmethod, color=HtmlColors.LightGreen)
    PaleGreen           = partialmethod(_partialmethod, color=HtmlColors.PaleGreen)
    DarkSeaGreen        = partialmethod(_partialmethod, color=HtmlColors.DarkSeaGreen)
    MediumSpringGreen   = partialmethod(_partialmethod, color=HtmlColors.MediumSpringGreen)
    SpringGreen         = partialmethod(_partialmethod, color=HtmlColors.SpringGreen)
    SeaGreen            = partialmethod(_partialmethod, color=HtmlColors.SeaGreen)
    MediumAquaMarine    = partialmethod(_partialmethod, color=HtmlColors.MediumAquaMarine)
    MediumSeaGreen      = partialmethod(_partialmethod, color=HtmlColors.MediumSeaGreen)
    LightSeaGreen       = partialmethod(_partialmethod, color=HtmlColors.LightSeaGreen)
    DarkSlateGray       = partialmethod(_partialmethod, color=HtmlColors.DarkSlateGray)
    Teal                = partialmethod(_partialmethod, color=HtmlColors.Teal)
    DarkCyan            = partialmethod(_partialmethod, color=HtmlColors.DarkCyan)
    Aqua                = partialmethod(_partialmethod, color=HtmlColors.Aqua)
    Cyan                = partialmethod(_partialmethod, color=HtmlColors.Cyan)
    LightCyan           = partialmethod(_partialmethod, color=HtmlColors.LightCyan)
    DarkTurquoise       = partialmethod(_partialmethod, color=HtmlColors.DarkTurquoise)
    Turquoise           = partialmethod(_partialmethod, color=HtmlColors.Turquoise)
    MediumTurquoise     = partialmethod(_partialmethod, color=HtmlColors.MediumTurquoise)
    PaleTurquoise       = partialmethod(_partialmethod, color=HtmlColors.PaleTurquoise)
    AquaMarine          = partialmethod(_partialmethod, color=HtmlColors.AquaMarine)
    PowderBlue          = partialmethod(_partialmethod, color=HtmlColors.PowderBlue)
    CadetBlue           = partialmethod(_partialmethod, color=HtmlColors.CadetBlue)
    SteelBlue           = partialmethod(_partialmethod, color=HtmlColors.SteelBlue)
    CornFlowerBlue      = partialmethod(_partialmethod, color=HtmlColors.CornFlowerBlue)
    DeepSkyBlue         = partialmethod(_partialmethod, color=HtmlColors.DeepSkyBlue)
    DodgerBlue          = partialmethod(_partialmethod, color=HtmlColors.DodgerBlue)
    LightBlue           = partialmethod(_partialmethod, color=HtmlColors.LightBlue)
    SkyBlue             = partialmethod(_partialmethod, color=HtmlColors.SkyBlue)
    LightSkyBlue        = partialmethod(_partialmethod, color=HtmlColors.LightSkyBlue)
    MidnightBlue        = partialmethod(_partialmethod, color=HtmlColors.MidnightBlue)
    Navy                = partialmethod(_partialmethod, color=HtmlColors.Navy)
    DarkBlue            = partialmethod(_partialmethod, color=HtmlColors.DarkBlue)
    MediumBlue          = partialmethod(_partialmethod, color=HtmlColors.MediumBlue)
    Blue                = partialmethod(_partialmethod, color=HtmlColors.Blue)
    RoyalBlue           = partialmethod(_partialmethod, color=HtmlColors.RoyalBlue)
    BlueViolet          = partialmethod(_partialmethod, color=HtmlColors.BlueViolet)
    Indigo              = partialmethod(_partialmethod, color=HtmlColors.Indigo)
    DarkSlateBlue       = partialmethod(_partialmethod, color=HtmlColors.DarkSlateBlue)
    SlateBlue           = partialmethod(_partialmethod, color=HtmlColors.SlateBlue)
    MediumSlateBlue     = partialmethod(_partialmethod, color=HtmlColors.MediumSlateBlue)
    MediumPurple        = partialmethod(_partialmethod, color=HtmlColors.MediumPurple)
    DarkMagenta         = partialmethod(_partialmethod, color=HtmlColors.DarkMagenta)
    DarkViolet          = partialmethod(_partialmethod, color=HtmlColors.DarkViolet)
    DarkOrchid          = partialmethod(_partialmethod, color=HtmlColors.DarkOrchid)
    MediumOrchid        = partialmethod(_partialmethod, color=HtmlColors.MediumOrchid)
    Purple              = partialmethod(_partialmethod, color=HtmlColors.Purple)
    Thistle             = partialmethod(_partialmethod, color=HtmlColors.Thistle)
    Plum                = partialmethod(_partialmethod, color=HtmlColors.Plum)
    Violet              = partialmethod(_partialmethod, color=HtmlColors.Violet)
    Magenta             = partialmethod(_partialmethod, color=HtmlColors.Magenta)
    Orchid              = partialmethod(_partialmethod, color=HtmlColors.Orchid)
    MediumVioletRed     = partialmethod(_partialmethod, color=HtmlColors.MediumVioletRed)
    PaleVioletRed       = partialmethod(_partialmethod, color=HtmlColors.PaleVioletRed)
    DeepPink            = partialmethod(_partialmethod, color=HtmlColors.DeepPink)
    HotPink             = partialmethod(_partialmethod, color=HtmlColors.HotPink)
    LightPink           = partialmethod(_partialmethod, color=HtmlColors.LightPink)
    Pink                = partialmethod(_partialmethod, color=HtmlColors.Pink)
    AntiqueWhite        = partialmethod(_partialmethod, color=HtmlColors.AntiqueWhite)
    Beige               = partialmethod(_partialmethod, color=HtmlColors.Beige)
    Bisque              = partialmethod(_partialmethod, color=HtmlColors.Bisque)
    BlanchedAlmond      = partialmethod(_partialmethod, color=HtmlColors.BlanchedAlmond)
    Wheat               = partialmethod(_partialmethod, color=HtmlColors.Wheat)
    CornSilk            = partialmethod(_partialmethod, color=HtmlColors.CornSilk)
    LemonChiffon        = partialmethod(_partialmethod, color=HtmlColors.LemonChiffon)
    LightGoldenRodYellow= partialmethod(_partialmethod, color=HtmlColors.LightGoldenRodYellow)
    LightYellow         = partialmethod(_partialmethod, color=HtmlColors.LightYellow)
    SaddleBrown         = partialmethod(_partialmethod, color=HtmlColors.SaddleBrown)
    Sienna              = partialmethod(_partialmethod, color=HtmlColors.Sienna)
    Chocolate           = partialmethod(_partialmethod, color=HtmlColors.Chocolate)
    Peru                = partialmethod(_partialmethod, color=HtmlColors.Peru)
    SandyBrown          = partialmethod(_partialmethod, color=HtmlColors.SandyBrown)
    BurlyWood           = partialmethod(_partialmethod, color=HtmlColors.BurlyWood)
    Tan                 = partialmethod(_partialmethod, color=HtmlColors.Tan)
    RosyBrown           = partialmethod(_partialmethod, color=HtmlColors.RosyBrown)
    Moccasin            = partialmethod(_partialmethod, color=HtmlColors.Moccasin)
    NavajoWhite         = partialmethod(_partialmethod, color=HtmlColors.NavajoWhite)
    PeachPuff           = partialmethod(_partialmethod, color=HtmlColors.PeachPuff)
    MistyRose           = partialmethod(_partialmethod, color=HtmlColors.MistyRose)
    LavenderBlush       = partialmethod(_partialmethod, color=HtmlColors.LavenderBlush)
    Linen               = partialmethod(_partialmethod, color=HtmlColors.Linen)
    OldLace             = partialmethod(_partialmethod, color=HtmlColors.OldLace)
    PapayaWhip          = partialmethod(_partialmethod, color=HtmlColors.PapayaWhip)
    WeaShell            = partialmethod(_partialmethod, color=HtmlColors.WeaShell)
    MintCream           = partialmethod(_partialmethod, color=HtmlColors.MintCream)
    SlateGray           = partialmethod(_partialmethod, color=HtmlColors.SlateGray)
    LightSlateGray      = partialmethod(_partialmethod, color=HtmlColors.LightSlateGray)
    LightSteelBlue      = partialmethod(_partialmethod, color=HtmlColors.LightSteelBlue)
    Lavender            = partialmethod(_partialmethod, color=HtmlColors.Lavender)
    FloralWhite         = partialmethod(_partialmethod, color=HtmlColors.FloralWhite)
    AliceBlue           = partialmethod(_partialmethod, color=HtmlColors.AliceBlue)
    GhostWhite          = partialmethod(_partialmethod, color=HtmlColors.GhostWhite)
    Honeydew            = partialmethod(_partialmethod, color=HtmlColors.Honeydew)
    Ivory               = partialmethod(_partialmethod, color=HtmlColors.Ivory)
    Azure               = partialmethod(_partialmethod, color=HtmlColors.Azure)
    Snow                = partialmethod(_partialmethod, color=HtmlColors.Snow)
    Black               = partialmethod(_partialmethod, color=HtmlColors.Black)
    DimGray             = partialmethod(_partialmethod, color=HtmlColors.DimGray)
    Gray                = partialmethod(_partialmethod, color=HtmlColors.Gray)
    DarkGray            = partialmethod(_partialmethod, color=HtmlColors.DarkGray)
    Silver              = partialmethod(_partialmethod, color=HtmlColors.Silver)
    LightGray           = partialmethod(_partialmethod, color=HtmlColors.LightGray)
    Gainsboro           = partialmethod(_partialmethod, color=HtmlColors.Gainsboro)
    WhiteSmoke          = partialmethod(_partialmethod, color=HtmlColors.WhiteSmoke)
    White               = partialmethod(_partialmethod, color=HtmlColors.White)