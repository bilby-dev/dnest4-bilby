# dnest4-bilby

`dnest4` plugin for bilby.

This plugin provides the `dnest4` sampler in bilby.

## Installation

This plugin is available via `pip`:

```
pip install dnest4-bilby
```

and `conda`:

```
conda install conda-forge:dnest4-bilby
```

**Note:** when installing via `pip`, you must install `dnest4` separately.

### Installing `dnest4`

`dnest4` is available [via conda](https://anaconda.org/conda-forge/dnest4), or
can be installed from source following [these instructions](https://github.com/eggplantbren/DNest4?tab=readme-ov-file#compiling).

### Caveats

* `dnest4` no longer provides a Python interface
* The `conda` version of the `dnest4` does not support `numpy>2.0`.
* Due to changes in `numpy` and Python that are incompatible with `dnest4` this plugin is only tested with Python < 3.11. It may be possible to compile a working version of `dynest4` with more recent `numpy` and Python versions but this has not  been tested.
* This plugin is tested against `dnest4` versions 0.2.4 and 0.3.3, the latest versions available via conda-forge and PyPI respectively.

## Usage

Once `dnest4-bilby` is installed, the sampler can be used directly in bilby via the run_sampler function:

```python
import bilby

likelihood = ...
priors = ...

bilby.run_sampler(
    sampler="dnest4",
    likelihood=likelihood,
    priors=priors,
    nlive=1000,
    ...
)
```

## Usage with bilby_pipe

This plugin has not been tested with bilby_pipe.
