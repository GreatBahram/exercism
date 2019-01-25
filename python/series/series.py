def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError('Oh no!')
    return [
        series[index: index + length]
        for index in range(length + 1)
        if len(series[index: index + length]) == length
    ]
