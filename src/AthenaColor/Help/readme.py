def readme():
    # *-* Base Needed imports *-*
    from AthenaColor import (
        Fore,   # All predefined Foreground colors
        Back,   # All predefined Background colors
        Style,  # All Style makeups
        rgb,
    )

    # *-* Use the objects in an f-string *-*
    print(
f"""||| {Style.Bold}Welcome to the AthenaColor Package{Style.Reset} |||  

- The {Fore.HotPink}Fore.HotPink{Style.Reset} Changes the Foreground color  
- The {Back.Indigo}Back.Indigo{Style.Reset} changes the background color  
- Combinations like {Back.Teal}{Fore.LightGoldenRodYellow}Back.Teal + Fore.LightGoldenRodYellow{Style.Reset} are also supported  
- Using {Fore.custom(rgb(123,45,67))}Fore.custom(rgb(123,45,67)){Style.Reset} will allow you to use custom rgb colors
"""
    )

    # *-* Create your own rgb objects *-*
    custom_color = rgb(r=86, g=54, b=186)
    print(
f"""
{Fore.custom(custom_color)}Text with a newly made rgb object{Style.Reset}
{Fore.rgb(r=186, g=54, b=86)}Text without first making a custom rgb object{Style.Reset}
"""
    )

    # *-* Print out of all colours and Style Formats *-*
    from AthenaColor.Help import (
        AllTable,
        AllBoxes
    )

    print(
f"""
{Style.Bold}The following is a full list of all predefined colors.  
Together with all Style makeups found in AthenaColor.ConsolePrinter:{Style.Reset}
"""
    )

    AllTable()

    print(
f"""
{Style.Bold}The following is a small view of all predefined colors:{Style.Reset}
"""
    )

    AllBoxes()