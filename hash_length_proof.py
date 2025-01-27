import hashlib
import sys
from hashlib import algorithms_available

shortest_input = sys.maxsize
longest_input = sys.maxsize * -1
hash_length = 0

for algorithm in algorithms_available:
    exception = None
    try:
        for length_ex in range(0, 32):
            length = pow(2, length_ex)
            to_be_hashed = length * 'x'
            shortest_input = min(shortest_input, len(to_be_hashed))
            longest_input = max(longest_input, len(to_be_hashed))
            message = hashlib.new(algorithm)
            message.update(to_be_hashed.encode('utf-8'))
            digest = message.hexdigest()
            if hash_length == 0:
                hash_length = len(digest)
            if hash_length != len(digest):
                raise Exception(f'hash length changed {hash_length} != {len(digest)} @ {length}')
    except Exception as ex:
        exception = ex

    print(f'algorithm: {algorithm}')
    print(f'hash length: {hash_length:,d}')
    print(f'shortest input: {shortest_input:,d}')
    print(f'longest input: {longest_input:,d}')
    if exception:
        print(f'ERROR: {exception}')
    print('\n')
