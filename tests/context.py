import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import lightmanager
from lightmanager.server.version import __version__


print("Testing lightmanager version {}. source located at: {}".format(__version__, lightmanager.__path__))

# In every test file: from context import lightmanager
