def triplets_with_sum(sum_of_triplet):
    return {
        triplet
        for triplet in triplets_in_range(1, sum_of_triplet)
        if sum(triplet) == sum_of_triplet
    }


def triplets_in_range(range_start, range_end):
    return (
        (i, j, int((i ** 2 + j ** 2) ** 0.5))
        for i in range(range_start, range_end)
        for j in range(i, range_end)
        if is_triplet(i, j)
        
    )



def is_triplet(i, j):
    return  ((i ** 2 + j ** 2) ** 0.5) % 1 == 0
