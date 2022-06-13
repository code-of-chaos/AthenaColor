# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.functions.ansi_sequences import ColorSequence, NestedColorSequence, NestedColorSequence_NoReset

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Style","Basic",
    "StyleNest", "BasicNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - StyleNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Style:
    # noinspection PyUnresolvedReferences
    __all__=[
        "Reset",
        "Italic",
        "NoItalic",
        "Bold",
        "NoBold",
        "UnderlineNest",
        "NoUnderline",
        "Crossed",
        "NoCrossed",
        "Reversed",
        "NoReversed",
        "Frame",
        "NoFrame",
        "Circle",
        "NoCircle",
        "UnderlineDouble",
        "NoForeground",
        "NoBackground"
    ]
    Reset                       = ColorSequence(0)
    Bold                        = ColorSequence(1)
    NoBold                      = ColorSequence(22)
    Dim                         = ColorSequence(2)
    NoDim                       = ColorSequence(22)
    Italic                      = ColorSequence(3)
    NoItalic                    = ColorSequence(23)
    Underline                   = ColorSequence(4)
    NoUnderline                 = ColorSequence(24)
    BlinkSlow                   = ColorSequence(5)  # NOT WORKING PYCHARM
    NoBlinkSlow                 = ColorSequence(25)  # NOT WORKING PYCHARM
    BlinkRapid                  = ColorSequence(6)  # NOT WORKING PYCHARM
    NoBlinkRapid                = ColorSequence(25)  # NOT WORKING PYCHARM
    Reversed                    = ColorSequence(7)
    NoReversed                  = ColorSequence(27)
    Conceal                     = ColorSequence(8)  # NOT WORKING PYCHARM
    NoConceal                   = ColorSequence(28)  # NOT WORKING PYCHARM
    Crossed                     = ColorSequence(9)
    NoCrossed                   = ColorSequence(29)
    FontPrimary                 = ColorSequence(10)  # NOT WORKING PYCHARM
    FontSecond1                 = ColorSequence(11)  # NOT WORKING PYCHARM
    FontSecond2                 = ColorSequence(12)  # NOT WORKING PYCHARM
    FontSecond3                 = ColorSequence(13)  # NOT WORKING PYCHARM
    FontSecond4                 = ColorSequence(14)  # NOT WORKING PYCHARM
    FontSecond5                 = ColorSequence(15)  # NOT WORKING PYCHARM
    FontSecond6                 = ColorSequence(16)  # NOT WORKING PYCHARM
    FontSecond8                 = ColorSequence(17)  # NOT WORKING PYCHARM
    FontSecond9                 = ColorSequence(18)  # NOT WORKING PYCHARM
    FontSecond10                = ColorSequence(19)  # NOT WORKING PYCHARM
    NoFont                      = ColorSequence(10)  # NOT WORKING PYCHARM
    Fraktur                     = ColorSequence(20)  # NOT WORKING PYCHARM
    UnderlineDouble             = ColorSequence(21)
    NoUnderlineDouble           = ColorSequence(24)
    PropSpacing                 = ColorSequence(26)  # NOT WORKING PYCHARM
    NoPropSpacing               = ColorSequence(26)  # NOT WORKING PYCHARM
    # 30 - 37 -> see BasicNest
    # 38 -> see RgbControlled.BackNest
    NoForeground                = ColorSequence(39)
    # 40 - 47 -> see BasicNest
    # 48 -> see RgbControlled.BackNest
    NoBackground                = ColorSequence(49)
    Frame                       = ColorSequence(51)
    NoFrame                     = ColorSequence(54)
    Circle                      = ColorSequence(52)
    NoCircle                    = ColorSequence(54)
    OverLine                    = ColorSequence(53)
    NoOverLine                  = ColorSequence(55)
    # ? 56
    # ? 57
    # 58 -> see RgbControlled.UnderlineNest
    UnderColourDefault          = ColorSequence(59)
    IdeogramUnderLine           = ColorSequence(60)
    IdeogramUnderLineDouble     = ColorSequence(61)
    IdeogramOverLine            = ColorSequence(62)
    IdeogramOverLineDouble      = ColorSequence(63)
    IdeogramStress              = ColorSequence(64)
    NoIdeogram                  = ColorSequence(65)
    SuperScript                 = ColorSequence(73)
    SubScript                   = ColorSequence(74)
    NoScript                    = ColorSequence(75)
    # ? 76 - 89
    # 100 - 107 see BasicNest
    # 90 - 97 see BasicNest

