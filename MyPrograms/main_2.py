import turtle


class LetpyAtom:
    def __init__(self):
        # Список всех доступных цветов
        self.colors = (
            'alice blue', 'antique white', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4',
            'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 'azure1', 'azure2',
            'azure3', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanched almond',
            'blue', 'blue violet', 'blue1', 'blue2', 'blue3', 'blue4', 'brown', 'brown1', 'brown2', 'brown3', 'brown4',
            'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'CadetBlue1', 'CadetBlue2',
            'CadetBlue3', 'CadetBlue4', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate',
            'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4',
            'cornflower blue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan1', 'cyan2',
            'cyan3', 'cyan4', 'dark blue', 'dark cyan', 'dark goldenrod', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
            'DarkGoldenrod4', 'dark gray', 'dark green', 'dark grey', 'dark khaki', 'dark magenta', 'dark orange', 'DarkOrange1',
            'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'dark orchid', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
            'dark red', 'dark salmon', 'dark sea green', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4',
            'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'DeepPink1',
            'DeepPink2', 'DeepPink3', 'DeepPink4', 'deep sky blue', 'DeepSkyBlue1', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
            'dim gray', 'dim grey', 'dodger blue', 'DodgerBlue1', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'firebrick',
            'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white',
            'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'Goldenrod1', 'Goldenrod2', 'Goldenrod3', 'Goldenrod4',
            'gray', 'green', 'green yellow', 'green1', 'green2', 'green3', 'green4', 'grey', 'honeydew', 'honeydew1', 'honeydew2',
            'honeydew3', 'honeydew4', 'hot pink', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'indian red', 'IndianRed1',
            'IndianRed2', 'IndianRed3', 'IndianRed4', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2',
            'khaki3', 'khaki4', 'lavender', 'lavender blush', 'LawnGreen', 'lemon chiffon', 'light blue', 'light coral', 'light cyan',
            'LightCyan1', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'light goldenrod', 'light goldenrod yellow', 'light gray',
            'light green', 'light grey', 'light pink', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'light salmon',
            'LightSalmon1', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'light sea green', 'light sky blue', 'LightSkyBlue1',
            'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'light slate blue', 'light slate gray', 'light slate grey',
            'light steel blue', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'light yellow',
            'LightYellow1', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'lime green', 'linen', 'magenta', 'magenta1', 'magenta2',
            'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue',
            'medium orchid', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'medium purple', 'MediumPurple1',
            'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'medium sea green', 'medium slate blue', 'medium spring green',
            'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'MistyRose1', 'MistyRose2',
            'MistyRose3', 'MistyRose4', 'moccasin', 'navajo white', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'navy', 'old lace', 'olive drab', 'OliveDrab1', 'OliveDrab2', 'OliveDrab3', 'OliveDrab4', 'orange', 'orange red',
            'orange1', 'orange2', 'orange3', 'orange4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod',
            'pale green', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'pale turquoise', 'PaleTurquoise1', 'PaleTurquoise2',
            'PaleTurquoise3', 'PaleTurquoise4', 'pale violet red', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4',
            'papaya whip', 'peach puff', 'PeachPuff1', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'peru', 'pink', 'pink1', 'pink2',
            'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3',
            'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosy brown', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4',
            'royal blue', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'saddle brown', 'salmon', 'salmon1', 'salmon2',
            'salmon3', 'salmon4', 'sandy brown', 'sea green', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SeaGreen4', 'seashell',
            'seashell1', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue',
            'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'slate blue', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4',
            'slate gray', 'slate grey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'spring green', 'SpringGreen1', 'SpringGreen2',
            'SpringGreen3', 'SpringGreen4', 'steel blue', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'tan', 'tan1',
            'tan2', 'tan3', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato2',
            'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet', 'violet red',
            'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white',
            'white smoke', 'yellow', 'yellow green', 'yellow1', 'yellow2', 'yellow3', 'yellow4'
        )

        # Параметры рисования
        self.steps = range(1, 10000)

        # Настройка черепахи
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        turtle.bgcolor('black')

    def draw_pattern(self):
        """Рисует узор, используя все цвета и шаги"""
        for color, step in zip(self.colors, self.steps):
            self.t.color(color)
            self.t.forward(step)
            self.t.right(step)
            self.t.speed(300)

    def run(self):
        """Запуск программы"""
        self.draw_pattern()
        turtle.done()


# === Запуск программы ===
if __name__ == "__main__":
    atom = LetpyAtom()
    atom.run()