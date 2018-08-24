#this project is implemented in Python 3.6
#makes use of Heapq to sort elements
#heapq employs min binary heap but we can tweak it into max by * it by -1

from math import log, floor
import time
import heapq

new_ls=[]
new_dic={} #to store the jobs with their incoming time
q=[] #heapq

#function for initial verification to check whether the job is already on the system
def get_value_and_timestamp(user_id):
    if user_id not in new_dic:#using a simple dictionary to check whether the job is already in the system
        #test dictionary
#        new_ls.append(user_id)
        time_now=time.time()
        new_dic[user_id]=time_now
        #new_ts[user_id]=floor(time_now)
        #return(new_ts)
#        if len(new_dic)<=1:
#            return(new_dic)
#        else:
        set_priority_val(user_id)#calling the set_priority_val to build the heapq
        
    else:
       print("user already exist")

#method to allocate the key as per the requirements. the results are multiplied
#by -1 since the Heapq library uses min binary heap and we need max binary heap.

def set_priority_val(key):
    #for keys in ID_user:
        if key%3==0 and key%5==0:#"Management priority"
            new_value1=(time.time())*(-9223372036854775807)
            heapq.heappush(q,(new_value1,key,"Management Priority"))
            return(new_value1)
        elif key%3==0:#"Normal priority id"
            new_value1=max(3,((time.time())*log(time.time())))*(-1)
            #return(new_value1)
            heapq.heappush(q,(new_value1,key,"Normal Priority ID"))
            return(new_value1)
        elif key%5== 0:
            new_value1=max(4,2*(time.time())*(log(time.time())))*(-1)
            heapq.heappush(q,(new_value1,key,"VIP Priority ID"))
            return(new_value1)
        else:
            new_value1=key*(-1)
            #return(new_value1)
            heapq.heappush(q,(new_value1,key,"Normal Priority"))
            return(new_value1)
        #print(heapq.heappop(q))
#module to calculate the amount of time the job was in the Queue
#exam={1245:11111,12334:200200}
def time_of_Avgwait():
    time_of_entry=sum(new_dic.values())
    time_now_after=time.time()
    time_wait_final=((time_now_after-time_of_entry)/len(new_dic)*-1)
    print(time_wait_final)
    #return(time_wait_final)

#module to find the top most job
def top_most_item():
     next_item=heapq.heappop(q)
     return(next_item)

def all_ls_value():
    return(q)

def findin_index_value(id):
    d=[x[1] for x in q]
    i=d.index(id)
    print(i)


