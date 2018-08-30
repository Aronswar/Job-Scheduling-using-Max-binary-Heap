# rainbowproject


The basic idea of this project is to develop a program which will handle the job requests as per the Priority we allocate and serve it using a Restful API endpoints.

Things considered during the implementation:
1. There are 4 classes of IDs, normal, priority, VIP, and management override.
    (1) IDs that are evenly divisible by 3 are priority IDs.
    (2) IDs that are evenly divisible by 5 are VIP IDs.
    (3) IDs that are evenly divisible by both 3 and 5 are management override
        IDs.
    (4) IDs that are not evenly divisible by 3 or 5 are normal IDs.
2. They are sorted with the help of the following formulation:
    (1) Normal IDs are given a rank equal to the number of seconds they’ve
        been in the queue.
    (2) Priority IDs are given a rank equal to the result of applying the fol-
        lowing formula to the number of seconds they’ve been in the queue:
        max(3, n log n)
    (3) VIP IDs are given a rank equal to the result of applying the following
        formula to the number of seconds they’ve been in the queue:
        max(4, 2n log n)
    (4) Management Override IDs are always ranked ahead of all other IDs
        and are ranked among themselves according to the number of seconds
        they’ve been in the queue.

The project makes use of pythons heapq library to build the needed min binary heap. I have made small tweaks with respect to the priority by multiplying the priority by -1 since we need to get the top most priority on the top. 

As per the requirements the API will be having six different endpoints with respect to operations:
    (1) An endpoint for adding a ID to queue (enqueue). 
    (2) An endpoint for getting the top ID from the queue and removing it
        it was entered into the queue.
    (3) An endpoint for getting the list of IDs in the queue. 
    (4) An endpoint for removing a specific ID from the queue. 
    (5) An endpoint to get the position of a specific ID in the queue.
    (6) An endpoint to get the average(mean) wait time. .

how to run the program:

1. Install all the requirements from the requirement.txt file
    you can just run pip install - r requirement.txt

2. The program can be executed by the command
    python3 API_file.py
    this file runs the restful api. Shows the Swagger editor
    1. to obtain the documentation just click on the link to the json file

3.You can also run the logic separately without the need of API file
    1. Run python3 timestam.py
    2. else just import * from timestam and can play around.
    
4. The pytests can be executed simply by the command pytest
    To know more details about the tests run pytest -q
    
    
    