# ----------------------------------------------------------------------------------------------------------------------
# - Basic Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Basic:
    class Fore:
        Black = ColorSequence(30)
        Red = ColorSequence(31)
        Green = ColorSequence(32)
        Yellow = ColorSequence(33)
        Blue = ColorSequence(34)
        Magenta = ColorSequence(35)
        Cyan = ColorSequence(36)
        White = ColorSequence(37)
        BrightBlack = ColorSequence(90)
        BrightRed = ColorSequence(91)
        BrightGreen = ColorSequence(92)
        BrightYellow = ColorSequence(93)
        BrightBlue = ColorSequence(94)
        BrightMagenta = ColorSequence(95)
        BrightCyan = ColorSequence(96)
        BrightWhite = ColorSequence(97)

    class Back:
        Black = ColorSequence(40)
        Red = ColorSequence(41)
        Green = ColorSequence(42)
        Yellow = ColorSequence(43)
        Blue = ColorSequence(44)
        Magenta = ColorSequence(45)
        Cyan = ColorSequence(46)
        White = ColorSequence(47)
        BrightBlack = ColorSequence(100)
        BrightRed = ColorSequence(101)
        BrightGreen = ColorSequence(102)
        BrightYellow = ColorSequence(103)
        BrightBlue = ColorSequence(104)
        BrightMagenta = ColorSequence(105)
        BrightCyan = ColorSequence(106)
        BrightWhite = ColorSequence(107)


# ----------------------------------------------------------------------------------------------------------------------
# - Nested Styling -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence            # Done for slight speed increase
NCSNO = NestedColorSequence_NoReset  # Done for slight speed increase
sep_ = " "

