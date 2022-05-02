# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from functools import partialmethod

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX
from AthenaColor.Functions.AnsiSquences import NestedColorSequence
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

    def rgb(self,*obj, r:int,g:int,b:int, **kwargs) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        color =  RGB(r, g, b)
        return NestedColorSequence(
            *obj,
            control_code=f"{self._param_code}{color.r};{color.g};{color.b}",
            reset_code=self._reset,
            **kwargs
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    Maroon              = partialmethod(custom, color=HtmlColors.Maroon)
    DarkRed             = partialmethod(custom, color=HtmlColors.DarkRed)
    Brown               = partialmethod(custom, color=HtmlColors.Brown)
    Firebrick           = partialmethod(custom, color=HtmlColors.Firebrick)
    Crimson             = partialmethod(custom, color=HtmlColors.Crimson)
    Red                 = partialmethod(custom, color=HtmlColors.Red)
    Tomato              = partialmethod(custom, color=HtmlColors.Tomato)
    Coral               = partialmethod(custom, color=HtmlColors.Coral)
    IndianRed           = partialmethod(custom, color=HtmlColors.IndianRed)
    LightCoral          = partialmethod(custom, color=HtmlColors.LightCoral)
    DarkSalmon          = partialmethod(custom, color=HtmlColors.DarkSalmon)
    Salmon              = partialmethod(custom, color=HtmlColors.Salmon)
    LightSalmon         = partialmethod(custom, color=HtmlColors.LightSalmon)
    OrangeRed           = partialmethod(custom, color=HtmlColors.OrangeRed)
    DarkOrange          = partialmethod(custom, color=HtmlColors.DarkOrange)
    Orange              = partialmethod(custom, color=HtmlColors.Orange)
    Gold                = partialmethod(custom, color=HtmlColors.Gold)
    DarkGoldenRod       = partialmethod(custom, color=HtmlColors.DarkGoldenRod)
    GoldenRod           = partialmethod(custom, color=HtmlColors.GoldenRod)
    PaleGoldenRod       = partialmethod(custom, color=HtmlColors.PaleGoldenRod)
    DarkKhaki           = partialmethod(custom, color=HtmlColors.DarkKhaki)
    Khaki               = partialmethod(custom, color=HtmlColors.Khaki)
    Olive               = partialmethod(custom, color=HtmlColors.Olive)
    Yellow              = partialmethod(custom, color=HtmlColors.Yellow)
    YellowGreen         = partialmethod(custom, color=HtmlColors.YellowGreen)
    DarkOliveGreen      = partialmethod(custom, color=HtmlColors.DarkOliveGreen)
    OliveDrab           = partialmethod(custom, color=HtmlColors.OliveDrab)
    LawnGreen           = partialmethod(custom, color=HtmlColors.LawnGreen)
    Chartreuse          = partialmethod(custom, color=HtmlColors.Chartreuse)
    GreenYellow         = partialmethod(custom, color=HtmlColors.GreenYellow)
    DarkGreen           = partialmethod(custom, color=HtmlColors.DarkGreen)
    Green               = partialmethod(custom, color=HtmlColors.Green)
    ForestGreen         = partialmethod(custom, color=HtmlColors.ForestGreen)
    Lime                = partialmethod(custom, color=HtmlColors.Lime)
    LimeGreen           = partialmethod(custom, color=HtmlColors.LimeGreen)
    LightGreen          = partialmethod(custom, color=HtmlColors.LightGreen)
    PaleGreen           = partialmethod(custom, color=HtmlColors.PaleGreen)
    DarkSeaGreen        = partialmethod(custom, color=HtmlColors.DarkSeaGreen)
    MediumSpringGreen   = partialmethod(custom, color=HtmlColors.MediumSpringGreen)
    SpringGreen         = partialmethod(custom, color=HtmlColors.SpringGreen)
    SeaGreen            = partialmethod(custom, color=HtmlColors.SeaGreen)
    MediumAquaMarine    = partialmethod(custom, color=HtmlColors.MediumAquaMarine)
    MediumSeaGreen      = partialmethod(custom, color=HtmlColors.MediumSeaGreen)
    LightSeaGreen       = partialmethod(custom, color=HtmlColors.LightSeaGreen)
    DarkSlateGray       = partialmethod(custom, color=HtmlColors.DarkSlateGray)
    Teal                = partialmethod(custom, color=HtmlColors.Teal)
    DarkCyan            = partialmethod(custom, color=HtmlColors.DarkCyan)
    Aqua                = partialmethod(custom, color=HtmlColors.Aqua)
    Cyan                = partialmethod(custom, color=HtmlColors.Cyan)
    LightCyan           = partialmethod(custom, color=HtmlColors.LightCyan)
    DarkTurquoise       = partialmethod(custom, color=HtmlColors.DarkTurquoise)
    Turquoise           = partialmethod(custom, color=HtmlColors.Turquoise)
    MediumTurquoise     = partialmethod(custom, color=HtmlColors.MediumTurquoise)
    PaleTurquoise       = partialmethod(custom, color=HtmlColors.PaleTurquoise)
    AquaMarine          = partialmethod(custom, color=HtmlColors.AquaMarine)
    PowderBlue          = partialmethod(custom, color=HtmlColors.PowderBlue)
    CadetBlue           = partialmethod(custom, color=HtmlColors.CadetBlue)
    SteelBlue           = partialmethod(custom, color=HtmlColors.SteelBlue)
    CornFlowerBlue      = partialmethod(custom, color=HtmlColors.CornFlowerBlue)
    DeepSkyBlue         = partialmethod(custom, color=HtmlColors.DeepSkyBlue)
    DodgerBlue          = partialmethod(custom, color=HtmlColors.DodgerBlue)
    LightBlue           = partialmethod(custom, color=HtmlColors.LightBlue)
    SkyBlue             = partialmethod(custom, color=HtmlColors.SkyBlue)
    LightSkyBlue        = partialmethod(custom, color=HtmlColors.LightSkyBlue)
    MidnightBlue        = partialmethod(custom, color=HtmlColors.MidnightBlue)
    Navy                = partialmethod(custom, color=HtmlColors.Navy)
    DarkBlue            = partialmethod(custom, color=HtmlColors.DarkBlue)
    MediumBlue          = partialmethod(custom, color=HtmlColors.MediumBlue)
    Blue                = partialmethod(custom, color=HtmlColors.Blue)
    RoyalBlue           = partialmethod(custom, color=HtmlColors.RoyalBlue)
    BlueViolet          = partialmethod(custom, color=HtmlColors.BlueViolet)
    Indigo              = partialmethod(custom, color=HtmlColors.Indigo)
    DarkSlateBlue       = partialmethod(custom, color=HtmlColors.DarkSlateBlue)
    SlateBlue           = partialmethod(custom, color=HtmlColors.SlateBlue)
    MediumSlateBlue     = partialmethod(custom, color=HtmlColors.MediumSlateBlue)
    MediumPurple        = partialmethod(custom, color=HtmlColors.MediumPurple)
    DarkMagenta         = partialmethod(custom, color=HtmlColors.DarkMagenta)
    DarkViolet          = partialmethod(custom, color=HtmlColors.DarkViolet)
    DarkOrchid          = partialmethod(custom, color=HtmlColors.DarkOrchid)
    MediumOrchid        = partialmethod(custom, color=HtmlColors.MediumOrchid)
    Purple              = partialmethod(custom, color=HtmlColors.Purple)
    Thistle             = partialmethod(custom, color=HtmlColors.Thistle)
    Plum                = partialmethod(custom, color=HtmlColors.Plum)
    Violet              = partialmethod(custom, color=HtmlColors.Violet)
    Magenta             = partialmethod(custom, color=HtmlColors.Magenta)
    Orchid              = partialmethod(custom, color=HtmlColors.Orchid)
    MediumVioletRed     = partialmethod(custom, color=HtmlColors.MediumVioletRed)
    PaleVioletRed       = partialmethod(custom, color=HtmlColors.PaleVioletRed)
    DeepPink            = partialmethod(custom, color=HtmlColors.DeepPink)
    HotPink             = partialmethod(custom, color=HtmlColors.HotPink)
    LightPink           = partialmethod(custom, color=HtmlColors.LightPink)
    Pink                = partialmethod(custom, color=HtmlColors.Pink)
    AntiqueWhite        = partialmethod(custom, color=HtmlColors.AntiqueWhite)
    Beige               = partialmethod(custom, color=HtmlColors.Beige)
    Bisque              = partialmethod(custom, color=HtmlColors.Bisque)
    BlanchedAlmond      = partialmethod(custom, color=HtmlColors.BlanchedAlmond)
    Wheat               = partialmethod(custom, color=HtmlColors.Wheat)
    CornSilk            = partialmethod(custom, color=HtmlColors.CornSilk)
    LemonChiffon        = partialmethod(custom, color=HtmlColors.LemonChiffon)
    LightGoldenRodYellow= partialmethod(custom, color=HtmlColors.LightGoldenRodYellow)
    LightYellow         = partialmethod(custom, color=HtmlColors.LightYellow)
    SaddleBrown         = partialmethod(custom, color=HtmlColors.SaddleBrown)
    Sienna              = partialmethod(custom, color=HtmlColors.Sienna)
    Chocolate           = partialmethod(custom, color=HtmlColors.Chocolate)
    Peru                = partialmethod(custom, color=HtmlColors.Peru)
    SandyBrown          = partialmethod(custom, color=HtmlColors.SandyBrown)
    BurlyWood           = partialmethod(custom, color=HtmlColors.BurlyWood)
    Tan                 = partialmethod(custom, color=HtmlColors.Tan)
    RosyBrown           = partialmethod(custom, color=HtmlColors.RosyBrown)
    Moccasin            = partialmethod(custom, color=HtmlColors.Moccasin)
    NavajoWhite         = partialmethod(custom, color=HtmlColors.NavajoWhite)
    PeachPuff           = partialmethod(custom, color=HtmlColors.PeachPuff)
    MistyRose           = partialmethod(custom, color=HtmlColors.MistyRose)
    LavenderBlush       = partialmethod(custom, color=HtmlColors.LavenderBlush)
    Linen               = partialmethod(custom, color=HtmlColors.Linen)
    OldLace             = partialmethod(custom, color=HtmlColors.OldLace)
    PapayaWhip          = partialmethod(custom, color=HtmlColors.PapayaWhip)
    WeaShell            = partialmethod(custom, color=HtmlColors.WeaShell)
    MintCream           = partialmethod(custom, color=HtmlColors.MintCream)
    SlateGray           = partialmethod(custom, color=HtmlColors.SlateGray)
    LightSlateGray      = partialmethod(custom, color=HtmlColors.LightSlateGray)
    LightSteelBlue      = partialmethod(custom, color=HtmlColors.LightSteelBlue)
    Lavender            = partialmethod(custom, color=HtmlColors.Lavender)
    FloralWhite         = partialmethod(custom, color=HtmlColors.FloralWhite)
    AliceBlue           = partialmethod(custom, color=HtmlColors.AliceBlue)
    GhostWhite          = partialmethod(custom, color=HtmlColors.GhostWhite)
    Honeydew            = partialmethod(custom, color=HtmlColors.Honeydew)
    Ivory               = partialmethod(custom, color=HtmlColors.Ivory)
    Azure               = partialmethod(custom, color=HtmlColors.Azure)
    Snow                = partialmethod(custom, color=HtmlColors.Snow)
    Black               = partialmethod(custom, color=HtmlColors.Black)
    DimGray             = partialmethod(custom, color=HtmlColors.DimGray)
    Gray                = partialmethod(custom, color=HtmlColors.Gray)
    DarkGray            = partialmethod(custom, color=HtmlColors.DarkGray)
    Silver              = partialmethod(custom, color=HtmlColors.Silver)
    LightGray           = partialmethod(custom, color=HtmlColors.LightGray)
    Gainsboro           = partialmethod(custom, color=HtmlColors.Gainsboro)
    WhiteSmoke          = partialmethod(custom, color=HtmlColors.WhiteSmoke)
    White               = partialmethod(custom, color=HtmlColors.White)