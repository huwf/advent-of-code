import io

with io.open('input.txt', encoding='utf-8') as f:
    total = 0
    for row in f:
        dimensions = row.split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        side_1 = l*w
        side_2 = w*h
        side_3 = h*l

        smallest_side = side_1
        for s in [side_1, side_2, side_3]:
            if s < smallest_side:
                smallest_side = s

        print "l: %d w: %d h: %d" % (l,w,h)
        current_row_total = 2*side_1 + 2*side_2 + 2*side_3
        total += current_row_total + smallest_side
    print total