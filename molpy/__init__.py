"""
molpy
Molecule Manipulation Package
"""

# Add imports here
from .molpy import *
from . import util # Get util as a function of molpy

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
