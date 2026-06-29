# JDBC and MySQL

This document describes how to set up your Arch system so that MySQL databases can be accessed via Java programs.

## Installation
## Installing MySQL
Install a MySQL implementation.

To allow for network access, make sure that  has the following line commented out, as shown here:

 #skip-networking

Your MySQL version may use the following line instead to restrict network access:

 bind-address = *

Then, start the MySQL service.

## Installing JDBC
Install a JDBC driver according to your MySQL variant:

*  - for the Arch Linux endorsed server
*  - for the Oracle variant

## Testing
To access MySQL's command line tool, run:

 $ mysql

## Creating the test database
The following commands create a database test, and grant all privileges to user foo identified by password bar. Change the variables at your discretion.

 create database test;
 grant all privileges on test.* to foo@localhost identified by "bar";
 flush privileges;

Afterwards, use  to exit the command line tool.

## Creating the test program
Use a text editor to create the file  with the following code in it. You will need to change the username and password accordingly.

{{bc|1=
import java.sql.*;

public class DBDemo {
  public static void main(String[] args) throws SQLException, ClassNotFoundException {
    // Load the JDBC driver
    Class.forName("org.mariadb.jdbc.Driver");
    System.out.println("Driver loaded");

    // Try to connect
    Connection connection = DriverManager.getConnection
      ("jdbc:mariadb://localhost/test", "foo", "bar");

    System.out.println("It works!");

    connection.close();
  }
}
}}

If using Oracle MySQL (as opposed to MariaDB), the above class name should be set to .

## Running the program
To compile and run the program (you will need ), execute:

 $ javac DBDemo.java
 $ java -classpath /usr/share/java/mariadb-jdbc/mariadb-java-client.jar:. DBDemo

If all was configured correctly, you should see:

 Driver loaded
 It works!
