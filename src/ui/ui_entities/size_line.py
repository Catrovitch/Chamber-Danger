from re import M
import pygame

from ui.ui_entities.button import Button
from ui.ui_entities.text import Text


class Sizeline:

    def __init__(self, start_x, end_x, y, title, spectrum):

        self.start_x = start_x
        self.end_x = end_x
        self.y = y

        mid_x = (self.start_x+self.end_x)//2

        self.line_length = self.end_x-self.start_x

        self.min_size = spectrum[0]
        self.max_size = spectrum[1]

        self.interval_size = self.line_length/(self.max_size-self.min_size)

        self.intervals = self.produce_intervals()

        self.button = Button(mid_x, y-12, 15, 25, "")

        mid_point = (self.min_size+self.max_size)//2

        self.title = Text(title, self.start_x, self.y-60, 23)
        self.size_text = Text(str(mid_point), self.end_x-15, self.y-60, 23)

        self.size = mid_point

        self.colour = (45, 45, 45)

    def produce_intervals(self):

        interval_list = []
        limit = self.start_x + (self.interval_size/2)

        for i in range(self.max_size-self.min_size+1):
            interval = limit + i*self.interval_size
            interval_list.append(interval)

        return interval_list

    def update_button_and_size(self, pos):

        x = pos[0]
        y = pos[1]

        if self.y-15 > y or y > self.y+15:
            return

        size = self.min_size-1

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

        self.title.blit(display)

        self.size_text.blit(display)

    def render_line(self, display):

        pygame.draw.line(display, (self.colour),
                         (self.start_x, self.y), (self.end_x, self.y), 3)

    def render_intervals(self, display):

        offset = self.interval_size/2

        interval_y1 = self.y - 10
        interval_y2 = self.y + 10

        for limit in self.intervals:

            pygame.draw.line(display, (self.colour), (limit-offset,
                             interval_y1), (limit-offset, interval_y2), 2)
