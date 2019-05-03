from general.core import Component
from general.dialog import Dialog

class SaJ4MOTOR():

    def calculations(self, values):
        x_values = Component(values['dot'], values['width'],values['signed']).get_width_variable()
        motor_current = [15.019/1.647 * (x/2**values['dot']) for x in x_values]
        for i, j in zip(x_values, motor_current):
            print("\nPL Input: {}\nOutput: {}\n.".format(i, j))


SaJ4MOTOR().calculations(Dialog.input())