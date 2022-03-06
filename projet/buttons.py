import pygame, random
pygame.init()
FONT = pygame.font.SysFont('Times New Roman', 20, True)

class PygameButton():
    def __init__(self, color, x, y, width, height, text = None, colorNumber = False, font=FONT):
        self.color       = color
        self.x           = x
        self.y           = y
        self.width       = width
        self.height      = height
        self.text        = text
        self.colorNumber = colorNumber
        self.font        = font

    def Construction(self, window):
        """_summary_

        Args:
            window (_type_): _description_
        """
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != None :
            text = self.font.render(str(self.text), 1, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def EndAction(self,pos):
        """_summary_

        Args:
            pos (_type_): _description_

        Returns:
            _type_: _description_
        """
        dic = {}
        dic[0], dic[1] = False, None
        if pos[0] > self.x and pos[0] < self.x +self.width:
            if pos[1] > self.y and pos[1] <self.y + self.height:
                dic[0] = True #yes, we clicked the button
                if self.colorNumber:
                    dic[1] = int(self.text)
                else:
                    if self.text is not None and self.text != "BG":
                        dic[1] = self.text #return number that is on button's text if there is any
                    else:
                        dic[1] = list()
                        for x in range (0,3):
                            dic[1].append(random.randint(0,255))
                return dic
        return dic

class Colors:

    def __init__(self, x, y, color, width):
        self.x     = x
        self.y     = y
        self.color = color
        self.width = width

    def Construction(self, window, COLORS):
        """_summary_

        Args:
            window (_type_): _description_
            COLORS (_type_): _description_
        """
        pygame.draw.rect(window, COLORS[self.color], (self.x, self.y, 50, 50), 0)

    
    def EndAction(self, pos) :
        """_summary_

        Args:
            pos (_type_): _description_

        Returns:
            _type_: _description_
        """
        List_ = []
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.width:
                List_.append(True)
                List_.append(self.color)
                return List_
        List_.append(False)
        return List_