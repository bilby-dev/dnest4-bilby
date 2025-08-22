"""Test the integration with bilby"""

import bilby


def test_sampling_dnest4(likelihood, priors, tmp_path):
    outdir = tmp_path / "test_sampling_dnest4"

    bilby.run_sampler(
        outdir=outdir,
        resume=False,
        plot=False,
        likelihood=likelihood,
        priors=priors,
        sampler="dnest4",
        max_num_levels=2,
        num_steps=10,
        new_level_interval=10,
        num_per_step=10,
        thread_steps=1,
        num_particles=50,
        max_pool=1,
    )
