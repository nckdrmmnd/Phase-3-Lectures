Hello and welcome to the warehouse database tracker README.

In this phase I learned one to many and many to many relationships. The SQL database in this program is randomly generated to visualize the functionality.
If you were to use this program there are a couple things to know. It is highly discouraged to manually insert the database one by one. Instead look to 
other methods that are more automatic and don't need a coffee break. 

The breakdown of the relationships is as follows.  A warehouse can have many employees and the region can have many warehouses with many employees. 
1: is functionality that will add an employee to the employee database. You must be sure to enter in all the information in this so there can be an accurate database. Again it is discouraged to add an entire list of employees by using this funcition and instead look to a script option instead. 
You can also add a warehouse from this line of logic. You can however add employees to a non existant warehouse and then add the warehouse after but
this is discouraged against as if you forget to add a warehouse with the right id there could be some problems

2: Problems that the 2 functionality can resolve. 2 deletes an entry to the database either warehouse or employee your choice. This is also easier to automate rather than enter in line by line. 

3: Can edit an entry to the database without deleting then addding for increased functionality. This is great for typos and such. The first 3 options are more for database functionality rather than getting better information out of it. 

4: 4 is where things start to get interesting. By entering in a warehouse ID you are able to see how many employees are at the warehouse. How much the warehouse is spending and how much of a percent of profits are going into the cost of labor for the warehouse. There are plans to add a list functionality to this but this function is able to be used multiple times without exiting out so you can easily compare the data to other warehouses. 

5: Is for ease of use. If you forget a exact ID than you can search for a warehouse by the location or an employee by their name. This feature is a little lack luster for me. I feel it could have been improved by converting the name or location to lowercase and then searching off of that but it does work.

The rest of the buttons are for more functionaltiy if you want so in that sense they are more of a placeholder. However 7 is nyan cat and should persit.