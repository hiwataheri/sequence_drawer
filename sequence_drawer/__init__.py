"""
Sequence Drawer
Create a 2D drawing out of a SMILES input.
"""

# Add imports here
from .drawer import *

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
