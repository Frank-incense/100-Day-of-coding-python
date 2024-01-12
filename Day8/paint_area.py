def paint_calc(height, width, cover):
    calc = (int(height) * int(width)) / int(cover)
    print(f"You'll need {round(calc)} cans of paint.")

test_h = input()
test_w = input()
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)
