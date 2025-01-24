# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = '''
        SELECT
            o.OrderID,
            Customers.ContactName,
            Employees.FirstName
        FROM Orders o
        JOIN Customers ON Customers.CustomerID = o.CustomerID
        JOIN Employees ON Employees.EmployeeID = o.EmployeeID
        ORDER BY o.OrderID ASC
        '''
    data = db.execute(query)
    result = data.fetchall()
    return result

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = '''
        SELECT
            Customers.ContactName AS name,
            ROUND(SUM(OrderDetails.Quantity * OrderDetails.UnitPrice),2) AS amount
        FROM
            Orders o
        JOIN Customers ON Customers.CustomerID = o.CustomerID
        JOIN OrderDetails ON OrderDetails.OrderID = o.OrderID
        GROUP BY
            name
        ORDER BY
            amount ASC
        '''
    data = db.execute(query)
    result = data.fetchall()
    return result

def best_employee(db):
    '''Implement the best_employee method to determine who\'s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query = '''
        SELECT
            Employees.FirstName,
            Employees.LastName,
            ROUND(SUM(OrderDetails.Quantity * OrderDetails.UnitPrice), 2) AS sales
        FROM
            Orders o
        JOIN Employees ON Employees.EmployeeID = o.EmployeeID
        JOIN OrderDetails ON OrderDetails.OrderID = o.OrderID
        GROUP BY
            Employees.EmployeeID
        ORDER BY
            sales DESC
        LIMIT 1
        '''
    data = db.execute(query)
    result = data.fetchone()
    return result

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = '''
    SELECT
        c.ContactName AS name,
        COUNT(o.OrderID) AS order_count
    FROM Customers c
    LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
    GROUP BY
        c.ContactName
    ORDER BY
        order_count ASC
    '''
    data = db.execute(query)
    result = data.fetchall()
    return result
