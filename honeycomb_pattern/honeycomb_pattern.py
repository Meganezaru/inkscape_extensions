import sys
import math
import inkex

class HoneycombPattern(inkex.EffectExtension):
    container_label = 'Honeycomb Pattern'
    def add_arguments(self, pars):
        pars.add_argument("--width", type=int, default=100, help="Width of the honeycomb pattern")
        pars.add_argument("--height", type=int, default=100, help="Height of the honeycomb pattern")
        pars.add_argument("--hex_size", type=int, default=50, help="Size of the hexagons")

    def create_hexagon_edges(self, x, y, size):
        points = []
        path_string = ""
        for i in range(7):  # We add 7 points to close the hexagon
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            points.append((x + size * math.cos(angle_rad), y + size * math.sin(angle_rad)))

        for i in range(7):
            if i <= 0:
                path_string += "M {:f},{:f} C {:f},{:f} ".format(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])
            else:
                path_string += "{:f},{:f} {:f},{:f}".format(points[i - 1][0], points[i - 1][1], points[i][0], points[i][1])
                if i < 6:
                    path_string += " C {:f},{:f} ".format(points[i + 1][0], points[i + 1][1])

        return path_string

    def effect(self):
        width = self.options.width
        height = self.options.height
        hex_size = self.options.hex_size

        hex_width = hex_size * 2
        hex_height = math.sqrt(3) * hex_size
        col_count = int(math.ceil(width / (0.75 * hex_width)))
        row_count = int(math.ceil(height / hex_height))

        for row in range(row_count):
            for col in range(col_count):
                x = col * 0.75 * hex_width
                y = row * hex_height
                if col % 2 == 1:
                    y += hex_height * 0.5
                
                polyline = inkex.PathElement()
                polyline.style = inkex.Style(stroke="#000000", fill="none", stroke_width="1", vector_effect="non-scaling-stroke")
                polyline.path = self.create_hexagon_edges(x, y, hex_size)
                self.svg.get_current_layer().append(polyline)

if __name__ == '__main__':
    HoneycombPattern().run()
