__author__ = 'tylin'

import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 8:
    import importlib.metadata
    version = importlib.metadata.version('xlcocotools')
