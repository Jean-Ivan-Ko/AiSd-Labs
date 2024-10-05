

def decode(message: str) -> int:
    class CharState:
        def __init__(self, n: int, cnt: int):
            self.n = n
            self.cnt = cnt

    msg = message.strip()
    prev = {}
    states = []

    for idx, chr in enumerate(msg):
        if chr in prev:
            prev_idx = prev[chr]
            state = CharState(
                n = states[prev_idx].n + 1,
                cnt = states[prev_idx].cnt + states[prev_idx].n * (idx - prev_idx) + (idx - prev_idx - 1)
            )
        else:
            state = CharState(0, 0)

        states.append(state)
        prev[chr] = idx

    return sum(state.cnt for state in states)


with open("input.txt", "r") as infile:
    message = infile.readline().strip()

result = decode(message)

with open("output.txt", "w") as outfile:
    outfile.write(str(result) + "\n")


