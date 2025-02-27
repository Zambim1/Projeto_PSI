import os
import sys


pycache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pycache')
os.environ['PYTHONPYCACHEPREFIX'] = pycache_dir


print(f"Diretório de pycache: {os.environ.get('PYTHONPYCACHEPREFIX')}")