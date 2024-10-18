import cairo
import math

#seting up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()




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




surface.write_to_png("house.png")