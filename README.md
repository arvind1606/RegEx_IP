# RegEx_IP

Below is the output of # show ip interface brief command on a router

Interface		IP-Address	OK? 	Method Status	Protocol
 
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down

a. Use regular expressions to extract and display Interface and method status for all the interfaces.
i. E.g.  FastEthernet0/0, manual up
