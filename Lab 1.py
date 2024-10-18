import cairo
import math

#seting up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

#drawing bottom rectangle
ctx.rectangle(100, 450, 500, 35)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(3)
ctx.stroke()

#creating walls
ctx.move_to(110, 450)
ctx.line_to(110, 250)

ctx.move_to(590, 450)
ctx.line_to(590, 250)

ctx.move_to(300, 450)
ctx.line_to(300, 250)

ctx.set_line_width(3)
ctx.set_source_rgb(0,0,0)
ctx.stroke()

#drawing bottom left window
ctx.rectangle(130, 400, 150, 15)
ctx.set_source_rgb(0,0,0)

ctx.rectangle(140, 300, 130, 100)
ctx.set_source_rgb(0,0,0)

ctx.set_line_width(3)
ctx.stroke()

#upper left window
ctx.rectangle(180, 200, 50, 50)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(3)
ctx.stroke()

ctx.rectangle(400, 400, 150, 15)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(3)
ctx.stroke()
ctx.move_to(410, 400)
ctx.line_to(410, 300)
ctx.move_to(540, 400)
ctx.line_to(540, 300)
ctx.move_to(540, 300)
ctx.line_to(410, 300)
ctx.stroke()

# Draw the left part of the roof (triangular)
ctx.move_to(65, 270)
ctx.line_to(200, 110)
ctx.line_to(345, 270)
ctx.stroke()

ctx.move_to(80, 280)
ctx.line_to(200, 140)
ctx.line_to(330, 280)
ctx.stroke()

ctx.move_to(65, 270)
ctx.line_to(80, 280)
ctx.stroke()

ctx.move_to(345, 270)
ctx.line_to(330, 280)
ctx.stroke()

def draw_parallelogram(ctx, x, y, width, height, offset):
    ctx.move_to(x, y)  # Move to the top-left corner
    ctx.line_to(x + width, y)  # Top-right corner
    ctx.line_to(x + y + offset, y + height)  # Bottom-right corner
    ctx.line_to(y - 45 + offset, y + height)  # Bottom-left corner
    ctx.stroke()  # Draw the lines

# Adjusted parallelogram parameters to touch the roof and slant to the right
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(3)  # Line width
draw_parallelogram(ctx, 240, 150, 320, 100, 220)  # Adjusted size and position

# Translate to the moon's center and rotate the ctx
ctx.save()
ctx.translate(700, 80)
angle = math.radians(45)
ctx.rotate(angle)

# Draw the moon (slanted)
ctx.set_source_rgb(0.7, 0.7, 0.7)  # light gray color for the moon
ctx.arc(0, 0, 40, 0, 2 * math.pi)  # Draw the full circle at (0, 0)
ctx.fill()

# Subtract to create the crescent shape (shifted circle)
ctx.set_source_rgb(1, 1, 1)  # white color for the subtracting part
ctx.arc(-30, 0, 40, 0, 2 * math.pi)  # Shifted circle to create crescent
ctx.fill()
ctx.set_line_width(3)
ctx.stroke

# Restore the ctx to avoid affecting other drawings
ctx.restore()

surface.write_to_png("house.png")