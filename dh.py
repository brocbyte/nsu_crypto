import random

# based on https://pub.deadnet.se/Books_on_Tech_Survival_woodworking_foraging_etc/cryptography_engineering_design_principles_and_practical_applications.pdf

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def generatePQG():
    # choose prime q (should be 256 bit long in real world)
    qbits = 8
    primes = [i for i in range((2 ** qbits) + 1, (2 ** (qbits + 1)) - 1) if isPrime(i) and isPrime(2 * i + 1)]
    q = random.choice(primes)
    print(f"q: {q}")

    # compute p
    p = 2 * q + 1
    print(f"p: {p}")

    # choose g
    g = None
    for gi in range(2, p):
        if pow(gi, q, p) > 1:
            g = gi
            break
    if g is None:
        print("error")
        return
    print(f"g: {g}")

    return p, q, g

def secret(k):
    return random.randint(1, 2**k - 1)

def public(x, g, p):
    return pow(g, x, p)

def main():
    N = int(input())
    k = int(input())
    print(f"generating {k}-bit keys for {N} users")
    p, q, g = generatePQG()

    # sanity check
    assert isPrime(p)
    assert isPrime(q)
    # assert q > (1 << 255) and q < (1 << 256)
    assert (p - 1) % q == 0
    assert g != 1 and pow(g, q, p) != 1
    secrets = [secret(k) for _ in range(N)]
    publics = [public(x, g, p) for x in secrets]
    print("secret and public keys:")
    for idx in range(N):
        print(f"#{idx}: " + "sec: {0: >5} ".format(secrets[idx]) + "pub: {0: >5}".format(publics[idx]))

    print("shared secrets:")
    for i in range(N):
        for j in range(N):
            z = pow(publics[j], secrets[i], p)
            if i != j:
                print("{0: >5}  ".format(z), end="")
                assert z == pow(publics[i], secrets[j], p)
            else:
                print("{0: >5}  ".format("-"), end="")
        print("")

if __name__ == "__main__":
    main()
