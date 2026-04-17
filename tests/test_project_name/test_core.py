import pytest

from project_name.core import increase


def test_increase():
    assert increase(2, 3) == 5
    assert increase(2, None) == 3
    assert increase(3) == 4
    with pytest.raises(TypeError):
        increase(0.5)
    with pytest.raises(TypeError):
        increase(1, 0.3)
    with pytest.raises(ValueError):
        increase(1, -1)
