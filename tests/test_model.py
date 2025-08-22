"""Tests for the DNest4Model class in dnest4_bilby.model"""

import numpy as np
import pytest

from dnest4_bilby.model import DNest4Model


def dummy_log_likelihood(coords):
    return -np.sum(np.square(coords))


def dummy_from_prior():
    return np.array([0.0, 1.0, 2.0])


def test_initialization():
    model = DNest4Model(
        dummy_log_likelihood,
        dummy_from_prior,
        widths=[1, 2, 3],
        centers=[0, 0, 0],
        highs=[1, 2, 3],
        lows=[-1, -2, -3],
    )
    assert model._n_dim == 3
    assert np.allclose(model._widths, [1, 2, 3])
    assert np.allclose(model._centers, [0, 0, 0])


def test_log_likelihood():
    model = DNest4Model(
        dummy_log_likelihood,
        dummy_from_prior,
        widths=[1, 2, 3],
        centers=[0, 0, 0],
        highs=[1, 2, 3],
        lows=[-1, -2, -3],
    )
    coords = np.array([1.0, 2.0, 3.0])
    result = model.log_likelihood(coords)
    assert result == -14.0


def test_from_prior():
    model = DNest4Model(
        dummy_log_likelihood,
        dummy_from_prior,
        widths=[1, 2, 3],
        centers=[0, 0, 0],
        highs=[1, 2, 3],
        lows=[-1, -2, -3],
    )
    prior = model.from_prior()
    assert np.allclose(prior, [0.0, 1.0, 2.0])


def test_wrap_basic():
    # Test wrap within bounds
    assert DNest4Model.wrap(5, 0, 10) == 5
    # Test wrap below minimum
    assert DNest4Model.wrap(-1, 0, 10) == 9
    # Test wrap above maximum
    assert DNest4Model.wrap(11, 0, 10) == 1


def test_wrap_error():
    with pytest.raises(ValueError):
        DNest4Model.wrap(1, 10, 0)


def test_perturb_changes_coords(monkeypatch):
    # Setup model
    model = DNest4Model(
        dummy_log_likelihood,
        dummy_from_prior,
        widths=[1, 2, 3],
        centers=[0, 0, 0],
        highs=[1, 2, 3],
        lows=[-1, -2, -3],
    )
    coords = np.array([0.0, 0.0, 0.0])

    # Patch bilby.core.utils.random.rng.integers and uniform
    class DummyRNG:
        def integers(self, n):
            return 1  # always pick index 1

        def uniform(self, size=None):
            return 0.5  # always return 0.5

    monkeypatch.setattr("bilby.core.utils.random.rng", DummyRNG())
    model.perturb(coords)
    # After perturb, coords[1] should be unchanged (since uniform() - 0.5 == 0)
    assert coords[1] == 0.0
