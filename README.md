# DataframeGUI
Query a dataframe and filter the results

# Prerequisites
1. Ensure MySQL client is installed and you have access to the MySQL server
2. Ensure Python 3.6+ is installed and working
3. Ensure MySQLdb and flask modules are installed for Python

# OPTIONAL: Create a sample database for testing
```
mysql -u <username> -p < sql/create_database.sql 
```

## Verify database created:
1. Login
```
mysql -u <username> -p
```

2. Select all records from table
```
use SampleData;
select * from records;
```

Output should look like

```
+----+---------------------+---------+---------+---------+
| id | date                | name    | column1 | column2 |
+----+---------------------+---------+---------+---------+
|  1 | 2025-08-01 10:00:00 | Alice   |  100.50 |  200.75 |
|  2 | 2025-08-02 12:30:00 | Bob     |  150.25 |  300.10 |
|  3 | 2025-08-03 15:45:00 | Charlie |  200.00 |  400.50 |
+----+---------------------+---------+---------+---------+
```

# Running the App
```
python app.py
```

# Configure Credentials
You need to configure `credentials.json` with the proper credentials to connect to the server.  This is in the root directory and looks like:

```
{
    "username": "your_username",
    "password": "your_password",
    "hostname": "localhost",
    "database": "SampleData",
    "table": "records"
}
```
