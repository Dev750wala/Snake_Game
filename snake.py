from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_snake_parts = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.all_snake_parts.append(timmy)

    def extend(self):
        self.add_part(self.all_snake_parts[-1].position())

    def move(self):
        for part in range(len(self.all_snake_parts) - 1, 0, -1):
            new_x = self.all_snake_parts[part - 1].xcor()
            new_y = self.all_snake_parts[part - 1].ycor()
            self.all_snake_parts[part].goto(new_x, new_y)
        self.all_snake_parts[0].forward(20)

    def up(self):
        if self.all_snake_parts[0].heading() != DOWN:
            self.all_snake_parts[0].setheading(UP)

    def down(self):
        if self.all_snake_parts[0].heading() != UP:
            self.all_snake_parts[0].setheading(DOWN)

    def left(self):
        if self.all_snake_parts[0].heading() != RIGHT:
            self.all_snake_parts[0].setheading(LEFT)

    def right(self):
        if self.all_snake_parts[0].heading() != LEFT:
            self.all_snake_parts[0].setheading(RIGHT)


