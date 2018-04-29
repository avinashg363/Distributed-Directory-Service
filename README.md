Basic Implementation of a Distributed Directory service like Microsoft Active Directory and openLDAP. Basic LDAP calls like Add,Delete,Modify,Rename,Subtreesearch,Search are implemented.


system requirements:

> python 2.7
> MySQLdb
> mysql database
> three computers

To setup the system:


> Arrange Three Computers.
> Assign them system1, system2 and system3. They all are servers.
> place sys1, sys2 and sys3 folder in respective systems.
> import dbempty.sql in three systems.
> Note down their IP and ports.
> make change of IP and port in timer_replicate.py in the corresponding code.
> start the server in three systems : python main.py port
> start the timer_replicate.py in three systems: python timer_replicate.py
> start the client in three systems: python client.py 127.0.0.1 <server_port>
> Enjoy


For commands, refer command.txt

For implementation details, refer implementation_details.pdf and for report refer Report.pdf
Although the system works correctly most of the times, the code is not well testes. So any pull request is welcome very much.