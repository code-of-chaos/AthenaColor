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
    def Maroon(self):
        return self.custom(HtmlColorObjects.MAROON)

    @property
    def DarkRed(self):
        return self.custom(HtmlColorObjects.DARKRED)

    @property
    def Brown(self):
        return self.custom(HtmlColorObjects.BROWN)

    @property
    def Firebrick(self):
        return self.custom(HtmlColorObjects.FIREBRICK)

    @property
    def Crimson(self):
        return self.custom(HtmlColorObjects.CRIMSON)

    @property
    def Red(self):
        return self.custom(HtmlColorObjects.RED)

    @property
    def Tomato(self):
        return self.custom(HtmlColorObjects.TOMATO)

    @property
    def Coral(self):
        return self.custom(HtmlColorObjects.CORAL)

    @property
    def IndianRed(self):
        return self.custom(HtmlColorObjects.INDIANRED)

    @property
    def LightCoral(self):
        return self.custom(HtmlColorObjects.LIGHTCORAL)

    @property
    def DarkSalmon(self):
        return self.custom(HtmlColorObjects.DARKSALMON)

    @property
    def Salmon(self):
        return self.custom(HtmlColorObjects.SALMON)

    @property
    def LightSalmon(self):
        return self.custom(HtmlColorObjects.LIGHTSALMON)

    @property
    def OrangeRed(self):
        return self.custom(HtmlColorObjects.ORANGERED)

    @property
    def DarkOrange(self):
        return self.custom(HtmlColorObjects.DARKORANGE)

    @property
    def Orange(self):
        return self.custom(HtmlColorObjects.ORANGE)

    @property
    def Gold(self):
        return self.custom(HtmlColorObjects.GOLD)

    @property
    def DarkGoldenRod(self):
        return self.custom(HtmlColorObjects.DARKGOLDENROD)

    @property
    def GoldenRod(self):
        return self.custom(HtmlColorObjects.GOLDENROD)

    @property
    def PaleGoldenRod(self):
        return self.custom(HtmlColorObjects.PALEGOLDENROD)

    @property
    def DarkKhaki(self):
        return self.custom(HtmlColorObjects.DARKKHAKI)

    @property
    def Khaki(self):
        return self.custom(HtmlColorObjects.KHAKI)

    @property
    def Olive(self):
        return self.custom(HtmlColorObjects.OLIVE)

    @property
    def Yellow(self):
        return self.custom(HtmlColorObjects.YELLOW)

    @property
    def YellowGreen(self):
        return self.custom(HtmlColorObjects.YELLOWGREEN)

    @property
    def DarkOliveGreen(self):
        return self.custom(HtmlColorObjects.DARKOLIVEGREEN)

    @property
    def OliveDrab(self):
        return self.custom(HtmlColorObjects.OLIVEDRAB)

    @property
    def LawnGreen(self):
        return self.custom(HtmlColorObjects.LAWNGREEN)

    @property
    def Chartreuse(self):
        return self.custom(HtmlColorObjects.CHARTREUSE)

    @property
    def GreenYellow(self):
        return self.custom(HtmlColorObjects.GREENYELLOW)

    @property
    def DarkGreen(self):
        return self.custom(HtmlColorObjects.DARKGREEN)

    @property
    def Green(self):
        return self.custom(HtmlColorObjects.GREEN)

    @property
    def ForestGreen(self):
        return self.custom(HtmlColorObjects.FORESTGREEN)

    @property
    def Lime(self):
        return self.custom(HtmlColorObjects.LIME)

    @property
    def LimeGreen(self):
        return self.custom(HtmlColorObjects.LIMEGREEN)

    @property
    def LightGreen(self):
        return self.custom(HtmlColorObjects.LIGHTGREEN)

    @property
    def PaleGreen(self):
        return self.custom(HtmlColorObjects.PALEGREEN)

    @property
    def DarkSeaGreen(self):
        return self.custom(HtmlColorObjects.DARKSEAGREEN)

    @property
    def MediumSpringGreen(self):
        return self.custom(HtmlColorObjects.MEDIUMSPRINGGREEN)

    @property
    def SpringGreen(self):
        return self.custom(HtmlColorObjects.SPRINGGREEN)

    @property
    def SeaGreen(self):
        return self.custom(HtmlColorObjects.SEAGREEN)

    @property
    def MediumAquaMarine(self):
        return self.custom(HtmlColorObjects.MEDIUMAQUAMARINE)

    @property
    def MediumSeaGreen(self):
        return self.custom(HtmlColorObjects.MEDIUMSEAGREEN)

    @property
    def LightSeaGreen(self):
        return self.custom(HtmlColorObjects.LIGHTSEAGREEN)

    @property
    def DarkSlateGray(self):
        return self.custom(HtmlColorObjects.DARKSLATEGRAY)

    @property
    def Teal(self):
        return self.custom(HtmlColorObjects.TEAL)

    @property
    def DarkCyan(self):
        return self.custom(HtmlColorObjects.DARKCYAN)

    @property
    def Aqua(self):
        return self.custom(HtmlColorObjects.AQUA)

    @property
    def Cyan(self):
        return self.custom(HtmlColorObjects.CYAN)

    @property
    def LightCyan(self):
        return self.custom(HtmlColorObjects.LIGHTCYAN)

    @property
    def DarkTurquoise(self):
        return self.custom(HtmlColorObjects.DARKTURQUOISE)

    @property
    def Turquoise(self):
        return self.custom(HtmlColorObjects.TURQUOISE)

    @property
    def MediumTurquoise(self):
        return self.custom(HtmlColorObjects.MEDIUMTURQUOISE)

    @property
    def PaleTurquoise(self):
        return self.custom(HtmlColorObjects.PALETURQUOISE)

    @property
    def AquaMarine(self):
        return self.custom(HtmlColorObjects.AQUAMARINE)

    @property
    def PowderBlue(self):
        return self.custom(HtmlColorObjects.POWDERBLUE)

    @property
    def CadetBlue(self):
        return self.custom(HtmlColorObjects.CADETBLUE)

    @property
    def SteelBlue(self):
        return self.custom(HtmlColorObjects.STEELBLUE)

    @property
    def CornFlowerBlue(self):
        return self.custom(HtmlColorObjects.CORNFLOWERBLUE)

    @property
    def DeepSkyBlue(self):
        return self.custom(HtmlColorObjects.DEEPSKYBLUE)

    @property
    def DodgerBlue(self):
        return self.custom(HtmlColorObjects.DODGERBLUE)

    @property
    def LightBlue(self):
        return self.custom(HtmlColorObjects.LIGHTBLUE)

    @property
    def SkyBlue(self):
        return self.custom(HtmlColorObjects.SKYBLUE)

    @property
    def LightSkyBlue(self):
        return self.custom(HtmlColorObjects.LIGHTSKYBLUE)

    @property
    def MidnightBlue(self):
        return self.custom(HtmlColorObjects.MIDNIGHTBLUE)

    @property
    def Navy(self):
        return self.custom(HtmlColorObjects.NAVY)

    @property
    def DarkBlue(self):
        return self.custom(HtmlColorObjects.DARKBLUE)

    @property
    def MediumBlue(self):
        return self.custom(HtmlColorObjects.MEDIUMBLUE)

    @property
    def Blue(self):
        return self.custom(HtmlColorObjects.BLUE)

    @property
    def RoyalBlue(self):
        return self.custom(HtmlColorObjects.ROYALBLUE)

    @property
    def BlueViolet(self):
        return self.custom(HtmlColorObjects.BLUEVIOLET)

    @property
    def Indigo(self):
        return self.custom(HtmlColorObjects.INDIGO)

    @property
    def DarkSlateBlue(self):
        return self.custom(HtmlColorObjects.DARKSLATEBLUE)

    @property
    def SlateBlue(self):
        return self.custom(HtmlColorObjects.SLATEBLUE)

    @property
    def MediumSlateBlue(self):
        return self.custom(HtmlColorObjects.MEDIUMSLATEBLUE)

    @property
    def MediumPurple(self):
        return self.custom(HtmlColorObjects.MEDIUMPURPLE)

    @property
    def DarkMagenta(self):
        return self.custom(HtmlColorObjects.DARKMAGENTA)

    @property
    def DarkViolet(self):
        return self.custom(HtmlColorObjects.DARKVIOLET)

    @property
    def DarkOrchid(self):
        return self.custom(HtmlColorObjects.DARKORCHID)

    @property
    def MediumOrchid(self):
        return self.custom(HtmlColorObjects.MEDIUMORCHID)

    @property
    def Purple(self):
        return self.custom(HtmlColorObjects.PURPLE)

    @property
    def Thistle(self):
        return self.custom(HtmlColorObjects.THISTLE)

    @property
    def Plum(self):
        return self.custom(HtmlColorObjects.PLUM)

    @property
    def Violet(self):
        return self.custom(HtmlColorObjects.VIOLET)

    @property
    def Magenta(self):
        return self.custom(HtmlColorObjects.MAGENTA)

    @property
    def Orchid(self):
        return self.custom(HtmlColorObjects.ORCHID)

    @property
    def MediumVioletRed(self):
        return self.custom(HtmlColorObjects.MEDIUMVIOLETRED)

    @property
    def PaleVioletRed(self):
        return self.custom(HtmlColorObjects.PALEVIOLETRED)

    @property
    def DeepPink(self):
        return self.custom(HtmlColorObjects.DEEPPINK)

    @property
    def HotPink(self):
        return self.custom(HtmlColorObjects.HOTPINK)

    @property
    def LightPink(self):
        return self.custom(HtmlColorObjects.LIGHTPINK)

    @property
    def Pink(self):
        return self.custom(HtmlColorObjects.PINK)

    @property
    def AntiqueWhite(self):
        return self.custom(HtmlColorObjects.ANTIQUEWHITE)

    @property
    def Beige(self):
        return self.custom(HtmlColorObjects.BEIGE)

    @property
    def Bisque(self):
        return self.custom(HtmlColorObjects.BISQUE)

    @property
    def BlanchedAlmond(self):
        return self.custom(HtmlColorObjects.BLANCHEDALMOND)

    @property
    def Wheat(self):
        return self.custom(HtmlColorObjects.WHEAT)

    @property
    def CornSilk(self):
        return self.custom(HtmlColorObjects.CORNSILK)

    @property
    def LemonChiffon(self):
        return self.custom(HtmlColorObjects.LEMONCHIFFON)

    @property
    def LightGoldenRodYellow(self):
        return self.custom(HtmlColorObjects.LIGHTGOLDENRODYELLOW)

    @property
    def LightYellow(self):
        return self.custom(HtmlColorObjects.LIGHTYELLOW)

    @property
    def SaddleBrown(self):
        return self.custom(HtmlColorObjects.SADDLEBROWN)

    @property
    def Sienna(self):
        return self.custom(HtmlColorObjects.SIENNA)

    @property
    def Chocolate(self):
        return self.custom(HtmlColorObjects.CHOCOLATE)

    @property
    def Peru(self):
        return self.custom(HtmlColorObjects.PERU)

    @property
    def SandyBrown(self):
        return self.custom(HtmlColorObjects.SANDYBROWN)

    @property
    def BurlyWood(self):
        return self.custom(HtmlColorObjects.BURLYWOOD)

    @property
    def Tan(self):
        return self.custom(HtmlColorObjects.TAN)

    @property
    def RosyBrown(self):
        return self.custom(HtmlColorObjects.ROSYBROWN)

    @property
    def Moccasin(self):
        return self.custom(HtmlColorObjects.MOCCASIN)

    @property
    def NavajoWhite(self):
        return self.custom(HtmlColorObjects.NAVAJOWHITE)

    @property
    def PeachPuff(self):
        return self.custom(HtmlColorObjects.PEACHPUFF)

    @property
    def MistyRose(self):
        return self.custom(HtmlColorObjects.MISTYROSE)

    @property
    def LavenderBlush(self):
        return self.custom(HtmlColorObjects.LAVENDERBLUSH)

    @property
    def Linen(self):
        return self.custom(HtmlColorObjects.LINEN)

    @property
    def OldLace(self):
        return self.custom(HtmlColorObjects.OLDLACE)

    @property
    def PapayaWhip(self):
        return self.custom(HtmlColorObjects.PAPAYAWHIP)

    @property
    def WeaShell(self):
        return self.custom(HtmlColorObjects.WEASHELL)

    @property
    def MintCream(self):
        return self.custom(HtmlColorObjects.MINTCREAM)

    @property
    def SlateGray(self):
        return self.custom(HtmlColorObjects.SLATEGRAY)

    @property
    def LightSlateGray(self):
        return self.custom(HtmlColorObjects.LIGHTSLATEGRAY)

    @property
    def LightSteelBlue(self):
        return self.custom(HtmlColorObjects.LIGHTSTEELBLUE)

    @property
    def Lavender(self):
        return self.custom(HtmlColorObjects.LAVENDER)

    @property
    def FloralWhite(self):
        return self.custom(HtmlColorObjects.FLORALWHITE)

    @property
    def AliceBlue(self):
        return self.custom(HtmlColorObjects.ALICEBLUE)

    @property
    def GhostWhite(self):
        return self.custom(HtmlColorObjects.GHOSTWHITE)

    @property
    def Honeydew(self):
        return self.custom(HtmlColorObjects.HONEYDEW)

    @property
    def Ivory(self):
        return self.custom(HtmlColorObjects.IVORY)

    @property
    def Azure(self):
        return self.custom(HtmlColorObjects.AZURE)

    @property
    def Snow(self):
        return self.custom(HtmlColorObjects.SNOW)

    @property
    def Black(self):
        return self.custom(HtmlColorObjects.BLACK)

    @property
    def DimGray(self):
        return self.custom(HtmlColorObjects.DIMGRAY)

    @property
    def Gray(self):
        return self.custom(HtmlColorObjects.GRAY)

    @property
    def DarkGray(self):
        return self.custom(HtmlColorObjects.DARKGRAY)

    @property
    def Silver(self):
        return self.custom(HtmlColorObjects.SILVER)

    @property
    def LightGray(self):
        return self.custom(HtmlColorObjects.LIGHTGRAY)

    @property
    def Gainsboro(self):
        return self.custom(HtmlColorObjects.GAINSBORO)

    @property
    def WhiteSmoke(self):
        return self.custom(HtmlColorObjects.WHITESMOKE)

    @property
    def White(self):
        return self.custom(HtmlColorObjects.WHITE)