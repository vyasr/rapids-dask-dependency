# Copyright (c) 2024, NVIDIA CORPORATION.


class BasePatch:
    module_name = None

    @classmethod
    def apply(cls, mod):
        raise NotImplementedError()


class Patcher:
    def __init__(self):
        self._patches = {}

    @property
    def module_names(self):
        return tuple(self._patches)

    def register(self, patch):
        if patch.module_name not in self._patches:
            self._patches[patch.module_name] = []
        self._patches[patch.module_name].append(patch)

    def apply(self, mod):
        for patch in self._patches.get(mod.__name__, []):
            patch.apply(mod)


dask_patcher = Patcher()
