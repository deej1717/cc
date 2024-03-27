CS 378 Ethical Hacking Command and Control Write Up
David Segalla, Dhruv Locke, and OTHER GUY!!!!!!!!!!!!!!!!!!!!!!

#Installing the Backdoor

1) Download the two .py files need to bedownloaded to your local machine.
2) Then using the 'scp' command copy over the .py files to the week4 machine and to the attackers machine. The attacker.py file will be for the attacker machine and the disk_controller.py file is to be copied to the week4 machine. For the attacker machine :'scp attacker.py ATTACKERNAME@ATTACKER_IP: PATH' For the week4 machine 'scp disk_controller.py user@WEEK4_IP: PATH'
3) Once the files are on their respective machines you must escalate the week4 machine to root priveleges. This can be done with the command 'sudo strace -o /dev/null /bin/sh -p'. To test this you can run 'whoami' and the response should be 'root'.
4) Once privleges have been escalted you must change the permissions of the .py file. 'chmod 750 disk_controller.py'
5) For each file you must configure it to the appropriate IP address, each file will have a designated spot for the IP address to be input to the source code. For the attacker.py file it will be the attacking machines IP address and for the disk_controller.py file it will be the week4 machines IP address. 
6) Now you must make sure port '6000' is open and listening on each machine. This can be done with the 'firewall-cmd --add-port=6000/tcp' command.
7) Next on the week4 machine you must add the file to the crontab. To do this run the command 'crontab -e' to open up the editor.
8) Then run '0 8 * * * PATH_TO_.py' this will add the file to the crontab which will execute it everyday at 0800. For the sake of grading the file can just be executed with 'python disk_controller.py'
9) Once that is executing you can move over to the attacker machine and execute the attacker.py file. This will establish the connection between the two machines.


#How the Backdoor Works

The backdoor works by setting up a connection between the two virtual machines. The file on the week4 machine listens on the specified port for a specific connection from a specified IP address. We authenticate the attacker with a password embedded into the source code that is immediately sent as the first communication. The user is not prompted for a password, it is automatic and only the attacker's source code on their machine has the password. We chose this because it eliminates someones ability to guess the password. Once authenticated the attacker is able to send commands to the week4 machine's shell and those commands will be executed then the output is relayed back to the attackers terminal. 


#Addressing the Five Requirements 

1) The backdoor creates a shell on the week4 machine which the attacker machine is allowed to manipulate and recieves feedback from.
2) The backdoor persists even after a reboot because we have added it to the crontab which will periodically execute the program.
3) The source code has the ability to be manipulated so that the appropriate IP addresses are allowed to be input.
4) We authenticate the attacker through the password that is innitally sent once the connection is established.
5) We attempt to hide our file from a user by naming it disk_controller. This is a name that we believe the average computer user would not think twice about.


#Detecting the Backdoor

Our backdoor could be detected by a system administrator who is able to check the crontab and notices our file there. A trained individual would likely notice the file is not where it is supposed to be. 

