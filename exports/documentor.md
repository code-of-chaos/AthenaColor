#class AthenaColor.**Basic**()

*`-!- Missing documentation -!-`*

**Fore**()

*`-!- Missing documentation -!-`*

**Back**()

*`-!- Missing documentation -!-`*

---

#class AthenaColor.**BasicNest**()

*`-!- Missing documentation -!-`*

**Fore**()

*`-!- Missing documentation -!-`*

**Back**()

*`-!- Missing documentation -!-`*

---

#class AthenaColor.**CMYK**(c: int | float = 0, m: int | float = 0, y: int | float = 0, k: int | float = 0)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, c: int | float = 0, m: int | float = 0, y: int | float = 0, k: int | float = 0)

Initialize self.  See help(type(self)) for accurate signature.

**export**(self) -> Tuple[int | float, int | float, int | float, int | float]

*`-!- Missing documentation -!-`*

**_value_setter**(self, values: tuple)

*`-!- Missing documentation -!-`*

**__repr__**(self) -> str

Return repr(self).

---

#class AthenaColor.**HEX**(hex_value: str = #000000)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, hex_value: str = #000000)

Initialize self.  See help(type(self)) for accurate signature.

**__str__**(self) -> str

Return str(self).

**__repr__**(self) -> str

Return repr(self).

**__round__**(self, n=None)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

---

#class AthenaColor.**HEXA**(hex_value: str = #00000000)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, hex_value: str = #00000000)

Initialize self.  See help(type(self)) for accurate signature.

**__str__**(self) -> str

Return str(self).

**__repr__**(self) -> str

Return repr(self).

**__round__**(self, n=None)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

---

#class AthenaColor.**HSL**(h: int | float = 0, s: int | float = 0, l: int | float = 0)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, h: int | float = 0, s: int | float = 0, l: int | float = 0)

Initialize self.  See help(type(self)) for accurate signature.

**export**(self) -> Tuple[int | float, int | float, int | float]

*`-!- Missing documentation -!-`*

**_value_setter**(self, values: tuple)

*`-!- Missing documentation -!-`*

**__repr__**(self) -> str

Return repr(self).

---

#class AthenaColor.**HSV**(h: int | float = 0.0, s: int | float = 0.0, v: int | float = 0.0)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, h: int | float = 0.0, s: int | float = 0.0, v: int | float = 0.0)

Initialize self.  See help(type(self)) for accurate signature.

**export**(self) -> Tuple[int | float, int | float, int | float]

*`-!- Missing documentation -!-`*

**_value_setter**(self, values: tuple)

*`-!- Missing documentation -!-`*

**__repr__**(self) -> str

Return repr(self).

---

#class AthenaColor.**RGB**(r: int | float = 0, g: int | float = 0, b: int | float = 0)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, r: int | float = 0, g: int | float = 0, b: int | float = 0)

Initialize self.  See help(type(self)) for accurate signature.

**export**(self) -> Tuple[int, int, int]

*`-!- Missing documentation -!-`*

**_value_setter**(self, values: tuple)

*`-!- Missing documentation -!-`*

**__repr__**(self) -> str

Return repr(self).

---

#class AthenaColor.**RGBA**(r: int = 0, g: int = 0, b: int = 0, a: int = 0)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, r: int = 0, g: int = 0, b: int = 0, a: int = 0)

Initialize self.  See help(type(self)) for accurate signature.

**export**(self) -> Tuple[int, int, int, int]

*`-!- Missing documentation -!-`*

**_value_setter**(self, values: tuple)

*`-!- Missing documentation -!-`*

**__repr__**(self) -> str

Return repr(self).

---

#class AthenaColor.**Style**()

*`-!- Missing documentation -!-`*



---

#class AthenaColor.**StyleNest**()

*`-!- Missing documentation -!-`*



---

#func AthenaColor.**fix_console**()

*`-!- Missing documentation -!-`*

---

#class AthenaColor.**RgbControlled**(param_code: str)

*`-!- Missing documentation -!-`*

**__init__**(self, param_code: str)

Initialize self.  See help(type(self)) for accurate signature.

