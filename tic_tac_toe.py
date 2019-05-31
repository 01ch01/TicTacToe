"""
Criação de um jogo da velha usando Orientação a Objetos,
com o sistema player vs player.
"""


class Player(object):
    """
    Classe Player: Esta classe será usada para criar os 2 jogadores,
    que terão nome (name) e o símbolo (symbol) - X ou O.
    """

    def __init__(self, symbol):
        self.symbol = symbol
        self.name = str(input("Insira o nome do jogador {}: ".format(self.symbol)))


class Board(object):
    """
    Classe Board: Esta classe será usada para criar o tabuleiro do jogo,
    além da inserção de X ou O no tabuleiro.
    O tabuleiro consistirá em uma lista, com números de 1 a 9,
    seguindo a ordem do teclado numérico. Dessa forma, é bem mais intuitivo para o jogador.
    """

    def __init__(self, p1, p2):
        self.board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        self.p1 = p1
        self.p2 = p2
        self.winner = 0

    @staticmethod
    def show_value_error():
        print("\n\tERRO. Por favor, tente novamente com uma opção válida!")

    def show_board(self):
        """
        Imprime o tabuleiro na ordem do teclado numérico.
        """
        for i in range(0, 9, 3):
            print("\t", self.board[i], "|", self.board[i + 1], "|", self.board[i + 2])

    def board_is_full(self):
        """
        Retorna True caso o tabuleiro esteja cheio.
        """
        for i in range(9):
            if self.board[i] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        return True

    def position_is_empty(self, position):
        """
        Retorna True caso a posição no tabuleiro esteja vazia.
        :param position: posição que o jogador escolheu.
        """
        if self.board[position] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True
        return False

    @staticmethod
    def converse(position):
        """
        Converte a posição do jogador (que ele escolheu de acordo com o teclado numérico) em
        um índice válido para a lista.
        :param position: posição que o jogador escolheu.
        :return: retorna a posição de acordo com o índice da lista.
        """
        if position == 7:
            position = 0
        elif position == 8:
            position = 1
        elif position == 9:
            position = 2
        elif position == 4:
            position = 3
        elif position == 5:
            position = 4
        elif position == 6:
            position = 5
        elif position == 1:
            position = 6
        elif position == 2:
            position = 7
        elif position == 3:
            position = 8
        return position

    def put_on_board(self, position, symbol):
        """
        Insere a posição escolhida no tabuleiro, em forma do símbolo do jogador (X ou O).
        :param position: posição escolhida pelo jogador.
        :param symbol: símbolo do jogador (X ou O).
        """
        self.board[position] = symbol

    def alinhamento_horizontal(self):
        """
        Verifica se houve um alinhamento (não vazio) na horizontal, de qualquer jogador.
        :return: retorna True caso haja um alinhamento na horizontal.
        """
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                if self.board[i] == 'X':
                    self.winner = 1
                elif self.board[i] == 'O':
                    self.winner = 2
                return True
        return False

    def alinhamento_vertical(self):
        """
        Verifica se houve um alinhamento (não vazio) na vertical, de qualquer jogador.
        :return: retorna True caso haja um alinhamento na vertical.
        """
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                if self.board[i] == 'X':
                    self.winner = 1
                elif self.board[i] == 'O':
                    self.winner = 2
                return True
        return False

    def alinhamento_diagonal(self):
        """
        Verifica se houve um alinhamento (não vazio) na diagonal, de qualquer jogador.
        :return: retorna True caso haja um alinhamento na diagonal.
        """
        for i in range(0, 3, 2):
            if self.board[i] == self.board[4] == self.board[8 - i]:
                if self.board[i] == 'X':
                    self.winner = 1
                elif self.board[i] == 'O':
                    self.winner = 2
                return True
        return False

    def won(self):
        """
        Verifica se algum alinhamento ocorreu.
        :return: retorna True caso algum alinhamento tenha ocorrido.
        """
        if self.alinhamento_diagonal() or self.alinhamento_horizontal() or self.alinhamento_vertical():
            return True
        return False

    def play(self, p1, p2):
        """
        Principal método da classe. Um laço é chamado até que haja algum vencedor,
        ou até o tabuleiro ser completamente preechido (neste último caso, não havendo vencedor, é declarado empate).
        Na vez de cada um, o tabuleiro será mostrado, o jogador informa a posição do tabuleiro que quer preencher,
        e depois, o programa verifica se o jogador atual venceu a partida.
        Em caso afirmativo, o laço é interrompido. Foi criado uma lista de jogadores para evitar duplicação de código.
        :param p1: player 1 (X)
        :param p2: player 2 (O)
        """
        players = [p1, p2]
        while self.winner == 0:
            for player in players:
                self.show_board()

                # tratamento de exceções
                while True:
                    try:
                        position = int(
                            input("\n\tQual posição {} ({}) deseja escolher? ".format(player.name, player.symbol)))
                        position = self.converse(position)
                        if self.position_is_empty(position):
                            self.put_on_board(position, player.symbol)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        self.show_value_error()

                if self.won():
                    break
                elif self.board_is_full():
                    print("\n\tEMPATE !\n")
                    exit()

        if self.winner == 1:
            print("\n\tJogador {} (X) venceu".format(self.p1.name))
        elif self.winner == 2:
            print("\n\tJogador {} (O) venceu".format(self.p2.name))


def main():
    p1 = Player('X')
    p2 = Player('O')
    board = Board(p1, p2)
    board.play(p1, p2)


if __name__ == '__main__':
    main()
