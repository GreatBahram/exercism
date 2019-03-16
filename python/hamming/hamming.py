def distance(strand_a, strand_b):
    """Return the Hamming distance between two DNA strands."""
    has_same_length = len(strand_a) == len(strand_b)
    if not has_same_length:
        raise ValueError('The Hamming distance is defined for same length strands.')
    return sum(
            a != b
            for a, b in zip(strand_a, strand_b)
    )
