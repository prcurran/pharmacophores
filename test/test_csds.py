"""
Test CSDS installation
"""

from ccdc import io

print(io.MoleculeReader('csd')[0].identifier)
