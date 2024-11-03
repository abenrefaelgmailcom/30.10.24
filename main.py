import func_my

help(func_my.input_int_number())

# פתרון באמצעות import
import func_my

for _ in range(5):
    func_my.print_stars()


# פתרון עם from

# main.py

# פתרון באמצעות from לייבוא הפונקציה בלבד
from func_my import print_stars

for _ in range(5):
    print_stars()

# שימוש ב-help ב-main.py
# main.py

from func_my import print_stars

# קריאה לדוקומנטציה של הפונקציה print_stars
help(print_stars)

