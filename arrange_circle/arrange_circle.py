import inkex
import math

class CreateCircles(inkex.GenerateExtension):
    container_label = 'Create Circles'
    rows_option = 'rows'
    cols_option = 'cols'
    diameter_option = 'diameter'
    space_option = 'space'

    def add_arguments(self, pars):
        pars.add_argument("--rows", type=int, help="Number of rows")
        pars.add_argument("--cols", type=int, help="Number of columns")
        pars.add_argument("--diameter", type=int, help="Diameter of circles")
        pars.add_argument("--space", type=int, help="Space between circles")

    def generate(self):
        rows = self.options.rows
        cols = self.options.cols
        diameter = self.options.diameter
        space = self.options.space

        offset = diameter + space
        for r in range(rows):
            for c in range(cols):
                x = (c + 0.5 * (r % 2)) * offset
                y = r * offset * math.sqrt(3) / 2
                style = {'stroke': '#000000', 'fill': '#ffffff'}
                attrs = {'style': str(inkex.Style(style)), 'cx': str(x), 'cy': str(y), 'r': str(diameter/2)}
                yield inkex.Circle(**attrs)

if __name__ == "__main__":
    CreateCircles().run()