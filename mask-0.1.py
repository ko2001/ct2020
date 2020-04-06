#
#   mask-0.1.py
#
#   this script generates an array of 6800*6800 circles, spaced by 10um. 
#   Requirements: python v3.6 and gdspy-1.3.1 (https://github.com/heitzmann/gdspy)
# 
#   usage: python3.6 mask-0.1.py
#
#   t.kolb@dkfz.de
# 

import gdspy
import time



# add a cell for the circles
#circle1 = gdspy.Cell('DOTS1.0UM')
circle2 = gdspy.Cell('DOTS2.0UM')

# size of the circles
#circle1.add(gdspy.Round((0, 0), 0.5, layer=2)) # 1um diameter 
circle2.add(gdspy.Round((0, 0), 1, layer=2))    # 2um diameter

# add a cell for the outline, text and arrays
rect_cell = gdspy.Cell('REFS')
#ref_cell2 = gdspy.Cell('DNA1')

# draw circle array (class gdspy.CellArray(ref_cell, columns,  rows,  spacing,  origin=(0,  0)
rect_cell.add(
    gdspy.CellArray(
        'DOTS2.0UM', 6800, 6800, (10, 10), (4100, 4100)))

# draw rectangle as border for the mask
rectangle = gdspy.Rectangle((0, 0), (76200, 76200))
rect_cell.add(rectangle)

# lable for the mask file
rect_cell.add(
    gdspy.Text(
        '2.0 um x 10 um', 1800, (27850, 73000), layer=6))

compile_date = time.strftime("%d-%m-%Y")
rect_cell.add(
    gdspy.Text(
        compile_date, 2500, (28000, 1000), layer=6))

curr_time = time.strftime("%H.%M.%S")
file_name = "Mask-{0}-{1}.gds".format(compile_date, curr_time)
print(file_name)
gdspy.write_gds(file_name, cells=[rect_cell, circle2], unit=1.0e-6, precision=1.0e-9)
