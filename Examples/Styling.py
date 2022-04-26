# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaColor import ForeNest, BackNest, StyleNest, Fore, Back, Style

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def Nested_General():
    print(
        StyleNest.Italic(ForeNest.SlateGray(
            "AthenaColor Example:",
            ForeNest.Red(
                "This is an",
                StyleNest.Bold("EXAMPLE"),
                "of nested styling"
            ),
            "As you can see, the correct color returns here by itself",
            sep="\n"
        ))
    )

def Inline_General():
    print(
f"""
{Style.Italic}{Fore.SlateGray}AthenaColor Example:{Style.NoForeground}
{Fore.Red}This is an {Style.Bold}EXAMPLE{Style.NoBold} of nested styling{Style.NoForeground}
{Fore.SlateGray}As you can see, the color needs to be manually returned here{Style.NoForeground}{Style.NoItalic}
"""
    )

if __name__ == '__main__':
    Nested_General()
    Inline_General()