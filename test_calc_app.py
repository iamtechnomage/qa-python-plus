import pytest
from src.calc import calc


@pytest.mark.parametrize("operation, first_int, second_int, result",
                         [("sum", 1, 2, 3),
                          ("subt", 5, 4, 1),
                          ("mult", 1, 2, 2),
                          ("div", 20, 2, 10), ],
                         )
def test_calc_operations(operation, first_int, second_int, result):
    assert calc(operation=operation,
                first_int=first_int,
                second_int=second_int,) == result


@pytest.mark.parametrize("operation, first_int, second_int, result",
                         [("sim", 1, 2, Exception("Wrong operation")), ],
                         ids=["Exception test"]
                         )
def test_calc_operations_exception(operation, first_int, second_int, result):
    with pytest.raises(Exception):
        calc(operation=operation,
             first_int=first_int,
             second_int=second_int,)
