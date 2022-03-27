# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from collections.abc import Callable

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
def stacked(fnc):
    def wrapper(*args):
        cls, *args_ = args #type:
        return "".join([
            fnc(cls),*[
                a+fnc(cls) for a in args_
            ],cls.reset()
        ])
    return wrapper

class RgbControlled_Callable:
    param_code:str
    _sufix:str

    def __init__(self, param_code:str,reset:Callable):
        self.param_code = param_code
        self._sufix =  "m"
        self.reset = reset

    @property
    def prefix(self) -> str:
        return init.esc + self.param_code
    @property
    def sufix(self) -> str:
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
    @stacked
    def Maroon              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Maroon              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkRed             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkRed             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Brown               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Brown               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Firebrick           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Firebrick           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Crimson             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Crimson             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Red                 (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Red                 )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Tomato              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Tomato              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Coral               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Coral               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def IndianRed           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.IndianRed           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightCoral          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightCoral          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkSalmon          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkSalmon          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Salmon              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Salmon              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightSalmon         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightSalmon         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def OrangeRed           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.OrangeRed           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkOrange          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkOrange          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Orange              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Orange              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Gold                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Gold                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkGoldenRod       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkGoldenRod       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def GoldenRod           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.GoldenRod           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PaleGoldenRod       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PaleGoldenRod       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkKhaki           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkKhaki           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Khaki               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Khaki               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Olive               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Olive               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Yellow              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Yellow              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def YellowGreen         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.YellowGreen         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkOliveGreen      (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkOliveGreen      )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def OliveDrab           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.OliveDrab           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LawnGreen           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LawnGreen           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Chartreuse          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Chartreuse          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def GreenYellow         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.GreenYellow         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkGreen           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkGreen           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Green               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Green               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def ForestGreen         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.ForestGreen         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Lime                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Lime                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LimeGreen           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LimeGreen           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightGreen          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightGreen          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PaleGreen           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PaleGreen           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkSeaGreen        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkSeaGreen        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumSpringGreen   (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumSpringGreen   )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SpringGreen         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SpringGreen         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SeaGreen            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SeaGreen            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumAquaMarine    (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumAquaMarine    )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumSeaGreen      (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumSeaGreen      )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightSeaGreen       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightSeaGreen       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkSlateGray       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkSlateGray       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Teal                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Teal                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkCyan            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkCyan            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Aqua                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Aqua                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Cyan                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Cyan                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightCyan           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightCyan           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkTurquoise       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkTurquoise       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Turquoise           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Turquoise           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumTurquoise     (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumTurquoise     )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PaleTurquoise       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PaleTurquoise       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def AquaMarine          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.AquaMarine          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PowderBlue          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PowderBlue          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def CadetBlue           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.CadetBlue           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SteelBlue           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SteelBlue           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def CornFlowerBlue      (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.CornFlowerBlue      )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DeepSkyBlue         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DeepSkyBlue         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DodgerBlue          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DodgerBlue          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightBlue           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightBlue           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SkyBlue             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SkyBlue             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightSkyBlue        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightSkyBlue        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MidnightBlue        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MidnightBlue        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Navy                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Navy                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkBlue            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkBlue            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumBlue          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumBlue          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Blue                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Blue                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def RoyalBlue           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.RoyalBlue           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def BlueViolet          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.BlueViolet          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Indigo              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Indigo              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkSlateBlue       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkSlateBlue       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SlateBlue           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SlateBlue           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumSlateBlue     (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumSlateBlue     )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumPurple        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumPurple        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkMagenta         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkMagenta         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkViolet          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkViolet          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkOrchid          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkOrchid          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumOrchid        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumOrchid        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Purple              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Purple              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Thistle             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Thistle             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Plum                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Plum                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Violet              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Violet              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Magenta             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Magenta             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Orchid              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Orchid              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MediumVioletRed     (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MediumVioletRed     )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PaleVioletRed       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PaleVioletRed       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DeepPink            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DeepPink            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def HotPink             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.HotPink             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightPink           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightPink           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Pink                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Pink                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def AntiqueWhite        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.AntiqueWhite        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Beige               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Beige               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Bisque              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Bisque              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def BlanchedAlmond      (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.BlanchedAlmond      )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Wheat               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Wheat               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def CornSilk            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.CornSilk            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LemonChiffon        (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LemonChiffon        )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightGoldenRodYellow(self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightGoldenRodYellow)}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightYellow         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightYellow         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SaddleBrown         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SaddleBrown         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Sienna              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Sienna              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Chocolate           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Chocolate           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Peru                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Peru                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SandyBrown          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SandyBrown          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def BurlyWood           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.BurlyWood           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Tan                 (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Tan                 )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def RosyBrown           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.RosyBrown           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Moccasin            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Moccasin            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def NavajoWhite         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.NavajoWhite         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PeachPuff           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PeachPuff           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MistyRose           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MistyRose           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LavenderBlush       (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LavenderBlush       )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Linen               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Linen               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def OldLace             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.OldLace             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def PapayaWhip          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.PapayaWhip          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def WeaShell            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.WeaShell            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def MintCream           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.MintCream           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def SlateGray           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.SlateGray           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightSlateGray      (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightSlateGray      )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightSteelBlue      (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightSteelBlue      )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Lavender            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Lavender            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def FloralWhite         (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.FloralWhite         )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def AliceBlue           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.AliceBlue           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def GhostWhite          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.GhostWhite          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Honeydew            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Honeydew            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Ivory               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Ivory               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Azure               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Azure               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Snow                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Snow                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Black               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Black               )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DimGray             (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DimGray             )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Gray                (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Gray                )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def DarkGray            (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.DarkGray            )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Silver              (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Silver              )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def LightGray           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.LightGray           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def Gainsboro           (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.Gainsboro           )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def WhiteSmoke          (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.WhiteSmoke          )}{self.sufix}{obj if obj is not None else ''}"
    @stacked
    def White               (self,obj=None)->str: return f"{self.prefix}{str(HtmlColors.White               )}{self.sufix}{obj if obj is not None else ''}"