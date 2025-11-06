class Color(int):
    def __init__(self, int):
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
        int.color = color_map[int]

    def __str__():
        return self.color


# This now works as expected:
print(Color(1))