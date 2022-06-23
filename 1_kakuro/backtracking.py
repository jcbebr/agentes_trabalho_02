from karuko import load_from_file, Karuko
from sys import argv

class Exec:
    def __init__(self, valid, ka):
        self.is_valid = valid
        self.ka = ka

def backtracking(ka: Karuko):
    i, j = ka.get_first_empty()

    is_terminal_state = (i, j) == (0, 0)
    if ka.is_valid() and is_terminal_state:
        return Exec(True, ka)
    
    if is_terminal_state:
        return Exec(False, ka)

    for value in ka.values[i][j]:
        r = ka.insertValue(i, j, value)
        if ka.is_valid():
            exec = backtracking(ka)
            if exec.is_valid:
                return exec
        ka.removeValues(i, j, value, r)

    return Exec(False, ka)

ka = load_from_file('dataset\\'+argv[1])
exec = backtracking(ka)
if exec.is_valid:
    print(exec.ka)
else:
    print('nao deu boa')