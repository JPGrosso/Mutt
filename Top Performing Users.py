# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:40:15 2019

@author: juanp

"""
#SQL challenge Top Performing Users (TPUs) 
""" For a given client, we call Top Performing Users the top 5% of users who 
have made the highest quantity (not amount!) of purchases, during the period of a month. 
Once we’ve defined these users, we analyze their behavior for strategic purposes.  
Every user is assigned a unique ID called “USER_ID”. 

Users can do all sort of events other than just purchasing. 
To identify each type of event, we have their corresponding event_ids. 
These signal different situations happening within a client’s platform. 
To illustrate this, see the following map:

#EVENT_ID = 1 -> LOGIN
#EVENT_ID = 2 -> PURCHASE
#EVENT_ID = 3 -> REGISTER
#EVENT_ID = 4 -> SHARE
    We would like you to write SQL queries for certain cases/analysis and save 
    them in one (or more) .sql files inside your repo. 
    Assume we have only one month of data:
"""
  #1-Count of UNIQUE USER_ID’s in the TPU (top 5% of purchasers, by quantity) group.
"""SELECT USER_ID AS TPU, COUNT (1) AS Number of purchases
    FROM client_database
    WHERE EVENT_ID=2
    GROUP BY USER_ID DESC 
    LIMIT (COUNT DISTINCT (USER_ID)*0.05)"""
    
# 2-Average amount of purchases for each Top Performing User (TPU) for that month.
    """SELECT USER_ID AS TPU, COUNT (1) AS Number of purchases, 
    AVG(EVENT_VALUE) AS AVG_PURCHASE_VALUE
    FROM client_database
    WHERE EVENT_ID=2
    GROUP BY USER_ID DESC 
    LIMIT (COUNT DISTINCT (USER_ID)*0.05)"""
    
#3-For each TPU, calculate the average amount of time between each pair of
# successive purchases. We call this the Time Delta between purchases.
    """SELECT USER_ID, 
    WHERE EVENT_ID=2 CASE 
        WHEN COUNT(*) < 2
            THEN 0
        ELSE DATEDIFF(
                MIN( EVENT_DATE), MAX( EVENT_DATE )) / ( COUNT(*) - 1 )
        END AS avgtime
FROM client_database
GROUP BY USER_ID DESC
 LIMIT (COUNT DISTINCT (USER_ID)*0.05)"""

    
    
  

