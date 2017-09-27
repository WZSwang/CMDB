
import os
import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from lib.config import settings

print(settings.NAME)
print(settings.TEST)