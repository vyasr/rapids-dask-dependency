# Copyright (c) 2024, NVIDIA CORPORATION.

import rapids_dask_dependency.patches.dask_patch  # noqa: F401
import rapids_dask_dependency.patches.distributed_patch  # noqa: F401

from .dask_loader import DaskLoader

DaskLoader.install()
