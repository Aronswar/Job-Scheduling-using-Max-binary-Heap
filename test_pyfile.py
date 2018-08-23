from timestam import *
from math import log


def test_time_priority():
    value=set_priority_val({15 : 1000})
    assert value==-1000
def test_time_priority2():
    value=set_priority_val({3 : 1000})
    assert value== -6907.755278982137
# (max(3,(1000*log(1000))))*(-1)
def test_time_priority3():
    value=set_priority_val({4})
    assert value==-4


def test_initial_check():
    value=get_value_and_timestamp(3)
    time_now=floor(time.time())
    new_va={3:time_now}
    assert value==new_va
