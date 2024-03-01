# Copyright (c) 2024, NVIDIA CORPORATION.


from rapids_dask_dependency.patches.base import BasePatch, dask_patcher


class DistributedPatch(BasePatch):
    module_name = "distributed"

    @classmethod
    def apply(cls, mod):
        # Add top-level attribute
        mod.test_attr = "hello world"


dask_patcher.register(DistributedPatch)
