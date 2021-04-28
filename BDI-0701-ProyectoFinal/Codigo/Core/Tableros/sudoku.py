import argparse
import time
from tkinter import Tk, Canvas, Frame, Label, Button, BOTH, TOP, BOTTOM, LEFT, RIGHT, X, Y

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

class SudokuError(Exception):
    """
    An application specific error.
    """
    pass

class SudokuBoard(object):
    """
    Sudoku Board representation
    """
    def __init__(self, board_file):
        self.board = self.__create_board(board_file)

    def __create_board(self, board_file):
        board=board_file
        if type(board_file)==str:
            board = []
            board_file=board_file.split("\n")
            for line in board_file:
                if len(line) > 8:
                    board.append([])
                    for c in line:
                        board[-1].append(int(c))
        return board
            
        """for line in board_file:
            line = line.strip()
            if len(line) != 9:
                raise SudokuError(
                    "Each line in the sudoku puzzle must be 9 chars long."
                )
            board.append([])
            for c in line:
                if not c.isdigit():
                    raise SudokuError(
                        "Valid characters for a sudoku puzzle must be in 0-9"
                    )
                board[-1].append(int(c))

        if len(board) != 9:
            raise SudokuError("Each sudoku puzzle must be 9 lines long")
        return board"""

class SudokuGame(object):
    """
    A Sudoku game, in charge of storing the state of the board and checking
    whether the puzzle is completed.
    """
    def __init__(self, board_file):
        self.board_file = board_file
        self.start_puzzle = SudokuBoard(board_file).board

    def start(self):
        self.game_over = False
        self.puzzle = []
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(self.start_puzzle[i][j])
                
    def check_win(self):
        for row in range(9):
            if not self.__check_row(row):
                return False
        for column in range(9):
            if not self.__check_column(column):
                return False
        for row in range(3):
            for column in range(3):
                if not self.__check_square(row, column):
                    return False
        self.game_over = True
        return True

    def __check_block(self, block):
        return set(block) == set(range(1, 10))

    def __check_row(self, row):
        return self.__check_block(self.puzzle[row])

    def __check_column(self, column):
        return self.__check_block(
            [self.puzzle[row][column] for row in range(9)]
        )

    def __check_square(self, row, column):
        return self.__check_block(
            [
                self.puzzle[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column + 1) * 3)
            ]
        )
