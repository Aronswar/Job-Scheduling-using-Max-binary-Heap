#This project is implemented in Python 3.X
#makes use of Heapq module to sort elements
#heapq employs min binary heap but we can tweak it into max by * it by -1

from math import log, floor
import time
import heapq

new_ls=[]
new_dic={} #to store the jobs with their incoming time
q=[] #heapq

#function for initial verification to check whether the job is already on the system
def get_value_and_timestamp(user_id,time_entry):
    if user_id not in new_dic:#using a simple dictionary to check whether the job is already in the system
        new_dic[user_id]=time_entry
        set_priority_val(user_id,time_entry)#calling the set_priority_val to build the heapq
        return("added")
    else:
       print("ID already in Q")
       return("ID exist")

#method to allocate the key as per the requirements. the results are multiplied
#by -1 since the Heapq library uses min binary heap and we need max binary heap.

def set_priority_val(key,time_entry_now):
    #for keys in ID_user:
        new_time=time_entry_now
        if key%3==0 and key%5==0:#"Management priority"
            new_value1=(new_time)*(-9223372036854775807)#multiplied with the top most allowable ID to make it the highest
            heapq.heappush(q,(new_value1,key,"Management Priority"))
            return(new_value1)
        elif key%3==0:#"Normal priority id"
            new_value1=max(3,((new_time)*log(new_time)))*(-1)
            #return(new_value1)
            heapq.heappush(q,(new_value1,key,"Normal Priority ID"))
            return(new_value1)
        elif key%5== 0:
            new_value1=max(4,2*(new_time)*(log(new_time)))*(-1)
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
def time_of_Avgwait(current_time_fr):
    new_lis=[]
    for keys in new_dic:
        dif=current_time_fr-new_dic[keys]
        new_lis.append(dif)
    return((sum(new_lis))/len(new_dic))

    #uncomment it for furthur unit testing
    #print(time_wait_final)
    #return(time_wait_final)
    #return(time_wait_final)

#module to find the top most job
def top_most_item():
     next_item=heapq.heappop(q)
     return(list(next_item))

#module to print all the items in the queue
def all_ls_value():
    return(q)
#function to find a specific idex of an ID
def findin_index_value(id):
    d=[x[1] for x in q]
    i=d.index(id)
    print(i)
    return(i)




#get_value_and_timestamp(155)



#get_value_and_timestamp(155)


#time_of_Avgwait()
#top_most_item()
#top_most_item()
