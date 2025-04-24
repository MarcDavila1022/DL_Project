
def naive_sampling(R, D, x_t, t):
    """
    Naive sampling (Algorithm 1) for cold diffusion.

    Args:
        R: restoration model
        D: chosen degradation (blurring, snowification, etc.)
        x_t: starting degraded image
        t: the total number of timesteps 

    Returns:
        x_0: reconstructed image
    """
    x_s = x_t
    # Iteratively apply the restoration and degradation
    for s in range(t, 0, -1):
        x_hat0 = R(x_s, s)
        x_s = D(x_hat0, s - 1)
    x_0 = x_hat0
    return x_0
