from functools import wraps
from multiprocessing import Process

import pytest


def run_test_in_subprocess(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        p = Process(target=func, args=args, kwargs=kwargs)
        p.start()
        p.join()

    return wrapper


@run_test_in_subprocess
def test_dask():
    import dask

    assert hasattr(dask, "test_attr")


@run_test_in_subprocess
def test_dask_dataframe_deprecation():
    with pytest.warns(DeprecationWarning):
        pass


@run_test_in_subprocess
def test_dask_compatibility():
    import dask._compatibility as dc

    assert hasattr(dc, "test_attr")

    with pytest.warns(DeprecationWarning):
        dc.entry_points()


@run_test_in_subprocess
def test_distributed():
    import distributed

    assert hasattr(distributed, "test_attr")
