# dnest4-bilby

`dnest4` plugin for bilby.

This plugin provides the `dnest4` sampler in bilby.

## Installation

`dnest4` is available [via conda](https://anaconda.org/conda-forge/dnest4), or
can be installed from source following [these instructions](https://github.com/eggplantbren/DNest4?tab=readme-ov-file#compiling).

Once `dnest4` is installed, the plugin can be installed using `pip`:

```bash
pip install dnest4-bilby
```

**Note:** the `conda` version of the `dnest4` does not support `numpy>2.0`.

**Note:** due to changes in `numpy` and Python that are incompatible with `dnest4` this plugin is only tested with Python < 3.11.
It may be possible to compile a working version of `dynest4` with more recent `numpy` and Python versions but this has not been
tested.

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
