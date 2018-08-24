from timestam import *
from math import log,floor
import time

#initial Unit test case for checking whether the IDs are being added
def test_initial_check():
    value1=get_value_and_timestamp(3,500)
    assert value1=="added"
def test_initial_check2():#to test whether it rejects already existing jobs
    value1=get_value_and_timestamp(3,500)
    value2=get_value_and_timestamp(3,500)
    assert value2=="ID exist"

#test case to verify whether the priority is being generates as expected

def test_time_priority():#test for priority ID
    value=floor(set_priority_val(3,100))
    testval=floor(max(3,((100)*log(100)))*(-1))
    assert value==testval
def test_time_priority2():#test for Management id
    value=set_priority_val(15,100)
    assert value== (100)*(-9223372036854775807)
def test_time_priority3():#test for VIP priority
    value=set_priority_val(5,100)
    assert value == max(4,2*(100)*(log(100)))*(-1)
def test_time_priority4():#test for normal ID
    value=set_priority_val(7,100)
    assert value==-7
#test case of averga mean time_entry
def test_Avg_mean_time():
        value=time_of_Avgwait(123)
        new_value1=377#manually Calculated value
        assert value==new_value1
#test to find the index value of particular id
#for this we are considering that the ids :3,15,5,7 are already in the Queue
#considering 15 being mangement Id it will be at 0 and  being VIP stays at
def test_find_ind():
    value=findin_index_value(5)
    assert value== 1
Fina
