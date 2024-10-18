import cairo

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
