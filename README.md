# Django framework, Oracle Database, HTML5(JavaScript, CSS)

This Django App is created for the final project of Data Management course. 
Type: Individual

Situation: Your boss has come to you and wants you to create a website that allows all employees to thank each other using a system of points and rewards. Each employee will be given 1,000 points per month to give to their coworkers. They can determine the number of points to give and include a message if they wish to any other coworker. If they do not hand out all their points for the month, they lose what they do not use, and the points reset at midnight on the last day of the month. Employees can use points they have been given to turn them into gift cards – every 10,000 points is a $100 gift card. More details are below in the Requirements section.

Task: Using everything you have learned this semester, create an Oracle database and website to accomplish the goal. 

To Turn In:
•	A Word document with the following
o	URL to your website with credentials (username/password) for an administrator and five individual users
o	ER Diagram
o	All DDL and DML
o	Any assumptions you made that you feel important to call out

Requirements:
You must have the following in your database:
•	As mentioned above, users:
o	One administrator – they can see reports but cannot give or receive points
o	Five individual users – they cannot see reports; they can only give and redeem points
•	At least one stored procedure using a transaction to handle the giving of points from one user to another
•	At least one view that simplifies how the admin gets raw report data for all users of the system. This could be used to power a report below or for some other purpose
•	At least one sequence must be used for a primary key
•	All passwords must be encrypted somehow
•	At least one trigger must be used
•	Foreign keys are required on your tables as appropriate
•	Sample data for the two previous months – you will need to create a way to insert random but valid data into your tables (part of building a system is figuring out how to test it)
•	Three reports (these should show up on the website but do not need to be fancy, the data can be raw on the page)
o	One that shows the aggregate usage of points on a monthly basis – both rewards given out and rewards cashed in, as well as broken down by user, ranked in order of most points received to least
o	One that shows who isn’t giving out all of their points for the most recent month only (including those that haven’t used any) 
o	One that shows all redemptions, by month by user, for the previous two months

Other Notes:
•	It is HIGHLY suggested that you store your DDL and DML in some form of source control
•	Highly suggested to use a website framework and language you are already familiar with. Most programming languag
