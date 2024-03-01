# Copyright (c) 2024, NVIDIA CORPORATION.

import importlib

from rapids_dask_dependency.patches.base import BasePatch, dask_patcher


class DaskPatch(BasePatch):
    module_name = "dask"

    @classmethod
    def apply(cls, mod):
        # Add top-level attribute
        mod.test_attr = "hello world"

        # Add attribute to dask.dataframe.io
        ddio = importlib.import_module("dask.dataframe.io")
        ddio.test_attr = "hello world"


dask_patcher.register(DaskPatch)
