# DOCUMENTATION
Python acts as the front-end program and MySQL acts as the back-end program, since Python acts as the user interface and MySQL, being able to handle large amounts of data, returns all the data requested by Python.
## MySQL
The name of the MySQL database is *‘chirag’*, which consists of two tables – *‘train_detail’* and *‘user_information’*.\
\
*‘train_detail’* table consists of 8 fields – 
`train_no` , `cost` , `starting_point` , `destination` , `via` , `time_of_departure` , `date_available` and `status`. \
![Table description #1](/images/train_detail desc.jpg)
*‘user_information’* table consists of 8 fields – 
`unique_id` , `uname` , `age` , `gender` , `train_no` , `starting_point`, `destination` and `reservation`. \
![Table description #2](/images/user_information desc.jpg)
## Python
1. **railsmenu()** function starts the program and provides the user with multiple options – check the details of any train based on starting point and destination, reserve or cancel a ticket, check the PNR (Passenger Name Record) of their reservation, etc. This function is called on after the execution of functions such as train_detail(), reservation(), cancel(), displayPNR(). 

2. **train_detail()** function asks the user about the starting point and destination of their preferred train and returns with the desirable trains satisfying the given conditions and the details of those trains. 

3. **reservation()** function lets the user reserve their ticket. \
    – If the ticket is confirmed, then a message saying “Your seats are reserved” is shown and the user is given a unique ID, which refers to their ticket details. \
    – If the ticket is not confirmed, a message saying, “Your seats are not reserved” is displayed. 

4. **cancel()** function lets the user cancel their reservation with the help of the unique ID given to them, when they reserved their ticket. 

5. **displayPNR()** function displays the personal information and the train booked by the passenger(s) having the specified unique ID. 

