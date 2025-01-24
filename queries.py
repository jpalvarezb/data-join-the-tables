# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders ordered by order id'''
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
    '''return the total amount spent per customer ordered by ascending order'''
    query = '''
        SELECT
            Customers.ContactName AS name,
            ROUND(
                SUM(OrderDetails.Quantity * OrderDetails.UnitPrice),2)
                AS amount
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
    '''Returns employee who sells the most'''
    query = '''
        SELECT
            Employees.FirstName,
            Employees.LastName,
            ROUND(
                SUM(OrderDetails.Quantity * OrderDetails.UnitPrice), 2)
                AS sales
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
    '''Returns a list of customers with their name and ordered
    by their order count'''
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
