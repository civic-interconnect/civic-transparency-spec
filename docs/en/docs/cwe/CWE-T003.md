# CWE-T003: Weak Deduplication Hash or Normalization

## Description

Deduplication hashes may use fragile normalization techniques (e.g., whitespace-only normalization) or rely on weak hash functions.

## Potential Impact

- Recycled or near-duplicate content may go undetected.
- Unstable hashes may cause false positives due to minor formatting changes.

## Detection

- Test hash stability across small variations in text or media.
- Check for collisions under common transformations (e.g., spacing, emoji variants, URL encodings).

## Mitigation

- Apply robust normalization:
  - Case folding
  - URL canonicalization
  - Emoji and Unicode normalization

- Use strong, collision-resistant hashing techniques (e.g., cryptographic hashes or rolling hashes for long content).
