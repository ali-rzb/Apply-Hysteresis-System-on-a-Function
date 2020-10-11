import numpy as np


def hysteresis_apply(_input, _up_cut, _down_cut, _up_way_function, _down_way_function):

    if (_up_way_function(_up_cut) != _down_way_function(_up_cut)) | (_up_way_function(_down_cut) != _down_way_function(_down_cut)):
        return False

    if _input[0] > _up_cut:
        way = "up-cut"
    elif _input[0] < _down_cut:
        way = "down-cut"
    else:
        way = "down-way"

    _output = np.zeros(len(_input))
    for i in range(0, len(_input)):

        if (_input[i - 1] >= _up_cut) & (_input[i] < _up_cut):
            way = "up-way"
        elif (_input[i - 1] >= _down_cut) & (_input[i] < _down_cut):
            way = "down-cut"
        elif (_input[i - 1] <= _down_cut) & (_input[i] > _down_cut):
            way = "down-way"
        elif (_input[i - 1] <= _up_cut) & (_input[i] >= _up_cut):
            way = "up-cut"

        # value
        if way == "up-way":
            _output[i] = _up_way_function(_input[i])
        elif way == "down-way":
            _output[i] = _down_way_function(_input[i])
        elif way == "up-cut":
            _output[i] = _up_cut
        elif way == "down-cut":
            _output[i] = _down_cut
        else:
            _output[i] = _up_cut * 2
    return _output
