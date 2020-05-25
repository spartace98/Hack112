# flappy bird implementation
from cmu_112_graphics import *
from tkinter import *
import random
from objectTracker import ballTracker
import cv2

def appStarted(app):
	

def initBirdAndPipes(app):
	

def keyPressed(app, event):
	if event.key == "Space" and not app.isPaused:
		doJump(app)
	elif event.key == "r":
		initBirdAndPipes(app)
	elif event.key == 'p':
		app.isPaused = not app.isPaused
		
# the bird jumps when a space is called
def doJump(app):
	app.birdY -= 50
	# everytime a jump is done, reset the delta
	app.delta = 10

def movePipes(app):
	numPipes = len(app.pipes)
	index = 0
	while index < numPipes:
		pipe = app.pipes[index]
		pipe.x0 += app.dx
		pipe.x1 += app.dx
		# checks if there is a pipe that has completely moved to the left side
		if pipe.x1 < 0:
			# pop that pipe
			app.pipesPopped.append(app.pipes.pop(0))
			# append a new Pipe
			rectWidth = app.width // 6
			# new pipe must be a distance away from the last pipe
			prevPipe = app.pipes[-1]
			prevPipeX = prevPipe.x1
			newPipeX = prevPipeX + 2*rectWidth
			newPipe = Pipe(newPipeX, newPipeX + rectWidth, newPipeX, app.height, app.radius)
			app.pipes.append(newPipe)
		else:
			index += 1

# checks if the game is over
def checkOver(app):
	if app.birdY - app.radius < 0 or app.birdY + app.radius > app.height:
		app.gameOver = True

	# if the bird collide with any of the pipe
	checkPipeCollision(app)

def checkPipeCollision(app):
	birdRadius = app.radius
	birdHead = app.birdY - birdRadius
	birdBottom = app.birdY + birdRadius
	birdLeft = app.birdX - birdRadius
	birdRight = app.birdX + birdRadius

	for pipe in app.pipes:
		pipeLeft = pipe.x0
		pipeRight = pipe.x1
		pipeTop = pipe.y0
		pipeBottom = pipe.y1
		# only check the pipe that the bird is passing through
		if birdRight >=  pipeLeft and birdLeft <= pipeRight:
			if birdHead < pipeTop or birdBottom > pipeBottom:
				app.gameOver = True
				app.currentPipe = pipe

def getScore(app):
	#  check the number of current pipes that were passed
	score = 0
	birdRadius = app.radius
	for pipe in app.pipes:
		birdLeft = app.birdX - birdRadius
		pipeRight = pipe.x1
		# only check the pipe that the bird is passing through
		if birdLeft >= pipeRight:
			score += 1
	# checks the length of the pipes popped
	score += len(app.pipesPopped)
	return score

def printScore(app, canvas):
	score = getScore(app)
	text = f'SCORE: {score}'
	canvas.create_text(app.width//2, 20, anchor = 'n', text = text, font = 'Arial 20 bold')

def timerFired(app):
    app.timer += app.timerDelay
    movePipes(app)
    app.birdY += app.delta
    # artifically creates gravity
    app.delta *= 1.3
    checkOver(app)
    if onCam:
        ret, frame = cam.read()
        # INITIALISING APRIL TAG DETECTOR
        tracker = ballTracker(frame)
        # detecting position of ball
        pos = tracker.positionTracker()
        # IF THE BALL CAN BE DETECTED
        if pos != None:
            doJump(app)
            cv2.imshow("video", tracker.draw(frame, pos))
        else:
            cv2.imshow("video", frame)

def drawBird(app, canvas):
	x0, y0 = app.birdX - app.radius, app.birdY - app.radius
	x1, y1 = app.birdX + app.radius, app.birdY + app.radius
	canvas.create_oval(x0, y0, x1, y1, fill = 'red')

def drawPipes(app, canvas):
	# draw top rectangle
	for pipe in app.pipes:
		x0, y0, x1, y1 = pipe.getTopRectCoords()
		canvas.create_rectangle(x0, y0, x1, y1, fill = 'green', width = 3)
		# draw bottom rectangle
		x2, y2, x3, y3 = pipe.getBottomRectCoords()
		canvas.create_rectangle(x2, y2, x3, y3, fill = 'green', width = 3)

def redrawAll(app, canvas):
	

# instantiate the camera
onCam = True
if onCam:
    cam = cv2.VideoCapture(0)
runApp(width=500, height=500)

