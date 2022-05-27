# - AthenaColor -
[![pypi](https://img.shields.io/pypi/v/AthenaColor)](https://pypi.org/project/AthenaColor/) [![GitHub license](https://img.shields.io/github/license/DirectiveAthena/VerSC-AthenaColor)](https://github.com/DirectiveAthena/VerSC-AthenaColor/blob/master/LICENSE) [![Discord](https://img.shields.io/discord/814599159926620160?color=maroon)](https://discord.gg/6JcDbhXkCH) [![Downloads](https://pepy.tech/badge/athenacolor)](https://pepy.tech/project/athenacolor)

<img height="128" src="https://github.com/DirectiveAthena/VSC-AthenaColor/blob/master/Resources/AthenaColor.png?raw=true" width="128"/>

A *No Dependency* python package for displaying the full spectrum of RGB colors in the Console.

--- 
## Details and features 
- *Nested* and *Inline* options to print StyleNest and Color makeup to the Console
- 140 predefined extended HTML colors
- By using the `RGB` object, you have access to print any RGB color to the console you desire

---
## Quick Examples
Inline styling:
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
Nested Styling:
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
       "As you can see, the correct color returns here by itself",
       sep="\n"  
   ))  
)
```

---
## Documentation
Full documentation can be found at:
**[directiveathena.com/athenacolor-docu](https://www.directiveathena.com/athenacolor-docu)** (redirect to Obsidian.md publish site)

---
## Install
To install the package in your Python environment

```console 
pip install AthenaColor --upgrade
```

---

## Links 
Project files can be found at:    
- [GitHub Repo](https://github.com/DirectiveAthena/VerSC-AthenaColor)     
- [Pypi link](https://pypi.org/project/AthenaColor/)    

---

## Disclaimer
With  *No Dependency*, the standard library is not counted as a dependency

---
Made By Andreas Sas, 2022
