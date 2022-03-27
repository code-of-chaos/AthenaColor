# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
from AthenaColor import (
    ForeNest  as Fore,
    BackNest  as Back,
    StyleNest as Style
)

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(
        Fore.Blue(
            "This is BLUE\n",
            Fore.Red("This should be RED\n"),
            "Please be Blue\n",
            Back.Crimson("Damm, this is important\n"),
            Fore.Lime(
                Style.Bold("PLEASE HELP ME\n"),
                Style.Underline("Lime HERE\n"),
            ),
            "Another Blue\n",
            Fore.Red("Another Red"),
        )
    )

    print(
        Style.Bold(
            "BOLD ",
            Style.Bold("BOLD "),
            "BOLD"
        ),
        "not"
    )
