import sys
import hashlib
import string
import random

SHA256_input = sys.argv[1]


def randomStringGenerator():
    def randomNumGenerator():
        return random.randrange(1, 100)

    return ''.join(random.choice(string.ascii_lowercase) for _ in range(randomNumGenerator()))


def bruteforce(hashinput):
    n = 0
    generated_string = randomStringGenerator()
    generated_hash = hashlib.sha256(generated_string.encode())
    while generated_hash.hexdigest()[:6] != hashinput[:6]:
        n += 1
        stringToHash = generated_string + str(n)
        generated_hash = hashlib.sha256(stringToHash.encode())
        if generated_hash.hexdigest()[:6] == hashinput[:6]:
            print(stringToHash)
            break


bruteforce(SHA256_input)
