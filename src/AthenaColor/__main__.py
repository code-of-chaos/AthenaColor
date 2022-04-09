# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
import AthenaColor

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    print(f"{AthenaColor.Fore.Crimson}This is a test{AthenaColor.Style.Reset}")
    print(AthenaColor.ForeNest.Azure(
        "help",
        AthenaColor.StyleNest.Bold(
            "this is a test"
        ),
        "yahoo!"
    ))

    color1 = AthenaColor.RGB(1,2,3)
    print(color1)
    print(repr(color1))
    color2 = AthenaColor.HSV(60,.3,.8)
    print(color2)
    print(repr(color2))
    print(repr(color1 - color2))
    print(repr(color2 ** color2))
    print(repr(color1 // color2))
    print(repr(color2 % color1))
    print(repr(color1 * color2))


    pass

if __name__ == '__main__':
    main()