class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, parent, game,newGame,idTablero,partida,idUsuario,engine):
        self.newGame=newGame
        self.idTablero=idTablero
        self.engine=engine
        self.idUsuario=idUsuario
        self.partida=partida
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()
        self.c,self.r=0,0
        self.lastr=[]
        self.lastc=[]
        self.proceso=0
        self.h,self.m,self.s=0,0,0
        self.iniciar()
    
    def iniciar(self, s=0):
        global proceso
        s=s+1
        self.s=s
        #etiqueta que muestra el cronometro en pantalla
        self.time['text'] = str(s)

        
        # iniciamos la cuenta progresiva de los segundos
        self.proceso=self.time.after(1000, self.iniciar, (s+1))
        
    def reanudar(self):
        global proceso
        self.s=self.s+1
        #etiqueta que muestra el cronometro en pantalla
        self.time['text'] = str(self.s)
        
        # iniciamos la cuenta progresiva de los segundos
        self.proceso=self.time.after(1000, self.iniciar, (self.s+1))
        
    def parar(self):
        global proceso
        self.time.after_cancel(self.proceso)
        

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=3)
        self.canvas = Canvas(self,
                             width=100,
                             height=HEIGHT)
        self.canvas.pack(fill=X, side=BOTTOM)
        clear_button = Button(self,
                              bg="blue3",
                              fg="white",
                              height=10,
                              width=10,
                              text="Limpiar Respuestas",
                              command=self.__clear_answers)
        undo_button = Button( self,
                              bg="blue3",
                              fg="white",
                              height=10,
                              width=10,
                              text="Deshacer Respuestas",
                              command=self.__undo_action)
        pause_button= Button(self,
                            bg="blue3",
                            fg="white",
                            height=10,
                            width=10,
                            text="Pausar juego",
                            command=self.parar)
        reanudar_button= Button(self, 
                                bg="blue3",
                                fg="white",
                                height=10,
                                width=10,
                                text="Reanudar Juego",
                                command=self.reanudar)
        reanudar_button.pack(side=LEFT, padx=8)
        pause_button.pack(side=LEFT, padx=8)
        clear_button.pack(side=LEFT, padx=8)
        undo_button.pack(side=LEFT, padx=8)

        self.time = Label(self.parent, fg='black', width=20, font=("","18"))
        self.time.pack(fill=Y, side=TOP)

        
        
                    
        '''font=("times",50,"bold"))
        clock.grid(row=2,column=1,pady=25, padx=100)
        #times()'''

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    
    
    def __draw_puzzle(self):
        """ ------------------------------------------------
            ------------------------------------------------
            ------------------------------------------------------
            ------------------------------------------------------"""
        if self.newGame:
            self.engine.IniciarJuego(self.idTablero, 0, self.partida, self.idUsuario, self.game.puzzle)
        else:
            self.game.start_puzzle=self.engine.obtenerUltimoJuego(self.idUsuario)

        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = self.game.start_puzzle[i][j]
                    if answer == original:
                        color = "black"  
                    else:
                        color="sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def __clear_answers(self):
        """ ------------------------------------------------
            ------------------------------------------------
            ------------------------------------------------------
            ------------------------------------------------------"""
       
        self.engine.EliminarJuego(self.idUsuario)
        self.game.start()
        self.canvas.delete("victory")
        self.canvas.delete("winner")
        self.__draw_puzzle()
    
    #FUNCION DESHACER ACCION
    #primero en un arreglo las coordenadas del ultimo numero ingresado en la funcion __keypressed 
    def __undo_action(self):
        self.r=self.lastr.pop()
        self.c=self.lastc.pop()
        self.game.puzzle[self.r][self.c]=None
        self.__draw_puzzle()

    def __cell_clicked(self, event):
        if self.game.game_over:
            return

        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = int((y - MARGIN) / SIDE), int((x - MARGIN) / SIDE)

            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.puzzle[row][col] == 0:
                self.row, self.col = row, col

        self.__draw_cursor()
    
    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )
    def __key_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.puzzle[self.row][self.col] = int(event.char)
            """ ------------------------------------------------
            ------------------------------------------------
            ------------------------------------------------------
            ------------------------------------------------------"""
            self.engine.guardarUltimoJuego(self.game.puzzle, self.idUsuario, self.s)

            self.lastr.append(self.row)
            self.lastc.append(self.col)
            self.col, self.row = -1, -1
            self.__draw_puzzle()
            self.__draw_cursor()
            if self.game.check_win():
                self.__draw_victory()

    def __draw_victory(self):
        
        
        nombrePartida=self.engine.obtenerNombrePartida(self.idUsuario)
        self.engine.guardarPuntuacion(nombrePartida, self.s, self.idUsuario, self.idTablero)
        self.engine.EliminarJuego(self.idUsuario)
        # create a oval (which will be a circle)
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="winner",
            fill="white", font=("Arial", 32)

        )
def parse_arguments():
    """
    Parses arguments of the form:
        sudoku.py <board name>
    Where `board name` must be in the `BOARD` list
    """
    arg_parser = argparse.ArgumentParser()

def parse_arguments():
    """
    Parses arguments of the form:
        sudoku.py <board name>
    Where `board name` must be in the `BOARD` list
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--board",
                            help="Desired board name",
                            type=str,
                            choices=BOARDS,
                            required=True)

    # Creates a dictionary of keys = argument flag, and value = argument
    args = arg_parser.parse_args()
    return args.board

if __name__ == '__main__':
    
    board_name = parse_arguments()

    with open('%s.sudoku' % board_name, 'r') as boards_file:
        game = SudokuGame(boards_file)
        game.start()

        root = Tk()
        SudokuUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    


    
