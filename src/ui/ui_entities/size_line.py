import pygame

from ui.ui_entities.button import Button
from ui.ui_entities.text import Text


class Sizeline:

    def __init__(self, start_x, end_x, y):

        
        self.start_x = start_x
        self.end_x = end_x
        self.y = y

        self.line_length = self.end_x-self.start_x

        self.interval_size = self.line_length/9

        self.intervals = self.produce_intervals()
    
        self.button = Button(end_x, y-12, 15, 25, "")

        self.size_text = Text("10", 1310, 250, 23)
        self.size = 10

        self.colour = (45, 45, 45)


    def produce_intervals(self):

        interval_list = []
        limit = self.start_x + (self.interval_size/2)

        for i in range(10):
            interval = limit + i*self.interval_size
            interval_list.append(interval)

        return interval_list


    def update_button_and_size(self, pos):


        x = pos[0]
        y = pos[1]

        if self.y-15 > y or y > self.y+15:
            return

        size = 0

        for limit in self.intervals:
            size += 1
            
            if x <= limit:
                self.button.x = limit - (self.interval_size/2)
                self.size_text.update_text(size)
                self.size = size
                return

        self.button.x = self.end_x

    def render(self, display):

        self.render_line(display)

        self.render_intervals(display)

        self.button.render(display)


    def render_line(self, display):

        pygame.draw.line(display, (self.colour), (self.start_x, self.y), (self.end_x, self.y), 3)


    def render_intervals(self, display):

        offset = self.interval_size/2

        interval_y1 = self.y -10
        interval_y2 = self.y +10

        for limit in self.intervals:
            
            pygame.draw.line(display, (self.colour), (limit-offset, interval_y1), (limit-offset, interval_y2), 2)


