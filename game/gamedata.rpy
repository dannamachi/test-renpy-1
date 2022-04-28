################################################################################
## Define game object structure
################################################################################

init -10 python:

    class AssetProvider:
        def __init__(self):
            anima_1_pref = 'images/sprites/anima_1/'
            self.anima_1_right = [
                'row-1-column-1.png',
                'row-1-column-2.png',
                'row-1-column-3.png',
                'row-1-column-4.png',
                'row-1-column-5.png',
                'row-1-column-6.png',
                'row-1-column-7.png',
                'row-1-column-8.png',
            ]
            for i in range(len(self.anima_1_right)):
                self.anima_1_right[i] = anima_1_pref + self.anima_1_right[i]

        
    class ClassicAnimator(renpy.Displayable):
        def __init__(self, animaLoop):
            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)
            self.animaLoop = animaLoop

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = 250
            self.by = 250
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # animation timer
            self.threshold = 0.0
            self.critical = 0.1
            self.a_index = 0

            # anima pos
            self.posx = 100
            self.posy = 100
            self.moveSpeed = 200
            self.isMoving = []

        def getAnima(self):
            return Image(self.animaLoop[self.a_index])

        def visit(self):
            return [ self.ball, self.getAnima() ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            # move ball
            self.bx += self.bdx * speed
            self.by += self.bdy * speed

            # change anima & increment threshold
            if len(self.isMoving) > 0:
                increment = dtime * 1.0
                self.threshold += increment
                if self.threshold >= self.critical:
                    self.threshold = 0.0
                    self.a_index += 1
                    if (self.a_index >= len(self.animaLoop)):
                        self.a_index = 0
            else:
                self.threshold = 0.0
                self.a_index = 0

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                            int(self.by - self.BALL_HEIGHT / 2)))

            # draw the anima
            anima = renpy.render(self.getAnima(), width, height, st, at)
            r.blit(anima, (self.posx, self.posy))

            # move the anima
            for direc in self.isMoving:
                if direc == 'left':
                    self.posx -= self.moveSpeed * dtime
                elif direc == 'right':
                    self.posx += self.moveSpeed * dtime
                

            # # Check for a winner.
            # if self.bx < -50:
            #     self.winner = "eileen"

            #     # Needed to ensure that event is called, noticing
            #     # the winner.
            #     renpy.timeout(0)

            # elif self.bx > width + 50:
            #     self.winner = "player"
            #     renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # # Mousebutton down == start the game by setting stuck to
            # # false.
            # if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            #     self.stuck = False

            #     # Ensure the pong screen updates.
            #     renpy.restart_interaction()

            # moving
            if ev.type == pygame.KEYDOWN:
                # moving left
                if ev.key == pygame.K_LEFT:
                    if not 'left' in self.isMoving:
                        self.isMoving.append('left')
                    renpy.restart_interaction()
                # moving right
                elif ev.key == pygame.K_RIGHT:
                    if not 'right' in self.isMoving:
                        self.isMoving.append('right')
                    renpy.restart_interaction()
            # not moving
            elif ev.type == pygame.KEYUP:
                # release left
                if ev.key == pygame.K_LEFT:
                    if 'left' in self.isMoving:
                        self.isMoving.remove('left')
                    renpy.restart_interaction()
                # release right
                elif ev.key == pygame.K_RIGHT:
                    if 'right' in self.isMoving:
                        self.isMoving.remove('right')
                    renpy.restart_interaction()

            raise renpy.IgnoreEvent()

    class GameData:
        def __init__(self):
            self.someList = [
                'dear god',
                'apple',
                'mint tea'
            ]
            self.anotherList = [
                {
                    'name'        : 'Mochi',
                    'age'         : 10,
                    'love_power'  : -1
                },
                {
                    'name'        : 'Kacchi',
                    'age'         : 20,
                    'love_power'  : 100
                }
            ]
            self.name = 'Hahahah'
            self.phones = []

            self.hide_phone_display = False
            self.send_to_phone = False

        def addToList(self, who, what):
            for item in self.phones:
                if item['who'] == what and item.name == who.name:
                    return

            self.phones.append({
                'who': who,
                'what': what
            })

        def getChatLines(self):
            linesList = []
            chat_count = self.getChatCount()
            chat_limit_count = 0
            for i in range(chat_count):
                # from latest message
                item = self.phones[chat_count - 1 - i] 
                lineList = divide_into_lines(item['what'], 25)
                # reverse segment as well... hmmmmm
                lineList.reverse()
                for segment in lineList:
                    linesList.append({
                        'who'  : item['who'],
                        'what' : segment
                    })
                chat_limit_count += len(lineList)
                if chat_limit_count >= numbers.chat_show:
                    break
            # reverse so show from top to bottom (mbe some way to do this in renscript ?)
            linesList.reverse()
            return linesList

        def getChatCount(self):
            return len(self.phones)

        def isHidingPhoneDisplay(self):
            return self.hide_phone_display

        def setHidePhoneDisplay(self, isHide=True):
            self.hide_phone_display = isHide

        def isSendingToPhone(self):
            return self.send_to_phone

        def setSendToPhone(self, isSend=False):
            self.send_to_phone = isSend