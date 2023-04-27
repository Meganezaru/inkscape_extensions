import sys
import math
import inkex

class FabricPattern(inkex.EffectExtension):
    container_label = 'Fabric Pattern'
    def add_arguments(self, pars):
        pars.add_argument("--width", type=float, default=100, help="Width of the fabric pattern")
        pars.add_argument("--height", type=float, default=100, help="Height of the fabric pattern")
        pars.add_argument("--thick", type=float, default=1, help="Thick of the fabric pattern")

    def create_fabric_edges(self, x, y, size, is_row_min, is_row_max, is_col_min, is_col_max):
        path_string = ""
        for i in range(4):
            if i == 0 and is_col_max:
                continue

            if i == 1 and is_row_max:
                continue

            if i == 2 and is_col_min:
                continue

            if i == 3 and is_row_min:
                continue

            angle_rad1 = math.pi / 180 * (90 * i)
            path_string += "M {:f},{:f} ".format(x, y)

            if (i == 0 and is_row_max) or (i == 1 and is_col_min) or (i == 2 and is_row_min) or (i == 3 and is_col_max):
                path_string += "l {:f},{:f} ".format(size * 6 * math.cos(angle_rad1), size * 6 * math.sin(angle_rad1))
                continue
            else:
                path_string += "l {:f},{:f} ".format(size * 4 * math.cos(angle_rad1), size * 4 * math.sin(angle_rad1))

            angle_rad2 = math.pi / 180 * (90 * i + 90)
            path_string += "l {:f},{:f} ".format(size * 4 * math.cos(angle_rad2), size * 4 * math.sin(angle_rad2))

            angle_rad3 = math.pi / 180 * (90 * i + 180)
            path_string += "l {:f},{:f} ".format(size * 2 * math.cos(angle_rad3), size * 2 * math.sin(angle_rad3))

            angle_rad4 = math.pi / 180 * (90 * i + 270)
            path_string += "l {:f},{:f} ".format(size * 2 * math.cos(angle_rad4), size * 2 * math.sin(angle_rad4))

        return path_string

    def effect(self):
        width = self.options.width
        height = self.options.height
        thick = self.options.thick

        item_size = thick * 10
        col_count = int(math.ceil(width / item_size) * 2 - 1)
        row_count = int(math.ceil(height / item_size))

        for col in range(col_count):
            process_row = row_count - col % 2
            for row in range(process_row):
                x = col * (item_size / 2)
                y = row * item_size
                if col % 2 == 1:
                    y += item_size / 2
                
                polyline = inkex.PathElement()
                polyline.style = inkex.Style(stroke="#000000", fill="none", stroke_width="1", vector_effect="non-scaling-stroke", _inkscape_stroke="hairline")
                polyline.path = self.create_fabric_edges(x, y, thick, y == 0, y == (row_count - 1) * item_size, x == 0, x == (col_count - 1) * (item_size / 2))
                self.svg.get_current_layer().append(polyline)

if __name__ == '__main__':
    FabricPattern().run()
