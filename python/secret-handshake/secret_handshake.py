HANDSHAKER = {
    8: 'jump',
    4: 'close your eyes',
    2: 'double blink',
    1: 'wink',
}

REVERSE_HANDSHAKER = {value: key for key, value in HANDSHAKER.items()} 


def handshake(code):
    output = [
        value
        for key, value in HANDSHAKER.items()
        if code & key > 0
    ]
    return output[::-1] if code < 16 else output

def secret_code(actions):
    output = [
        REVERSE_HANDSHAKER[action]
        for action in actions
    ]
    if output == sorted(output):
        return sum(output)
    return sum(output) + 16
