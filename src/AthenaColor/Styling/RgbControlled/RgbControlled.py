# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from ...Objects import (
    rgb,
    HtmlColors
)
from AthenaColor import init

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlled:
    param_code:str
    _sufix:str

    def __init__(self, param_code:str):
        self.param_code = param_code
        self._sufix =  "m"

    @property
    def prefix(self):
        return init.esc + self.param_code
    @property
    def sufix(self):
        return self._sufix

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def custom(self, color:rgb):
      return f"{self.prefix}{color}{self.sufix}"

    def c(self,color:rgb): #synonim for cls.custom()
      return self.custom(color)

    def rgb(self, r:int,g:int,b:int):
      return f"{self.prefix}{rgb(r,g,b)}{self.sufix}"

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def Maroon              (self): return self.prefix + str(HtmlColors.Maroon              )+ self.sufix
    @property
    def DarkRed             (self): return self.prefix + str(HtmlColors.DarkRed             )+ self.sufix
    @property
    def Brown               (self): return self.prefix + str(HtmlColors.Brown               )+ self.sufix
    @property
    def Firebrick           (self): return self.prefix + str(HtmlColors.Firebrick           )+ self.sufix
    @property
    def Crimson             (self): return self.prefix + str(HtmlColors.Crimson             )+ self.sufix
    @property
    def Red                 (self): return self.prefix + str(HtmlColors.Red                 )+ self.sufix
    @property
    def Tomato              (self): return self.prefix + str(HtmlColors.Tomato              )+ self.sufix
    @property
    def Coral               (self): return self.prefix + str(HtmlColors.Coral               )+ self.sufix
    @property
    def IndianRed           (self): return self.prefix + str(HtmlColors.IndianRed           )+ self.sufix
    @property
    def LightCoral          (self): return self.prefix + str(HtmlColors.LightCoral          )+ self.sufix
    @property
    def DarkSalmon          (self): return self.prefix + str(HtmlColors.DarkSalmon          )+ self.sufix
    @property
    def Salmon              (self): return self.prefix + str(HtmlColors.Salmon              )+ self.sufix
    @property
    def LightSalmon         (self): return self.prefix + str(HtmlColors.LightSalmon         )+ self.sufix
    @property
    def OrangeRed           (self): return self.prefix + str(HtmlColors.OrangeRed           )+ self.sufix
    @property
    def DarkOrange          (self): return self.prefix + str(HtmlColors.DarkOrange          )+ self.sufix
    @property
    def Orange              (self): return self.prefix + str(HtmlColors.Orange              )+ self.sufix
    @property
    def Gold                (self): return self.prefix + str(HtmlColors.Gold                )+ self.sufix
    @property
    def DarkGoldenRod       (self): return self.prefix + str(HtmlColors.DarkGoldenRod       )+ self.sufix
    @property
    def GoldenRod           (self): return self.prefix + str(HtmlColors.GoldenRod           )+ self.sufix
    @property
    def PaleGoldenRod       (self): return self.prefix + str(HtmlColors.PaleGoldenRod       )+ self.sufix
    @property
    def DarkKhaki           (self): return self.prefix + str(HtmlColors.DarkKhaki           )+ self.sufix
    @property
    def Khaki               (self): return self.prefix + str(HtmlColors.Khaki               )+ self.sufix
    @property
    def Olive               (self): return self.prefix + str(HtmlColors.Olive               )+ self.sufix
    @property
    def Yellow              (self): return self.prefix + str(HtmlColors.Yellow              )+ self.sufix
    @property
    def YellowGreen         (self): return self.prefix + str(HtmlColors.YellowGreen         )+ self.sufix
    @property
    def DarkOliveGreen      (self): return self.prefix + str(HtmlColors.DarkOliveGreen      )+ self.sufix
    @property
    def OliveDrab           (self): return self.prefix + str(HtmlColors.OliveDrab           )+ self.sufix
    @property
    def LawnGreen           (self): return self.prefix + str(HtmlColors.LawnGreen           )+ self.sufix
    @property
    def Chartreuse          (self): return self.prefix + str(HtmlColors.Chartreuse          )+ self.sufix
    @property
    def GreenYellow         (self): return self.prefix + str(HtmlColors.GreenYellow         )+ self.sufix
    @property
    def DarkGreen           (self): return self.prefix + str(HtmlColors.DarkGreen           )+ self.sufix
    @property
    def Green               (self): return self.prefix + str(HtmlColors.Green               )+ self.sufix
    @property
    def ForestGreen         (self): return self.prefix + str(HtmlColors.ForestGreen         )+ self.sufix
    @property
    def Lime                (self): return self.prefix + str(HtmlColors.Lime                )+ self.sufix
    @property
    def LimeGreen           (self): return self.prefix + str(HtmlColors.LimeGreen           )+ self.sufix
    @property
    def LightGreen          (self): return self.prefix + str(HtmlColors.LightGreen          )+ self.sufix
    @property
    def PaleGreen           (self): return self.prefix + str(HtmlColors.PaleGreen           )+ self.sufix
    @property
    def DarkSeaGreen        (self): return self.prefix + str(HtmlColors.DarkSeaGreen        )+ self.sufix
    @property
    def MediumSpringGreen   (self): return self.prefix + str(HtmlColors.MediumSpringGreen   )+ self.sufix
    @property
    def SpringGreen         (self): return self.prefix + str(HtmlColors.SpringGreen         )+ self.sufix
    @property
    def SeaGreen            (self): return self.prefix + str(HtmlColors.SeaGreen            )+ self.sufix
    @property
    def MediumAquaMarine    (self): return self.prefix + str(HtmlColors.MediumAquaMarine    )+ self.sufix
    @property
    def MediumSeaGreen      (self): return self.prefix + str(HtmlColors.MediumSeaGreen      )+ self.sufix
    @property
    def LightSeaGreen       (self): return self.prefix + str(HtmlColors.LightSeaGreen       )+ self.sufix
    @property
    def DarkSlateGray       (self): return self.prefix + str(HtmlColors.DarkSlateGray       )+ self.sufix
    @property
    def Teal                (self): return self.prefix + str(HtmlColors.Teal                )+ self.sufix
    @property
    def DarkCyan            (self): return self.prefix + str(HtmlColors.DarkCyan            )+ self.sufix
    @property
    def Aqua                (self): return self.prefix + str(HtmlColors.Aqua                )+ self.sufix
    @property
    def Cyan                (self): return self.prefix + str(HtmlColors.Cyan                )+ self.sufix
    @property
    def LightCyan           (self): return self.prefix + str(HtmlColors.LightCyan           )+ self.sufix
    @property
    def DarkTurquoise       (self): return self.prefix + str(HtmlColors.DarkTurquoise       )+ self.sufix
    @property
    def Turquoise           (self): return self.prefix + str(HtmlColors.Turquoise           )+ self.sufix
    @property
    def MediumTurquoise     (self): return self.prefix + str(HtmlColors.MediumTurquoise     )+ self.sufix
    @property
    def PaleTurquoise       (self): return self.prefix + str(HtmlColors.PaleTurquoise       )+ self.sufix
    @property
    def AquaMarine          (self): return self.prefix + str(HtmlColors.AquaMarine          )+ self.sufix
    @property
    def PowderBlue          (self): return self.prefix + str(HtmlColors.PowderBlue          )+ self.sufix
    @property
    def CadetBlue           (self): return self.prefix + str(HtmlColors.CadetBlue           )+ self.sufix
    @property
    def SteelBlue           (self): return self.prefix + str(HtmlColors.SteelBlue           )+ self.sufix
    @property
    def CornFlowerBlue      (self): return self.prefix + str(HtmlColors.CornFlowerBlue      )+ self.sufix
    @property
    def DeepSkyBlue         (self): return self.prefix + str(HtmlColors.DeepSkyBlue         )+ self.sufix
    @property
    def DodgerBlue          (self): return self.prefix + str(HtmlColors.DodgerBlue          )+ self.sufix
    @property
    def LightBlue           (self): return self.prefix + str(HtmlColors.LightBlue           )+ self.sufix
    @property
    def SkyBlue             (self): return self.prefix + str(HtmlColors.SkyBlue             )+ self.sufix
    @property
    def LightSkyBlue        (self): return self.prefix + str(HtmlColors.LightSkyBlue        )+ self.sufix
    @property
    def MidnightBlue        (self): return self.prefix + str(HtmlColors.MidnightBlue        )+ self.sufix
    @property
    def Navy                (self): return self.prefix + str(HtmlColors.Navy                )+ self.sufix
    @property
    def DarkBlue            (self): return self.prefix + str(HtmlColors.DarkBlue            )+ self.sufix
    @property
    def MediumBlue          (self): return self.prefix + str(HtmlColors.MediumBlue          )+ self.sufix
    @property
    def Blue                (self): return self.prefix + str(HtmlColors.Blue                )+ self.sufix
    @property
    def RoyalBlue           (self): return self.prefix + str(HtmlColors.RoyalBlue           )+ self.sufix
    @property
    def BlueViolet          (self): return self.prefix + str(HtmlColors.BlueViolet          )+ self.sufix
    @property
    def Indigo              (self): return self.prefix + str(HtmlColors.Indigo              )+ self.sufix
    @property
    def DarkSlateBlue       (self): return self.prefix + str(HtmlColors.DarkSlateBlue       )+ self.sufix
    @property
    def SlateBlue           (self): return self.prefix + str(HtmlColors.SlateBlue           )+ self.sufix
    @property
    def MediumSlateBlue     (self): return self.prefix + str(HtmlColors.MediumSlateBlue     )+ self.sufix
    @property
    def MediumPurple        (self): return self.prefix + str(HtmlColors.MediumPurple        )+ self.sufix
    @property
    def DarkMagenta         (self): return self.prefix + str(HtmlColors.DarkMagenta         )+ self.sufix
    @property
    def DarkViolet          (self): return self.prefix + str(HtmlColors.DarkViolet          )+ self.sufix
    @property
    def DarkOrchid          (self): return self.prefix + str(HtmlColors.DarkOrchid          )+ self.sufix
    @property
    def MediumOrchid        (self): return self.prefix + str(HtmlColors.MediumOrchid        )+ self.sufix
    @property
    def Purple              (self): return self.prefix + str(HtmlColors.Purple              )+ self.sufix
    @property
    def Thistle             (self): return self.prefix + str(HtmlColors.Thistle             )+ self.sufix
    @property
    def Plum                (self): return self.prefix + str(HtmlColors.Plum                )+ self.sufix
    @property
    def Violet              (self): return self.prefix + str(HtmlColors.Violet              )+ self.sufix
    @property
    def Magenta             (self): return self.prefix + str(HtmlColors.Magenta             )+ self.sufix
    @property
    def Orchid              (self): return self.prefix + str(HtmlColors.Orchid              )+ self.sufix
    @property
    def MediumVioletRed     (self): return self.prefix + str(HtmlColors.MediumVioletRed     )+ self.sufix
    @property
    def PaleVioletRed       (self): return self.prefix + str(HtmlColors.PaleVioletRed       )+ self.sufix
    @property
    def DeepPink            (self): return self.prefix + str(HtmlColors.DeepPink            )+ self.sufix
    @property
    def HotPink             (self): return self.prefix + str(HtmlColors.HotPink             )+ self.sufix
    @property
    def LightPink           (self): return self.prefix + str(HtmlColors.LightPink           )+ self.sufix
    @property
    def Pink                (self): return self.prefix + str(HtmlColors.Pink                )+ self.sufix
    @property
    def AntiqueWhite        (self): return self.prefix + str(HtmlColors.AntiqueWhite        )+ self.sufix
    @property
    def Beige               (self): return self.prefix + str(HtmlColors.Beige               )+ self.sufix
    @property
    def Bisque              (self): return self.prefix + str(HtmlColors.Bisque              )+ self.sufix
    @property
    def BlanchedAlmond      (self): return self.prefix + str(HtmlColors.BlanchedAlmond      )+ self.sufix
    @property
    def Wheat               (self): return self.prefix + str(HtmlColors.Wheat               )+ self.sufix
    @property
    def CornSilk            (self): return self.prefix + str(HtmlColors.CornSilk            )+ self.sufix
    @property
    def LemonChiffon        (self): return self.prefix + str(HtmlColors.LemonChiffon        )+ self.sufix
    @property
    def LightGoldenRodYellow(self): return self.prefix + str(HtmlColors.LightGoldenRodYellow)+ self.sufix
    @property
    def LightYellow         (self): return self.prefix + str(HtmlColors.LightYellow         )+ self.sufix
    @property
    def SaddleBrown         (self): return self.prefix + str(HtmlColors.SaddleBrown         )+ self.sufix
    @property
    def Sienna              (self): return self.prefix + str(HtmlColors.Sienna              )+ self.sufix
    @property
    def Chocolate           (self): return self.prefix + str(HtmlColors.Chocolate           )+ self.sufix
    @property
    def Peru                (self): return self.prefix + str(HtmlColors.Peru                )+ self.sufix
    @property
    def SandyBrown          (self): return self.prefix + str(HtmlColors.SandyBrown          )+ self.sufix
    @property
    def BurlyWood           (self): return self.prefix + str(HtmlColors.BurlyWood           )+ self.sufix
    @property
    def Tan                 (self): return self.prefix + str(HtmlColors.Tan                 )+ self.sufix
    @property
    def RosyBrown           (self): return self.prefix + str(HtmlColors.RosyBrown           )+ self.sufix
    @property
    def Moccasin            (self): return self.prefix + str(HtmlColors.Moccasin            )+ self.sufix
    @property
    def NavajoWhite         (self): return self.prefix + str(HtmlColors.NavajoWhite         )+ self.sufix
    @property
    def PeachPuff           (self): return self.prefix + str(HtmlColors.PeachPuff           )+ self.sufix
    @property
    def MistyRose           (self): return self.prefix + str(HtmlColors.MistyRose           )+ self.sufix
    @property
    def LavenderBlush       (self): return self.prefix + str(HtmlColors.LavenderBlush       )+ self.sufix
    @property
    def Linen               (self): return self.prefix + str(HtmlColors.Linen               )+ self.sufix
    @property
    def OldLace             (self): return self.prefix + str(HtmlColors.OldLace             )+ self.sufix
    @property
    def PapayaWhip          (self): return self.prefix + str(HtmlColors.PapayaWhip          )+ self.sufix
    @property
    def WeaShell            (self): return self.prefix + str(HtmlColors.WeaShell            )+ self.sufix
    @property
    def MintCream           (self): return self.prefix + str(HtmlColors.MintCream           )+ self.sufix
    @property
    def SlateGray           (self): return self.prefix + str(HtmlColors.SlateGray           )+ self.sufix
    @property
    def LightSlateGray      (self): return self.prefix + str(HtmlColors.LightSlateGray      )+ self.sufix
    @property
    def LightSteelBlue      (self): return self.prefix + str(HtmlColors.LightSteelBlue      )+ self.sufix
    @property
    def Lavender            (self): return self.prefix + str(HtmlColors.Lavender            )+ self.sufix
    @property
    def FloralWhite         (self): return self.prefix + str(HtmlColors.FloralWhite         )+ self.sufix
    @property
    def AliceBlue           (self): return self.prefix + str(HtmlColors.AliceBlue           )+ self.sufix
    @property
    def GhostWhite          (self): return self.prefix + str(HtmlColors.GhostWhite          )+ self.sufix
    @property
    def Honeydew            (self): return self.prefix + str(HtmlColors.Honeydew            )+ self.sufix
    @property
    def Ivory               (self): return self.prefix + str(HtmlColors.Ivory               )+ self.sufix
    @property
    def Azure               (self): return self.prefix + str(HtmlColors.Azure               )+ self.sufix
    @property
    def Snow                (self): return self.prefix + str(HtmlColors.Snow                )+ self.sufix
    @property
    def Black               (self): return self.prefix + str(HtmlColors.Black               )+ self.sufix
    @property
    def DimGray             (self): return self.prefix + str(HtmlColors.DimGray             )+ self.sufix
    @property
    def Gray                (self): return self.prefix + str(HtmlColors.Gray                )+ self.sufix
    @property
    def DarkGray            (self): return self.prefix + str(HtmlColors.DarkGray            )+ self.sufix
    @property
    def Silver              (self): return self.prefix + str(HtmlColors.Silver              )+ self.sufix
    @property
    def LightGray           (self): return self.prefix + str(HtmlColors.LightGray           )+ self.sufix
    @property
    def Gainsboro           (self): return self.prefix + str(HtmlColors.Gainsboro           )+ self.sufix
    @property
    def WhiteSmoke          (self): return self.prefix + str(HtmlColors.WhiteSmoke          )+ self.sufix
    @property
    def White               (self): return self.prefix + str(HtmlColors.White               )+ self.sufix