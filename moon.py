import cairo
import math

OUTPUT_DIR = "output/"

# Set up surface and context
WIDTH, HEIGHT = 800, 500
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set background color (white)
context.set_source_rgb(1, 1, 1)
context.paint()

# Translate to the moon's center and rotate the context
context.save()
context.translate(700, 80)
angle = math.radians(45)
context.rotate(angle)

# Draw the moon (slanted)
context.set_source_rgb(0.7, 0.7, 0.7)  # light gray color for the moon
context.arc(0, 0, 40, 0, 2 * math.pi)  # Draw the full circle at (0, 0)
context.fill()

# Subtract to create the crescent shape (shifted circle)
context.set_source_rgb(1, 1, 1)  # white color for the subtracting part
context.arc(-30, 0, 40, 0, 2 * math.pi)  # Shifted circle to create crescent
context.fill()
context.set_line_width(3)
context.stroke()

# Restore the context to avoid affecting other drawings
context.restore()


surface.write_to_png(f"{OUTPUT_DIR}/arrow.png")

