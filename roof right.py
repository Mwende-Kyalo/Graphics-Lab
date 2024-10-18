import cairo
from main import ctx
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 700, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light gray background
ctx.paint()

def draw_parallelogram(ctx, x, y, width, height, offset):
    ctx.move_to(x, y)
    ctx.line_to(x + width, y)
    ctx.line_to(x + y + offset, y + height)
    ctx.line_to(y - 45 + offset, y + height)
    ctx.stroke()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(3)  # Line width
draw_parallelogram(ctx, 240, 150, 320, 100, 220)

