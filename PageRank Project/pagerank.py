"""
pagerank.py
-----------

  PageRank: An Eigenvector Problem (class presentation)
  By: Tran, Wussinu, and Nielsen  

  Recreates Google's PageRank as described in:
- The Web is a directed graph (pages = nodes, links = edges)
- Build column-stochastic transition matrix M
- Form Google matrix G = α M + (1-α)/n * ee^T
- Find the dominant eigenvector R using power iteration
  so that G R = R (eigenvalue λ = 1)
"""

from typing import List, Tuple
import math


def build_transition_matrix(
    n: int,
    edges: List[Tuple[int, int]]
) -> List[List[float]]:
    """
    Build the raw transition matrix M (column-stochastic) for PageRank.

    n: number of pages (nodes labeled 0..n-1)
    edges: list of directed edges (j -> i) meaning "page j links to page i"

    For each page j:
      - let d_j = number of outgoing links from j
      - if d_j > 0, then for each i that j links to:
            M[i][j] = 1 / d_j
      - if d_j == 0 (dangling page), we give it a uniform link to all pages:
            M[i][j] = 1 / n  for all i

    Returns M as an n x n *row-major* matrix:
      M[i][j] is prob of going from page j to page i.
    That is: each COLUMN j sums to 1 → column-stochastic.
    """
    # Build adjacency list: outlinks[j] = [i1, i2, ...] pages j points to
    outlinks = {j: [] for j in range(n)}
    for src, dst in edges:
        if 0 <= src < n and 0 <= dst < n:
            outlinks[src].append(dst)

    # Initialize M with zeros
    M = [[0.0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        if len(outlinks[j]) == 0:
            # Dangling node: distribute uniformly
            for i in range(n):
                M[i][j] = 1.0 / n
        else:
            prob = 1.0 / len(outlinks[j])
            for i in outlinks[j]:
                M[i][j] = prob

    return M


def build_google_matrix(
    M: List[List[float]],
    alpha: float = 0.85
) -> List[List[float]]:
    """
    Build the Google matrix:
        G = α M + (1-α)/n * ee^T

    Where:
    - α is the damping factor (typically 0.85 ~ 85% link-following)
    - (1-α)/n * ee^T is the "teleportation"/reset term
      meaning with probability (1-α) we jump uniformly to any page.

    G is also column-stochastic, guaranteed to be positive everywhere.
    """
    n = len(M)
    G = [[0.0 for _ in range(n)] for _ in range(n)]

    teleport_value = (1.0 - alpha) / n

    for i in range(n):
        for j in range(n):
            G[i][j] = alpha * M[i][j] + teleport_value
            # Every entry is > 0, which prevents rank sinks
            # and makes G irreducible and aperiodic
    return G


def matvec(G: List[List[float]], x: List[float]) -> List[float]:
    """
    Compute y = G x  where G is n x n and x is length n.
    We assume G is in row-major form: G[i][j]
    """
    n = len(G)
    y = [0.0] * n
    for i in range(n):
        s = 0.0
        row = G[i]
        for j in range(n):
            s += row[j] * x[j]
        y[i] = s
    return y


def l1_normalize(v: List[float]) -> List[float]:
    """
    Normalize a vector so its entries sum to 1 (L1 norm = 1).
    PageRank is a probability distribution over pages.
    """
    s = sum(v)
    if s == 0:
        # fallback to uniform
        n = len(v)
        return [1.0 / n] * n
    return [vi / s for vi in v]


def vector_diff_l1(a: List[float], b: List[float]) -> float:
    """
    ||a - b||_1 = sum |a_i - b_i|
    We'll use this as our convergence test.
    """
    return sum(abs(ai - bi) for ai, bi in zip(a, b))


def pagerank_power_iteration(
    G: List[List[float]],
    tol: float = 1e-10,
    max_iter: int = 10_000
) -> Tuple[List[float], int, float]:
    """
    Compute the PageRank vector R such that
        G R = R
    using the power iteration method described in the slides.

    Start with a uniform distribution, repeatedly apply G,
    and stop when the change is below tolerance in L1 norm.

    Returns:
      (R, iters, last_change)
      - R: final PageRank vector (stationary distribution)
      - iters: how many iterations we actually ran
      - last_change: ||R_new - R_old||_1 at termination
    """
    n = len(G)
    # start uniform
    R = [1.0 / n] * n

    for k in range(1, max_iter + 1):
        R_next = matvec(G, R)
        R_next = l1_normalize(R_next)

        change = vector_diff_l1(R_next, R)
        if change < tol:
            return (R_next, k, change)
        R = R_next

    return (R, max_iter, change)


def pretty_print_rank(R: List[float]):
    """
    Convenience helper: print rank scores with indices sorted
    from most important page to least.
    """
    ranking = list(enumerate(R))
    ranking.sort(key=lambda t: t[1], reverse=True)
    print("PageRank scores (highest = most 'important'):")
    for node, score in ranking:
        print(f"  Page {node}: {score:.6f}")
    print()


def demo():
    """
    Small demo graph.
    We create a tiny directed web of 4 pages:

        Page 0 → Page 1, Page 2
        Page 1 → Page 2
        Page 2 → Page 0, Page 3
        Page 3 → Page 0

    This is consistent with the 'web as a directed graph':
    - Nodes are pages
    - Directed edges represent links

    We'll:
    (1) build M (transition matrix),
    (2) build G (Google matrix with α=0.85),
    (3) run power iteration to find the steady-state eigenvector R.
    """

    n = 4
    edges = [
        (0, 1), (0, 2),  # page 0 links to 1 and 2
        (1, 2),          # page 1 links to 2
        (2, 0), (2, 3),  # page 2 links to 0 and 3
        (3, 0),          # page 3 links to 0
        # Note: no dangling pages here, but build_transition_matrix
        # handles them if they exist
    ]

    # Step 1: Build transition matrix M
    M = build_transition_matrix(n, edges)

    print("Transition matrix M (column-stochastic):")
    for i in range(n):
        row_str = " ".join(f"{M[i][j]:.3f}" for j in range(n))
        print(f"row {i}: {row_str}")
    print()

    # Step 2: Build Google matrix G with damping factor α=0.85
    alpha = 0.85
    G = build_google_matrix(M, alpha=alpha)

    print(f"Google matrix G (alpha={alpha}):")
    for i in range(n):
        row_str = " ".join(f"{G[i][j]:.3f}" for j in range(n))
        print(f"row {i}: {row_str}")
    print()

    # Step 3: Power iteration: solve G R = R
    R, iters, last_change = pagerank_power_iteration(G, tol=1e-12)
    print("Converged PageRank vector R:")
    for i, val in enumerate(R):
        print(f"  R[{i}] = {val:.6f}")
    print(f"\nIterations: {iters}")
    print(f"Final L1 change: {last_change:.3e}\n")

    # Step 4: Sort and display importance
    pretty_print_rank(R)

    # Sanity check: R should sum to ~1
    print(f"Check sum(R) = {sum(R):.6f} (should be ~1.0)")
    print("Largest component -> most 'important' page.\n")


if __name__ == "__main__":
    demo()
