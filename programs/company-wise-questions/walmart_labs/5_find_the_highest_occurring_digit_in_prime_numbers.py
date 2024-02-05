def check_prime(prime, n):
    p = 2
    while p * p <= n:
        if (prime[p] == False):
            for i in range(p * 2, n, p):
                prime[i] = True

        p += 1


# Returns maximum occurring digits in primes from l to r.
def maxDigitInPrimes(L, R):
    prime = [0] * (R + 1)

    # Finding the prime number up to R.
    check_prime(prime, R)

    # Initialse frequency of all digit to 0.
    freq = [0] * 10

    # For all number between L to R, check if prime or not. If prime,
    # incrementing the frequency of digits present in the prime number.
    for i in range(L, R + 1):
        if not prime[i]:
            p = i  # If i is prime
            while p:
                freq[p % 10] += 1
                p //= 10

    # Finding digit with highest frequency.
    max = freq[0]
    ans = 0
    for j in range(1, 10):
        if (max <= freq[j]):
            max = freq[j]
            ans = j

    return ans


if __name__ == "__main__":
    l = 1
    r = 20
    print(maxDigitInPrimes(l, r))
