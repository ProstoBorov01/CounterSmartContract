import typing
from pytoniq import Cell


class StateInit:

    def __init__(self, code: Cell, data: Cell):

        self.code = code
        self.data = data


    def validate(vars: typing.List) -> bool:

        for elem in vars:
            if isinstance(elem, Cell): 
                return True

            return False

    
    