**custom**(self, color: RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaColor.**RgbControlledNested**(inline_class: RgbControlled, reset: str)

*`-!- Missing documentation -!-`*

**__init__**(self, inline_class: RgbControlled, reset: str)

Initialize self.  See help(type(self)) for accurate signature.

**custom**(self, *obj, color: RGB | HEX, sep= ) -> str

*`-!- Missing documentation -!-`*

**rgb**(self, *obj, r: int, g: int, b: int, sep= ) -> str

*`-!- Missing documentation -!-`*

**Maroon**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkRed**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Brown**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Firebrick**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Crimson**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Red**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Tomato**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Coral**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**IndianRed**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightCoral**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkSalmon**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Salmon**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightSalmon**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**OrangeRed**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkOrange**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Orange**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Gold**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkGoldenRod**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**GoldenRod**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PaleGoldenRod**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkKhaki**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Khaki**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Olive**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Yellow**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**YellowGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkOliveGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**OliveDrab**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LawnGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Chartreuse**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**GreenYellow**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Green**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**ForestGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Lime**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LimeGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PaleGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkSeaGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumSpringGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SpringGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SeaGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumAquaMarine**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumSeaGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightSeaGreen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkSlateGray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Teal**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkCyan**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Aqua**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Cyan**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightCyan**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkTurquoise**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Turquoise**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumTurquoise**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PaleTurquoise**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**AquaMarine**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PowderBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**CadetBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SteelBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**CornFlowerBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DeepSkyBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DodgerBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SkyBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightSkyBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MidnightBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Navy**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Blue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**RoyalBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**BlueViolet**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Indigo**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkSlateBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SlateBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumSlateBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumPurple**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkMagenta**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkViolet**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkOrchid**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumOrchid**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Purple**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Thistle**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Plum**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Violet**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Magenta**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Orchid**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MediumVioletRed**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PaleVioletRed**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DeepPink**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**HotPink**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightPink**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Pink**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**AntiqueWhite**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Beige**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Bisque**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**BlanchedAlmond**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Wheat**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**CornSilk**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LemonChiffon**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightGoldenRodYellow**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightYellow**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SaddleBrown**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Sienna**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Chocolate**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Peru**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SandyBrown**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**BurlyWood**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Tan**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**RosyBrown**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Moccasin**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**NavajoWhite**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PeachPuff**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MistyRose**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LavenderBlush**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Linen**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**OldLace**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**PapayaWhip**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**WeaShell**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**MintCream**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**SlateGray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightSlateGray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightSteelBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Lavender**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**FloralWhite**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**AliceBlue**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**GhostWhite**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Honeydew**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Ivory**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Azure**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Snow**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Black**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DimGray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Gray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**DarkGray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Silver**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**LightGray**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**Gainsboro**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**WhiteSmoke**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

**White**(self, *obj, sep= )

*`-!- Missing documentation -!-`*

---

#func AthenaColor._info._v.**_version**()

*`-!- Missing documentation -!-`*

---

#func AthenaColor._info.formatting.**header**(header_text: str, to_str: bool)

*`-!- Missing documentation -!-`*

---

#func AthenaColor._info.formatting.**reference**(reference_text: str, to_str: bool)

*`-!- Missing documentation -!-`*

---

#func AthenaColor._info.formatting.**sub_modules**(module_text: str, to_str: bool)

*`-!- Missing documentation -!-`*

---

#func AthenaColor._info.formatting.**title**(title_text: str, to_str: bool)

*`-!- Missing documentation -!-`*

---

#class AthenaColor.models.color_system.**ColorSystem**(*_)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, *_)

Initialize self.  See help(type(self)) for accurate signature.

**__str__**(self) -> str

Return str(self).

**__repr__**(self) -> str

Return repr(self).

**export**(self) -> tuple

*`-!- Missing documentation -!-`*

**_value_setter**(self, values: tuple)

*`-!- Missing documentation -!-`*

**average**(self) -> float

*`-!- Missing documentation -!-`*

**__bool__**(self) -> bool

*`-!- Missing documentation -!-`*

**__round__**(self, n=None) -> ColorSystem

*`-!- Missing documentation -!-`*

**__iter__**(self)

*`-!- Missing documentation -!-`*

**__hash__**(self)

Return hash(self).

**__copy__**(self)

*`-!- Missing documentation -!-`*

**__contains__**(self, item)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

**wrapper**(self, other: ColorSystem | int | tuple)

*`-!- Missing documentation -!-`*

---

#func AthenaColor.models.color_system.**_ColorConversionInput**(fnc)

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.color_tuple_conversion.**rgb_to_hex**(r: int | float, g: int | float, b: int | float) -> str

Function to convert a rgb to a hexadecimal string.
Does not create a HEX object.

---

#func AthenaColor.functions.color_tuple_conversion.**rgba_to_hexa**(r: int, g: int, b: int, a: int) -> str

Function to convert a rgba tuple to a hexa string.
Does not create an HEXA object.

---

#func AthenaColor.functions.color_tuple_conversion.**cmyk_to_hex**(c: int | float, m: int | float, y: int | float, k: int | float) -> str

Function to convert a cmyk to a hexadecimal string.
Does not create a HEX object.

---

#func AthenaColor.functions.color_tuple_conversion.**cmyk_to_hsl**(c: int | float, m: int | float, y: int | float, k: int | float) -> Tuple[float, float, float]

Function to convert a cmyk tuple to a hsl tuple.
Does not create an HSL object.

---

#func AthenaColor.functions.color_tuple_conversion.**cmyk_to_hsv**(c: int | float, m: int | float, y: int | float, k: int | float) -> Tuple[float, float, float]

Function to convert a cmyk tuple to a hsv tuple.
Does not create an HSV object.

---

#func AthenaColor.functions.color_tuple_conversion.**cmyk_to_rgb**(c: int | float, m: int | float, y: int | float, k: int | float) -> Tuple[int, int, int]

Function to convert a cmyk tuple to a rgb tuple.
Does not create an RGB object.

---

#func AthenaColor.functions.color_tuple_conversion.**hex_to_cmyk**(hexadecimal: str) -> Tuple[float, float, float, float]

Function to convert a hexadecimal string to a cmyk tuple.
Does not create an CMYK object.

---

#func AthenaColor.functions.color_tuple_conversion.**hex_to_hsl**(hexadecimal: str) -> Tuple[float, float, float]

Function to convert a hexadecimal string to a hsl tuple.
Does not create an HSL object.

---

#func AthenaColor.functions.color_tuple_conversion.**hex_to_hsv**(hexadecimal: str) -> Tuple[float, float, float]

Function to convert a hexadecimal string to a hsv tuple.
Does not create an HSV object.

---

#func AthenaColor.functions.color_tuple_conversion.**hex_to_rgb**(hexadecimal: str) -> Tuple[int, ...]

Function to convert a hexadecimal string to a rgb tuple.
Does not create an RGB object.

---

#func AthenaColor.functions.color_tuple_conversion.**hexa_to_rgba**(hexadecimal: str) -> Tuple[int, ...]

Function to convert a hexadecimal string to a rgb tuple.
Does not create an RGBA object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsl_to_cmyk**(h: int | float, s: int | float, l: int | float) -> Tuple[float, float, float, float]

Function to convert a hsl tuple to a cmyk tuple.
Does not create an CMYK object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsl_to_hex**(h: int | float, s: int | float, l: int | float) -> str

Function to convert a hsl to a hexadecimal string.
Does not create a HEX object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsl_to_hsv**(h: int | float, s: int | float, l: int | float) -> Tuple[float, float, float]

Function to convert a hsl tuple to a hsv tuple.
Does not create an HSV object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsl_to_rgb**(h: int | float, s: int | float, l: int | float) -> Tuple[int, int, int]

Function to convert a hsl tuple to a rgb tuple.
Does not create an RGB object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsv_to_cmyk**(h: int | float, s: int | float, v: int | float) -> Tuple[float, float, float, float]

Function to convert a hsv tuple to a cmyk tuple.
Does not create an CMYK object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsv_to_hex**(h: int | float, s: int | float, v: int | float) -> str

Function to convert a hsv to a hexadecimal string.
Does not create a HEX object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsv_to_hsl**(h: int | float, s: int | float, v: int | float) -> Tuple[float, float, float]

Function to convert a hsv tuple to a hsl tuple.
Does not create an HSL object.

---

#func AthenaColor.functions.color_tuple_conversion.**hsv_to_rgb**(h: int | float, s: int | float, v: int | float) -> Tuple[int, int, int]

Function to convert a hsv tuple to a rgb tuple.
Does not create an RGB object.

---

#func AthenaColor.functions.color_tuple_conversion.**normalize_rgb**(r: int, g: int, b: int) -> Tuple[float, ...]

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.color_tuple_conversion.**normalize_rgba**(r: int, g: int, b: int, a: int) -> Tuple[float, ...]

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.color_tuple_conversion.**rgb_to_cmyk**(r: int, g: int, b: int) -> Tuple[float, float, float, float]

Function to convert a rgb tuple to a cmyk tuple.
Does not create an CMYK object.

---

#func AthenaColor.functions.color_tuple_conversion.**rgb_to_hsl**(r: int, g: int, b: int) -> Tuple[float, float, float]

Function to convert a rgb tuple to a hsl tuple.
Does not create an HSL object.

---

#func AthenaColor.functions.color_tuple_conversion.**rgb_to_hsv**(r: int, g: int, b: int) -> Tuple[float, float, float]

Function to convert a rgb tuple to a hsv tuple.
Does not create an HSV object.

---

#func AthenaColor.functions.color_object_conversion.**to_CMYK**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> CMYK

Function which converts any Color Object to an CMYK object.

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : CMYK

---

#func AthenaColor.functions.color_object_conversion.**to_HEX**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> HEX

Function which converts any Color Object to an HEX object.

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : HEX

---

#func AthenaColor.functions.color_object_conversion.**to_HEXA**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> HEXA

Function which converts any Color Object to an HEXA object.

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : HEXA

---

#func AthenaColor.functions.color_object_conversion.**to_HSL**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> HSL

Function which converts any Color Object to an HSL object.

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : HSL

---

#func AthenaColor.functions.color_object_conversion.**to_HSV**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> HSV

Function which converts any Color Object to an HSV object.

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : HSV

---

#func AthenaColor.functions.color_object_conversion.**to_RGB**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> RGB

Function which converts any Color Object to an RGB object

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : RGB

---

#func AthenaColor.functions.color_object_conversion.**to_RGBA**(color: ColorSystem | RGB | HEX | CMYK | HSL | HSV | RGBA | HEXA) -> RGBA

Function which converts any Color Object to an RGBA object.

Parameters:
- color : ColorSystem|RGB|HEX|CMYK|HSL|HSV|RGBA|HEXA -> Any valid ColorSystem object

Returns : RGBA

---

#func AthenaColor.functions.constrains.**constrain_cmyk**(c: int | float, m: int | float, y: int | float, k: int | float) -> Tuple[int | float, int | float, int | float, int | float]

Constrain the given values to the CMYK format

---

#func AthenaColor.functions.constrains.**constrain_hsl**(h: int | float, s: int | float, l: int | float) -> Tuple[int | float, int | float, int | float]

Constrain the given values to the HSL format

---

#func AthenaColor.functions.constrains.**constrain_hsv**(h: int | float, s: int | float, v: int | float) -> Tuple[int | float, int | float, int | float]

Constrain the given values to the HSV format

---

#func AthenaColor.functions.constrains.**constrain_rgb**(r: int, g: int, b: int) -> Tuple[int, int, int]

Constrain the given values to the RGB format

---

#func AthenaColor.functions.constrains.**constrain_rgba**(r: int, g: int, b: int, a: int) -> Tuple[int, int, int, int]

Constrain the given values to the RGBA format

---

#func AthenaColor.functions.constrains.**constrain**(value: int | float, maximum: int | float, minimum: int | float = 0) -> int | float

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.functions.**round_half_up**(value: int | float) -> int

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.ansi_sequences.**color_sequence_nested**(obj: tuple, color_code: str, reset_code: int | str, sep: str =  ) -> str

Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
Function wraps every obj in the properly defined control- and reset codes.
This is made to prevent style makeup bleed

Parameters:
- obj : tuple -> Collection of all objects to be wrapped
- color_code : str -> Full color_sequenced ANSI code
- reset_code : int|str -> Full color_sequenced ANSI code to reset the given color
- sep : str -> separation string between the various objects

---

#func AthenaColor.functions.ansi_sequences.**color_sequence_nested_no_reset**(obj: tuple, color_code: int | str, sep: str =  ) -> str

Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
Function wraps every obj in the properly defined control- and reset codes.
This is made to prevent style makeup bleed

Parameters:
- obj : tuple -> Collection of all objects to be wrapped
- color_code : str -> Full color_sequenced ANSI code
- sep : str -> separation string between the various objects

---

#func AthenaColor.functions.ansi_sequences.**color_sequence**(control_code: int | str) -> str

Used for quick assembly of correct Ansi Escape functions
Used the escape code defined in AthenaColor init

Parameters:
- control_code : int|str -> numerical ANSI fragment

---

#func AthenaColor.functions.ansi_sequences.**color_sequence_nested**(obj: tuple, color_code: str, reset_code: int | str, sep: str =  ) -> str

Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
Function wraps every obj in the properly defined control- and reset codes.
This is made to prevent style makeup bleed

Parameters:
- obj : tuple -> Collection of all objects to be wrapped
- color_code : str -> Full color_sequenced ANSI code
- reset_code : int|str -> Full color_sequenced ANSI code to reset the given color
- sep : str -> separation string between the various objects

---

#func AthenaColor.functions.ansi_sequences.**color_sequence_nested_no_reset**(obj: tuple, color_code: int | str, sep: str =  ) -> str

Used by Nested Console StyleNest Makeup operations like ForeNest, BackNest, StyleNest.
Function wraps every obj in the properly defined control- and reset codes.
This is made to prevent style makeup bleed

Parameters:
- obj : tuple -> Collection of all objects to be wrapped
- color_code : str -> Full color_sequenced ANSI code
- sep : str -> separation string between the various objects

---

#func AthenaColor.functions.dunder_functions.**add**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**divmod_function**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**eq**(left: tuple, right: tuple) -> bool

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**floordiv**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**ge**(left: tuple, right: tuple) -> bool

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**gt**(left: tuple, right: tuple) -> bool

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**le**(left: tuple, right: tuple) -> bool

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**lt**(left: tuple, right: tuple) -> bool

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**mod**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**mul**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**ne**(left: tuple, right: tuple) -> bool

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**power**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**sub**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

#func AthenaColor.functions.dunder_functions.**truediv**(left: tuple, right: tuple) -> tuple

*`-!- Missing documentation -!-`*

---

