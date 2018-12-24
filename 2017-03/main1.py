final = 347991

square = int(final ** 0.5)
if square % 2 == 0:
    square -= 1

halfdown = square // 2
halfup = halfdown + 1

x = square**2 + halfup
for y in range(4):
    if final <= x:
        steps = halfup + x - final
        break
    if final <= x + halfup:
        steps = halfup + final - x
        break
    x += 2*halfup

print(steps)