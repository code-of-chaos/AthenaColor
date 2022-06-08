# - AthenaColor -
[![pypi](https://img.shields.io/pypi/v/AthenaColor)](https://pypi.org/project/AthenaColor/) [![GitHub license](https://img.shields.io/github/license/DirectiveAthena/VerSC-AthenaColor)](https://github.com/DirectiveAthena/VerSC-AthenaColor/blob/master/LICENSE) [![Discord](https://img.shields.io/discord/814599159926620160?color=maroon)](https://discord.gg/6JcDbhXkCH) [![Downloads](https://pepy.tech/badge/athenacolor)](https://pepy.tech/project/athenacolor)

<img height="128" src="https://github.com/DirectiveAthena/AthenaColor/blob/master/Resources/AthenaColor.png?raw=true" width="128" alt="AthenaColor Logo"/>

--- 
## Package Details
#### Details and features 
A *No Dependency* Python package do display stext styling in a console.
- Next to the full ability to use ANSI styling options, commonly used HTML color names are defined as default colors for Fore- and Background color styling
  - The color option are avaible permitting the console can take advantage of RGB ANSI codes
  - For a full list of all 140 out of the box available colors, go to [the full documentatio](https://publish.obsidian.md/directiveathena/Content/Programming/AthenaColor/Documentation/HTML+Named+Colors)
  - By using the `RGB` object, you have access to print any RGB color to the console you desire
- Uses a similar syntax to Colorama, but also allows for nested function patterns

#### Python Version
- Supported Python versions: **3.7**, **3.8**, **3.9**, **3.10**
  - Other older versions of Python are not currently supported. 
  - These older versions will probably not be supported by @AndreasSas himself, but if you want to contribute to the project and make this package compatible with older versions of Python, Pull requests are always welcome.

---
## Quick Examples
**Inline styling**:
```python
from AthenaColor import Fore, Style

print(  
    f"""  
    {Style.Italic}{Fore.SlateGray}AthenaColor Example:{Style.NoForeground}
    {Fore.Red}This is an of {Style.Bold}EXAMPLE{Style.NoBold} nested styling{Style.NoForeground}    
    {Fore.SlateGray}As you can see, the color needs to be manually returned here{Style.NoForeground}{Style.NoItalic}
    """  
)
```
**Nested Styling**:
```python
from AthenaColor import ForeNest, StyleNest

print(  
   StyleNest.Italic(ForeNest.SlateGray(  
       "AthenaColor Example:",  
       ForeNest.Red(  
           "This is an",  
           StyleNest.Bold("EXAMPLE"),  
           "of nested styling"  
       ),    
       "As you can see, a reset of color doesn't need to happen as this is done automatically",
       sep="\n"  
   ))  
)
```

---
## Documentation
Full documentation can be found at:
**[directiveathena.com/athenacolor-docu](https://www.directiveathena.com/athenacolor-docu)** (redirect to Obsidian.md publish site)
(Reminder, the documentation is still under heavy development)

---
## Install
To install the package in your Python environment

``` 
pip install AthenaColor --upgrade
```

---

## Links 
Project files can be found at:    
- [GitHub Repo](https://github.com/DirectiveAthena/AthenaColor)     
- [Pypi link](https://pypi.org/project/AthenaColor/)    

---

## Disclaimer
With  *No Dependency*, the standard library is not counted as a dependency

---
Made By Andreas Sas, 2022
