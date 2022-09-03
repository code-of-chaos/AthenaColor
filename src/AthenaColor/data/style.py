# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

from typing import Any

# Custom Library

# Custom Packages
from AthenaColor.func.ansi_sequences import color_sequence, color_sequence_nested, color_sequence_nested_no_reset

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
    Reset                       = color_sequence(0)
    Bold                        = color_sequence(1)
    NoBold                      = color_sequence(22)
    Dim                         = color_sequence(2)
    NoDim                       = color_sequence(22)
    Italic                      = color_sequence(3)
    NoItalic                    = color_sequence(23)
    Underline                   = color_sequence(4)
    NoUnderline                 = color_sequence(24)
    BlinkSlow                   = color_sequence(5)  # NOT WORKING PYCHARM
    NoBlinkSlow                 = color_sequence(25)  # NOT WORKING PYCHARM
    BlinkRapid                  = color_sequence(6)  # NOT WORKING PYCHARM
    NoBlinkRapid                = color_sequence(25)  # NOT WORKING PYCHARM
    Reversed                    = color_sequence(7)
    NoReversed                  = color_sequence(27)
    Conceal                     = color_sequence(8)  # NOT WORKING PYCHARM
    NoConceal                   = color_sequence(28)  # NOT WORKING PYCHARM
    Crossed                     = color_sequence(9)
    NoCrossed                   = color_sequence(29)
    FontPrimary                 = color_sequence(10)  # NOT WORKING PYCHARM
    FontSecond1                 = color_sequence(11)  # NOT WORKING PYCHARM
    FontSecond2                 = color_sequence(12)  # NOT WORKING PYCHARM
    FontSecond3                 = color_sequence(13)  # NOT WORKING PYCHARM
    FontSecond4                 = color_sequence(14)  # NOT WORKING PYCHARM
    FontSecond5                 = color_sequence(15)  # NOT WORKING PYCHARM
    FontSecond6                 = color_sequence(16)  # NOT WORKING PYCHARM
    FontSecond8                 = color_sequence(17)  # NOT WORKING PYCHARM
    FontSecond9                 = color_sequence(18)  # NOT WORKING PYCHARM
    FontSecond10                = color_sequence(19)  # NOT WORKING PYCHARM
    NoFont                      = color_sequence(10)  # NOT WORKING PYCHARM
    Fraktur                     = color_sequence(20)  # NOT WORKING PYCHARM
    UnderlineDouble             = color_sequence(21)
    NoUnderlineDouble           = color_sequence(24)
    PropSpacing                 = color_sequence(26)  # NOT WORKING PYCHARM
    NoPropSpacing               = color_sequence(26)  # NOT WORKING PYCHARM
    # 30 - 37 -> see BasicNest
    # 38 -> see RgbControlled.BackNest
    NoForeground                = color_sequence(39)
    # 40 - 47 -> see BasicNest
    # 48 -> see RgbControlled.BackNest
    NoBackground                = color_sequence(49)
    Frame                       = color_sequence(51)
    NoFrame                     = color_sequence(54)
    Circle                      = color_sequence(52)
    NoCircle                    = color_sequence(54)
    OverLine                    = color_sequence(53)
    NoOverLine                  = color_sequence(55)
    # ? 56
    # ? 57
    # 58 -> see RgbControlled.UnderlineNest
    UnderColourDefault          = color_sequence(59)
    IdeogramUnderLine           = color_sequence(60)
    IdeogramUnderLineDouble     = color_sequence(61)
    IdeogramOverLine            = color_sequence(62)
    IdeogramOverLineDouble      = color_sequence(63)
    IdeogramStress              = color_sequence(64)
    NoIdeogram                  = color_sequence(65)
    SuperScript                 = color_sequence(73)
    SubScript                   = color_sequence(74)
    NoScript                    = color_sequence(75)
    # ? 76 - 89
    # 100 - 107 see BasicNest
    # 90 - 97 see BasicNest

