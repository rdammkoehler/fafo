# FAFO

A repo where I find out

## hash_length_proof

Within reason, does the length of the input change the length of the hash?

Hypothesis: No, the length of the hash value is uniform for any input

Proof:

| algorithm   | hash length | shortest input | longest input |
| ----------- | ----------: | -------------: | ------------: |
| blake2b     |         128 |              1 | 2,147,483,648 |
| blake2s     |          64 |              1 | 2,147,483,648 |
| md5         |          32 |              1 | 2,147,483,648 |
| md5-sha1    |          72 |              1 | 2,147,483,648 |
| ripemd160   |          40 |              1 | 2,147,483,648 |
| sha1        |          40 |              1 | 2,147,483,648 |
| sha224      |          56 |              1 | 2,147,483,648 |
| sha256      |          64 |              1 | 2,147,483,648 |
| sha384      |          96 |              1 | 2,147,483,648 |
| sha3_224    |          56 |              1 | 2,147,483,648 |
| sha3_256    |          64 |              1 | 2,147,483,648 |
| sha3_384    |          96 |              1 | 2,147,483,648 |
| sha3_512    |         128 |              1 | 2,147,483,648 |
| sha512      |         128 |              1 | 2,147,483,648 |
| sha512_224  |          56 |              1 | 2,147,483,648 |
| sha512_256  |          64 |              1 | 2,147,483,648 |
| shake_128   |          40 |              1 | 2,147,483,648 |
| shake_256   |          40 |              1 | 2,147,483,648 |
| sm3         |          64 |              1 | 2,147,483,648 |


