class Board:
    ## board size is 6 * 7
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.num_to_char = {-1: '.', 0: '0', 1: 'X'}
        self.state = [[-1 for _ in range(self.columns)] for _ in range(self.rows)]
        self.valid_moves = set([(0, i) for i in range(self.columns)])


    def _to_string(self):
        bstring = ''
        for row in self.state:
            for val in row:
                bstring += self.num_to_char[val]
        return bstring

    def place(self, val, r, c):
        self.state[r][c] = val
        if r + 1 < self.rows:
            self.valid_moves.add((r + 1, c))
        self.valid_moves.remove((r, c))
        return self.check_win(val, r, c)

    def _in_bound(self, r, c):
        return (0 <= r < self.rows) and (0 <= c < self.columns)

    def _check_help(self, val, r, c, radd, cadd):
        if self._in_bound(r,c) and self.state[r][c] == -1:
            return 0, False
        if not self._in_bound(r, c) or self.state[r][c] != val:
            return 0, True

        count, blocked =  self._check_help(val, r + radd, c + cadd, radd, cadd)
        return count +1 , blocked

    def calc_score(self, val):
        maxs = -1
        for r in range(self.rows):
            for c in range(self.columns):
                if self.state[r][c] == val:
                    ver1_c, ver1_b = self._check_help(val, r - 1, c, -1, 0)
                    ver2_c, ver2_b = self._check_help(val, r + 1, c, 1, 0)
                    ver = ver1_c + ver2_c
                    if ver == 3:
                        return 4000 if val == 1 else -4000
                    if ver1_b and ver2_b == True:
                        ver = 0

                    hor1_c, hor1_b = self._check_help(val, r, c - 1, 0, -1)
                    hor2_c , hor2_b = self._check_help(val, r, c + 1, 0, 1)
                    hor = hor1_c + hor2_c
                    if hor == 3:
                        return 4000 if val == 1 else -4000
                    if hor1_b and hor2_b == True:
                        hor = 0



                    diag11_c, diag11_b  = self._check_help(val, r - 1, c - 1, -1, -1)
                    diag12_c, diag12_b = self._check_help(val, r + 1, c + 1, 1, 1)
                    diag1 = diag11_c + diag12_c
                    if diag1 == 3:
                        return 4000 if val == 1 else -4000
                    if diag11_b and diag12_b == True:
                        diag1 = 0


                    diag21_c, diag21_b = self._check_help(val, r + 1, c - 1, 1, -1)
                    diag22_c, diag22_b = self._check_help(val, r - 1, c + 1, -1, 1)
                    diag2 = diag21_c + diag22_c
                    if diag2 == 3:
                        return 4000 if val == 1 else -4000
                    if diag21_b and diag22_b == True:
                        diag2 = 0
                    maxscore = max([ver, hor, diag1, diag2]) + 1
                    maxs = max(maxscore, maxs)

        if maxs == 4:
            maxs = 4000
        if val == 0:
            return -1 * maxs
        return maxs

    #old version

    # def _check_help(self, val, r, c, radd, cadd):
    #     if not self._in_bound(r, c) or self.state[r][c] != val:
    #         return 0
    #     return 1 + self._check_help(val, r + radd, c + cadd, radd, cadd)
    #
    # def calc_score(self, val):
    #     maxs = -1
    #     for r in range(self.rows):
    #         for c in range(self.columns):
    #             if self.state[r][c] == val:
    #                 ver = self._check_help(val, r - 1, c, -1, 0) + self._check_help(val, r + 1, c, 1, 0)
    #                 hor = self._check_help(val, r, c - 1, 0, -1) + self._check_help(val, r, c + 1, 0, 1)
    #                 diag1 = self._check_help(val, r - 1, c - 1, -1, -1) + self._check_help(val, r + 1, c + 1, 1, 1)
    #                 diag2 = self._check_help(val, r + 1, c - 1, 1, -1) + self._check_help(val, r - 1, c + 1, -1, 1)
    #                 maxscore = max([ver, hor, diag1, diag2]) + 1
    #                 maxs = max(maxscore, maxs)
    #     if maxs == 4:
    #         maxs = 4000
    #     if val == 0:
    #         return -1 * maxs
    #     return maxs


    def check_win(self, val, r, c):
        '''check in all directions if 4 dots have connected'''
        # vertical
        if self._check_help(val, r - 1, c, -1, 0)[0] + self._check_help(val, r + 1, c, 1, 0)[0] == 3:
            return 1
        # horizontal
        if self._check_help(val, r, c - 1, 0, -1)[0] + self._check_help(val, r, c + 1, 0, 1)[0] == 3:
            return 1
        # diag1
        if self._check_help(val, r - 1, c - 1, -1, -1)[0] + self._check_help(val, r + 1, c + 1, 1, 1)[0] == 3:
            return 1
        # daig2
        if self._check_help(val, r + 1, c - 1, 1, -1)[0] + self._check_help(val, r - 1, c + 1, -1, 1)[0] == 3:
            return 1

        return -1

    def print_board(self):
        for row in reversed(self.state):
            board_str = ''
            for num in row:
                board_str += self.num_to_char[num] + ' '
            print(board_str)
        print('.......................')
        print('.......................')
