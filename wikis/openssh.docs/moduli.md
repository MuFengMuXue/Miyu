# Moduli

The

file contains prime numbers and generators for use by

in the Diffie-Hellman Group Exchange key exchange method.

New moduli may be generated with

using a two-step process. An initial

pass, using

calculates numbers that are likely to be useful. A second

pass, using

provides a high degree of assurance that the numbers are prime and are safe for use in Diffie-Hellman operations by

This

format is used as the output from each pass.

The file consists of newline-separated records, one per modulus, containing seven space-separated fields. These fields are as follows:

The time that the modulus was last processed as YYYYMMDDHHMMSS.

Decimal number specifying the internal structure of the prime modulus. Supported types are:

Unknown, not tested.

"Safe" prime; (p-1)/2 is also prime.

Sophie Germain; 2p+1 is also prime.

Moduli candidates initially produced by

are Sophie Germain primes (type 4). Further primality testing with

produces safe prime moduli (type 2) that are ready for use in

Other types are not used by OpenSSH.

Decimal number indicating the type of primality tests that the number has been subjected to represented as a bitmask of the following values:

Not tested.

Composite number – not prime.

Sieve of Eratosthenes.

Probabilistic Miller-Rabin primality tests.

The

moduli candidate generation uses the Sieve of Eratosthenes (flag 0x02). Subsequent

primality tests are Miller-Rabin tests (flag 0x04).

Decimal number indicating the number of primality trials that have been performed on the modulus.

Decimal number indicating the size of the prime in bits.

The recommended generator for use with this modulus (hexadecimal).

The modulus itself in hexadecimal.

When performing Diffie-Hellman Group Exchange,

first estimates the size of the modulus required to produce enough Diffie-Hellman output to sufficiently key the selected symmetric cipher.

then randomly selects a modulus from

that best meets the size requirement.
