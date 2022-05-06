# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaColor.Objects.Color.ColorSystem import RGB,HEX, NormalizeRgb
from AthenaColor.Functions.ANSIsquences import NestedColorSequence
from AthenaColor.Functions.General import StrictType

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "BackNest"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
NCS = NestedColorSequence # Done for slight speed increase
resetCode=49
sep_=" "

# Predefined Strings to speed calls up
Maroon                  =f"48;2;128;0;0"
DarkRed                 =f"48;2;139;0;0"
Brown                   =f"48;2;165;42;42"
Firebrick               =f"48;2;178;34;34"
Crimson                 =f"48;2;220;20;60"
Red                     =f"48;2;255;0;0"
Tomato                  =f"48;2;255;99;71"
Coral                   =f"48;2;255;127;80"
IndianRed               =f"48;2;205;92;92"
LightCoral              =f"48;2;240;128;128"
DarkSalmon              =f"48;2;233;150;122"
Salmon                  =f"48;2;250;128;114"
LightSalmon             =f"48;2;255;160;122"
OrangeRed               =f"48;2;255;69;0"
DarkOrange              =f"48;2;255;140;0"
Orange                  =f"48;2;255;165;0"
Gold                    =f"48;2;255;215;0"
DarkGoldenRod           =f"48;2;184;134;11"
GoldenRod               =f"48;2;218;165;32"
PaleGoldenRod           =f"48;2;238;232;170"
DarkKhaki               =f"48;2;189;183;107"
Khaki                   =f"48;2;240;230;140"
Olive                   =f"48;2;128;128;0"
Yellow                  =f"48;2;255;255;0"
YellowGreen             =f"48;2;154;205;50"
DarkOliveGreen          =f"48;2;85;107;47"
OliveDrab               =f"48;2;107;142;35"
LawnGreen               =f"48;2;124;252;0"
Chartreuse              =f"48;2;127;255;0"
GreenYellow             =f"48;2;173;255;47"
DarkGreen               =f"48;2;0;100;0"
Green                   =f"48;2;0;128;0"
ForestGreen             =f"48;2;34;139;34"
Lime                    =f"48;2;0;255;0"
LimeGreen               =f"48;2;50;205;50"
LightGreen              =f"48;2;144;238;144"
PaleGreen               =f"48;2;152;251;152"
DarkSeaGreen            =f"48;2;143;188;143"
MediumSpringGreen       =f"48;2;0;250;154"
SpringGreen             =f"48;2;0;255;127"
SeaGreen                =f"48;2;46;139;87"
MediumAquaMarine        =f"48;2;102;205;170"
MediumSeaGreen          =f"48;2;60;179;113"
LightSeaGreen           =f"48;2;32;178;170"
DarkSlateGray           =f"48;2;47;79 ;79"
Teal                    =f"48;2;0;128;128"
DarkCyan                =f"48;2;0;139;139"
Aqua                    =f"48;2;0;255;255"
Cyan                    =f"48;2;0;255;255"
LightCyan               =f"48;2;224;255;255"
DarkTurquoise           =f"48;2;0;206;209"
Turquoise               =f"48;2;64;224;208"
MediumTurquoise         =f"48;2;72;209;204"
PaleTurquoise           =f"48;2;175;238;238"
AquaMarine              =f"48;2;127;255;212"
PowderBlue              =f"48;2;176;224;230"
CadetBlue               =f"48;2;95;158;160"
SteelBlue               =f"48;2;70;130;180"
CornFlowerBlue          =f"48;2;100;149;237"
DeepSkyBlue             =f"48;2;0;191;255"
DodgerBlue              =f"48;2;30;144;255"
LightBlue               =f"48;2;173;216;230"
SkyBlue                 =f"48;2;135;206;235"
LightSkyBlue            =f"48;2;135;206;250"
MidnightBlue            =f"48;2;25;25;112"
Navy                    =f"48;2;0;0;128"
DarkBlue                =f"48;2;0;0;139"
MediumBlue              =f"48;2;0;0;205"
Blue                    =f"48;2;0;0;255"
RoyalBlue               =f"48;2;65;105;225"
BlueViolet              =f"48;2;138;43;226"
Indigo                  =f"48;2;75;0;130"
DarkSlateBlue           =f"48;2;72;61;139"
SlateBlue               =f"48;2;106;90;205"
MediumSlateBlue         =f"48;2;123;104;238"
MediumPurple            =f"48;2;147;112;219"
DarkMagenta             =f"48;2;139;0;139"
DarkViolet              =f"48;2;148;0;211"
DarkOrchid              =f"48;2;153;50;204"
MediumOrchid            =f"48;2;186;85;211"
Purple                  =f"48;2;128;0;128"
Thistle                 =f"48;2;216;191;216"
Plum                    =f"48;2;221;160;221"
Violet                  =f"48;2;238;130;238"
Magenta                 =f"48;2;255;0;255"
Orchid                  =f"48;2;218;112;214"
MediumVioletRed         =f"48;2;199;21;133"
PaleVioletRed           =f"48;2;219;112;147"
DeepPink                =f"48;2;255;20;147"
HotPink                 =f"48;2;255;105;180"
LightPink               =f"48;2;255;182;193"
Pink                    =f"48;2;255;192;203"
AntiqueWhite            =f"48;2;250;235;215"
Beige                   =f"48;2;245;245;220"
Bisque                  =f"48;2;255;228;196"
BlanchedAlmond	        =f"48;2;255;235;205"
Wheat                   =f"48;2;245;222;179"
CornSilk                =f"48;2;255;248;220"
LemonChiffon            =f"48;2;255;250;205"
LightGoldenRodYellow    =f"48;2;250;250;210"
LightYellow             =f"48;2;255;255;224"
SaddleBrown             =f"48;2;139;69;19"
Sienna                  =f"48;2;160;82;45"
Chocolate               =f"48;2;210;105;30"
Peru                    =f"48;2;205;133;63"
SandyBrown              =f"48;2;244;164;96"
BurlyWood               =f"48;2;222;184;135"
Tan                     =f"48;2;210;180;140"
RosyBrown               =f"48;2;188;143;143"
Moccasin                =f"48;2;255;228;181"
NavajoWhite             =f"48;2;255;222;173"
PeachPuff               =f"48;2;255;218;185"
MistyRose               =f"48;2;255;228;225"
LavenderBlush           =f"48;2;255;240;245"
Linen                   =f"48;2;250;240;230"
OldLace                 =f"48;2;253;245;230"
PapayaWhip              =f"48;2;255;239;213"
WeaShell                =f"48;2;255;245;238"
MintCream               =f"48;2;245;255;250"
SlateGray               =f"48;2;112;128;144"
LightSlateGray          =f"48;2;119;136;153"
LightSteelBlue          =f"48;2;176;196;222"
Lavender                =f"48;2;230;230;250"
FloralWhite             =f"48;2;255;250;240"
AliceBlue               =f"48;2;240;248;255"
GhostWhite              =f"48;2;248;248;255"
Honeydew                =f"48;2;240;255;240"
Ivory                   =f"48;2;255;255;240"
Azure                   =f"48;2;240;255;255"
Snow                    =f"48;2;255;250;250"
Black                   =f"48;2;0;0;0"
DimGray                 =f"48;2;105;105;105"
Gray	                =f"48;2;128;128;128"
DarkGray	            =f"48;2;169;169;169"
Silver	                =f"48;2;192;192;192"
LightGray	            =f"48;2;211;211;211"
Gainsboro               =f"48;2;220;220;220"
WhiteSmoke              =f"48;2;245;245;245"
White                   =f"48;2;255;255;255"

