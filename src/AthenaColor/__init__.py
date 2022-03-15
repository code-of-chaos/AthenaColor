from .Colors import Colors

from .Objects import (
    rgb
)

from .Content import (
    Foreground,
    Background,

    Reset,
    Italic,
    NoItalic,
    Bold,
    NoBold,
    Underline,
    NoUnderline,
    Dim,
    NoDim,
    Crossed,
    NoCrossed,
    Reversed,
    NoReversed,
    Frame,
    NoFrame,
    Circle,
    NoCircle,
    UnderlineDouble,
)

Colors = Colors()

class maybe_working:
    from .Content import (
        BlinkSlow,
        NoBlinkSlow,
        BlinkRapid,
        NoBlinkRapid,
        Conceal,
        FontPrimary,
        FontSecond1,
        FontSecond2,
        FontSecond3,
        FontSecond4,
        FontSecond5,
        FontSecond6,
        FontSecond8,
        FontSecond9,
        FontSecond10,
        NoFont,
        Fraktur,
        PropSpacing,
    )