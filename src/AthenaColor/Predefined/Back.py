# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects import (
   HtmlColors
)
from AthenaColor.BASE import (
    esc,
    end,
   rgb_controlled
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Back(rgb_controlled):
    _prefix = f"{esc}[48;2;"
    _sufix = end

    Maroon               = f"{_prefix}{HtmlColors.Maroon                 }{_sufix}"
    DarkRed              = f"{_prefix}{HtmlColors.DarkRed                }{_sufix}"
    Brown                = f"{_prefix}{HtmlColors.Brown                  }{_sufix}"
    Firebrick            = f"{_prefix}{HtmlColors.Firebrick              }{_sufix}"
    Crimson              = f"{_prefix}{HtmlColors.Crimson                }{_sufix}"
    Red                  = f"{_prefix}{HtmlColors.Red                    }{_sufix}"
    Tomato               = f"{_prefix}{HtmlColors.Tomato                 }{_sufix}"
    Coral                = f"{_prefix}{HtmlColors.Coral                  }{_sufix}"
    IndianRed            = f"{_prefix}{HtmlColors.IndianRed              }{_sufix}"
    LightCoral           = f"{_prefix}{HtmlColors.LightCoral             }{_sufix}"
    DarkSalmon           = f"{_prefix}{HtmlColors.DarkSalmon             }{_sufix}"
    Salmon               = f"{_prefix}{HtmlColors.Salmon                 }{_sufix}"
    LightSalmon          = f"{_prefix}{HtmlColors.LightSalmon            }{_sufix}"
    OrangeRed            = f"{_prefix}{HtmlColors.OrangeRed              }{_sufix}"
    DarkOrange           = f"{_prefix}{HtmlColors.DarkOrange             }{_sufix}"
    Orange               = f"{_prefix}{HtmlColors.Orange                 }{_sufix}"
    Gold                 = f"{_prefix}{HtmlColors.Gold                   }{_sufix}"
    DarkGoldenRod        = f"{_prefix}{HtmlColors.DarkGoldenRod          }{_sufix}"
    GoldenRod            = f"{_prefix}{HtmlColors.GoldenRod              }{_sufix}"
    PaleGoldenRod        = f"{_prefix}{HtmlColors.PaleGoldenRod          }{_sufix}"
    DarkKhaki            = f"{_prefix}{HtmlColors.DarkKhaki              }{_sufix}"
    Khaki                = f"{_prefix}{HtmlColors.Khaki                  }{_sufix}"
    Olive                = f"{_prefix}{HtmlColors.Olive                  }{_sufix}"
    Yellow               = f"{_prefix}{HtmlColors.Yellow                 }{_sufix}"
    YellowGreen          = f"{_prefix}{HtmlColors.YellowGreen            }{_sufix}"
    DarkOliveGreen       = f"{_prefix}{HtmlColors.DarkOliveGreen         }{_sufix}"
    OliveDrab            = f"{_prefix}{HtmlColors.OliveDrab              }{_sufix}"
    LawnGreen            = f"{_prefix}{HtmlColors.LawnGreen              }{_sufix}"
    Chartreuse           = f"{_prefix}{HtmlColors.Chartreuse             }{_sufix}"
    GreenYellow          = f"{_prefix}{HtmlColors.GreenYellow            }{_sufix}"
    DarkGreen            = f"{_prefix}{HtmlColors.DarkGreen              }{_sufix}"
    Green                = f"{_prefix}{HtmlColors.Green                  }{_sufix}"
    ForestGreen          = f"{_prefix}{HtmlColors.ForestGreen            }{_sufix}"
    Lime                 = f"{_prefix}{HtmlColors.Lime                   }{_sufix}"
    LimeGreen            = f"{_prefix}{HtmlColors.LimeGreen              }{_sufix}"
    LightGreen           = f"{_prefix}{HtmlColors.LightGreen             }{_sufix}"
    PaleGreen            = f"{_prefix}{HtmlColors.PaleGreen              }{_sufix}"
    DarkSeaGreen         = f"{_prefix}{HtmlColors.DarkSeaGreen           }{_sufix}"
    MediumSpringGreen    = f"{_prefix}{HtmlColors.MediumSpringGreen      }{_sufix}"
    SpringGreen          = f"{_prefix}{HtmlColors.SpringGreen            }{_sufix}"
    SeaGreen             = f"{_prefix}{HtmlColors.SeaGreen               }{_sufix}"
    MediumAquaMarine     = f"{_prefix}{HtmlColors.MediumAquaMarine       }{_sufix}"
    MediumSeaGreen       = f"{_prefix}{HtmlColors.MediumSeaGreen         }{_sufix}"
    LightSeaGreen        = f"{_prefix}{HtmlColors.LightSeaGreen          }{_sufix}"
    DarkSlateGray        = f"{_prefix}{HtmlColors.DarkSlateGray          }{_sufix}"
    Teal                 = f"{_prefix}{HtmlColors.Teal                   }{_sufix}"
    DarkCyan             = f"{_prefix}{HtmlColors.DarkCyan               }{_sufix}"
    Aqua                 = f"{_prefix}{HtmlColors.Aqua                   }{_sufix}"
    Cyan                 = f"{_prefix}{HtmlColors.Cyan                   }{_sufix}"
    LightCyan            = f"{_prefix}{HtmlColors.LightCyan              }{_sufix}"
    DarkTurquoise        = f"{_prefix}{HtmlColors.DarkTurquoise          }{_sufix}"
    Turquoise            = f"{_prefix}{HtmlColors.Turquoise              }{_sufix}"
    MediumTurquoise      = f"{_prefix}{HtmlColors.MediumTurquoise        }{_sufix}"
    PaleTurquoise        = f"{_prefix}{HtmlColors.PaleTurquoise          }{_sufix}"
    AquaMarine           = f"{_prefix}{HtmlColors.AquaMarine             }{_sufix}"
    PowderBlue           = f"{_prefix}{HtmlColors.PowderBlue             }{_sufix}"
    CadetBlue            = f"{_prefix}{HtmlColors.CadetBlue              }{_sufix}"
    SteelBlue            = f"{_prefix}{HtmlColors.SteelBlue              }{_sufix}"
    CornFlowerBlue       = f"{_prefix}{HtmlColors.CornFlowerBlue         }{_sufix}"
    DeepSkyBlue          = f"{_prefix}{HtmlColors.DeepSkyBlue            }{_sufix}"
    DodgerBlue           = f"{_prefix}{HtmlColors.DodgerBlue             }{_sufix}"
    LightBlue            = f"{_prefix}{HtmlColors.LightBlue              }{_sufix}"
    SkyBlue              = f"{_prefix}{HtmlColors.SkyBlue                }{_sufix}"
    LightSkyBlue         = f"{_prefix}{HtmlColors.LightSkyBlue           }{_sufix}"
    MidnightBlue         = f"{_prefix}{HtmlColors.MidnightBlue           }{_sufix}"
    Navy                 = f"{_prefix}{HtmlColors.Navy                   }{_sufix}"
    DarkBlue             = f"{_prefix}{HtmlColors.DarkBlue               }{_sufix}"
    MediumBlue           = f"{_prefix}{HtmlColors.MediumBlue             }{_sufix}"
    Blue                 = f"{_prefix}{HtmlColors.Blue                   }{_sufix}"
    RoyalBlue            = f"{_prefix}{HtmlColors.RoyalBlue              }{_sufix}"
    BlueViolet           = f"{_prefix}{HtmlColors.BlueViolet             }{_sufix}"
    Indigo               = f"{_prefix}{HtmlColors.Indigo                 }{_sufix}"
    DarkSlateBlue        = f"{_prefix}{HtmlColors.DarkSlateBlue          }{_sufix}"
    SlateBlue            = f"{_prefix}{HtmlColors.SlateBlue              }{_sufix}"
    MediumSlateBlue      = f"{_prefix}{HtmlColors.MediumSlateBlue        }{_sufix}"
    MediumPurple         = f"{_prefix}{HtmlColors.MediumPurple           }{_sufix}"
    DarkMagenta          = f"{_prefix}{HtmlColors.DarkMagenta            }{_sufix}"
    DarkViolet           = f"{_prefix}{HtmlColors.DarkViolet             }{_sufix}"
    DarkOrchid           = f"{_prefix}{HtmlColors.DarkOrchid             }{_sufix}"
    MediumOrchid         = f"{_prefix}{HtmlColors.MediumOrchid           }{_sufix}"
    Purple               = f"{_prefix}{HtmlColors.Purple                 }{_sufix}"
    Thistle              = f"{_prefix}{HtmlColors.Thistle                }{_sufix}"
    Plum                 = f"{_prefix}{HtmlColors.Plum                   }{_sufix}"
    Violet               = f"{_prefix}{HtmlColors.Violet                 }{_sufix}"
    Magenta              = f"{_prefix}{HtmlColors.Magenta                }{_sufix}"
    Orchid               = f"{_prefix}{HtmlColors.Orchid                 }{_sufix}"
    MediumVioletRed      = f"{_prefix}{HtmlColors.MediumVioletRed        }{_sufix}"
    PaleVioletRed        = f"{_prefix}{HtmlColors.PaleVioletRed          }{_sufix}"
    DeepPink             = f"{_prefix}{HtmlColors.DeepPink               }{_sufix}"
    HotPink              = f"{_prefix}{HtmlColors.HotPink                }{_sufix}"
    LightPink            = f"{_prefix}{HtmlColors.LightPink              }{_sufix}"
    Pink                 = f"{_prefix}{HtmlColors.Pink                   }{_sufix}"
    AntiqueWhite         = f"{_prefix}{HtmlColors.AntiqueWhite           }{_sufix}"
    Beige                = f"{_prefix}{HtmlColors.Beige                  }{_sufix}"
    Bisque               = f"{_prefix}{HtmlColors.Bisque                 }{_sufix}"
    BlanchedAlmond	    = f"{_prefix}{HtmlColors.BlanchedAlmond	        }{_sufix}"
    Wheat                = f"{_prefix}{HtmlColors.Wheat                  }{_sufix}"
    CornSilk             = f"{_prefix}{HtmlColors.CornSilk               }{_sufix}"
    LemonChiffon         = f"{_prefix}{HtmlColors.LemonChiffon           }{_sufix}"
    LightGoldenRodYellow = f"{_prefix}{HtmlColors.LightGoldenRodYellow   }{_sufix}"
    LightYellow          = f"{_prefix}{HtmlColors.LightYellow            }{_sufix}"
    SaddleBrown          = f"{_prefix}{HtmlColors.SaddleBrown            }{_sufix}"
    Sienna               = f"{_prefix}{HtmlColors.Sienna                 }{_sufix}"
    Chocolate            = f"{_prefix}{HtmlColors.Chocolate              }{_sufix}"
    Peru                 = f"{_prefix}{HtmlColors.Peru                   }{_sufix}"
    SandyBrown           = f"{_prefix}{HtmlColors.SandyBrown             }{_sufix}"
    BurlyWood            = f"{_prefix}{HtmlColors.BurlyWood              }{_sufix}"
    Tan                  = f"{_prefix}{HtmlColors.Tan                    }{_sufix}"
    RosyBrown            = f"{_prefix}{HtmlColors.RosyBrown              }{_sufix}"
    Moccasin             = f"{_prefix}{HtmlColors.Moccasin               }{_sufix}"
    NavajoWhite          = f"{_prefix}{HtmlColors.NavajoWhite            }{_sufix}"
    PeachPuff            = f"{_prefix}{HtmlColors.PeachPuff              }{_sufix}"
    MistyRose            = f"{_prefix}{HtmlColors.MistyRose              }{_sufix}"
    LavenderBlush        = f"{_prefix}{HtmlColors.LavenderBlush          }{_sufix}"
    Linen                = f"{_prefix}{HtmlColors.Linen                  }{_sufix}"
    OldLace              = f"{_prefix}{HtmlColors.OldLace                }{_sufix}"
    PapayaWhip           = f"{_prefix}{HtmlColors.PapayaWhip             }{_sufix}"
    WeaShell             = f"{_prefix}{HtmlColors.WeaShell               }{_sufix}"
    MintCream            = f"{_prefix}{HtmlColors.MintCream              }{_sufix}"
    SlateGray            = f"{_prefix}{HtmlColors.SlateGray              }{_sufix}"
    LightSlateGray       = f"{_prefix}{HtmlColors.LightSlateGray         }{_sufix}"
    LightSteelBlue       = f"{_prefix}{HtmlColors.LightSteelBlue         }{_sufix}"
    Lavender             = f"{_prefix}{HtmlColors.Lavender               }{_sufix}"
    FloralWhite          = f"{_prefix}{HtmlColors.FloralWhite            }{_sufix}"
    AliceBlue            = f"{_prefix}{HtmlColors.AliceBlue              }{_sufix}"
    GhostWhite           = f"{_prefix}{HtmlColors.GhostWhite             }{_sufix}"
    Honeydew             = f"{_prefix}{HtmlColors.Honeydew               }{_sufix}"
    Ivory                = f"{_prefix}{HtmlColors.Ivory                  }{_sufix}"
    Azure                = f"{_prefix}{HtmlColors.Azure                  }{_sufix}"
    Snow                 = f"{_prefix}{HtmlColors.Snow                   }{_sufix}"
    Black                = f"{_prefix}{HtmlColors.Black                  }{_sufix}"
    DimGray              = f"{_prefix}{HtmlColors.DimGray                }{_sufix}"
    Gray	                = f"{_prefix}{HtmlColors.Gray	                }{_sufix}"
    DarkGray	            = f"{_prefix}{HtmlColors.DarkGray	            }{_sufix}"
    Silver	            = f"{_prefix}{HtmlColors.Silver	                }{_sufix}"
    LightGray	        = f"{_prefix}{HtmlColors.LightGray	            }{_sufix}"
    Gainsboro            = f"{_prefix}{HtmlColors.Gainsboro              }{_sufix}"
    WhiteSmoke           = f"{_prefix}{HtmlColors.WhiteSmoke             }{_sufix}"
    White                = f"{_prefix}{HtmlColors.White                  }{_sufix}"