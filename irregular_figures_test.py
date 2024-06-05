import pytest

import irregular_figures


@pytest.mark.parametrize('side, coorx, coory, expected', [
    (3, [0, 3, 0], [0, 0, 4], (6.0, 12)),
    (4, [0, 4, 4, 0], [0, 0, 4, 4], (16.0, 16.0)),
    (0, [0, 0], [0, 3], (28.27, 18.85))
])
def test_irregular_figures(side, coorx, coory, expected):
    if side == 0:
        assert expected == irregular_figures.calculate_circle(coorx,coory)
    elif side >= 3:
        assert expected == irregular_figures.calculate_polygon(side, coorx,coory)

if __name__ == "__main__":
    pytest.main(['--no-header', __file__])