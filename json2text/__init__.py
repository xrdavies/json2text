__version__ = '0.0.1'
import sys

if sys.version_info[0] > 2:
    from .json2text import JSON2Text, Text2JSON
else:
    from .json2text import JSON2Text, Text2JSON