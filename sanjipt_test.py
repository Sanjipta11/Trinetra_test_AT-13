'''Python Section'''
# What is decorator , write a decorator?
#    ans:- Decorator is a function it takes another function as an argument .
# ex:-
# def decorator (say_hello):
#     print("say hello")

'''2-What is lambda expression, write a lambda expression?'''
 # ans - lambda expression is a function which is use for nay number of argument in only one expression , there are 3 types of function
 #    map, filter and reduce

# add = lambda a,b : a+b
# print(add)

'''3-WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
repetitive character , without using any inbuilt function.'''


# """
# Input = "hello world"
# output=""
# for i in Input:
#     output=i+output
# print(output)


'''4-WAF , Reverse a string words.
> Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function'''
# Input = "hello world"
# output=""
# for i in Input:
#     output=i+output
# print(output)
# """
#
# "Q5"
# """WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’"""
# """def compress_string(s):
#     if not s:
#         return ""
#     result=[]
#     count=1
#     for i in range(1,len(s)):
#         if s[i]==s[i - 1]:
#             count+=1
#         else:
#             result.append(f"{count}{s[i - 1]}")
#             count = 1
#     result.append(f"{count}{s[-1]}")
#     return ''.join(result)
# input = 'aaabbaacd'
# output_string = compress_string(input)
# print("Output","=",output_string)"""

'''5- WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’'''

'''11) Difference between List vs tuple vs set vs dictionary?'''
List: Mutable  and used in sqaure bracket []
Tuple: Immutable . it uses () parenthesis bracket
Set: Mutable, but elements inside must be immutable. , use curly bracket {}
Dictionary: Mutable; keys are immutable, .

9-What is exception handling , how handel the exception in python , explain with each
block

exception handeiling is basically it allows handel error

'''Selenium'''

# 1-What is webdriver?
#  webdriver is a tool which is use for automate the web brouser funcanlity .

'''2=How to handel selective dropdown, write a snippet for it?'''



'''3-How to handel auto suggestive dropdown, write a snippet for it.?'''
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# search_boxes = driver.find_elements(By.XPATH, "//input[@type='text']")
# if search_boxes:
#     search_box = search_boxes[0]
#     search_box.send_keys(" i phone ")

'''6- Explain the wait mechanism, write syntax and snippet for it.'''

# there are two type od wait mechanism
# 1- implicit waai - it is a default waiting time for the webdriver for find the element to display
#     driver.implicitly_wait(5)
# 2-Explicity wait -it display  to wait for visible the element  to specific condition.
#     WebDriver Wait(10)
#     wait.until(EC.condition)


'''7-How to handle dynamic web element, (write at least 3 point)'''

using find_Elements , Always we have to use Xpath(preceding, following)

'''8-How many locators in selenium'''

# 8 types of locators
# ID, Name, Class Name , tag name, link text , partial link text,
# Xpath, css selector

''' 9- In web table want to fetch 3rd Column , 3rd row data, write a xpath for it.'''

# //table//tr[3]//td[3]

'''10 question '''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/")
driver.maximize_window()
driver.find_element(By.ID,"link_2").click()
time.sleep(5)
driver.find_elements(By.XPATH,"(//a[@href='https://www.nseindia.com/national-stock-exchange/about-nse-company'])[1]").click()
time.sleep(5)
driver.find_elements(By.XPATH,"(//td[@width = "8%"])[1]")


'''Unix'''

'''1-Copyafile onedirectory to another directory?'''
Ans:cp Existing directory path
     New directory path name

'''3-difference between chown vs chmod?'''
# chown will change the ownership of the file
# Chmode will change the parmission  of the file

'''4) In adirectory a find a file name abc.txt?'''
# find -name abc.txt

'''5)Why we are using sed command?'''
# for inserting and deleting using sed command

'''6) How to list directories in Unix?'''
#  use Ls command


'''SQL'''

'''#1.Explain about the DML,DDL,TCL,DQL commands?'''
# 1. DML (Data Manipulation Language) ( SELECT , INSERT, UPDATE, DELETE,)
# SELECT * FROM employees;
# INSERT INTO employees (id):
# UPDATE EMP
# DELETE FROM employees WHERE id = 1;

2. DDL (Data Definition Language)( CREATE,ALTER,DROP,TRUNCATE,)
# CREATE TABLE EMPLOYEE:
# ALTER TABLE EMPLOYEE:
# DROP TABLE EMPLOYEE:
# TRUNCATE TABLE EMPLOYEE:

3. TCL (Transaction Control Language)( COMMIT, ROLLBACK)

# COMMIT;
# ROLLBACK;

4. DQL (Data Query Language),(SELECT)

SELECT: Retrieves data



#2.What is join, explain about the all joins?

# INNERJOIN: Retrieves matching rows from both tables.
# LEFT JOIN: Retrieves all rows from the left table and matched rows from the right table.
# RIGHT JOIN: Retrieves all rows from the right table and matched rows from the left table.
# FULL JOIN: Retrieves all rows when there is a match in one of  the tables,with NULLs
#     where there is no match.
# CROSS JOIN: Retrieves the Cartesian product of both tables.
# SELF JOIN: Joins a table with itself to compare rows within the same table.

#3. Difference between Joins vs Subquery?
# Joins combine rows from two or more tablesbased on a related column between them.
# Types: INNER
# JOIN, LEFT
# JOIN, RIGHT
# JOIN, FULL
# JOIN, etc.

Subquery:
Definition: Subqueries (or nested queries) are queries embedded within another query.
They can be used in various clauses like SELECT, WHERE, FROM, or HAVING.

'''4.Find 3rd Highest Salary Of employee table ?'''
SELECT MAX(salary) AS third_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
);

'''6  Difference between Rank vs Dense_rank?'''
# Definition: The RANK() function assigns a unique rank to each distinct value in
# the result set, but it leaves gaps in the rank sequence when there are
# ties (i.e., rows with the same value).
# Example:
# Salesperson	Sales	Dense_Rank
# Alice	     500	1
# Bob	         400	2
# Carol	     400	2
# Dave	     300	3

DENSE_RANK()
# Definition: The DENSE_RANK() function assigns a unique rank to each distinct
# value without leaving gaps in the rank sequence, even when there are ties.
# example:
# Salesperson	Sales	Rank
# Alice	     500	1
# Bob	         400	2
# Carol	     400	2
# Dave	     300	4




