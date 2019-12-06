FILE_DIR = 'day5/data/diagnostics.txt'


# Parameter Modes:
# 0 - Position
# 1 - Immediate
# none = 0
PARAM_MODES = [0, 1]


class IntcodeComputer:
    def __init__(self):
        # Puzzle input of diagnostics
        self.diagnostics = list(map(int, open(FILE_DIR).readline().split(',')))
        # By default, parameter mode is 0
        self.param_mode = PARAM_MODES[0]
    
    def run_test(self):
        pass

    def do_opcode1(self, inputs):
        if self.param_mode == 1:
            pass
        else:
            pass
        return 0

    def do_opcode2(self, inputs):
        if self.param_mode == 1:
            pass
        else:
            pass
        return 0

    def do_opcode3(self, inputs):
        if self.param_mode == 1:
            pass
        else:
            pass
        return 0

    def do_opcode4(self, inputs):
        if self.param_mode == 1:
            pass
        else:
            pass
        return 0

    def do_opcode99(self, inputs):
        if self.param_mode == 1:
            pass
        else:
            pass
        return 0