from general.core import Component
from general.dialog import Dialog


class RAL1PINCHSENSOR:

    def calculations(self, values):
        x_values = Component(values['dot'], values['width'],values['signed']).get_width_variable()

        y = [x/2**values['dot'] * 2 for x in x_values]
        for i, j in zip(x_values, y):
            print("\nPL Input: {}\nOutput: {}\n.".format(i, j))


RAL1PINCHSENSOR().calculations(Dialog.input())