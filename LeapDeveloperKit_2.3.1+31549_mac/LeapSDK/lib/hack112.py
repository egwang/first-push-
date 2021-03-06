import pygame
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class PygameGame(object):

    def init(self):
        self.controller = Leap.Controller()
        self.win = pygame.display.set_mode((500,500))
<<<<<<< HEAD
        self.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)        
=======
        self.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)  
        self.openHand = pygame.image.load("openHand.png") 
        self.closedHand = pygame.image.load("closedHand.png") 
        self.knife = pygame.image.load("knife.png")
        self.fistKnife = pygame.image.load("fistknife.png")
        self.steak = pygame.image.load("steak.png")
        self.steakMod = pygame.transform.scale(self.steak, (200,200))
        self.knifeX = 50
        self.knifeY = 250    
        self.toolGrabbed = False
        self.isClosed = False
>>>>>>> 6dbf2265079e8d64e08282da44ad4934a6f99fc5
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
<<<<<<< HEAD
=======
        self.win.blit(self.steak,(150,200))
>>>>>>> 6dbf2265079e8d64e08282da44ad4934a6f99fc5
        
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                print("swipe")
                
        for hand in frame.hands:
<<<<<<< HEAD
            if hand.grab_strength > 0.5:
                color = (200,200,0)
            else:
                color = (200,200,200)
=======
>>>>>>> 6dbf2265079e8d64e08282da44ad4934a6f99fc5
            normalized = frame.interaction_box.normalize_point(hand.palm_position, True)
            currentX = int(normalized[0]*500)
            currentY = int(500-normalized[1]*500)
            if hand.grab_strength > 0.5:
                smallImg = pygame.transform.scale(self.closedHand, (int(normalized[2]*500),int(normalized[2]*500)))
                if abs(currentX-self.knifeX)<=50:
                    self.knifeX=int(normalized[0]*500)
                    self.knifeY=500-int(normlized[1]*500)
                    smallImg = pygame.transform.scale(self.fistKnife, (int(normalized[2]*500),int(normalized[2]*500)))
                else:
                    knife = pygame.transform.scale(self.knife,(80,80))

                    self.win.blit(knife,(50,50))
            else:
                knife = pygame.transform.scale(self.knife,(80,80))
                self.knifeX=50
                self.knifeY=250
                self.win.blit(knife,(self.knifeX,self.knifeY))
                smallImg = pygame.transform.scale(self.openHand, (int(normalized[2]*500),int(normalized[2]*500)))
            
        
            self.win.blit(smallImg,(int(normalized[0]*500),500-int(normalized[1]*500)))


            print(normalized)

            #pygame.draw.rect(self.win,color,(int(normalized[0]*500),500-int(normalized[1]*500),normalized[2]*200,normalized[2]*200))
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