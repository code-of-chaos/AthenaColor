from .Bodies import (
    Fore,
    Back,
    Underline # Technically present, but does not work in PyCharm
)
class Style:
    from .MakeUp import (
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
        from .MakeUp import (
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