#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
screen_width = 400
screen_height = 400
ground_level = -200
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")
# apple = trtl.Turtle()
# apple.penup()
wn.tracer(False)
active_apple = trtl.Turtle()
letter = "a"
active_apple.penup()
active_apple.hideturtle

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
current_letters = []
apple_list = []
number_of_apples = 5

# letter_choice = rand.choice(alphabet)
currentletter = "a"

def reset_apple(active_apple):
  global currentletter
  length_of_list = len(alphabet)
  if (length_of_list != 0):
    index = rand.randint(0, length_of_list)
    currentletter = alphabet.pop(index)
    active_apple.goto(rand.randint(-(screen_height)/2, screen_height/2), rand.randint(-(screen_width)/2, screen_width/2))
    draw_apple(active_apple, currentletter)
    draw_the_letters(active_apple, currentletter)
    current_letters.append(currentletter)
    

def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_the_letters(active_apple,letter)
  wn.update()

def drop_apple(letter):
  wn.tracer(True)
  index = current_letters.index(letter)
  current_letters.pop(index)

  active_apple = apple_list.pop(index)

  active_apple.penup()
  active_apple.goto(active_apple.xcor(), ground_level)
  active_apple.clear()
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)


def draw_the_letters(active_apple, letter):
  active_apple.hideturtle()
  active_apple.goto(active_apple.xcor(), 160)
  font = ("Arial", 30)
  # active_apple.clear()
  active_apple.pendown()
  active_apple.write(letter, font = font)
  active_apple.penup()

for i in range(number_of_apples):
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  reset_apple(active_apple)
  apple_list.append(active_apple)
  # print(apple_list)
  # print(current_letters)

def check_letter_a():
  if("a" in current_letters):
    drop_apple("a")
def check_letter_b():
  if("b" in current_letters):
    drop_apple("b")
def check_letter_c():
  if("c" in current_letters):
    drop_apple("c")
def check_letter_d():
  if("d" in current_letters):
    drop_apple("d")
def check_letter_e():   
  if("e" in current_letters):
    drop_apple("e")
def check_letter_f():
  if("f" in current_letters):
    drop_apple("f")
def check_letter_g():
  if("g" in current_letters):
    drop_apple("g")
def check_letter_h():
  if("h" in current_letters):
    drop_apple("h")
def check_letter_i():
  if("i" in current_letters):
    drop_apple("i")
def check_letter_j():
  if("j" in current_letters):
    drop_apple("j")
def check_letter_k():
  if("k" in current_letters):
    drop_apple("k")
def check_letter_l():
  if("l" in current_letters):
    drop_apple("l")
def check_letter_m():
  if("m" in current_letters):
    drop_apple("m")
def check_letter_n():
  if("n" in current_letters):
    drop_apple("n")
def check_letter_o():
  if("o" in current_letters):
    drop_apple("o")
def check_letter_p():
  if("p" in current_letters):
    drop_apple("p")
def check_letter_q():
  if("q" in current_letters):
    drop_apple("q")
def check_letter_r():
  if("r" in current_letters):
    drop_apple("r")
def check_letter_s():
  if("s" in current_letters):
    drop_apple("s")
def check_letter_t():
  if("t" in current_letters):
    drop_apple("t")
def check_letter_u():
  if("u" in current_letters):
    drop_apple("u")
def check_letter_v():
  if("v" in current_letters):
    drop_apple("v")
def check_letter_w():
  if("w" in current_letters):
    drop_apple("w")
def check_letter_x():
  if("x" in current_letters):
    drop_apple("x")
def check_letter_y():
  if("y" in current_letters):
    drop_apple("y")
def check_letter_z():
  if("z" in current_letters):
    drop_apple("z")

# draw_apple(apple, "a")
wn.onkeypress(check_letter_a, "a")
wn.onkeypress(check_letter_b, "b")
wn.onkeypress(check_letter_c, "c")
wn.onkeypress(check_letter_d, "d")
wn.onkeypress(check_letter_e, "e")
wn.onkeypress(check_letter_f, "f")
wn.onkeypress(check_letter_g, "g")
wn.onkeypress(check_letter_h, "h")
wn.onkeypress(check_letter_i, "i")
wn.onkeypress(check_letter_j, "j")
wn.onkeypress(check_letter_k, "k")
wn.onkeypress(check_letter_l, "l")
wn.onkeypress(check_letter_m, "m")
wn.onkeypress(check_letter_n, "n")
wn.onkeypress(check_letter_o, "o")
wn.onkeypress(check_letter_p, "p")
wn.onkeypress(check_letter_q, "q")
wn.onkeypress(check_letter_r, "r")
wn.onkeypress(check_letter_s, "s")
wn.onkeypress(check_letter_t, "t")
wn.onkeypress(check_letter_u, "u")
wn.onkeypress(check_letter_v, "v")
wn.onkeypress(check_letter_w, "w")
wn.onkeypress(check_letter_x, "x")
wn.onkeypress(check_letter_y, "y")
wn.onkeypress(check_letter_z, "z")

wn.listen()
trtl.mainloop()