# ----------------------------------------------------------------------------------------------------------------------
# - Basic Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class Basic:
    class Fore:
        Black = color_sequence(30)
        Red = color_sequence(31)
        Green = color_sequence(32)
        Yellow = color_sequence(33)
        Blue = color_sequence(34)
        Magenta = color_sequence(35)
        Cyan = color_sequence(36)
        White = color_sequence(37)
        BrightBlack = color_sequence(90)
        BrightRed = color_sequence(91)
        BrightGreen = color_sequence(92)
        BrightYellow = color_sequence(93)
        BrightBlue = color_sequence(94)
        BrightMagenta = color_sequence(95)
        BrightCyan = color_sequence(96)
        BrightWhite = color_sequence(97)

    class Back:
        Black = color_sequence(40)
        Red = color_sequence(41)
        Green = color_sequence(42)
        Yellow = color_sequence(43)
        Blue = color_sequence(44)
        Magenta = color_sequence(45)
        Cyan = color_sequence(46)
        White = color_sequence(47)
        BrightBlack = color_sequence(100)
        BrightRed = color_sequence(101)
        BrightGreen = color_sequence(102)
        BrightYellow = color_sequence(103)
        BrightBlue = color_sequence(104)
        BrightMagenta = color_sequence(105)
        BrightCyan = color_sequence(106)
        BrightWhite = color_sequence(107)


# ----------------------------------------------------------------------------------------------------------------------
# - Nested Styling -
# ----------------------------------------------------------------------------------------------------------------------
NCS = color_sequence_nested            # Done for slight speed increase
NCSNO = color_sequence_nested_no_reset  # Done for slight speed increase
sep_ = " "

