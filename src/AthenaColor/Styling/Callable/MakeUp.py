# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor import init
from AthenaColor.BASE import end_codes


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
esc = init.esc
end = end_codes.color

def Reset                       (*obj) -> str: return ''.join([f'{esc}[0{end}' ,*[o+ f'{esc}[0{end}'  for o in obj],f''                ])
def Bold                        (*obj) -> str: return ''.join([f'{esc}[1{end}' ,*[o+ f'{esc}[1{end}'  for o in obj],f'{esc}[22{end}'   ])
def NoBold                      (*obj) -> str: return ''.join([f'{esc}[22{end}',*[o+ f'{esc}[22{end}' for o in obj],f'{esc}[1{end}'    ])
def Dim                         (*obj) -> str: return ''.join([f'{esc}[2{end}' ,*[o+ f'{esc}[2{end}'  for o in obj],f'{esc}[22{end}'   ])
def NoDim                       (*obj) -> str: return ''.join([f'{esc}[22{end}',*[o+ f'{esc}[22{end}' for o in obj],f'{esc}[2{end}'    ])
def Italic                      (*obj) -> str: return ''.join([f'{esc}[3{end}' ,*[o+ f'{esc}[3{end}'  for o in obj],f'{esc}[23{end}'   ])
def NoItalic                    (*obj) -> str: return ''.join([f'{esc}[23{end}',*[o+ f'{esc}[23{end}' for o in obj],f'{esc}[3{end}'    ])
def Underline                   (*obj) -> str: return ''.join([f'{esc}[4{end}' ,*[o+ f'{esc}[4{end}'  for o in obj],f'{esc}[24{end}'   ])
def NoUnderline                 (*obj) -> str: return ''.join([f'{esc}[24{end}',*[o+ f'{esc}[24{end}' for o in obj],f'{esc}[4{end}'    ])
def BlinkSlow                   (*obj) -> str: return ''.join([f'{esc}[5{end}' ,*[o+ f'{esc}[5{end}'  for o in obj],f'{esc}[25{end}'   ])      # NOT WORKING PYCHARM
def NoBlinkSlow                 (*obj) -> str: return ''.join([f'{esc}[25{end}',*[o+ f'{esc}[25{end}' for o in obj],f'{esc}[5{end}'    ])    # NOT WORKING PYCHARM
def BlinkRapid                  (*obj) -> str: return ''.join([f'{esc}[6{end}' ,*[o+ f'{esc}[6{end}'  for o in obj],f'{esc}[25{end}'   ])      # NOT WORKING PYCHARM
def NoBlinkRapid                (*obj) -> str: return ''.join([f'{esc}[25{end}',*[o+ f'{esc}[25{end}' for o in obj],f'{esc}[6{end}'    ])    # NOT WORKING PYCHARM
def Reversed                    (*obj) -> str: return ''.join([f'{esc}[7{end}' ,*[o+ f'{esc}[7{end}'  for o in obj],f'{esc}[27{end}'   ])
def NoReversed                  (*obj) -> str: return ''.join([f'{esc}[27{end}',*[o+ f'{esc}[27{end}' for o in obj],f'{esc}[7{end}'    ])
def Conceal                     (*obj) -> str: return ''.join([f'{esc}[8{end}' ,*[o+ f'{esc}[8{end}'  for o in obj],f'{esc}[28{end}'   ])      # NOT WORKING PYCHARM
def NoConceal                   (*obj) -> str: return ''.join([f'{esc}[28{end}',*[o+ f'{esc}[28{end}' for o in obj],f'{esc}[8{end}'    ])    # NOT WORKING PYCHARM
def Crossed                     (*obj) -> str: return ''.join([f'{esc}[9{end}' ,*[o+ f'{esc}[9{end}'  for o in obj],f'{esc}[29{end}'   ])
def NoCrossed                   (*obj) -> str: return ''.join([f'{esc}[29{end}',*[o+ f'{esc}[29{end}' for o in obj],f'{esc}[9{end}'    ])
def FontPrimary                 (*obj) -> str: return ''.join([f'{esc}[10{end}',*[o+ f'{esc}[10{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond1                 (*obj) -> str: return ''.join([f'{esc}[11{end}',*[o+ f'{esc}[11{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond2                 (*obj) -> str: return ''.join([f'{esc}[12{end}',*[o+ f'{esc}[12{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond3                 (*obj) -> str: return ''.join([f'{esc}[13{end}',*[o+ f'{esc}[13{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond4                 (*obj) -> str: return ''.join([f'{esc}[14{end}',*[o+ f'{esc}[14{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond5                 (*obj) -> str: return ''.join([f'{esc}[15{end}',*[o+ f'{esc}[15{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond6                 (*obj) -> str: return ''.join([f'{esc}[16{end}',*[o+ f'{esc}[16{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond8                 (*obj) -> str: return ''.join([f'{esc}[17{end}',*[o+ f'{esc}[17{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond9                 (*obj) -> str: return ''.join([f'{esc}[18{end}',*[o+ f'{esc}[18{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def FontSecond10                (*obj) -> str: return ''.join([f'{esc}[19{end}',*[o+ f'{esc}[19{end}' for o in obj],f'{esc}[10{end}'   ])     # NOT WORKING PYCHARM
def NoFont                      (*obj) -> str: return ''.join([f'{esc}[10{end}',*[o+ f'{esc}[10{end}' for o in obj]                    ])     # NOT WORKING PYCHARM
def Fraktur                     (*obj) -> str: return ''.join([f'{esc}[20{end}',*[o+ f'{esc}[20{end}' for o in obj]                    ])        # NOT WORKING PYCHARM
def UnderlineDouble             (*obj) -> str: return ''.join([f'{esc}[21{end}',*[o+ f'{esc}[21{end}' for o in obj],f'{esc}[24{end}'   ])
def NoUnderlineDouble           (*obj) -> str: return ''.join([f'{esc}[24{end}',*[o+ f'{esc}[24{end}' for o in obj],f'{esc}[21{end}'   ])
def PropSpacing                 (*obj) -> str: return ''.join([f'{esc}[26{end}',*[o+ f'{esc}[26{end}' for o in obj],f'{esc}[26{end}'   ])     # NOT WORKING PYCHARM
def NoPropSpacing               (*obj) -> str: return ''.join([f'{esc}[26{end}',*[o+ f'{esc}[26{end}' for o in obj],f'{esc}[26{end}'   ])     # NOT WORKING PYCHARM
def NoForeground                (*obj) -> str: return ''.join([f'{esc}[39m'    ,*[o+ f'{esc}[39m'     for o in obj],f''                ])
def NoBackground                (*obj) -> str: return ''.join([f'{esc}[49{end}',*[o+ f'{esc}[49{end}' for o in obj],f''                ])
def Frame                       (*obj) -> str: return ''.join([f'{esc}[51{end}',*[o+ f'{esc}[51{end}' for o in obj],f'{esc}[54{end}'   ])
def NoFrame                     (*obj) -> str: return ''.join([f'{esc}[54{end}',*[o+ f'{esc}[54{end}' for o in obj],f'{esc}[51{end}'   ])
def Circle                      (*obj) -> str: return ''.join([f'{esc}[52{end}',*[o+ f'{esc}[52{end}' for o in obj],f'{esc}[54{end}'   ])
def NoCircle                    (*obj) -> str: return ''.join([f'{esc}[54{end}',*[o+ f'{esc}[54{end}' for o in obj],f'{esc}[52{end}'   ])
def OverLine                    (*obj) -> str: return ''.join([f'{esc}[53{end}',*[o+ f'{esc}[53{end}' for o in obj],f'{esc}[55{end}'   ])
def NoOverLine                  (*obj) -> str: return ''.join([f'{esc}[55{end}',*[o+ f'{esc}[55{end}' for o in obj],f'{esc}[53{end}'   ])
def UnderColourDefault          (*obj) -> str: return ''.join([f'{esc}[59{end}',*[o+ f'{esc}[59{end}' for o in obj],f''                ])
def IdeogramUnderLine           (*obj) -> str: return ''.join([f'{esc}[60{end}',*[o+ f'{esc}[60{end}' for o in obj],f'{esc}[65{end}'   ])
def IdeogramUnderLineDouble     (*obj) -> str: return ''.join([f'{esc}[61{end}',*[o+ f'{esc}[61{end}' for o in obj],f'{esc}[65{end}'   ])
def IdeogramOverLine            (*obj) -> str: return ''.join([f'{esc}[62{end}',*[o+ f'{esc}[62{end}' for o in obj],f'{esc}[65{end}'   ])
def IdeogramOverLineDouble      (*obj) -> str: return ''.join([f'{esc}[63{end}',*[o+ f'{esc}[63{end}' for o in obj],f'{esc}[65{end}'   ])
def IdeogramStress              (*obj) -> str: return ''.join([f'{esc}[64{end}',*[o+ f'{esc}[64{end}' for o in obj],f'{esc}[65{end}'   ])
def NoIdeogram                  (*obj) -> str: return ''.join([f'{esc}[65{end}',*[o+ f'{esc}[65{end}' for o in obj],f''                ])
def SuperScript                 (*obj) -> str: return ''.join([f'{esc}[73{end}',*[o+ f'{esc}[73{end}' for o in obj],f'{esc}[75{end}'   ])
def SubScript                   (*obj) -> str: return ''.join([f'{esc}[74{end}',*[o+ f'{esc}[74{end}' for o in obj],f'{esc}[75{end}'   ])
def NoScript                    (*obj) -> str: return ''.join([f'{esc}[75{end}',*[o+ f'{esc}[75{end}' for o in obj],f''                ])

class Basic:
    class Fore:
        def Black         (*obj) -> str: return ''.join([f"{esc}[30m", *[o+f"{esc}[30m" for o in obj], f'{esc}[39m'])
        def Red           (*obj) -> str: return ''.join([f"{esc}[31m", *[o+f"{esc}[31m" for o in obj], f'{esc}[39m'])
        def Green         (*obj) -> str: return ''.join([f"{esc}[32m", *[o+f"{esc}[32m" for o in obj], f'{esc}[39m'])
        def Yellow        (*obj) -> str: return ''.join([f"{esc}[33m", *[o+f"{esc}[33m" for o in obj], f'{esc}[39m'])
        def Blue          (*obj) -> str: return ''.join([f"{esc}[34m", *[o+f"{esc}[34m" for o in obj], f'{esc}[39m'])
        def Magenta       (*obj) -> str: return ''.join([f"{esc}[35m", *[o+f"{esc}[35m" for o in obj], f'{esc}[39m'])
        def Cyan          (*obj) -> str: return ''.join([f"{esc}[36m", *[o+f"{esc}[36m" for o in obj], f'{esc}[39m'])
        def White         (*obj) -> str: return ''.join([f"{esc}[37m", *[o+f"{esc}[37m" for o in obj], f'{esc}[39m'])
        def BrightBlack   (*obj) -> str: return ''.join([f"{esc}[90m", *[o+f"{esc}[90m" for o in obj], f'{esc}[39m'])
        def BrightRed     (*obj) -> str: return ''.join([f"{esc}[91m", *[o+f"{esc}[91m" for o in obj], f'{esc}[39m'])
        def BrightGreen   (*obj) -> str: return ''.join([f"{esc}[92m", *[o+f"{esc}[92m" for o in obj], f'{esc}[39m'])
        def BrightYellow  (*obj) -> str: return ''.join([f"{esc}[93m", *[o+f"{esc}[93m" for o in obj], f'{esc}[39m'])
        def BrightBlue    (*obj) -> str: return ''.join([f"{esc}[94m", *[o+f"{esc}[94m" for o in obj], f'{esc}[39m'])
        def BrightMagenta (*obj) -> str: return ''.join([f"{esc}[95m", *[o+f"{esc}[95m" for o in obj], f'{esc}[39m'])
        def BrightCyan    (*obj) -> str: return ''.join([f"{esc}[96m", *[o+f"{esc}[96m" for o in obj], f'{esc}[39m'])
        def BrightWhite   (*obj) -> str: return ''.join([f"{esc}[97m", *[o+f"{esc}[97m" for o in obj], f'{esc}[39m'])

    class Back:
        def Black         (*obj) -> str: return ''.join([f"{esc}[40m" , *[o+f"{esc}[40m"  for o in obj], f'{esc}[49m'])
        def Red           (*obj) -> str: return ''.join([f"{esc}[41m" , *[o+f"{esc}[41m"  for o in obj], f'{esc}[49m'])
        def Green         (*obj) -> str: return ''.join([f"{esc}[42m" , *[o+f"{esc}[42m"  for o in obj], f'{esc}[49m'])
        def Yellow        (*obj) -> str: return ''.join([f"{esc}[43m" , *[o+f"{esc}[43m"  for o in obj], f'{esc}[49m'])
        def Blue          (*obj) -> str: return ''.join([f"{esc}[44m" , *[o+f"{esc}[44m"  for o in obj], f'{esc}[49m'])
        def Magenta       (*obj) -> str: return ''.join([f"{esc}[45m" , *[o+f"{esc}[45m"  for o in obj], f'{esc}[49m'])
        def Cyan          (*obj) -> str: return ''.join([f"{esc}[46m" , *[o+f"{esc}[46m"  for o in obj], f'{esc}[49m'])
        def White         (*obj) -> str: return ''.join([f"{esc}[47m" , *[o+f"{esc}[47m"  for o in obj], f'{esc}[49m'])
        def BrightBlack   (*obj) -> str: return ''.join([f"{esc}[100m", *[o+f"{esc}[100m" for o in obj], f'{esc}[49m'])
        def BrightRed     (*obj) -> str: return ''.join([f"{esc}[101m", *[o+f"{esc}[101m" for o in obj], f'{esc}[49m'])
        def BrightGreen   (*obj) -> str: return ''.join([f"{esc}[102m", *[o+f"{esc}[102m" for o in obj], f'{esc}[49m'])
        def BrightYellow  (*obj) -> str: return ''.join([f"{esc}[103m", *[o+f"{esc}[103m" for o in obj], f'{esc}[49m'])
        def BrightBlue    (*obj) -> str: return ''.join([f"{esc}[104m", *[o+f"{esc}[104m" for o in obj], f'{esc}[49m'])
        def BrightMagenta (*obj) -> str: return ''.join([f"{esc}[105m", *[o+f"{esc}[105m" for o in obj], f'{esc}[49m'])
        def BrightCyan    (*obj) -> str: return ''.join([f"{esc}[106m", *[o+f"{esc}[106m" for o in obj], f'{esc}[49m'])
        def BrightWhite   (*obj) -> str: return ''.join([f"{esc}[107m", *[o+f"{esc}[107m" for o in obj], f'{esc}[49m'])
















