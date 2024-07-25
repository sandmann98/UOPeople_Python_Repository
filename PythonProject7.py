#Programming Assignment Unit 5
#Python Program
import math
def mysqrt(a):
 x = a
 while True:
 y = (x + a/x) / 2.0
 if y == x:
 break
 x = y
 return x
def test_square_root():
 a = 1
 while a < 26:
 mine = mysqrt(a)
 maths = math.sqrt(a)
 print("a =", a, "| mysqrt(a) =", mine, "|
math.sqrt(a) =", maths, "| diff =", abs(mine-maths))
 a = a + 1
test_square_root()

