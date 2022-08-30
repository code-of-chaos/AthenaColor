# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.func.ansi_sequences import color_sequence
import AthenaColor.data.colors_html as HtmlColorObjects

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlled:
    __name__ = "RgbControlled"
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
        self.Maroon = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MAROON))}"
        )
        self.DarkRed = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKRED))}"
        )
        self.Brown = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BROWN))}"
        )
        self.Firebrick = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.FIREBRICK))}"
        )
        self.Crimson = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CRIMSON))}"
        )
        self.Red = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.RED))}"
        )
        self.Tomato = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.TOMATO))}"
        )
        self.Coral = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CORAL))}"
        )
        self.IndianRed = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.INDIANRED))}"
        )
        self.LightCoral = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTCORAL))}"
        )
        self.DarkSalmon = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKSALMON))}"
        )
        self.Salmon = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SALMON))}"
        )
        self.LightSalmon = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTSALMON))}"
        )
        self.OrangeRed = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ORANGERED))}"
        )
        self.DarkOrange = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKORANGE))}"
        )
        self.Orange = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ORANGE))}"
        )
        self.Gold = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GOLD))}"
        )
        self.DarkGoldenRod = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKGOLDENROD))}"
        )
        self.GoldenRod = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GOLDENROD))}"
        )
        self.PaleGoldenRod = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PALEGOLDENROD))}"
        )
        self.DarkKhaki = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKKHAKI))}"
        )
        self.Khaki = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.KHAKI))}"
        )
        self.Olive = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.OLIVE))}"
        )
        self.Yellow = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.YELLOW))}"
        )
        self.YellowGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.YELLOWGREEN))}"
        )
        self.DarkOliveGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKOLIVEGREEN))}"
        )
        self.OliveDrab = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.OLIVEDRAB))}"
        )
        self.LawnGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LAWNGREEN))}"
        )
        self.Chartreuse = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CHARTREUSE))}"
        )
        self.GreenYellow = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GREENYELLOW))}"
        )
        self.DarkGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKGREEN))}"
        )
        self.Green = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GREEN))}"
        )
        self.ForestGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.FORESTGREEN))}"
        )
        self.Lime = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIME))}"
        )
        self.LimeGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIMEGREEN))}"
        )
        self.LightGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTGREEN))}"
        )
        self.PaleGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PALEGREEN))}"
        )
        self.DarkSeaGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKSEAGREEN))}"
        )
        self.MediumSpringGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMSPRINGGREEN))}"
        )
        self.SpringGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SPRINGGREEN))}"
        )
        self.SeaGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SEAGREEN))}"
        )
        self.MediumAquaMarine = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMAQUAMARINE))}"
        )
        self.MediumSeaGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMSEAGREEN))}"
        )
        self.LightSeaGreen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTSEAGREEN))}"
        )
        self.DarkSlateGray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKSLATEGRAY))}"
        )
        self.Teal = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.TEAL))}"
        )
        self.DarkCyan = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKCYAN))}"
        )
        self.Aqua = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.AQUA))}"
        )
        self.Cyan = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CYAN))}"
        )
        self.LightCyan = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTCYAN))}"
        )
        self.DarkTurquoise = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKTURQUOISE))}"
        )
        self.Turquoise = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.TURQUOISE))}"
        )
        self.MediumTurquoise = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMTURQUOISE))}"
        )
        self.PaleTurquoise = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PALETURQUOISE))}"
        )
        self.AquaMarine = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.AQUAMARINE))}"
        )
        self.PowderBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.POWDERBLUE))}"
        )
        self.CadetBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CADETBLUE))}"
        )
        self.SteelBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.STEELBLUE))}"
        )
        self.CornFlowerBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CORNFLOWERBLUE))}"
        )
        self.DeepSkyBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DEEPSKYBLUE))}"
        )
        self.DodgerBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DODGERBLUE))}"
        )
        self.LightBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTBLUE))}"
        )
        self.SkyBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SKYBLUE))}"
        )
        self.LightSkyBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTSKYBLUE))}"
        )
        self.MidnightBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MIDNIGHTBLUE))}"
        )
        self.Navy = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.NAVY))}"
        )
        self.DarkBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKBLUE))}"
        )
        self.MediumBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMBLUE))}"
        )
        self.Blue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BLUE))}"
        )
        self.RoyalBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ROYALBLUE))}"
        )
        self.BlueViolet = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BLUEVIOLET))}"
        )
        self.Indigo = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.INDIGO))}"
        )
        self.DarkSlateBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKSLATEBLUE))}"
        )
        self.SlateBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SLATEBLUE))}"
        )
        self.MediumSlateBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMSLATEBLUE))}"
        )
        self.MediumPurple = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMPURPLE))}"
        )
        self.DarkMagenta = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKMAGENTA))}"
        )
        self.DarkViolet = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKVIOLET))}"
        )
        self.DarkOrchid = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKORCHID))}"
        )
        self.MediumOrchid = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMORCHID))}"
        )
        self.Purple = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PURPLE))}"
        )
        self.Thistle = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.THISTLE))}"
        )
        self.Plum = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PLUM))}"
        )
        self.Violet = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.VIOLET))}"
        )
        self.Magenta = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MAGENTA))}"
        )
        self.Orchid = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ORCHID))}"
        )
        self.MediumVioletRed = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MEDIUMVIOLETRED))}"
        )
        self.PaleVioletRed = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PALEVIOLETRED))}"
        )
        self.DeepPink = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DEEPPINK))}"
        )
        self.HotPink = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.HOTPINK))}"
        )
        self.LightPink = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTPINK))}"
        )
        self.Pink = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PINK))}"
        )
        self.AntiqueWhite = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ANTIQUEWHITE))}"
        )
        self.Beige = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BEIGE))}"
        )
        self.Bisque = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BISQUE))}"
        )
        self.BlanchedAlmond = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BLANCHEDALMOND))}"
        )
        self.Wheat = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.WHEAT))}"
        )
        self.CornSilk = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CORNSILK))}"
        )
        self.LemonChiffon = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LEMONCHIFFON))}"
        )
        self.LightGoldenRodYellow = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTGOLDENRODYELLOW))}"
        )
        self.LightYellow = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTYELLOW))}"
        )
        self.SaddleBrown = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SADDLEBROWN))}"
        )
        self.Sienna = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SIENNA))}"
        )
        self.Chocolate = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.CHOCOLATE))}"
        )
        self.Peru = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PERU))}"
        )
        self.SandyBrown = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SANDYBROWN))}"
        )
        self.BurlyWood = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BURLYWOOD))}"
        )
        self.Tan = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.TAN))}"
        )
        self.RosyBrown = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ROSYBROWN))}"
        )
        self.Moccasin = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MOCCASIN))}"
        )
        self.NavajoWhite = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.NAVAJOWHITE))}"
        )
        self.PeachPuff = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PEACHPUFF))}"
        )
        self.MistyRose = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MISTYROSE))}"
        )
        self.LavenderBlush = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LAVENDERBLUSH))}"
        )
        self.Linen = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LINEN))}"
        )
        self.OldLace = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.OLDLACE))}"
        )
        self.PapayaWhip = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.PAPAYAWHIP))}"
        )
        self.WeaShell = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.WEASHELL))}"
        )
        self.MintCream = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.MINTCREAM))}"
        )
        self.SlateGray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SLATEGRAY))}"
        )
        self.LightSlateGray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTSLATEGRAY))}"
        )
        self.LightSteelBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTSTEELBLUE))}"
        )
        self.Lavender = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LAVENDER))}"
        )
        self.FloralWhite = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.FLORALWHITE))}"
        )
        self.AliceBlue = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.ALICEBLUE))}"
        )
        self.GhostWhite = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GHOSTWHITE))}"
        )
        self.Honeydew = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.HONEYDEW))}"
        )
        self.Ivory = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.IVORY))}"
        )
        self.Azure = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.AZURE))}"
        )
        self.Snow = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SNOW))}"
        )
        self.Black = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.BLACK))}"
        )
        self.DimGray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DIMGRAY))}"
        )
        self.Gray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GRAY))}"
        )
        self.DarkGray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.DARKGRAY))}"
        )
        self.Silver = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.SILVER))}"
        )
        self.LightGray = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.LIGHTGRAY))}"
        )
        self.Gainsboro = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.GAINSBORO))}"
        )
        self.WhiteSmoke = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.WHITESMOKE))}"
        )
        self.White = color_sequence(
            f"{self.param_code}{';'.join((str(c) for c in HtmlColorObjects.WHITE))}"
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:tuple[int,int,int]) -> str:
        return color_sequence(f"{self.param_code}{color[0]};{color[1]};{color[2]}")