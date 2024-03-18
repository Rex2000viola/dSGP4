__version__ = '0.1.0'

import torch
torch.set_default_dtype(torch.float64)
from .sgp4 import sgp4
from .initl import initl
from .sgp4init import sgp4init
from .newton_method import newton_method, update_TLE
from .sgp4_batched import sgp4_batched
from .util import propagate, initialize_tle, propagate_batch
from .plot import plot_orbit, plot_tles
from . import tle
from .tle import TLE
