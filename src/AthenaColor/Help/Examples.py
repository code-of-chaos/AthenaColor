# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def example_nested():
    from AthenaColor import (
        ForeNest,
        BackNest,
        StyleNest
    )
    pre_formated = lambda t_: ForeNest.SkyBlue(StyleNest.Italic(BackNest.MidnightBlue(t_) ))

    text = ForeNest.GoldenRod(
        StyleNest.Italic("Hello there!"),
        ForeNest.PaleGoldenRod ("This is an example of",StyleNest.Bold("NESTED"),"styling"),
        "Here we have some Golden rod again",
        BackNest.DarkViolet("No matter the makeup, everything is closed correctly"),
        pre_formated("The style of this part was preformatted"),
        sep="\n"
    )
    print(text)

def example_inline():
    from AthenaColor import (
        Fore,
        Back,
        Style,
    )
    pre_formated = lambda t_: f"{Fore.SkyBlue}{Style.Italic}{Back.MidnightBlue}{t_}{Style.NoForeground}{Style.NoItalic}{Style.NoBackground}"

    text = \
f"""{Fore.GoldenRod}{Style.Italic}Hello there!{Style.NoItalic}{Style.NoForeground}
{Fore.PaleGoldenRod}This is an example of {Style.Bold}INLINE{Style.NoBold} styling{Style.NoForeground}
{Fore.GoldenRod}Here we have some Golden rod again{Style.NoForeground},
{Back.DarkViolet}{Fore.GoldenRod}Here we have to redefined colors and worry about resets{Style.NoForeground}{Style.NoBackground}
{pre_formated("The style of this part was preformatted")}
"""
    print(text)

def example_rgb():
    from AthenaColor import (
        ForeNest,
        BackNest,
        rgb
    )
    color1 = rgb(r=86, g=54, b=251)
    color2 = rgb(214,124,61)
    text = ForeNest.custom(BackNest.custom("This is a custom color",color=color2),color=color1)
    print(text)

if __name__ == '__main__':
    example_nested()
    print()
    example_inline()
    print()
    example_rgb()