```python
from AthenaColor import (
	Fore, # Foreground colors
	Back, #	Background colors
	Reset # Reset tag, to be used at the end of the printed text
) 
import AthenaColor.GraphicMakeup as GM

print(f"{Fore.HotPink}This is a test {Reset}")
print(f"{Fore.DodgerBlue + GM.Bold}This is a second test{Reset}")
```