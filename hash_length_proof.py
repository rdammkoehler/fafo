#!/usr/bin/env python3
import hashlib
import random
import string
import sys
from hashlib import algorithms_available

anomaly = False
shortest_input = sys.maxsize
longest_input = sys.maxsize * -1

for algorithm in sorted(algorithms_available):
    current_hash_length = 0
    hash_lengths = set()
    try:
        for length_ex in range(0, 32):
            length = pow(2, length_ex)
            to_be_hashed = length * random.choice(string.ascii_letters)
            shortest_input = min(shortest_input, len(to_be_hashed))
            longest_input = max(longest_input, len(to_be_hashed))
            message = hashlib.new(algorithm)
            message.update(to_be_hashed.encode('utf-8'))
            if algorithm in ['shake_128', 'shake_256']:
                digest = message.hexdigest(20)
            else:
                digest = message.hexdigest()
            current_hash_length = len(digest)
            hash_lengths.add(current_hash_length)
    except Exception as ex:
        print(f'ERROR: {ex}')

    print(f'algorithm: {algorithm}')
    print(f'hash length: {current_hash_length:,d}')
    if len(hash_lengths) > 1:
        anomaly = True
        print('\033[93mThe hash length changed during execution.')
        print(f'hash lengths: {hash_lengths}')
    print(f'shortest input: {shortest_input:,d}')
    print(f'longest input: {longest_input:,d}')
    print('\n')

if anomaly:
    print('\033[93mAt least one of the hashe lengths changed during execution.')