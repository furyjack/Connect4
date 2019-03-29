from board import Board
from node import Node
from copy import deepcopy
from tree_render import create_graph
from random import shuffle

class Game:
    def __init__(self):
        self.has_ended = False
        self.current_state = Board()
        #assuming game starts with the player
        self.turn = 0

    def play(self):
        self.turn = int(input("Who would start?\n"))
        while not self.has_ended :
            if self.turn == 0:
                self.player_move()
            else:
                self.comp_move()
            self.current_state.print_board()
        if self.turn == 1:
            print("Player won!")
        else:
            print("Computer won!")

    def player_move(self):
        try:
            r, c = input('Enter row, col\n').split(',')
            r = int(r)
            c = int(c)
        except:
            return self.player_move()
        if (r,c) not in self.current_state.valid_moves:
            print("please enter a valid move")
            return self.player_move()

        if self.current_state.place(self.turn, r, c) == 1:
            self.has_ended = True
        self.turn = 1

    def comp_move(self):
        #calculate best move and play
        #max depth 5 moves
        r,c = self.minmax()
        if self.current_state.place(self.turn, r, c) == 1:
            self.has_ended = True
        self.turn = 0

    def _minmax(self, node):
        if node.depth >= 8 or (node.lastmove and (node.board.check_win(0, node.lastmove[0], node.lastmove[1]) == 1  or node.board.check_win(1, node.lastmove[0], node.lastmove[1]) == 1)):
            node.val = node.evaluate()
            node.alpha = node.val
            node.beta = node.val
            node.isimp = True
            return node
        scores = {}
        moves = list(node.board.valid_moves)
        shuffle(moves)
        for i, move in enumerate(moves):
            nboard = deepcopy(node.board)
            didwin = nboard.place(node.chance, move[0], move[1])
            child_chance = (node.chance + 1) % 2
            child_node = Node(node.depth + 1, child_chance, nboard, 4000 if child_chance == 0 else -4000, move)
            child_node.alpha = node.alpha
            child_node.beta = node.beta
            self._minmax(child_node)
            node.children.append(child_node)
            # minimize
            if node.chance == 0:
                node.val = min(node.val, child_node.val)
                node.beta = min(node.beta, node.val)
                if node.alpha >= node.beta:
                    child_node.isimp = True
                    return child_node
            else:
                node.val = max(node.val, child_node.val)
                node.alpha = max(node.alpha, node.val)
                if node.alpha >= node.beta:
                    child_node.isimp = True
                    return child_node
            if child_node.val not in scores:
                scores[child_node.val] = i

        node.children[scores[node.val]].isimp = True
        return node.children[scores[node.val]]

    def minmax(self):
        root = Node(0, 1, self.current_state, -4000)
        bestchild = self._minmax(root)
        root.isimp = True
        create_graph(root)
        return bestchild.lastmove

obj = Game()
obj.play()