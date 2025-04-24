import torch
import pytest
from diffusion import naive_sampling

# Dummy restoration model: simply halves input


class DummyRestoration:
    def __call__(self, x, timestep):
        return x * 0.5


def dummy_degradation(x, timestep):
    return x + 1


def test_naive_sampling_output_shape():
    R = DummyRestoration()
    D = dummy_degradation

    x_t = torch.ones((1, 3, 32, 32))  # batch_size=1, channels=3, image=32x32
    t = 5

    x_0 = naive_sampling(R, D, x_t, t)

    assert x_0.shape == x_t.shape, "Output shape must match input shape"


def test_naive_sampling_known_output():
    R = DummyRestoration()
    D = dummy_degradation

    x_t = torch.ones(1) * 32
    t = 2

    x_0 = naive_sampling(R, D, x_t, t)
    expected = torch.tensor([8.5])

    assert torch.allclose(
        x_0, expected, atol=1e-4), f"Expected {expected}, got {x_0}"
