# flake8: noqa
from . import config
from .core import JobQueueCluster
from .job import Job
from .moab import MoabCluster
from .pbs import PBSCluster, PBSJob
from .slurm import SLURMCluster
from .sge import SGECluster, SGEJob
from .lsf import LSFCluster
from .oar import OARCluster
from .htcondor import HTCondorCluster

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
