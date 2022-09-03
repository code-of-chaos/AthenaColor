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
    param_code:str

    def __init__(self, param_code:str):
        self.param_code = param_code

    def custom(self, color:tuple[int,int,int]) -> str:
        return color_sequence(f"{self.param_code}{color[0]};{color[1]};{color[2]}")

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def Maroon(self) -> str:
        return self.custom(HtmlColorObjects.MAROON)

    @property
    def DarkRed(self) -> str:
        return self.custom(HtmlColorObjects.DARKRED)

    @property
    def Brown(self) -> str:
        return self.custom(HtmlColorObjects.BROWN)

    @property
    def Firebrick(self) -> str:
        return self.custom(HtmlColorObjects.FIREBRICK)

    @property
    def Crimson(self) -> str:
        return self.custom(HtmlColorObjects.CRIMSON)

    @property
    def Red(self) -> str:
        return self.custom(HtmlColorObjects.RED)

    @property
    def Tomato(self) -> str:
        return self.custom(HtmlColorObjects.TOMATO)

    @property
    def Coral(self) -> str:
        return self.custom(HtmlColorObjects.CORAL)

    @property
    def IndianRed(self) -> str:
        return self.custom(HtmlColorObjects.INDIANRED)

    @property
    def LightCoral(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTCORAL)

    @property
    def DarkSalmon(self) -> str:
        return self.custom(HtmlColorObjects.DARKSALMON)

    @property
    def Salmon(self) -> str:
        return self.custom(HtmlColorObjects.SALMON)

    @property
    def LightSalmon(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTSALMON)

    @property
    def OrangeRed(self) -> str:
        return self.custom(HtmlColorObjects.ORANGERED)

    @property
    def DarkOrange(self) -> str:
        return self.custom(HtmlColorObjects.DARKORANGE)

    @property
    def Orange(self) -> str:
        return self.custom(HtmlColorObjects.ORANGE)

    @property
    def Gold(self) -> str:
        return self.custom(HtmlColorObjects.GOLD)

    @property
    def DarkGoldenRod(self) -> str:
        return self.custom(HtmlColorObjects.DARKGOLDENROD)

    @property
    def GoldenRod(self) -> str:
        return self.custom(HtmlColorObjects.GOLDENROD)

    @property
    def PaleGoldenRod(self) -> str:
        return self.custom(HtmlColorObjects.PALEGOLDENROD)

    @property
    def DarkKhaki(self) -> str:
        return self.custom(HtmlColorObjects.DARKKHAKI)

    @property
    def Khaki(self) -> str:
        return self.custom(HtmlColorObjects.KHAKI)

    @property
    def Olive(self) -> str:
        return self.custom(HtmlColorObjects.OLIVE)

    @property
    def Yellow(self) -> str:
        return self.custom(HtmlColorObjects.YELLOW)

    @property
    def YellowGreen(self) -> str:
        return self.custom(HtmlColorObjects.YELLOWGREEN)

    @property
    def DarkOliveGreen(self) -> str:
        return self.custom(HtmlColorObjects.DARKOLIVEGREEN)

    @property
    def OliveDrab(self) -> str:
        return self.custom(HtmlColorObjects.OLIVEDRAB)

    @property
    def LawnGreen(self) -> str:
        return self.custom(HtmlColorObjects.LAWNGREEN)

    @property
    def Chartreuse(self) -> str:
        return self.custom(HtmlColorObjects.CHARTREUSE)

    @property
    def GreenYellow(self) -> str:
        return self.custom(HtmlColorObjects.GREENYELLOW)

    @property
    def DarkGreen(self) -> str:
        return self.custom(HtmlColorObjects.DARKGREEN)

    @property
    def Green(self) -> str:
        return self.custom(HtmlColorObjects.GREEN)

    @property
    def ForestGreen(self) -> str:
        return self.custom(HtmlColorObjects.FORESTGREEN)

    @property
    def Lime(self) -> str:
        return self.custom(HtmlColorObjects.LIME)

    @property
    def LimeGreen(self) -> str:
        return self.custom(HtmlColorObjects.LIMEGREEN)

    @property
    def LightGreen(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTGREEN)

    @property
    def PaleGreen(self) -> str:
        return self.custom(HtmlColorObjects.PALEGREEN)

    @property
    def DarkSeaGreen(self) -> str:
        return self.custom(HtmlColorObjects.DARKSEAGREEN)

    @property
    def MediumSpringGreen(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMSPRINGGREEN)

    @property
    def SpringGreen(self) -> str:
        return self.custom(HtmlColorObjects.SPRINGGREEN)

    @property
    def SeaGreen(self) -> str:
        return self.custom(HtmlColorObjects.SEAGREEN)

    @property
    def MediumAquaMarine(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMAQUAMARINE)

    @property
    def MediumSeaGreen(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMSEAGREEN)

    @property
    def LightSeaGreen(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTSEAGREEN)

    @property
    def DarkSlateGray(self) -> str:
        return self.custom(HtmlColorObjects.DARKSLATEGRAY)

    @property
    def Teal(self) -> str:
        return self.custom(HtmlColorObjects.TEAL)

    @property
    def DarkCyan(self) -> str:
        return self.custom(HtmlColorObjects.DARKCYAN)

    @property
    def Aqua(self) -> str:
        return self.custom(HtmlColorObjects.AQUA)

    @property
    def Cyan(self) -> str:
        return self.custom(HtmlColorObjects.CYAN)

    @property
    def LightCyan(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTCYAN)

    @property
    def DarkTurquoise(self) -> str:
        return self.custom(HtmlColorObjects.DARKTURQUOISE)

    @property
    def Turquoise(self) -> str:
        return self.custom(HtmlColorObjects.TURQUOISE)

    @property
    def MediumTurquoise(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMTURQUOISE)

    @property
    def PaleTurquoise(self) -> str:
        return self.custom(HtmlColorObjects.PALETURQUOISE)

    @property
    def AquaMarine(self) -> str:
        return self.custom(HtmlColorObjects.AQUAMARINE)

    @property
    def PowderBlue(self) -> str:
        return self.custom(HtmlColorObjects.POWDERBLUE)

    @property
    def CadetBlue(self) -> str:
        return self.custom(HtmlColorObjects.CADETBLUE)

    @property
    def SteelBlue(self) -> str:
        return self.custom(HtmlColorObjects.STEELBLUE)

    @property
    def CornFlowerBlue(self) -> str:
        return self.custom(HtmlColorObjects.CORNFLOWERBLUE)

    @property
    def DeepSkyBlue(self) -> str:
        return self.custom(HtmlColorObjects.DEEPSKYBLUE)

    @property
    def DodgerBlue(self) -> str:
        return self.custom(HtmlColorObjects.DODGERBLUE)

    @property
    def LightBlue(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTBLUE)

    @property
    def SkyBlue(self) -> str:
        return self.custom(HtmlColorObjects.SKYBLUE)

    @property
    def LightSkyBlue(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTSKYBLUE)

    @property
    def MidnightBlue(self) -> str:
        return self.custom(HtmlColorObjects.MIDNIGHTBLUE)

    @property
    def Navy(self) -> str:
        return self.custom(HtmlColorObjects.NAVY)

    @property
    def DarkBlue(self) -> str:
        return self.custom(HtmlColorObjects.DARKBLUE)

    @property
    def MediumBlue(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMBLUE)

    @property
    def Blue(self) -> str:
        return self.custom(HtmlColorObjects.BLUE)

    @property
    def RoyalBlue(self) -> str:
        return self.custom(HtmlColorObjects.ROYALBLUE)

    @property
    def BlueViolet(self) -> str:
        return self.custom(HtmlColorObjects.BLUEVIOLET)

    @property
    def Indigo(self) -> str:
        return self.custom(HtmlColorObjects.INDIGO)

    @property
    def DarkSlateBlue(self) -> str:
        return self.custom(HtmlColorObjects.DARKSLATEBLUE)

    @property
    def SlateBlue(self) -> str:
        return self.custom(HtmlColorObjects.SLATEBLUE)

    @property
    def MediumSlateBlue(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMSLATEBLUE)

    @property
    def MediumPurple(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMPURPLE)

    @property
    def DarkMagenta(self) -> str:
        return self.custom(HtmlColorObjects.DARKMAGENTA)

    @property
    def DarkViolet(self) -> str:
        return self.custom(HtmlColorObjects.DARKVIOLET)

    @property
    def DarkOrchid(self) -> str:
        return self.custom(HtmlColorObjects.DARKORCHID)

    @property
    def MediumOrchid(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMORCHID)

    @property
    def Purple(self) -> str:
        return self.custom(HtmlColorObjects.PURPLE)

    @property
    def Thistle(self) -> str:
        return self.custom(HtmlColorObjects.THISTLE)

    @property
    def Plum(self) -> str:
        return self.custom(HtmlColorObjects.PLUM)

    @property
    def Violet(self) -> str:
        return self.custom(HtmlColorObjects.VIOLET)

    @property
    def Magenta(self) -> str:
        return self.custom(HtmlColorObjects.MAGENTA)

    @property
    def Orchid(self) -> str:
        return self.custom(HtmlColorObjects.ORCHID)

    @property
    def MediumVioletRed(self) -> str:
        return self.custom(HtmlColorObjects.MEDIUMVIOLETRED)

    @property
    def PaleVioletRed(self) -> str:
        return self.custom(HtmlColorObjects.PALEVIOLETRED)

    @property
    def DeepPink(self) -> str:
        return self.custom(HtmlColorObjects.DEEPPINK)

    @property
    def HotPink(self) -> str:
        return self.custom(HtmlColorObjects.HOTPINK)

    @property
    def LightPink(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTPINK)

    @property
    def Pink(self) -> str:
        return self.custom(HtmlColorObjects.PINK)

    @property
    def AntiqueWhite(self) -> str:
        return self.custom(HtmlColorObjects.ANTIQUEWHITE)

    @property
    def Beige(self) -> str:
        return self.custom(HtmlColorObjects.BEIGE)

    @property
    def Bisque(self) -> str:
        return self.custom(HtmlColorObjects.BISQUE)

    @property
    def BlanchedAlmond(self) -> str:
        return self.custom(HtmlColorObjects.BLANCHEDALMOND)

    @property
    def Wheat(self) -> str:
        return self.custom(HtmlColorObjects.WHEAT)

    @property
    def CornSilk(self) -> str:
        return self.custom(HtmlColorObjects.CORNSILK)

    @property
    def LemonChiffon(self) -> str:
        return self.custom(HtmlColorObjects.LEMONCHIFFON)

    @property
    def LightGoldenRodYellow(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTGOLDENRODYELLOW)

    @property
    def LightYellow(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTYELLOW)

    @property
    def SaddleBrown(self) -> str:
        return self.custom(HtmlColorObjects.SADDLEBROWN)

    @property
    def Sienna(self) -> str:
        return self.custom(HtmlColorObjects.SIENNA)

    @property
    def Chocolate(self) -> str:
        return self.custom(HtmlColorObjects.CHOCOLATE)

    @property
    def Peru(self) -> str:
        return self.custom(HtmlColorObjects.PERU)

    @property
    def SandyBrown(self) -> str:
        return self.custom(HtmlColorObjects.SANDYBROWN)

    @property
    def BurlyWood(self) -> str:
        return self.custom(HtmlColorObjects.BURLYWOOD)

    @property
    def Tan(self) -> str:
        return self.custom(HtmlColorObjects.TAN)

    @property
    def RosyBrown(self) -> str:
        return self.custom(HtmlColorObjects.ROSYBROWN)

    @property
    def Moccasin(self) -> str:
        return self.custom(HtmlColorObjects.MOCCASIN)

    @property
    def NavajoWhite(self) -> str:
        return self.custom(HtmlColorObjects.NAVAJOWHITE)

    @property
    def PeachPuff(self) -> str:
        return self.custom(HtmlColorObjects.PEACHPUFF)

    @property
    def MistyRose(self) -> str:
        return self.custom(HtmlColorObjects.MISTYROSE)

    @property
    def LavenderBlush(self) -> str:
        return self.custom(HtmlColorObjects.LAVENDERBLUSH)

    @property
    def Linen(self) -> str:
        return self.custom(HtmlColorObjects.LINEN)

    @property
    def OldLace(self) -> str:
        return self.custom(HtmlColorObjects.OLDLACE)

    @property
    def PapayaWhip(self) -> str:
        return self.custom(HtmlColorObjects.PAPAYAWHIP)

    @property
    def WeaShell(self) -> str:
        return self.custom(HtmlColorObjects.WEASHELL)

    @property
    def MintCream(self) -> str:
        return self.custom(HtmlColorObjects.MINTCREAM)

    @property
    def SlateGray(self) -> str:
        return self.custom(HtmlColorObjects.SLATEGRAY)

    @property
    def LightSlateGray(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTSLATEGRAY)

    @property
    def LightSteelBlue(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTSTEELBLUE)

    @property
    def Lavender(self) -> str:
        return self.custom(HtmlColorObjects.LAVENDER)

    @property
    def FloralWhite(self) -> str:
        return self.custom(HtmlColorObjects.FLORALWHITE)

    @property
    def AliceBlue(self) -> str:
        return self.custom(HtmlColorObjects.ALICEBLUE)

    @property
    def GhostWhite(self) -> str:
        return self.custom(HtmlColorObjects.GHOSTWHITE)

    @property
    def Honeydew(self) -> str:
        return self.custom(HtmlColorObjects.HONEYDEW)

    @property
    def Ivory(self) -> str:
        return self.custom(HtmlColorObjects.IVORY)

    @property
    def Azure(self) -> str:
        return self.custom(HtmlColorObjects.AZURE)

    @property
    def Snow(self) -> str:
        return self.custom(HtmlColorObjects.SNOW)

    @property
    def Black(self) -> str:
        return self.custom(HtmlColorObjects.BLACK)

    @property
    def DimGray(self) -> str:
        return self.custom(HtmlColorObjects.DIMGRAY)

    @property
    def Gray(self) -> str:
        return self.custom(HtmlColorObjects.GRAY)

    @property
    def DarkGray(self) -> str:
        return self.custom(HtmlColorObjects.DARKGRAY)

    @property
    def Silver(self) -> str:
        return self.custom(HtmlColorObjects.SILVER)

    @property
    def LightGray(self) -> str:
        return self.custom(HtmlColorObjects.LIGHTGRAY)

    @property
    def Gainsboro(self) -> str:
        return self.custom(HtmlColorObjects.GAINSBORO)

    @property
    def WhiteSmoke(self) -> str:
        return self.custom(HtmlColorObjects.WHITESMOKE)

    @property
    def White(self) -> str:
        return self.custom(HtmlColorObjects.WHITE)