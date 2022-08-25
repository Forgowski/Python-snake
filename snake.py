from turtle import Turtle
class Snake:


    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    #create the snake
    def create_snake(self):
        for _ in range(3):
             x = int(0+_ * -20)
             new_part_of_snake = Turtle(shape="square")
             new_part_of_snake.penup()
             new_part_of_snake.color("white")
             new_part_of_snake.setpos(x, 0)
             self.snake.append(new_part_of_snake)

    #snake moving forwoard
    def move_snake(self):
        self.new_place=self.snake[len(self.snake)-1].pos()
        for part in range(len(self.snake) - 1):
            self.snake[len(self.snake) - part - 1].setpos(self.snake[len(self.snake) - part - 2].pos())
        self.snake[0].forward(20)


    def turn_right(self):
        self.snake[0].right(90)

    def turn_left(self):
        self.snake[0].left(90)

    #extend snake
    def grow_up(self):
        new_part_of_snake = Turtle(shape="square")
        new_part_of_snake.penup()
        new_part_of_snake.color("white")
        new_part_of_snake.setpos(self.new_place)
        self.snake.append(new_part_of_snake)

