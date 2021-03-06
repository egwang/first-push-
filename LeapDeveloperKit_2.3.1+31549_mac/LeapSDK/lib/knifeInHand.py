import pygame
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class PygameGame(object):

    def init(self):
        self.controller = Leap.Controller()
        self.win = pygame.display.set_mode((500,500))
        self.controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)  
        self.openHand = pygame.image.load("openhand.png") 
        self.closedHand = pygame.image.load("closedhand.png") 
        self.knife = pygame.image.load("knife.png")
        self.fistKnife = pygame.image.load("fistknife.png")
        self.steak = pygame.image.load("steak.png")
        self.steakDim = 200
        self.steak=pygame.transform.scale(self.steak,(self.steakDim,self.steakDim))
        self.knifeX = 50
        self.knifeY = 250  
        self.steakX = 150
        self.steakY = 150  
        self.toolGrabbed = False
        self.isClosed = False
        self.lineLst = []
        self.brown = (139,69,19)
        self.black = (0,0,0)
        self.background = pygame.image.load("background.png")
        self.swipe = False
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.cut = 0
        self.score = 0
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
        textsurface = self.myfont.render("Score: " + str(int(self.score)), False, (0, 0, 0))
        self.win.blit(textsurface,(50,50))
        
        pygame.draw.rect(self.win,(255,0,0),(0,0,10+(5*self.cut),10))
        pygame.draw.polygon(self.win,(0,255,0),[(400,10),(380,20),(420,20)])
        
        print(self.cut)
        self.score = self.cut

        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                print("swipe")
                
        for hand in frame.hands:
            normalized = frame.interaction_box.normalize_point(hand.palm_position, True)
            currentX = int(normalized[0]*500)
            currentY = int(500-normalized[1]*500)
            currentZ = normalized[2]*0.5 + 0.5
            smallImg = 0
            if hand.grab_strength > 0.5:
#<<<<<<< HEAD
                #modifies image size based on the z parameter/ depth of hand
                smallImg = pygame.transform.scale(self.closedHand, (int(normalized[2]*500),int(normalized[2]*500)))
                #grabs tool if hand is closed and next to knife
                if abs(currentX-self.knifeX)<=50:
                    self.toolGrabbed = True
                    self.knifeX=int(normalized[0]*500)
                    self.knifeY=500-int(normalized[1]*500)
                    #swiches image
                    smallImg = pygame.transform.scale(self.fistKnife, (int(normalized[2]*500),int(normalized[2]*500)))
                else:
                    self.toolGrabbed = False
                    knife = pygame.transform.scale(self.knife,(150,150))
                    self.win.blit(knife,(50,250))
            #sets knife to original position if hand is open
#=======
                smallImg = pygame.transform.rotozoom(self.closedHand,0,currentZ)
                if abs(currentX-self.knifeX)<=50:
                    self.toolGrabbed = True

#>>>>>>> 8e62a992a4d4bf0780b5f92c9f963f7790a0cdc0
            else:
                self.toolGrabbed = False
                #knife = pygame.transform.scale(self.knife,(150,150))
                self.knifeX=50
                self.knifeY=250
                self.win.blit(self.knife,(self.knifeX,self.knifeY))
                smallImg = pygame.transform.rotozoom(self.openHand,0,currentZ)

            if self.toolGrabbed:
                smallImg = pygame.transform.rotozoom(self.fistKnife,0,currentZ)

                self.win.blit(self.knife,(1000,1000))
            else:
                self.win.blit(self.knife,(50,250))
            
            if self.toolGrabbed == True and self.steakX<currentX<self.steakX+self.steakDim and \
            not self.swipe:
                if hand.palm_velocity[1] < -400:
                    self.swipe = True
                    self.lineLst.append(currentX+40)
                    self.cut += 5
            
            if hand.palm_velocity[1] > 0:
                self.swipe = False
            
        #yeet
            self.win.blit(smallImg,(int(normalized[0]*500),500-int(normalized[1]*500)))
        if len(frame.hands) == 0:
            self.win.blit(self.knife,(50,250))

            

            #pygame.draw.rect(self.win,color,(int(normalized[0]*500),500-int(normalized[1]*500),normalized[2]*200,normalized[2]*200))
        pygame.display.update()
        
        
                
            
        pass
    #draws background and images that are not dependent on the hand sensoring
    def redrawAll(self, screen):
        background = pygame.transform.scale(self.background,(500,500))
        self.win.blit(background, (0,0))
        pygame.draw.rect(self.win,self.brown,[100,100,300,300])
        self.win.blit(self.steak,(self.steakX,self.steakY))
        for line in self.lineLst:
            pygame.draw.line(self.win, self.brown,(line,150), (line,350))
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