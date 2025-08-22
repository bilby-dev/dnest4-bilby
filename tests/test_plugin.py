import bilby
import pytest

from dnest4_bilby.plugin import DNest4


@pytest.fixture()
def sampler(likelihood, priors, tmp_path):
    return DNest4(
        likelihood,
        priors,
        outdir=tmp_path / "outdir",
        label="label",
        use_ratio=False,
        plot=False,
        skip_import_verification=True,
    )


def test_default_kwargs(sampler):
    expected = dict(
        max_num_levels=20,
        num_steps=500,
        new_level_interval=10000,
        num_per_step=10000,
        thread_steps=1,
        num_particles=1000,
        lam=10.0,
        beta=100,
        seed=None,
        verbose=True,
        backend="memory",
    )
    for key in sampler.kwargs.keys():
        print(
            "key={}, expected={}, actual={}".format(
                key, expected[key], sampler.kwargs[key]
            )
        )
    assert expected == sampler.kwargs


def test_translate_kwargs(sampler):
    expected = dict(
        max_num_levels=20,
        num_steps=500,
        new_level_interval=10000,
        num_per_step=10000,
        thread_steps=1,
        num_particles=1000,
        lam=10.0,
        beta=100,
        seed=None,
        verbose=True,
        backend="memory",
    )

    for (
        equiv
    ) in bilby.core.sampler.base_sampler.NestedSampler.npoints_equiv_kwargs:
        new_kwargs = sampler.kwargs.copy()
        del new_kwargs["num_particles"]
        new_kwargs[equiv] = 1000
        sampler.kwargs = new_kwargs
        assert expected == sampler.kwargs
