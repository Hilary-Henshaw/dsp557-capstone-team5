from __future__ import annotations

import ctypes
import platform
import pathlib
from typing import Optional


def _default_lib_path(project_root: pathlib.Path) -> pathlib.Path:
    name = "libchurn_risk.dylib" if platform.system() == "Darwin" else "libchurn_risk.so"
    return project_root / "src" / "cpp_engine" / name


_lib: Optional[ctypes.CDLL] = None


def load_churn_risk_lib(project_root: pathlib.Path) -> ctypes.CDLL:
    global _lib
    if _lib is not None:
        return _lib
    path = _default_lib_path(project_root)
    if not path.is_file():
        raise FileNotFoundError(
            f"Missing {path}. From repo root run: bash src/cpp_engine/build_churn_risk.sh"
        )
    _lib = ctypes.CDLL(str(path))
    _lib.churn_risk_band.argtypes = [ctypes.c_double]
    _lib.churn_risk_band.restype = ctypes.c_char_p
    return _lib


def risk_band(probability: float, *, project_root: pathlib.Path) -> str:
    lib = load_churn_risk_lib(project_root)
    raw = lib.churn_risk_band(float(probability))
    if not raw:
        return "Unknown"
    return raw.decode("utf-8")
