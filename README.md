* Basic Implementation of a Distributed Directory service like Microsoft Active Directory and openLDAP. Basic LDAP calls like Add,Delete,Modify,Rename,Subtreesearch,Search are implemented.


* system requirements:<br />

  * python 2.7<br />
  * MySQLdb<br />
  * mysql database<br />
  * Three systems<br />

* To setup the system:<br />


  * Arrange Three Computers.<br />
  * Assign them system1, system2 and system3. They all are servers.<br />
  * place sys1, sys2 and sys3 folder in respective systems.<br />
  * import dbempty.sql in three systems.<br />
  * Note down their IP and ports.<br />
  * make change of IP and port in timer_replicate.py in the corresponding code.<br />
  * start the server in three systems : python main.py port.<br />
  * start the timer_replicate.py in three systems: python timer_replicate.py <br />
  * start the client in three systems: python client.py 127.0.0.1 <server_port> <br />
  * Enjoy Directory Service


* For commands, refer command.txt<br />

* For implementation details, refer implementation_details.pdf and for report refer Report.pdf
Although the system works correctly most of the times, the code is not well testes. So any pull request is welcome very much.
