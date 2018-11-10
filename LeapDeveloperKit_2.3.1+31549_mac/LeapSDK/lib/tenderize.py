import pygame
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class PygameGame(object):

    def init(self):
        self.controller = Leap.Controller()
        self.win = pygame.display.set_mode((500,500))
        self.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)      
        self.dots = []  
        self.swipe = False
        self.tenderize = 0
        pass

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        frame = self.controller.frame()
        
        # for gesture in frame.gestures():
        #     if gesture.type is Leap.Gesture.TYPE_SWIPE:
        #         swipe = Leap.SwipeGesture(gesture)
        #         if abs(swipe.direction[0]) < 0.5 and swipe.direction[1] < -0.9 and abs(swipe.direction[2] < 0.5):
        #             print(swipe.speed)
        #
        
        
        pygame.draw.rect(self.win,(255,0,0),(100,300,100,100))
        pygame.draw.rect(self.win,(255,0,0),(0,0,10+(5*self.tenderize),100))

        
        for dot in self.dots:
            pygame.draw.circle(self.win, (0,255,0), (int(dot[0]),int(dot[1])), 2)

        
        for hand in frame.hands:
            print(hand.palm_velocity)
            normalized = frame.interaction_box.normalize_point(hand.palm_position, True)
            currentX = normalized[0]*500
            currentY = 500-normalized[1]*500
            currentZ = normalized[2]*200
            if currentX + currentZ / 2 < 200 and currentY < 400 and currentX + currentZ / 2 > 100 and currentY > 300 and not self.swipe:
                if hand.palm_velocity[1] < -400:
                    self.swipe = True
                    for i in range(3):
                        for j in range(3):
                            self.dots.append(((currentX + currentZ / 2)+i*5,currentY+j*5))
                    self.tenderize += abs(hand.palm_velocity[1]/80)
                
            if hand.palm_velocity[1] > 0:
                self.swipe = False
            if hand.grab_strength > 0.5:
                color = (200,200,0)
            else:
                color = (200,200,200)
            normalized = frame.interaction_box.normalize_point(hand.palm_position, True)
            pygame.draw.rect(self.win,color,(int(normalized[0]*500),500-int(normalized[1]*500),25 + normalized[2]*70,25 + normalized[2]*70))
        pygame.display.update()
            #print(normalized[0]*500)
        
        
                
            
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()