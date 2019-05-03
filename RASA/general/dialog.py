import os


class Dialog:

    @staticmethod
    def input():
        dot = int(input('input Dot: '))
        width = int(input('input Width: '))
        signed = bool(input('input Signed (True\\False):  '))
        if signed == 'True':
            signed = True
        return {'dot': dot, 'width': width, 'signed': signed}

    @staticmethod
    def get_path():
        class_name = input('input class name =  ') + '.py'
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(root_dir, 'components', class_name)
        return file_path