# I know this is technically a model,
#   BUT, given it depends so much on the code above I've decideded to place it here
class StyleNest:
    @staticmethod
    def Reset(*obj,sep=sep_):                      return NCSNO(obj,Style.Reset,sep)
    @staticmethod
    def Bold(*obj,sep=sep_):                       return NCS(obj,Style.Bold,Style.NoBold,sep)
    @staticmethod
    def NoBold(*obj,sep=sep_):                     return NCSNO(obj,Style.NoBold,sep)
    @staticmethod
    def Dim(*obj,sep=sep_):                        return NCS(obj,Style.Dim,Style.NoBold,sep)
    @staticmethod
    def NoDim(*obj,sep=sep_):                      return NCSNO(obj,Style.NoBold,sep)
    @staticmethod
    def Italic(*obj,sep=sep_):                     return NCS(obj,Style.Italic,Style.NoItalic,sep)
    @staticmethod
    def NoItalic(*obj,sep=sep_):                   return NCSNO(obj,Style.NoItalic,sep)
    @staticmethod
    def Underline(*obj,sep=sep_):                  return NCS(obj,Style.Underline,Style.NoUnderline,sep)
    @staticmethod
    def NoUnderline(*obj,sep=sep_):                return NCSNO(obj,Style.NoUnderline,sep)
    @staticmethod
    def BlinkSlow(*obj,sep=sep_):                  return NCS(obj,Style.BlinkSlow,Style.NoBlinkSlow,sep)
    @staticmethod
    def NoBlinkSlow(*obj,sep=sep_):                return NCSNO(obj,Style.NoBlinkSlow,sep)
    @staticmethod
    def BlinkRapid(*obj,sep=sep_):                 return NCS(obj,Style.BlinkRapid,Style.NoBlinkRapid,sep)
    @staticmethod
    def NoBlinkRapid(*obj,sep=sep_):               return NCSNO(obj,Style.NoBlinkRapid,sep)
    @staticmethod
    def Reversed(*obj,sep=sep_):                   return NCS(obj,Style.Reversed,Style.NoReversed,sep)
    @staticmethod
    def NoReversed(*obj,sep=sep_):                 return NCSNO(obj,Style.NoReversed,sep)
    @staticmethod
    def Conceal(*obj,sep=sep_):                    return NCS(obj,Style.Conceal,Style.NoConceal,sep)
    @staticmethod
    def NoConceal(*obj,sep=sep_):                  return NCSNO(obj,Style.NoConceal,sep)
    @staticmethod
    def Crossed(*obj,sep=sep_):                    return NCS(obj,Style.Crossed,Style.NoCrossed,sep)
    @staticmethod
    def NoCrossed(*obj,sep=sep_):                  return NCSNO(obj,Style.NoCrossed,sep)
    @staticmethod
    def FontPrimary(*obj,sep=sep_):                return NCS(obj,Style.NoFont,Style.NoFont,sep)
    @staticmethod
    def FontSecond1(*obj,sep=sep_):                return NCS(obj,Style.FontSecond1,Style.NoFont,sep)
    @staticmethod
    def FontSecond2(*obj,sep=sep_):                return NCS(obj,Style.FontSecond2,Style.NoFont,sep)
    @staticmethod
    def FontSecond3(*obj,sep=sep_):                return NCS(obj,Style.FontSecond3,Style.NoFont,sep)
    @staticmethod
    def FontSecond4(*obj,sep=sep_):                return NCS(obj,Style.FontSecond4,Style.NoFont,sep)
    @staticmethod
    def FontSecond5(*obj,sep=sep_):                return NCS(obj,Style.FontSecond5,Style.NoFont,sep)
    @staticmethod
    def FontSecond6(*obj,sep=sep_):                return NCS(obj,Style.FontSecond6,Style.NoFont,sep)
    @staticmethod
    def FontSecond8(*obj,sep=sep_):                return NCS(obj,Style.FontSecond8,Style.NoFont,sep)
    @staticmethod
    def FontSecond9(*obj,sep=sep_):                return NCS(obj,Style.FontSecond9,Style.NoFont,sep)
    @staticmethod
    def FontSecond10(*obj,sep=sep_):               return NCS(obj,Style.FontSecond10,Style.NoFont,sep)
    @staticmethod
    def NoFont(*obj,sep=sep_):                     return NCSNO(obj,Style.NoFont,sep)
    @staticmethod
    def Fraktur(*obj,sep=sep_):                    return NCSNO(obj,Style.Fraktur,sep)
    @staticmethod
    def UnderlineDouble(*obj,sep=sep_):            return NCS(obj,Style.UnderlineDouble,Style.NoUnderline,sep)
    @staticmethod
    def NoUnderlineDouble(*obj,sep=sep_):          return NCSNO(obj,Style.NoUnderline,sep)
    @staticmethod
    def PropSpacing(*obj,sep=sep_):                return NCS(obj,Style.PropSpacing,Style.NoPropSpacing,sep)
    @staticmethod
    def NoPropSpacing(*obj,sep=sep_):              return NCSNO(obj,Style.NoPropSpacing,sep)
    @staticmethod
    def NoForeground(*obj,sep=sep_):               return NCSNO(obj,Style.NoForeground,sep)
    @staticmethod
    def NoBackground(*obj,sep=sep_):               return NCSNO(obj,Style.NoBackground,sep)
    @staticmethod
    def Frame(*obj,sep=sep_):                      return NCS(obj,Style.Frame,Style.NoFrame,sep)
    @staticmethod
    def NoFrame(*obj,sep=sep_):                    return NCSNO(obj,Style.NoFrame,sep)
    @staticmethod
    def Circle(*obj,sep=sep_):                     return NCS(obj,Style.Circle,Style.NoFrame,sep)
    @staticmethod
    def NoCircle(*obj,sep=sep_):                   return NCSNO(obj,Style.NoFrame,sep)
    @staticmethod
    def OverLine(*obj,sep=sep_):                   return NCS(obj,Style.OverLine,Style.NoOverLine,sep)
    @staticmethod
    def NoOverLine(*obj,sep=sep_):                 return NCSNO(obj,Style.NoOverLine,sep)
    @staticmethod
    def UnderColourDefault(*obj,sep=sep_):         return NCSNO(obj,Style.UnderColourDefault,sep)
    @staticmethod
    def IdeogramUnderLine(*obj,sep=sep_):          return NCS(obj,Style.IdeogramUnderLine,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramUnderLineDouble(*obj,sep=sep_):    return NCS(obj,Style.IdeogramUnderLineDouble,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramOverLine(*obj,sep=sep_):           return NCS(obj,Style.IdeogramOverLine,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramOverLineDouble(*obj,sep=sep_):     return NCS(obj,Style.IdeogramOverLineDouble,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramStress(*obj,sep=sep_):             return NCS(obj,Style.IdeogramStress,Style.NoIdeogram,sep)
    @staticmethod
    def NoIdeogram(*obj,sep=sep_):                 return NCSNO(obj,Style.NoIdeogram,sep)
    @staticmethod
    def SuperScript(*obj,sep=sep_):                return NCS(obj,Style.SuperScript,Style.NoScript,sep)
    @staticmethod
    def SubScript(*obj,sep=sep_):                  return NCS(obj,Style.SubScript,Style.NoScript,sep)
    @staticmethod
    def NoScript(*obj,sep=sep_):                   return NCSNO(obj,Style.NoScript,sep)

# ----------------------------------------------------------------------------------------------------------------------
# - BasicNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class BasicNest:
    class Fore:
        @staticmethod
        def Black(*obj,sep=sep_):           return NCS(obj, Basic.Fore.Black, Style.NoForeground,sep)
        @staticmethod
        def Red(*obj,sep=sep_):             return NCS(obj, Basic.Fore.Red, Style.NoForeground,sep)
        @staticmethod
        def Green(*obj,sep=sep_):           return NCS(obj, Basic.Fore.Green, Style.NoForeground,sep)
        @staticmethod
        def Yellow(*obj,sep=sep_):          return NCS(obj, Basic.Fore.Yellow, Style.NoForeground,sep)
        @staticmethod
        def Blue(*obj,sep=sep_):            return NCS(obj, Basic.Fore.Blue, Style.NoForeground,sep)
        @staticmethod
        def Magenta(*obj,sep=sep_):         return NCS(obj, Basic.Fore.Magenta, Style.NoForeground,sep)
        @staticmethod
        def Cyan(*obj,sep=sep_):            return NCS(obj, Basic.Fore.Cyan, Style.NoForeground,sep)
        @staticmethod
        def White(*obj,sep=sep_):           return NCS(obj, Basic.Fore.White, Style.NoForeground,sep)
        @staticmethod
        def BrightBlack(*obj,sep=sep_):     return NCS(obj, Basic.Fore.BrightBlack, Style.NoForeground,sep)
        @staticmethod
        def BrightRed(*obj,sep=sep_):       return NCS(obj, Basic.Fore.BrightRed, Style.NoForeground,sep)
        @staticmethod
        def BrightGreen(*obj,sep=sep_):     return NCS(obj, Basic.Fore.BrightGreen, Style.NoForeground,sep)
        @staticmethod
        def BrightYellow(*obj,sep=sep_):    return NCS(obj, Basic.Fore.BrightYellow, Style.NoForeground,sep)
        @staticmethod
        def BrightBlue(*obj,sep=sep_):      return NCS(obj, Basic.Fore.BrightBlue, Style.NoForeground,sep)
        @staticmethod
        def BrightMagenta(*obj,sep=sep_):   return NCS(obj, Basic.Fore.BrightMagenta, Style.NoForeground,sep)
        @staticmethod
        def BrightCyan(*obj,sep=sep_):      return NCS(obj, Basic.Fore.BrightCyan, Style.NoForeground,sep)
        @staticmethod
        def BrightWhite(*obj,sep=sep_):     return NCS(obj, Basic.Fore.BrightWhite, Style.NoForeground,sep)

    class Back:
        @staticmethod
        def Black(*obj,sep=sep_):           return NCS(obj, Basic.Back.Black, Style.NoBackground,sep)
        @staticmethod
        def Red(*obj,sep=sep_):             return NCS(obj, Basic.Back.Red, Style.NoBackground,sep)
        @staticmethod
        def Green(*obj,sep=sep_):           return NCS(obj, Basic.Back.Green, Style.NoBackground,sep)
        @staticmethod
        def Yellow(*obj,sep=sep_):          return NCS(obj, Basic.Back.Yellow, Style.NoBackground,sep)
        @staticmethod
        def Blue(*obj,sep=sep_):            return NCS(obj, Basic.Back.Blue, Style.NoBackground,sep)
        @staticmethod
        def Magenta(*obj,sep=sep_):         return NCS(obj, Basic.Back.Magenta, Style.NoBackground,sep)
        @staticmethod
        def Cyan(*obj,sep=sep_):            return NCS(obj, Basic.Back.Cyan, Style.NoBackground,sep)
        @staticmethod
        def White(*obj,sep=sep_):           return NCS(obj, Basic.Back.White, Style.NoBackground,sep)
        @staticmethod
        def BrightBlack(*obj,sep=sep_):     return NCS(obj, Basic.Back.BrightBlack, Style.NoBackground,sep)
        @staticmethod
        def BrightRed(*obj,sep=sep_):       return NCS(obj, Basic.Back.BrightRed, Style.NoBackground,sep)
        @staticmethod
        def BrightGreen(*obj,sep=sep_):     return NCS(obj, Basic.Back.BrightGreen, Style.NoBackground,sep)
        @staticmethod
        def BrightYellow(*obj,sep=sep_):    return NCS(obj, Basic.Back.BrightYellow, Style.NoBackground,sep)
        @staticmethod
        def BrightBlue(*obj,sep=sep_):      return NCS(obj, Basic.Back.BrightBlue, Style.NoBackground,sep)
        @staticmethod
        def BrightMagenta(*obj,sep=sep_):   return NCS(obj, Basic.Back.BrightMagenta, Style.NoBackground,sep)
        @staticmethod
        def BrightCyan(*obj,sep=sep_):      return NCS(obj, Basic.Back.BrightCyan, Style.NoBackground,sep)
        @staticmethod
        def BrightWhite(*obj,sep=sep_):     return NCS(obj, Basic.Back.BrightWhite, Style.NoBackground,sep)