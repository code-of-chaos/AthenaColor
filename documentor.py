# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaDocumentor
import AthenaColor

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main(root_module):
    parser = AthenaDocumentor.Parser(root_module=root_module).parse()
    # output the desired root_module to JSON
    parser.output_to_json_file(
        "exports/documentor.json"
    )
    # output the desired root_module to Markdown
    parser.output_to_markdown_file(
        r"exports\documentor.md",
        r"D:\Directive Athena\Programs\Veritas\Storage\Documentation\Content\Programming\AthenaColor\reference.md"
    )

if __name__ == '__main__':
    main(
      root_module = AthenaColor
    )