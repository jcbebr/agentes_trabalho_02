from advsearch.othello.board import Board
from advsearch.othello.board import from_string

# Visualização
# from pyvis.network import Network

# net = Network(height='100%', width='100%')
# net.set_options("""
# const options = {
#   "layout": {
#     "hierarchical": {
#       "enabled": true
#     }
#   },
#   "physics": {
#     "enabled": false,
#     "hierarchicalRepulsion": {
#       "centralGravity": 0,
#       "avoidOverlap": null
#     },
#     "minVelocity": 0.75,
#     "solver": "hierarchicalRepulsion"
#   }
# }
# """)

count = 0

def addNode(board, father):
    global count
    count = count + 1
    id = count
#     labelText = ""
#     #labelText = labelText + 'id  ' + str(id) + ' fth ' + str(father) + '\n'
#     labelText = labelText + 'utl ' + str(utility(board)) + '\n'
#     labelText = labelText + board.__str__()
#     net.add_node(id, label=labelText, font="14px courier")
#     if father != None:
#         net.add_edge(father, id)
    return id

## Visualização

class Exec:
    def __init__(self, nUtility, nPosition, nAlpha):
        self.nUtility = nUtility
        self.nPosition = nPosition
        self.nAlpha = nAlpha
    def __str__(self):
        return 'nUtility ' + str(self.nUtility) + ' nPosition ' + str(self.nPosition) + ' nAlpha ' + str(self.nAlpha)

mycolor = None

# Retorna o número de blocos da cor do jogador
def utility(board: Board):
    r = 0
    for t0 in board.tiles:
        for t1 in t0:
            if t1 == mycolor:
                r = r + 1
    return r

#Executa o movimento
def make_move(the_board: Board, color, camadas):
    global mycolor
    mycolor = color

    id = addNode(the_board, None)
    exec = mmax(the_board, color, -9999, 9999, int(camadas), id)

    # if exec.nPosition == (7,3):
    #     net.show('round.html')

    return exec.nPosition

def mmax(board: Board, color, alpha, beta, level, father):
    id = addNode(board, father)

    if board.is_terminal_state() or level == 0:
        return Exec(utility(board), None, None)
    level = level - 1
    
    oUtility = -9999
    oPosition = None
    
    oBoard = board
    legal_moves = oBoard.legal_moves(color)
    for position in legal_moves:
        nBoard = from_string(oBoard.__str__())
        nBoard.process_move(position, color)
        exec = mmin(nBoard, nBoard.opponent(color), alpha, beta, level, id)

        if exec.nUtility > oUtility:
            oUtility = exec.nUtility
            oPosition = position

        alpha = max(alpha, exec.nUtility)
        if beta <= alpha:
            break

        del nBoard

    return Exec(oUtility, oPosition, alpha)

def mmin(board: Board, color, alpha, beta, level, father):
    id = addNode(board, father)

    if board.is_terminal_state() or level == 0:
        return Exec(utility(board), None, None)
    level = level - 1

    oUtility = 9999
    oPosition = None

    oBoard = board
    legal_moves = oBoard.legal_moves(color)
    for position in legal_moves:
        nBoard = from_string(oBoard.__str__())
        nBoard.process_move(position, color)
        exec = mmax(nBoard, nBoard.opponent(color), alpha, beta, level, id)

        if exec.nUtility < oUtility:
            oUtility = exec.nUtility
            oPosition = position

        beta = min(beta, exec.nUtility)
        if beta <= alpha:
            break

        del nBoard

    return Exec(oUtility, oPosition, alpha)
