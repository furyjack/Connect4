from random import shuffle
import copy
class Node:
    def __init__(self, depth, chance, board, val, lastmove = None, alpha = -4000, beta = 4000):
        self.depth = depth
        self.chance = chance
        self.board = board
        self.val = val
        self.alpha = alpha # worst score for comp
        self.beta = beta # worst score for palyer
        self.children = []
        self.lastmove = lastmove
        self.isimp = False

    def evaluate(self):
        return self.board.calc_score(0) + self.board.calc_score(1)

    # def create_children(self):
    #     if self.depth >= 5 :
    #         return
    #     moves = list(self.board.valid_moves)
    #     shuffle(moves)
    #     for move in moves:
    #         nboard = copy.deepcopy(self.board)
    #         nboard.place(self.chance, move[0], move[1])
    #         if nboard.check_win(self.chance, move[0], move[1]) == 1:
    #             self.children.append(Node(self.depth + 1, 1 if self.turn == 0 else 0, nboard, -4000 if self.turn == 0 else 4000, move))
    #             break
    #         node = Node(self.depth + 1, 1 if self.turn ==0 else 0, nboard, -4000 if self.turn == 0 else 4000, move)
    #         node.create_children()
    #         self.children.append(node)