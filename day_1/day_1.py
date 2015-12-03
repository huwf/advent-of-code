import io

with io.open('input.txt', 'r', encoding='utf-8') as f:
    stringy = f.read()
    current_floor = 0
    i = 0
    for s in stringy:
        i += 1
        if s == '(':
            current_floor += 1
        elif s == ')':
            current_floor -= 1

        if current_floor == -1:
            print 'First time for basement position: %d' % i

    print 'Final floor: %d' % current_floor