class BackNest:
    # ------------------------------------------------------------------------------------------------------------------
    # - Methods -
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def custom(*obj, color:RGB|HEX, **kwargs) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        color = StrictType(color,(RGB,HEX))
        return NestedColorSequence(
            *obj,
            control_code=f"48;2;{color.r};{color.g};{color.b}",
            reset_code=resetCode,
            **kwargs
        )

    @staticmethod
    def rgb(*obj, r:int,g:int,b:int, **kwargs) -> str:
        # Don't rely on init.stringSeparation as the ANSI code rely on it being a ';'
        r,g,b =  NormalizeRgb(r, g, b)
        return NestedColorSequence(
            *obj,
            control_code=f"48;2;{r};{g};{b}",
            reset_code=resetCode,
            **kwargs
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - HTML colors -
    # ------------------------------------------------------------------------------------------------------------------
    # No partial methods, as this was increase the speed impact 2-fold
    @staticmethod
    def Maroon(*obj, sep=sep_):              return NCS(obj,Maroon,resetCode,sep)
    @staticmethod
    def DarkRed(*obj, sep=sep_):             return NCS(obj,DarkRed,resetCode,sep)
    @staticmethod
    def Brown(*obj, sep=sep_):               return NCS(obj,Brown,resetCode,sep)
    @staticmethod
    def Firebrick(*obj, sep=sep_):           return NCS(obj,Firebrick,resetCode,sep)
    @staticmethod
    def Crimson(*obj, sep=sep_):             return NCS(obj,Crimson,resetCode,sep)
    @staticmethod
    def Red(*obj, sep=sep_):                 return NCS(obj,Red,resetCode,sep)
    @staticmethod
    def Tomato(*obj, sep=sep_):              return NCS(obj,Tomato,resetCode,sep)
    @staticmethod
    def Coral(*obj, sep=sep_):               return NCS(obj,Coral,resetCode,sep)
    @staticmethod
    def IndianRed(*obj, sep=sep_):           return NCS(obj,IndianRed,resetCode,sep)
    @staticmethod
    def LightCoral(*obj, sep=sep_):          return NCS(obj,LightCoral,resetCode,sep)
    @staticmethod
    def DarkSalmon(*obj, sep=sep_):          return NCS(obj,DarkSalmon,resetCode,sep)
    @staticmethod
    def Salmon(*obj, sep=sep_):              return NCS(obj,Salmon,resetCode,sep)
    @staticmethod
    def LightSalmon(*obj, sep=sep_):         return NCS(obj,LightSalmon,resetCode,sep)
    @staticmethod
    def OrangeRed(*obj, sep=sep_):           return NCS(obj,OrangeRed,resetCode,sep)
    @staticmethod
    def DarkOrange(*obj, sep=sep_):          return NCS(obj,DarkOrange,resetCode,sep)
    @staticmethod
    def Orange(*obj, sep=sep_):              return NCS(obj,Orange,resetCode,sep)
    @staticmethod
    def Gold(*obj, sep=sep_):                return NCS(obj,Gold,resetCode,sep)
    @staticmethod
    def DarkGoldenRod(*obj, sep=sep_):       return NCS(obj,DarkGoldenRod,resetCode,sep)
    @staticmethod
    def GoldenRod(*obj, sep=sep_):           return NCS(obj,GoldenRod,resetCode,sep)
    @staticmethod
    def PaleGoldenRod(*obj, sep=sep_):       return NCS(obj,PaleGoldenRod,resetCode,sep)
    @staticmethod
    def DarkKhaki(*obj, sep=sep_):           return NCS(obj,DarkKhaki,resetCode,sep)
    @staticmethod
    def Khaki(*obj, sep=sep_):               return NCS(obj,Khaki,resetCode,sep)
    @staticmethod
    def Olive(*obj, sep=sep_):               return NCS(obj,Olive,resetCode,sep)
    @staticmethod
    def Yellow(*obj, sep=sep_):              return NCS(obj,Yellow,resetCode,sep)
    @staticmethod
    def YellowGreen(*obj, sep=sep_):         return NCS(obj,YellowGreen,resetCode,sep)
    @staticmethod
    def DarkOliveGreen(*obj, sep=sep_):      return NCS(obj,DarkOliveGreen,resetCode,sep)
    @staticmethod
    def OliveDrab(*obj, sep=sep_):           return NCS(obj,OliveDrab,resetCode,sep)
    @staticmethod
    def LawnGreen(*obj, sep=sep_):           return NCS(obj,LawnGreen,resetCode,sep)
    @staticmethod
    def Chartreuse(*obj, sep=sep_):          return NCS(obj,Chartreuse,resetCode,sep)
    @staticmethod
    def GreenYellow(*obj, sep=sep_):         return NCS(obj,GreenYellow,resetCode,sep)
    @staticmethod
    def DarkGreen(*obj, sep=sep_):           return NCS(obj,DarkGreen,resetCode,sep)
    @staticmethod
    def Green(*obj, sep=sep_):               return NCS(obj,Green,resetCode,sep)
    @staticmethod
    def ForestGreen(*obj, sep=sep_):         return NCS(obj,ForestGreen,resetCode,sep)
    @staticmethod
    def Lime(*obj, sep=sep_):                return NCS(obj,Lime,resetCode,sep)
    @staticmethod
    def LimeGreen(*obj, sep=sep_):           return NCS(obj,LimeGreen,resetCode,sep)
    @staticmethod
    def LightGreen(*obj, sep=sep_):          return NCS(obj,LightGreen,resetCode,sep)
    @staticmethod
    def PaleGreen(*obj, sep=sep_):           return NCS(obj,PaleGreen,resetCode,sep)
    @staticmethod
    def DarkSeaGreen(*obj, sep=sep_):        return NCS(obj,DarkSeaGreen,resetCode,sep)
    @staticmethod
    def MediumSpringGreen(*obj, sep=sep_):   return NCS(obj,MediumSpringGreen,resetCode,sep)
    @staticmethod
    def SpringGreen(*obj, sep=sep_):         return NCS(obj,SpringGreen,resetCode,sep)
    @staticmethod
    def SeaGreen(*obj, sep=sep_):            return NCS(obj,SeaGreen,resetCode,sep)
    @staticmethod
    def MediumAquaMarine(*obj, sep=sep_):    return NCS(obj,MediumAquaMarine,resetCode,sep)
    @staticmethod
    def MediumSeaGreen(*obj, sep=sep_):      return NCS(obj,MediumSeaGreen,resetCode,sep)
    @staticmethod
    def LightSeaGreen(*obj, sep=sep_):       return NCS(obj,LightSeaGreen,resetCode,sep)
    @staticmethod
    def DarkSlateGray(*obj, sep=sep_):       return NCS(obj,DarkSlateGray,resetCode,sep)
    @staticmethod
    def Teal(*obj, sep=sep_):                return NCS(obj,Teal,resetCode,sep)
    @staticmethod
    def DarkCyan(*obj, sep=sep_):            return NCS(obj,DarkCyan,resetCode,sep)
    @staticmethod
    def Aqua(*obj, sep=sep_):                return NCS(obj,Aqua,resetCode,sep)
    @staticmethod
    def Cyan(*obj, sep=sep_):                return NCS(obj,Cyan,resetCode,sep)
    @staticmethod
    def LightCyan(*obj, sep=sep_):           return NCS(obj,LightCyan,resetCode,sep)
    @staticmethod
    def DarkTurquoise(*obj, sep=sep_):       return NCS(obj,DarkTurquoise,resetCode,sep)
    @staticmethod
    def Turquoise(*obj, sep=sep_):           return NCS(obj,Turquoise,resetCode,sep)
    @staticmethod
    def MediumTurquoise(*obj, sep=sep_):     return NCS(obj,MediumTurquoise,resetCode,sep)
    @staticmethod
    def PaleTurquoise(*obj, sep=sep_):       return NCS(obj,PaleTurquoise,resetCode,sep)
    @staticmethod
    def AquaMarine(*obj, sep=sep_):          return NCS(obj,AquaMarine,resetCode,sep)
    @staticmethod
    def PowderBlue(*obj, sep=sep_):          return NCS(obj,PowderBlue,resetCode,sep)
    @staticmethod
    def CadetBlue(*obj, sep=sep_):           return NCS(obj,CadetBlue,resetCode,sep)
    @staticmethod
    def SteelBlue(*obj, sep=sep_):           return NCS(obj,SteelBlue,resetCode,sep)
    @staticmethod
    def CornFlowerBlue(*obj, sep=sep_):      return NCS(obj,CornFlowerBlue,resetCode,sep)
    @staticmethod
    def DeepSkyBlue(*obj, sep=sep_):         return NCS(obj,DeepSkyBlue,resetCode,sep)
    @staticmethod
    def DodgerBlue(*obj, sep=sep_):          return NCS(obj,DodgerBlue,resetCode,sep)
    @staticmethod
    def LightBlue(*obj, sep=sep_):           return NCS(obj,LightBlue,resetCode,sep)
    @staticmethod
    def SkyBlue(*obj, sep=sep_):             return NCS(obj,SkyBlue,resetCode,sep)
    @staticmethod
    def LightSkyBlue(*obj, sep=sep_):        return NCS(obj,LightSkyBlue,resetCode,sep)
    @staticmethod
    def MidnightBlue(*obj, sep=sep_):        return NCS(obj,MidnightBlue,resetCode,sep)
    @staticmethod
    def Navy(*obj, sep=sep_):                return NCS(obj,Navy,resetCode,sep)
    @staticmethod
    def DarkBlue(*obj, sep=sep_):            return NCS(obj,DarkBlue,resetCode,sep)
    @staticmethod
    def MediumBlue(*obj, sep=sep_):          return NCS(obj,MediumBlue,resetCode,sep)
    @staticmethod
    def Blue(*obj, sep=sep_):                return NCS(obj,Blue,resetCode,sep)
    @staticmethod
    def RoyalBlue(*obj, sep=sep_):           return NCS(obj,RoyalBlue,resetCode,sep)
    @staticmethod
    def BlueViolet(*obj, sep=sep_):          return NCS(obj,BlueViolet,resetCode,sep)
    @staticmethod
    def Indigo(*obj, sep=sep_):              return NCS(obj,Indigo,resetCode,sep)
    @staticmethod
    def DarkSlateBlue(*obj, sep=sep_):       return NCS(obj,DarkSlateBlue,resetCode,sep)
    @staticmethod
    def SlateBlue(*obj, sep=sep_):           return NCS(obj,SlateBlue,resetCode,sep)
    @staticmethod
    def MediumSlateBlue(*obj, sep=sep_):     return NCS(obj,MediumSlateBlue,resetCode,sep)
    @staticmethod
    def MediumPurple(*obj, sep=sep_):        return NCS(obj,MediumPurple,resetCode,sep)
    @staticmethod
    def DarkMagenta(*obj, sep=sep_):         return NCS(obj,DarkMagenta,resetCode,sep)
    @staticmethod
    def DarkViolet(*obj, sep=sep_):          return NCS(obj,DarkViolet,resetCode,sep)
    @staticmethod
    def DarkOrchid(*obj, sep=sep_):          return NCS(obj,DarkOrchid,resetCode,sep)
    @staticmethod
    def MediumOrchid(*obj, sep=sep_):        return NCS(obj,MediumOrchid,resetCode,sep)
    @staticmethod
    def Purple(*obj, sep=sep_):              return NCS(obj,Purple,resetCode,sep)
    @staticmethod
    def Thistle(*obj, sep=sep_):             return NCS(obj,Thistle,resetCode,sep)
    @staticmethod
    def Plum(*obj, sep=sep_):                return NCS(obj,Plum,resetCode,sep)
    @staticmethod
    def Violet(*obj, sep=sep_):              return NCS(obj,Violet,resetCode,sep)
    @staticmethod
    def Magenta(*obj, sep=sep_):             return NCS(obj,Magenta,resetCode,sep)
    @staticmethod
    def Orchid(*obj, sep=sep_):              return NCS(obj,Orchid,resetCode,sep)
    @staticmethod
    def MediumVioletRed(*obj, sep=sep_):     return NCS(obj,MediumVioletRed,resetCode,sep)
    @staticmethod
    def PaleVioletRed(*obj, sep=sep_):       return NCS(obj,PaleVioletRed,resetCode,sep)
    @staticmethod
    def DeepPink(*obj, sep=sep_):            return NCS(obj,DeepPink,resetCode,sep)
    @staticmethod
    def HotPink(*obj, sep=sep_):             return NCS(obj,HotPink,resetCode,sep)
    @staticmethod
    def LightPink(*obj, sep=sep_):           return NCS(obj,LightPink,resetCode,sep)
    @staticmethod
    def Pink(*obj, sep=sep_):                return NCS(obj,Pink,resetCode,sep)
    @staticmethod
    def AntiqueWhite(*obj, sep=sep_):        return NCS(obj,AntiqueWhite,resetCode,sep)
    @staticmethod
    def Beige(*obj, sep=sep_):               return NCS(obj,Beige,resetCode,sep)
    @staticmethod
    def Bisque(*obj, sep=sep_):              return NCS(obj,Bisque,resetCode,sep)
    @staticmethod
    def BlanchedAlmond(*obj, sep=sep_):      return NCS(obj,BlanchedAlmond,resetCode,sep)
    @staticmethod
    def Wheat(*obj, sep=sep_):               return NCS(obj,Wheat,resetCode,sep)
    @staticmethod
    def CornSilk(*obj, sep=sep_):            return NCS(obj,CornSilk,resetCode,sep)
    @staticmethod
    def LemonChiffon(*obj, sep=sep_):        return NCS(obj,LemonChiffon,resetCode,sep)
    @staticmethod
    def LightGoldenRodYellow(*obj, sep=sep_):return NCS(obj,LightGoldenRodYellow,resetCode,sep)
    @staticmethod
    def LightYellow(*obj, sep=sep_):         return NCS(obj,LightYellow,resetCode,sep)
    @staticmethod
    def SaddleBrown(*obj, sep=sep_):         return NCS(obj,SaddleBrown,resetCode,sep)
    @staticmethod
    def Sienna(*obj, sep=sep_):              return NCS(obj,Sienna,resetCode,sep)
    @staticmethod
    def Chocolate(*obj, sep=sep_):           return NCS(obj,Chocolate,resetCode,sep)
    @staticmethod
    def Peru(*obj, sep=sep_):                return NCS(obj,Peru,resetCode,sep)
    @staticmethod
    def SandyBrown(*obj, sep=sep_):          return NCS(obj,SandyBrown,resetCode,sep)
    @staticmethod
    def BurlyWood(*obj, sep=sep_):           return NCS(obj,BurlyWood,resetCode,sep)
    @staticmethod
    def Tan(*obj, sep=sep_):                 return NCS(obj,Tan,resetCode,sep)
    @staticmethod
    def RosyBrown(*obj, sep=sep_):           return NCS(obj,RosyBrown,resetCode,sep)
    @staticmethod
    def Moccasin(*obj, sep=sep_):            return NCS(obj,Moccasin,resetCode,sep)
    @staticmethod
    def NavajoWhite(*obj, sep=sep_):         return NCS(obj,NavajoWhite,resetCode,sep)
    @staticmethod
    def PeachPuff(*obj, sep=sep_):           return NCS(obj,PeachPuff,resetCode,sep)
    @staticmethod
    def MistyRose(*obj, sep=sep_):           return NCS(obj,MistyRose,resetCode,sep)
    @staticmethod
    def LavenderBlush(*obj, sep=sep_):       return NCS(obj,LavenderBlush,resetCode,sep)
    @staticmethod
    def Linen(*obj, sep=sep_):               return NCS(obj,Linen,resetCode,sep)
    @staticmethod
    def OldLace(*obj, sep=sep_):             return NCS(obj,OldLace,resetCode,sep)
    @staticmethod
    def PapayaWhip(*obj, sep=sep_):          return NCS(obj,PapayaWhip,resetCode,sep)
    @staticmethod
    def WeaShell(*obj, sep=sep_):            return NCS(obj,WeaShell,resetCode,sep)
    @staticmethod
    def MintCream(*obj, sep=sep_):           return NCS(obj,MintCream,resetCode,sep)
    @staticmethod
    def SlateGray(*obj, sep=sep_):           return NCS(obj,SlateGray,resetCode,sep)
    @staticmethod
    def LightSlateGray(*obj, sep=sep_):      return NCS(obj,LightSlateGray,resetCode,sep)
    @staticmethod
    def LightSteelBlue(*obj, sep=sep_):      return NCS(obj,LightSteelBlue,resetCode,sep)
    @staticmethod
    def Lavender(*obj, sep=sep_):            return NCS(obj,Lavender,resetCode,sep)
    @staticmethod
    def FloralWhite(*obj, sep=sep_):         return NCS(obj,FloralWhite,resetCode,sep)
    @staticmethod
    def AliceBlue(*obj, sep=sep_):           return NCS(obj,AliceBlue,resetCode,sep)
    @staticmethod
    def GhostWhite(*obj, sep=sep_):          return NCS(obj,GhostWhite,resetCode,sep)
    @staticmethod
    def Honeydew(*obj, sep=sep_):            return NCS(obj,Honeydew,resetCode,sep)
    @staticmethod
    def Ivory(*obj, sep=sep_):               return NCS(obj,Ivory,resetCode,sep)
    @staticmethod
    def Azure(*obj, sep=sep_):               return NCS(obj,Azure,resetCode,sep)
    @staticmethod
    def Snow(*obj, sep=sep_):                return NCS(obj,Snow,resetCode,sep)
    @staticmethod
    def Black(*obj, sep=sep_):               return NCS(obj,Black,resetCode,sep)
    @staticmethod
    def DimGray(*obj, sep=sep_):             return NCS(obj,DimGray,resetCode,sep)
    @staticmethod
    def Gray(*obj, sep=sep_):                return NCS(obj,Gray,resetCode,sep)
    @staticmethod
    def DarkGray(*obj, sep=sep_):            return NCS(obj,DarkGray,resetCode,sep)
    @staticmethod
    def Silver(*obj, sep=sep_):              return NCS(obj,Silver,resetCode,sep)
    @staticmethod
    def LightGray(*obj, sep=sep_):           return NCS(obj,LightGray,resetCode,sep)
    @staticmethod
    def Gainsboro(*obj, sep=sep_):           return NCS(obj,Gainsboro,resetCode,sep)
    @staticmethod
    def WhiteSmoke(*obj, sep=sep_):          return NCS(obj,WhiteSmoke,resetCode,sep)
    @staticmethod
    def White(*obj, sep=sep_):               return NCS(obj,White,resetCode,sep)