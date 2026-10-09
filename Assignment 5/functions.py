import numpy as np
import matplotlib.pyplot as plt
from gaussian import set_seed, generate_gaussian


def covariance(X):
    Xc = X - X.mean(axis=0)
    return Xc.T @ Xc / len(X)


def transform(X, mu, Sigma):
    e, V = np.linalg.eigh(Sigma)
    A = V @ np.diag(np.sqrt(e)) @ V.T
    return mu + (X - mu) @ A.T


def same_scale(X, Y=None, pad=1):
    if Y is None:
        Y = X

    Z = np.vstack((X, Y)) if Y is not X else X

    xmin, xmax = Z[:, 0].min(), Z[:, 0].max()
    ymin, ymax = Z[:, 1].min(), Z[:, 1].max()

    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2

    r = max(xmax - xmin, ymax - ymin) / 2 + pad

    plt.xlim(cx - r, cx + r)
    plt.ylim(cy - r, cy + r)

    plt.gca().set_aspect('equal', adjustable='box')


def logpdf(P, mu, Sigma):
    d = P - mu

    return -0.5 * (
        2 * np.log(2 * np.pi)
        + np.linalg.slogdet(Sigma)[1]
        + np.sum(
            (d @ np.linalg.inv(Sigma)) * d,
            axis=1
        )
    )