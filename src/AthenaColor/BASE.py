# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects import rgb

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

esc = "\033"
end = "m"

class rgb_controlled:
    _prefix = ""
    _sufix = ""

    @classmethod
    def custom(cls,color:rgb):
      return f"{cls._prefix}{color}{cls._sufix}"

    @classmethod
    def c(cls,color:rgb): #synonim for cls.custom()
      return cls.custom(color)
