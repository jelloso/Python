import random

FONT_COLOUR = (255, 255, 255)

WIDTH = 800

HEIGHT = 800

CENTRE_X = WIDTH / 2

CENTRE_Y = HEIGHT / 2

CENTRE = (CENTRE_X, CENTRE_Y)

FINAL_LEVEL = 6

START_SPEED = 10

COLOURS = ["green", "blue"]

game_over = False

game_complete = False

current_level = 1

stars = []

animation = []

def draw():

	global starts, current_level, game_over, game_complete
	screen.clear()
	screen.blit("space", (0,0))
	if game_over:
		display_message("GAME OVER!", "Try again.")
	elif game_complete:
		display_message("YOU WON!", "Well done.")
	else:
		for star in stars:
			star.draw()

def update():
	global stars
	if len(stars) == 0:
		stars = make_stars(current_level)


def make_stars(number_of_extra_stars):
	colours_to_create = get_colours_to_create(number_of_extra_stars)
	new_stars = create_stars(colours_to_create)
	layout_stars(new_stars)
	return new_stars

def get_colours_to_create(number_of_extra_stars):
	colours_to_create = ["red"]

	for i in range(0, number_of_extra_stars):
		random_colour = random.choice(COLOURS)
		colours_to_create.append(random_colour)
	return colours_to_create

def create_stars(colours_to_create):
	new_stars = []
	for colour in colours_to_create:
		star = Actor(colour + "-star")
		new_stars.append(star)
	return new_stars

def layout_stars(stars_to_layout):
	pass

def animate_stars(stars_to_animate):
	pass

