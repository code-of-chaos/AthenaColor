# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import sys

# Custom Library

# Custom Packages
import time

import AthenaColor as AC

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    AC.readme()
    AC.Help.all_NotWorkingPycharm()

    from AthenaColor.Predefined.ColorsBasic import esc

    # Initialize output line with spaces
    sys.stdout.write(' ' * 100)

    # Update line in a loop
    for k in range(10):
        # Generate new line of text
        cur_line = f'foo {k}'

        # Remove last 100 characters, write new line and pad with spaces
        sys.stdout.write('\b' * 100)
        sys.stdout.flush()
        sys.stdout.write(cur_line + ' ' * (100 - len(cur_line)))
        sys.stdout.flush()
