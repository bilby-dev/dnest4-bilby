"""Plugin for using dnest4 in bilby."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

try:
    import dnest4  # noqa: F401
except ImportError:
    raise ImportError(
        "dnest4 is not installed. Please ins tall dnest4 to use the dnest4 "
        "plugin for bilby. See the README for installation instructions: "
        "https://github.com/bilby-dev/dnest4-bilby."
    )
