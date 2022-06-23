from copy import deepcopy
import random

class Karuko:
    #allValues = [1,2,3,4,5,6,7,8,9]
    def __init__(self, size: int):
        self.allValues = []
        for i in range(int(size * 1.5)):
            if i > 0:
                self.allValues.append(i)
        self.tiles = [['-'] * size for i in range(size)]
        self.values = deepcopy(self.tiles)
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] = self.allValues.copy()
        self.rb = 0

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
        
    def is_valid(self):
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
                
                if not has_zero and sum != self.tiles[i][0]:
                    return False
                if duplicated: 
                    return False
                    
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

                if has_zero and sum != self.tiles[0][i]:
                    return False
                if duplicated: 
                    return False

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
        # self.values[i][j].remove(value)
        removed = [[i,j]]
        # for n in self.getNeib(i, j):
        #     try:
        #         self.values[n[0]][n[1]].remove(value)
        #         removed.append([n[0],n[1]])
        #     except ValueError:
        #         pass
        return removed
    
    def removeValues(self, i, j, value, removed):
        self.tiles[i][j] = 0
        # for r in removed:
        #     self.values[r[0]][r[1]].append(value)

    def removeValue(self, i, j, value):
        self.tiles[i][j] = 0
        self.values[i][j].append(value)
        for n in self.getNeib(i, j):
            self.values[n[0]][n[1]].append(value)
        return True

    def randomSolution(self):
        for i in range(len(self.tiles)):
            if i > 0:
                for j in range(len(self.tiles)):
                    if j > 0:
                        if self.tiles[i][j] == 0:
                            self.tiles[i][j] = random.randint(1,self.allValues[len(self.allValues) - 1])

    def restrictions_breaked(self):
        rb = 0
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
                
                if not has_zero and sum != self.tiles[i][0]:
                    rb += 1
                if duplicated: 
                    rb += 1
                    
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

                if has_zero and sum != self.tiles[0][i]:
                    rb += 1
                if duplicated: 
                    rb += 1

        return rb

    def copy(self):
        ka = Karuko(len(self.tiles))
        ka.tiles = deepcopy(self.tiles)
        return ka

    def getNeib2(self):
        result = []
        for i in range(len(self.tiles)):
            if i > 0:
                for j in range(len(self.tiles)):
                    if j > 0:
                        for v in self.allValues:
                            ka = self.copy()
                            ka.tiles[i][j] = v
                            ka.rb = ka.restrictions_breaked()
                            result.append(ka)
        return result

def load_from_file(fileName):
    file = list(open(fileName, "r"))
    
    ka = Karuko(int(file[0]))
    
    for nline in range(len(file)):
        if nline > 0:
            if file[nline] == '\n':
                continue
            if file[nline] == 'result\n':
                break
            tiles = file[nline].split(',')
            for ntile in range(len(tiles)):
                ka.tiles[nline - 1][ntile] = int(tiles[ntile].strip())
    # print(ka)
    # print(ka.res())
    # print(ka.is_terminal_state())
    return ka

#load_from_file('3x3_1.txt')