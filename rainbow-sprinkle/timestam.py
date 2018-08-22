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
    print(new_ls)
    next_item=heapq.heappop(q)
    print(next_item)
new_dict_vla={3:1234566,15:5555,30:2344444 }

set_priority_val(new_dict_vla)
