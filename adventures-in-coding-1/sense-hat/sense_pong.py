## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## sense_pong.py

## LET'S PLAY PONG
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
bat_y = 4
ball_position = [3,3]
ball_velocity = [1,1]

# Clear the screen
def clear():
  sense.clear(black)

# Draw the bat in its current position
def draw_bat():
  sense.set_pixel(0, bat_y, white)
  sense.set_pixel(0, bat_y-1, white)
  sense.set_pixel(0, bat_y+1, white)

# Move the bat up
def move_up(event):
  global bat_y
  if ((event.action == 'pressed') and (bat_y > 1)):
    sense.set_pixel(0, bat_y + 1, black)
    bat_y -= 1

# Move the bat down
def move_down(event):
  global bat_y
  if ((event.action == 'pressed') and (bat_y < 6)):
    sense.set_pixel(0, bat_y - 1, black)
    bat_y += 1

# Draw the ball
def draw_ball():
  global ball_position
  global ball_velocity

  sense.set_pixel(ball_position[0], ball_position[1], black)

  ball_position[0] += ball_velocity[0]
  if ((ball_position[0] > 7) or (ball_position[0] < 0)):
    ball_position[0] -= ball_velocity[0]
    ball_velocity[0] = -ball_velocity[0]

  ball_position[1] += ball_velocity[1]
  if ((ball_position[1] > 7) or (ball_position[1] < 0)):
    ball_position[1] -= ball_velocity[1]
    ball_velocity[1] = -ball_velocity[1]
  sense.set_pixel(ball_position[0], ball_position[1], green)

# See if the ball collided with the wall
def check_collision():
  if (ball_position[0] == 0): 
    sense.show_message(":(", scroll_speed=0.15)
    reset()

  elif ((ball_position[0] == 1) and ((bat_y - 1) <= ball_position[1] <= (bat_y + 1))):
    ball_velocity[0] = -ball_velocity[0]
  
# Start the game over
def reset():
  global ball_position
  global ball_velocity
  global bat_y

  bat_y = 4
  ball_position = [3,3]
  ball_velocity = [1,1]

  clear()

# Main function
if __name__ == "__main__":
  reset()
  sense.stick.direction_up     = move_up
  sense.stick.direction_down   = move_down
  sense.stick.direction_middle = reset

  # Our game loop
  while True:
    draw_ball()
    draw_bat()
    check_collision()

    sleep(0.1)

