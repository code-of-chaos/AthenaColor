# AthenaColor Examples

## Nested Example:
Copy directly
```python
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
```

Or find the exact function:
```python
from AthenaColor.Help import example_nested
example_nested()
```

---
## Inline Example:

Copy directly
```python
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
```

Or find the exact function:
```python
from AthenaColor.Help import example_inline
example_inline()
```

---
## custom RGB Example:
Copy directly
```python
from AthenaColor import (  
    ForeNest,
    BackNest,
    RGB
)  

color1 = RGB(r=86, g=54, b=251)
color2 = RGB(214,124,61)

text = ForeNest.custom(BackNest.custom("This is a custom color",color=color2),color=color1)

print(text)
```

Or find the exact function:
```python
from AthenaColor.Help import example_rgb
example_rgb()
```