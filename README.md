# - Athena Color Package - v3.0.4
<img height="128" src="https://github.com/DirectiveAthena/VSC-AthenaColor/blob/master/Resources/AthenaColor.png?raw=true" width="128"/>
  
Python Package used to print rgb colors to the console


---  
## Details and features  
- Support for Fore- and Background colours  
- Support for Underline, Bold, Italic and other Text Styling  
- Custom rgb class with full support for math operators  
- All basic and extended web colors are available as the default predefined Fore and Back colors.
- Access to the full rgb spectrum to be printed to the console  
  
---  
  
## Usage  
The following import will print the underlying python code to console:
```python  
import AthenaColor.Help.readme
```

```python
# *-* Base Needed imports *-*
from AthenaColor import (
    Fore,   # All predefined Foreground colors
    Back,   # All predefined Background colors
    Style,  # All Style makeups
    rgb
)

# *-* Use the objects in an f-string *-*  
print(
f"""||| {Style.Bold}Welcome to the AthenaColor Package!{Style.Reset} |||  

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
```  
---  
## Links  
Project files can be found at:  
- [GitHub Repo](https://github.com/DirectiveAthena/AthenaColor)   
- [Pypi link](https://pypi.org/project/AthenaColor/)  
- [Full Version History](https://github.com/DirectiveAthena/VSC-AthenaColor/blob/master/Docu/Version%20History.md)
  
Pip installs by the following command:   
```  
pip install AthenaColor  
```  
Made By Andreas Sas, 2022