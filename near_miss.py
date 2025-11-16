# Fermat Near Miss Finder
# Programmer: Yamini Saraswathi
# Email: parvathalyaminisaraswathi@lewisu.edu
# Course: <Add course here if needed>
# Date: <Add today's date>
# Purpose:
#   This program lets the user search for "near misses" of Fermat’s equation:
#   x^n + y^n = z^n. For 3 <= n <= 11 and x,y >= 10 up to user value k.
#   It finds values where x^n + y^n is close to some z^n and shows which
#   combination gives the smallest "relative miss".

def get_int(message, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(message))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except:
            print("Please enter a valid number.")

def main():
    print("=== Fermat Near Miss Program ===")

    n = get_int("Enter n (3–11): ", 3, 11)
    k = get_int("Enter k (>10): ", 11)

    best_rel = None
    best_data = None

    for x in range(10, k+1):
        for y in range(10, k+1):

            S = x**n + y**n
            z = int(S**(1/n))  # approximate z
            miss1 = abs(S - z**n)
            miss2 = abs((z+1)**n - S)
            miss = min(miss1, miss2)
            rel = miss / S

            if best_rel is None or rel < best_rel:
                best_rel = rel
                best_data = (x, y, z, miss, rel)
                print(f"New best near miss:")
                print(f"  x={x}, y={y}, z={z}")
                print(f"  absolute miss = {miss}")
                print(f"  relative miss = {rel:.10f}")
                print()

    print("=== Final Best Near Miss ===")
    x, y, z, miss, rel = best_data
    print(f"x={x}, y={y}, z={z}")
    print(f"absolute miss = {miss}")
    print(f"relative miss = {rel:.10f}")

    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()
