import sys, os
import pdb
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))
sys.path.append(os.path.join(os.path.dirname("__file__"), '..', '..'))
pos='vfscale'
path = os.getcwd()
SRC_PATH = path.split('vfscale_src')[0]+"vfscale_src/"
CURRENT_WP=path.split('vfscale_src')[0]
if pos=='vfscale':
    EXP_PATH = CURRENT_WP
else:
    raise ValueError("Please specify the position of the project directory")
