from .TestValues import (
    testCMYK,
    testHSV,
    testRGB,
    testHSL,
    testHEX
)
from .Constraints import (
    ConstrainHSV,
    ConstrainCMYK,
    ConstrainRGB,
    ConstrainHSL
)
from .ColorConversion import (
    # to rgb
    hex_to_rgb, hsv_to_rgb, cmyk_to_rgb, hsl_to_rgb,
    # to hexadecimal
    rgb_to_hex,hsv_to_hex,cmyk_to_hex,hsl_to_hex,
    # to HSV
    rgb_to_hsv, hex_to_hsv, cmyk_to_hsv, hsl_to_hsv,
    # to CMYK
    rgb_to_cmyk, hex_to_cmyk, hsv_to_cmyk, hsl_to_cmyk,
    # to HSL
    rgb_to_hsl,hex_to_hsl,cmyk_to_hsl,hsv_to_hsl,
)
