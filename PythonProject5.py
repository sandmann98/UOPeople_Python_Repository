#Unit 2 Python program
# define a function to print one blank line
def new_line():
print('.')
# define a function to print 3 blank lines
def three_lines():
new_line()
new_line()
new_line()
# define a function to print 9 blank lines
def nine_lines():
three_lines()
three_lines()
three_lines()
# define a funciton to print 25 blank lines
def clear_screen():
nine_lines()
nine_lines()
three_lines()
three_lines()
new_line()
# Print nine lines to console
print("Printing nine lines")
nine_lines()
# Print 25 lines to console
print("Calling clearScreen()")
clear_screen(