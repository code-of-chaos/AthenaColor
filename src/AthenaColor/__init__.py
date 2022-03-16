# All custom objects
from .Objects import (
    rgb,    # rgb object
    Colors  # Formed Colors list as soon as possible inside the objects package
)

from .ConsolePrinter import (
    Foreground,
    Background,

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
    ForegroundDefault,
    BackgroundDefault
)

class maybe_working:
    class ConsolePrinter:
        from .ConsolePrinter import (
            Dim,
            NoDim,
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
            NoPropSpacing,
            OverLine,
            NoOverLine,
            UnderColour,
            UnderColourDefault,
            SuperScript,
            SubScript,
            NoScript,
            IdeogramUnderLine,
            IdeogramUnderLineDouble,
            IdeogramOverLine,
            IdeogramOverLineDouble,
            IdeogramStress,
            NoIdeogram,
        )

class Colours_Limited:
    from .ConsolePrinter import (
        ForeEasyBlack,
        ForeEasyRed,
        ForeEasyGreen,
        ForeEasyYellow,
        ForeEasyBlue,
        ForeEasyMagenta,
        ForeEasyCyan,
        ForeEasyWhite,

        BackEasyBlack,
        BackEasyRed,
        BackEasyGreen,
        BackEasyYellow,
        BackEasyBlue,
        BackEasyMagenta,
        BackEasyCyan,
        BackEasyWhite,

        FrontBrightBlack,
        FrontBrightRed,
        FrontBrightGreen,
        FrontBrightYellow,
        FrontBrightBlue,
        FrontBrightMagenta,
        FrontBrightCyan,
        FrontBrightWhite,

        BackBrightBlack,
        BackBrightRed,
        BackBrightGreen,
        BackBrightYellow,
        BackBrightBlue,
        BackBrightMagenta,
        BackBrightCyan,
        BackBrightWhite,
    )

# DOCU
import AthenaColor.Docu

