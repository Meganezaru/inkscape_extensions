#!/usr/bin/env python
import inkex

class ArrangeCircles(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument("--rows", type=int, dest="rows", default=5, help="Number of rows")
        self.arg_parser.add_argument("--columns", type=int, dest="columns", default=5, help="Number of columns")
        self.arg_parser.add_argument("--circle_size", type=float, dest="circle_size", default=20.0, help="Size of the circles")
        self.arg_parser.add_argument("--spacing", type=float, dest="spacing", default=5.0, help="Spacing between circles")

    def effect(self):
        rows = self.options.rows
        columns = self.options.columns
        circle_size = self.options.circle_size
        spacing = self.options.spacing

        # Calculate the offsets for each row to place circles at the vertices of equilateral triangles
        x_offset = circle_size * 3**0.5 / 2
        y_offset = circle_size * 1.5

        # Create a new layer to place the circles
        layer = inkex.etree.SubElement(self.get_svg().getroot(), 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'Circles')

        # Loop through rows and columns to place circles
        for row in range(rows):
            for col in range(columns):
                # Calculate the center coordinates of the circle
                center_x = col * (circle_size + spacing) + (row % 2) * x_offset
                center_y = row * (circle_size + spacing) * 0.866 + spacing + y_offset

                # Create the circle element
                circle = inkex.etree.Element(inkex.addNS('circle', 'svg'))
                circle.set('cx', str(center_x))
                circle.set('cy', str(center_y))
                circle.set('r', str(circle_size / 2))
                circle.set('style', 'fill:none;stroke:black;stroke-width:1')

                # Append the circle to the layer
                layer.append(circle)

# Create an instance of the ArrangeCircles class and apply the effect
if __name__ == '__main__':
    effect = ArrangeCircles()
    effect.run()
