"""Model class for dnest4 in bilby"""


class DNest4Model:
    def __init__(
        self,
        log_likelihood_func,
        from_prior_func,
        widths,
        centers,
        highs,
        lows,
    ):
        """Initialize the DNest4 model.
        Args:
            log_likelihood_func: function
                The loglikelihood function to use during the Nested Sampling run.
            from_prior_func: function
                The function to use when randomly selecting parameter vectors from the prior space.
            widths: array_like
                The approximate widths of the prior distrbutions.
            centers: array_like
                The approximate center points of the prior distributions.
        """
        self._log_likelihood = log_likelihood_func
        self._from_prior = from_prior_func
        self._widths = widths
        self._centers = centers
        self._highs = highs
        self._lows = lows
        self._n_dim = len(widths)
        return

    def log_likelihood(self, coords):
        """The model's log_likelihood function"""
        return self._log_likelihood(coords)

    def from_prior(self):
        """The model's function to select random points from the prior space."""
        return self._from_prior()

    def perturb(self, coords):
        """The perturb function to perform Monte Carlo trial moves."""
        from bilby.core.utils import random

        idx = random.rng.integers(self._n_dim)
        coords[idx] += self._widths[idx] * (random.rng.uniform() - 0.5)
        cw = self._widths[idx]
        cc = self._centers[idx]

        coords[idx] = self.wrap(coords[idx], (cc - 0.5 * cw), cc + 0.5 * cw)

        return 0.0

    @staticmethod
    def wrap(x, minimum, maximum):
        if maximum <= minimum:
            raise ValueError(
                f"maximum {maximum} <= minimum {minimum}, when trying to wrap coordinates"
            )
        return (x - minimum) % (maximum - minimum) + minimum
