class ColoredInt(int):
    def __str__(self):
        color_map = {
            0: "\033[31m",                   # red foreground
            1: "\033[97m",                   # white background
            2: "\033[31m",                   # red foreground
            3: "\033[103m",                  # light yellow background
            4: "\033[44m",                   # dark blue background
            5: "\033[42m",                   # green background
            6: "\033[33m",                   # yellow background
            7: "\033[105m",                  # pink background
            8: "\033[45m",                   # purple background
            9: "\033[48;5;208m",             # orange background (256-color)
            10: "\033[48;5;22m",             # darker green background (256-color)
            11: "\033[49m",                  # default background (body color)
            12: "\033[46m",                  # cyan background
        }
        reset = "\033[0m"
        color = color_map.get(self, "")
        return f"{color}{super().__str__()}{reset}"

    def __repr__(self):
        color_map = {
            0: "\033[97m",
            1: "\033[96m",
            2: "\033[31m",
            3: "\033[93m",
            4: "\033[36m",
            5: "\033[32m",
            6: "\033[33m",
            7: "\033[95m",
            8: "\033[35m",
            9: "\033[38;5;208m",
            10: "\033[38;5;22m",
            11: "\033[39m",
            12: "\033[36m",
        }
        reset = "\033[0m"
        color = color_map.get(self, "")
        base_repr = int.__repr__(self)
        return f"{color}{base_repr}{reset}"
