from math import log, floor
import time
import heapq

new_ls=[]
new_dic={}
q=[]

def get_value_and_timestamp(user_id):
    if user_id not in new_ls:
        time_now=time.time()
        new_ls.append(user_id)
        new_dic[user_id]=time_now
        set_priority_val(new_dic)
    else:
        print("user already exist")

#method to allocate the key as per the requirements. the results are multiplied
#by -1 since the Heapq library uses min binary heap and we need max binary heap.

def set_priority_val(ID_user):
    for key in ID_user:
        if key%3==0 and key%5==0:
            new_value1=ID_user[key]*(-1)
            heapq.heappush(q,(new_value1,key,"Management priority"))
        elif key%3==0:
            new_value1=max(3,(ID_user[key]*log(ID_user[key])))*(-1)
            heapq.heappush(q,(new_value1,key,"Normal priority id"))
        elif key%5== 0:
            new_value1=max(4,2*new*(log(new)))*(-1)
            heapq.heappush(q,(new_value1,new_value,"VIP priority"))
        else:
            new_value1=key*(-1)
            heapq.heappush(q,(new_value1,key,"Normal"))

#module to calculate the amount of time the job was in the Queue
def time_of_wait(id_value):
    time_of_entry=new_dic[id_value]
    time_now_after=time.time()
    time_wait_final=time_now_after-time_of_entry
    return(time_wait_final)

#module to find the top most job
def top_most_item():
    next_item=heapq.heappop(q)
    print(next_item)
