#!/usr/bin/env python3
# ============================ Opening Comment Block =============================
# Program Title: Looking for Fermat’s Last Theorem Near Misses
# Source File: near_miss.py
#
# External files required to run: none
# External files created by this program: none
#
# Programmer Name(s):
#   - Yamini Saraswathi
#
# Programmer Email(s):
#   - parvathalyaminisaraswathi@lewisu.edu
#
# Course & Section:
#   - <COURSE & SECTION>
#
# Completion / Submission Date:
#   - <COMPLETION DATE>
#
# Program Description (one paragraph):
#   This program helps an interactive user search for “near misses” of Fermat’s
#   Last Theorem equation x^n + y^n = z^n, where 3 <= n <= 11 and 10 <= x,y <= k
#   for a user-chosen upper bound k > 10. For every pair (x, y) in this range,
#   the program computes S = x^n + y^n, finds an integer z such that z^n and
#   (z+1)^n are close to S, and calculates how far S is from the nearest z^n or
#   (z+1)^n. This distance is the absolute “miss”; dividing by S gives the
#   relative miss. Whenever a new smallest relative miss is found, the program
#   prints x, y, z, the absolute miss, and the relative miss. After checking all
#   pairs, it prints the smallest relative miss as the final result and pauses
#   so the user can review the output.
#
# Resources Used (websites, texts, AI tools, etc.):
#   - Python 3 documentation (integer arithmetic, input handling)
#   - Instructor’s assignment handout for algorithm idea
#   - ChatGPT (OpenAI) for help with structuring the solution and comments
#
# Language & Version:
#   - Python 3.x
#
# How to Run (brief):
#   - From a terminal or command prompt, run:
#       python near_miss.py
# ===============================================================================
from typing import Tuple

def get_int(message: str, min_val: int | None = None, max_val: int | None = None) -> int:
    """
    Purpose:
        Safely read an integer from the user, enforcing optional min/max limits.
    Params:
        message: Text to show to the user.
        min_val: Minimum allowed value (inclusive), or None for no limit.
        max_val: Maximum allowed value (inclusive), or None for no limit.
    Returns:
        A valid integer that satisfies the given bounds.
    """
    while True:
        raw = input(message)
        raw = raw.strip()
        try:
            value = int(raw)
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}. Please try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def compute_near_miss(x: int, y: int, n: int) -> Tuple[int, int, int, float]:
    """
    Purpose:
        For a given x, y, and n, compute:
          - S = x^n + y^n
          - an integer z near the n-th root of S
          - the absolute miss (how far S is from the closest z^n or (z+1)^n)
          - the relative miss = miss / S
    Params:
        x: integer base for x^n (>= 10)
        y: integer base for y^n (>= 10)
        n: exponent (3 <= n <= 11)
    Returns:
        (z, S, miss, relative_miss)
    """
    # Declaration: S stores the sum x^n + y^n for this pair (x, y).
    S = x**n + y**n

    # z is an approximate n-th root of S using floating-point power.
    z = int(S ** (1.0 / n))

    # We check both z and z+1 to see which gives the smaller absolute difference.
    miss1 = abs(S - z**n)
    miss2 = abs((z + 1)**n - S)

    # miss is the smaller of the two candidate misses.
    miss = miss1 if miss1 < miss2 else miss2

    # relative_miss is the miss as a fraction of S.
    relative_miss = miss / S

    return z, S, miss, relative_miss

def main() -> None:
    """
    Purpose:
        Main driver of the program.
        - Prompts the user for n and k with proper validation.
        - Loops over all x, y from 10 to k (inclusive).
        - For each pair (x, y), computes near-miss data.
        - Prints every time a new smallest relative miss is found.
        - At the end, prints the smallest relative miss as the final result and
          waits for the user to press ENTER before exiting.
    """
    print("=== Fermat Near Miss Program ===")
    print("This program searches for near misses of x^n + y^n = z^n.")
    print("You will choose n (3–11) and k (>10). We test all 10 <= x,y <= k.\n")

    # Prompt for n with bounds: 3 <= n <= 11
    n = get_int("Enter n (3–11): ", min_val=3, max_val=11)

    # Prompt for k with bound: k > 10, so we enforce k >= 11
    k = get_int("Enter k (>10): ", min_val=11)

    print(f"\nSearching for near misses with n = {n}, and 10 <= x,y <= {k}...\n")

    # best_rel_miss keeps track of the smallest relative miss seen so far.
    best_rel_miss: float | None = None
    # best_data stores the tuple (x, y, z, S, miss) for that best relative miss.
    best_data: Tuple[int, int, int, int, int] | None = None

    # Outer loop: iterate x from 10 to k (inclusive).
    for x in range(10, k + 1):
        # Inner loop: iterate y from 10 to k (inclusive) for each x.
        for y in range(10, k + 1):
            z, S, miss, rel = compute_near_miss(x, y, n)

            # If this is the first result or a better (smaller) relative miss:
            if best_rel_miss is None or rel < best_rel_miss:
                best_rel_miss = rel
                best_data = (x, y, z, S, miss)

                # Print clearly labeled new best near miss.
                print("New smallest relative miss found:")
                print(f"  n = {n}")
                print(f"  x = {x}, y = {y}, z = {z}")
                print(f"  x^n + y^n = {S}")
                print(f"  Absolute miss = {miss}")
                print(f"  Relative miss = {rel:.12f} ({rel * 100:.8f}%)\n")

    # After all combinations are tested, print the final/best result.
    if best_data is not None and best_rel_miss is not None:
        x, y, z, S, miss = best_data
        print("=== Search Complete ===")
        print("Smallest relative miss (FINAL RESULT):")
        print(f"  n = {n}")
        print(f"  x = {x}, y = {y}, z = {z}")
        print(f"  x^n + y^n = {S}")
        print(f"  Absolute miss = {miss}")
        print(f"  Relative miss = {best_rel_miss:.12f} ({best_rel_miss * 100:.8f}%)")
    else:
        print("No near misses found. (This should not normally happen.)")

    # Pause at the end so the user can read the output.
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()

