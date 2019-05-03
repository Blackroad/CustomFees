from general.core import Component
from general.dialog import Dialog


class RaJ5JFS:
    seb_output = 2.00662
    capacity = 200
    el_gain = 132.83
    offset = 35.433

    def calculations(self, values):
        x_values = Component(values['dot'], values['width'],values['signed']).get_width_variable()
        gain = float(self.capacity/(self.seb_output/1000*self.el_gain))
        force_values = [float(gain*(x/2 ** values['dot']) - self.offset) for x in x_values]
        for i, j in zip(x_values, force_values):
            print("\nPL Input: {}\nOutput: {}\n.".format(i, j))


RaJ5JFS().calculations(Dialog.input())