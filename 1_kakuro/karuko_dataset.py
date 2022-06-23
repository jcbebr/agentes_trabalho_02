from copy import deepcopy
from random import shuffle

class Karuko:
    def __init__(self, size: int):
        self.allValues = []
        for i in range(int(size * 1.5)):
            if i > 0:
                self.allValues.append(i)
        self.tiles = [[0] * size for i in range(size)]
        self.values = deepcopy(self.tiles)
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                temp = self.allValues.copy()
                shuffle(temp)
                self.values[i][j] = temp

    def __str__(self):
        r = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                r += str(self.tiles[i][j]) + '\t'
            r += '\n'
        return r

    def get_first_empty(self):
        for i in range(len(self.tiles)):
            if i > 0:
                for j in range(len(self.tiles)):
                    if j > 0:
                        if self.tiles[i][j] == 0:
                            return i, j
        return 0, 0

    def is_terminal_state(self):
        return self.get_first_empty() == 0, 0
        
    def is_valid(self, insertheader = False):
        for i in range(len(self.tiles)):
            if i > 0:
                sum = 0
                has_zero = False
                allValues = self.allValues.copy()
                duplicated = False

                for j in range(len(self.tiles)):
                    if j > 0:
                        if self.tiles[i][j] == 0:
                            has_zero = True
                            break
                        if self.tiles[i][j] not in allValues:
                            duplicated = True
                            break
                        allValues.remove(self.tiles[i][j])
                        sum = sum + self.tiles[i][j]
                
                if not has_zero and sum != self.tiles[i][0] and self.tiles[i][0] != 0:
                    return False
                if duplicated: 
                    return False
                if insertheader:
                    self.tiles[i][0] = sum
                    
        for i in range(len(self.tiles)):
            if i > 0:
                sum = 0
                has_zero = True
                allValues = self.allValues.copy()
                duplicated = False

                for j in range(len(self.tiles)):
                    if j > 0:
                        if self.tiles[j][i] == 0:
                            has_zero = False
                            break
                        if self.tiles[j][i] not in allValues:
                            duplicated = True
                            break
                        allValues.remove(self.tiles[j][i])
                        sum = sum + self.tiles[j][i]

                if has_zero and sum != self.tiles[0][i] and self.tiles[0][i] != 0:
                    return False
                if duplicated:
                    return False
                if insertheader:
                    self.tiles[0][i] = sum

        return True

    def getNeib(self, i, j):
        nei = []
        if i + 1 > 0 and i + 1 < len(self.tiles):
            nei.append([i+1, j])
        if i - 1 > 0 and i - 1 < len(self.tiles):
            nei.append([i - 1, j])
        if j + 1 > 0 and j + 1 < len(self.tiles):
            nei.append([i, j + 1])
        if j - 1 > 0 and j - 1 < len(self.tiles):
            nei.append([i, j - 1])
        return nei

    def insertValue(self, i, j, value):
        self.tiles[i][j] = value
        # for n in self.getNeib(i, j):
        #     try:
        #         self.values[n[0]][n[1]].remove(value)
        #     except ValueError:
        #         pass
        return True
    
    def removeValue(self, i, j, value):
        self.tiles[i][j] = 0
        # for n in self.getNeib(i, j):
        #     self.values[n[0]][n[1]].append(value)
        return True

    def removeResult(self):
        for i in range(len(self.tiles)):
            if i > 0:
                for j in range(len(self.tiles)):
                    if j > 0:
                        self.tiles[i][j] = 0

def load_from_file(fileName):
    file = list(open(fileName, "r"))
    
    ka = Karuko(int(file[0]))
    
    for nline in range(len(file)):
        if nline > 0:
            tiles = file[nline].split(',')
            for ntile in range(len(tiles)):
                ka.tiles[nline - 1][ntile] = int(tiles[ntile].strip())
    # print(ka)
    # print(ka.res())
    # print(ka.is_terminal_state())
    return ka


class Exec:
    def __init__(self, valid, ka):
        self.is_valid = valid
        self.ka = ka

def back(ka: Karuko):
    i, j = ka.get_first_empty()

    is_terminal_state = (i, j) == (0, 0)
    if ka.is_valid() and is_terminal_state:
        return Exec(True, ka)
    
    if is_terminal_state:
        return Exec(False, ka)

    for value in ka.values[i][j]:
        ka.insertValue(i, j, value)
        #print(value, '\n', ka)
        if ka.is_valid():
            exec = back(ka)
            if exec.is_valid:
                return exec
        ka.removeValue(i, j, value)

    return Exec(False, ka)

for i in range(20):
    if i > 2:
        for j in range(3):
            writer = open('dataset\\'+str(i)+'_' + str(j+1) + '.txt', 'w')
            exec = back(Karuko(i))
            exec.ka.is_valid(True)
            if exec.is_valid:
                result = exec.ka.__str__().replace('\t\n','\n').replace('\t',',')
                exec.ka.removeResult()
                writer.writelines(str(i) + '\n')
                writer.writelines(exec.ka.__str__().replace('\t\n','\n').replace('\t',','))
                writer.writelines('result\n\n')
                writer.writelines(result)
                result
            else:
                print('nao deu boa')
            writer.close()
            del exec
            del writer