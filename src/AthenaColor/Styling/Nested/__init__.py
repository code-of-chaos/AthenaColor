from .Nested_Bodies import (
    Fore,
    Back,
    Underline
)

class Style:
    __all__ = [
        "Reset",
        "Italic",
        "NoItalic",
        "Bold",
        "NoBold",
        "Underline",
        "NoUnderline",
        "Crossed",
        "NoCrossed",
        "Reversed",
        "NoReversed",
        "Frame",
        "NoFrame",
        "Circle",
        "NoCircle",
        "UnderlineDouble",
        "NoForeground",
        "NoBackground"
    ]

    from .Nested_MakeUp import (
        Reset,
        Italic,
        NoItalic,
        Bold,
        NoBold,
        Underline,
        NoUnderline,
        Crossed,
        NoCrossed,
        Reversed,
        NoReversed,
        Frame,
        NoFrame,
        Circle,
        NoCircle,
        UnderlineDouble,
        NoForeground,
        NoBackground
    )
    class Unverfified:
        from .Nested_MakeUp import (
            BlinkSlow,
            NoBlinkSlow,
            BlinkRapid,
            NoBlinkRapid,
            Conceal,
            NoConceal,
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
            NoPropSpacing,
        )