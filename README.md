# rainowproject


The project makes use of pythons heapq library to build the needed min binary heap. I have made small tweaks with respect to the priority by multiplying the priority by -1 since we need to get the top most priority on the top. 

As per the requirements the API will be having six different endpoints with respect to operations. 

how to run:

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
    
    
    