# I know this is technically a model,
#   BUT, given it depends so much on the code above I've decided to place it here
class StyleNest:
    @staticmethod
    def Reset(*obj:tuple[Any, ...],sep:str=sep_) -> str:                      return NCSNO(obj,Style.Reset,sep)
    @staticmethod
    def Bold(*obj:tuple[Any, ...],sep:str=sep_) -> str:                       return NCS(obj,Style.Bold,Style.NoBold,sep)
    @staticmethod
    def NoBold(*obj:tuple[Any, ...],sep:str=sep_) -> str:                     return NCSNO(obj,Style.NoBold,sep)
    @staticmethod
    def Dim(*obj:tuple[Any, ...],sep:str=sep_) -> str:                        return NCS(obj,Style.Dim,Style.NoBold,sep)
    @staticmethod
    def NoDim(*obj:tuple[Any, ...],sep:str=sep_) -> str:                      return NCSNO(obj,Style.NoBold,sep)
    @staticmethod
    def Italic(*obj:tuple[Any, ...],sep:str=sep_) -> str:                     return NCS(obj,Style.Italic,Style.NoItalic,sep)
    @staticmethod
    def NoItalic(*obj:tuple[Any, ...],sep:str=sep_) -> str:                   return NCSNO(obj,Style.NoItalic,sep)
    @staticmethod
    def Underline(*obj:tuple[Any, ...],sep:str=sep_) -> str:                  return NCS(obj,Style.Underline,Style.NoUnderline,sep)
    @staticmethod
    def NoUnderline(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCSNO(obj,Style.NoUnderline,sep)
    @staticmethod
    def BlinkSlow(*obj:tuple[Any, ...],sep:str=sep_) -> str:                  return NCS(obj,Style.BlinkSlow,Style.NoBlinkSlow,sep)
    @staticmethod
    def NoBlinkSlow(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCSNO(obj,Style.NoBlinkSlow,sep)
    @staticmethod
    def BlinkRapid(*obj:tuple[Any, ...],sep:str=sep_) -> str:                 return NCS(obj,Style.BlinkRapid,Style.NoBlinkRapid,sep)
    @staticmethod
    def NoBlinkRapid(*obj:tuple[Any, ...],sep:str=sep_) -> str:               return NCSNO(obj,Style.NoBlinkRapid,sep)
    @staticmethod
    def Reversed(*obj:tuple[Any, ...],sep:str=sep_) -> str:                   return NCS(obj,Style.Reversed,Style.NoReversed,sep)
    @staticmethod
    def NoReversed(*obj:tuple[Any, ...],sep:str=sep_) -> str:                 return NCSNO(obj,Style.NoReversed,sep)
    @staticmethod
    def Conceal(*obj:tuple[Any, ...],sep:str=sep_) -> str:                    return NCS(obj,Style.Conceal,Style.NoConceal,sep)
    @staticmethod
    def NoConceal(*obj:tuple[Any, ...],sep:str=sep_) -> str:                  return NCSNO(obj,Style.NoConceal,sep)
    @staticmethod
    def Crossed(*obj:tuple[Any, ...],sep:str=sep_) -> str:                    return NCS(obj,Style.Crossed,Style.NoCrossed,sep)
    @staticmethod
    def NoCrossed(*obj:tuple[Any, ...],sep:str=sep_) -> str:                  return NCSNO(obj,Style.NoCrossed,sep)
    @staticmethod
    def FontPrimary(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.NoFont,Style.NoFont,sep)
    @staticmethod
    def FontSecond1(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond1,Style.NoFont,sep)
    @staticmethod
    def FontSecond2(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond2,Style.NoFont,sep)
    @staticmethod
    def FontSecond3(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond3,Style.NoFont,sep)
    @staticmethod
    def FontSecond4(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond4,Style.NoFont,sep)
    @staticmethod
    def FontSecond5(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond5,Style.NoFont,sep)
    @staticmethod
    def FontSecond6(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond6,Style.NoFont,sep)
    @staticmethod
    def FontSecond8(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond8,Style.NoFont,sep)
    @staticmethod
    def FontSecond9(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.FontSecond9,Style.NoFont,sep)
    @staticmethod
    def FontSecond10(*obj:tuple[Any, ...],sep:str=sep_) -> str:               return NCS(obj,Style.FontSecond10,Style.NoFont,sep)
    @staticmethod
    def NoFont(*obj:tuple[Any, ...],sep:str=sep_) -> str:                     return NCSNO(obj,Style.NoFont,sep)
    @staticmethod
    def Fraktur(*obj:tuple[Any, ...],sep:str=sep_) -> str:                    return NCSNO(obj,Style.Fraktur,sep)
    @staticmethod
    def UnderlineDouble(*obj:tuple[Any, ...],sep:str=sep_) -> str:            return NCS(obj,Style.UnderlineDouble,Style.NoUnderline,sep)
    @staticmethod
    def NoUnderlineDouble(*obj:tuple[Any, ...],sep:str=sep_) -> str:          return NCSNO(obj,Style.NoUnderline,sep)
    @staticmethod
    def PropSpacing(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.PropSpacing,Style.NoPropSpacing,sep)
    @staticmethod
    def NoPropSpacing(*obj:tuple[Any, ...],sep:str=sep_) -> str:              return NCSNO(obj,Style.NoPropSpacing,sep)
    @staticmethod
    def NoForeground(*obj:tuple[Any, ...],sep:str=sep_) -> str:               return NCSNO(obj,Style.NoForeground,sep)
    @staticmethod
    def NoBackground(*obj:tuple[Any, ...],sep:str=sep_) -> str:               return NCSNO(obj,Style.NoBackground,sep)
    @staticmethod
    def Frame(*obj:tuple[Any, ...],sep:str=sep_) -> str:                      return NCS(obj,Style.Frame,Style.NoFrame,sep)
    @staticmethod
    def NoFrame(*obj:tuple[Any, ...],sep:str=sep_) -> str:                    return NCSNO(obj,Style.NoFrame,sep)
    @staticmethod
    def Circle(*obj:tuple[Any, ...],sep:str=sep_) -> str:                     return NCS(obj,Style.Circle,Style.NoFrame,sep)
    @staticmethod
    def NoCircle(*obj:tuple[Any, ...],sep:str=sep_) -> str:                   return NCSNO(obj,Style.NoFrame,sep)
    @staticmethod
    def OverLine(*obj:tuple[Any, ...],sep:str=sep_) -> str:                   return NCS(obj,Style.OverLine,Style.NoOverLine,sep)
    @staticmethod
    def NoOverLine(*obj:tuple[Any, ...],sep:str=sep_) -> str:                 return NCSNO(obj,Style.NoOverLine,sep)
    @staticmethod
    def UnderColourDefault(*obj:tuple[Any, ...],sep:str=sep_) -> str:         return NCSNO(obj,Style.UnderColourDefault,sep)
    @staticmethod
    def IdeogramUnderLine(*obj:tuple[Any, ...],sep:str=sep_) -> str:          return NCS(obj,Style.IdeogramUnderLine,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramUnderLineDouble(*obj:tuple[Any, ...],sep:str=sep_) -> str:    return NCS(obj,Style.IdeogramUnderLineDouble,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramOverLine(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj,Style.IdeogramOverLine,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramOverLineDouble(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj,Style.IdeogramOverLineDouble,Style.NoIdeogram,sep)
    @staticmethod
    def IdeogramStress(*obj:tuple[Any, ...],sep:str=sep_) -> str:             return NCS(obj,Style.IdeogramStress,Style.NoIdeogram,sep)
    @staticmethod
    def NoIdeogram(*obj:tuple[Any, ...],sep:str=sep_) -> str:                 return NCSNO(obj,Style.NoIdeogram,sep)
    @staticmethod
    def SuperScript(*obj:tuple[Any, ...],sep:str=sep_) -> str:                return NCS(obj,Style.SuperScript,Style.NoScript,sep)
    @staticmethod
    def SubScript(*obj:tuple[Any, ...],sep:str=sep_) -> str:                  return NCS(obj,Style.SubScript,Style.NoScript,sep)
    @staticmethod
    def NoScript(*obj:tuple[Any, ...],sep:str=sep_) -> str:                   return NCSNO(obj,Style.NoScript,sep)

# ----------------------------------------------------------------------------------------------------------------------
# - BasicNest Sequences -
# ----------------------------------------------------------------------------------------------------------------------
class BasicNest:
    class Fore:
        @staticmethod
        def Black(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj, Basic.Fore.Black, Style.NoForeground,sep)
        @staticmethod
        def Red(*obj:tuple[Any, ...],sep:str=sep_) -> str:             return NCS(obj, Basic.Fore.Red, Style.NoForeground,sep)
        @staticmethod
        def Green(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj, Basic.Fore.Green, Style.NoForeground,sep)
        @staticmethod
        def Yellow(*obj:tuple[Any, ...],sep:str=sep_) -> str:          return NCS(obj, Basic.Fore.Yellow, Style.NoForeground,sep)
        @staticmethod
        def Blue(*obj:tuple[Any, ...],sep:str=sep_) -> str:            return NCS(obj, Basic.Fore.Blue, Style.NoForeground,sep)
        @staticmethod
        def Magenta(*obj:tuple[Any, ...],sep:str=sep_) -> str:         return NCS(obj, Basic.Fore.Magenta, Style.NoForeground,sep)
        @staticmethod
        def Cyan(*obj:tuple[Any, ...],sep:str=sep_) -> str:            return NCS(obj, Basic.Fore.Cyan, Style.NoForeground,sep)
        @staticmethod
        def White(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj, Basic.Fore.White, Style.NoForeground,sep)
        @staticmethod
        def BrightBlack(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj, Basic.Fore.BrightBlack, Style.NoForeground,sep)
        @staticmethod
        def BrightRed(*obj:tuple[Any, ...],sep:str=sep_) -> str:       return NCS(obj, Basic.Fore.BrightRed, Style.NoForeground,sep)
        @staticmethod
        def BrightGreen(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj, Basic.Fore.BrightGreen, Style.NoForeground,sep)
        @staticmethod
        def BrightYellow(*obj:tuple[Any, ...],sep:str=sep_) -> str:    return NCS(obj, Basic.Fore.BrightYellow, Style.NoForeground,sep)
        @staticmethod
        def BrightBlue(*obj:tuple[Any, ...],sep:str=sep_) -> str:      return NCS(obj, Basic.Fore.BrightBlue, Style.NoForeground,sep)
        @staticmethod
        def BrightMagenta(*obj:tuple[Any, ...],sep:str=sep_) -> str:   return NCS(obj, Basic.Fore.BrightMagenta, Style.NoForeground,sep)
        @staticmethod
        def BrightCyan(*obj:tuple[Any, ...],sep:str=sep_) -> str:      return NCS(obj, Basic.Fore.BrightCyan, Style.NoForeground,sep)
        @staticmethod
        def BrightWhite(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj, Basic.Fore.BrightWhite, Style.NoForeground,sep)

    class Back:
        @staticmethod
        def Black(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj, Basic.Back.Black, Style.NoBackground,sep)
        @staticmethod
        def Red(*obj:tuple[Any, ...],sep:str=sep_) -> str:             return NCS(obj, Basic.Back.Red, Style.NoBackground,sep)
        @staticmethod
        def Green(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj, Basic.Back.Green, Style.NoBackground,sep)
        @staticmethod
        def Yellow(*obj:tuple[Any, ...],sep:str=sep_) -> str:          return NCS(obj, Basic.Back.Yellow, Style.NoBackground,sep)
        @staticmethod
        def Blue(*obj:tuple[Any, ...],sep:str=sep_) -> str:            return NCS(obj, Basic.Back.Blue, Style.NoBackground,sep)
        @staticmethod
        def Magenta(*obj:tuple[Any, ...],sep:str=sep_) -> str:         return NCS(obj, Basic.Back.Magenta, Style.NoBackground,sep)
        @staticmethod
        def Cyan(*obj:tuple[Any, ...],sep:str=sep_) -> str:            return NCS(obj, Basic.Back.Cyan, Style.NoBackground,sep)
        @staticmethod
        def White(*obj:tuple[Any, ...],sep:str=sep_) -> str:           return NCS(obj, Basic.Back.White, Style.NoBackground,sep)
        @staticmethod
        def BrightBlack(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj, Basic.Back.BrightBlack, Style.NoBackground,sep)
        @staticmethod
        def BrightRed(*obj:tuple[Any, ...],sep:str=sep_) -> str:       return NCS(obj, Basic.Back.BrightRed, Style.NoBackground,sep)
        @staticmethod
        def BrightGreen(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj, Basic.Back.BrightGreen, Style.NoBackground,sep)
        @staticmethod
        def BrightYellow(*obj:tuple[Any, ...],sep:str=sep_) -> str:    return NCS(obj, Basic.Back.BrightYellow, Style.NoBackground,sep)
        @staticmethod
        def BrightBlue(*obj:tuple[Any, ...],sep:str=sep_) -> str:      return NCS(obj, Basic.Back.BrightBlue, Style.NoBackground,sep)
        @staticmethod
        def BrightMagenta(*obj:tuple[Any, ...],sep:str=sep_) -> str:   return NCS(obj, Basic.Back.BrightMagenta, Style.NoBackground,sep)
        @staticmethod
        def BrightCyan(*obj:tuple[Any, ...],sep:str=sep_) -> str:      return NCS(obj, Basic.Back.BrightCyan, Style.NoBackground,sep)
        @staticmethod
        def BrightWhite(*obj:tuple[Any, ...],sep:str=sep_) -> str:     return NCS(obj, Basic.Back.BrightWhite, Style.NoBackground,sep)