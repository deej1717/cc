CS 378 Ethical Hacking Command and Control Write Up
David Segalla, Dhruv Loke, and Andrew Teoh

#Installing the Backdoor

1) Download the two .py files, attacker.py and disk_controller.py, to your local machine.
2) Then using the `scp` command copy over the .py files to the week4 machine and to the attacker's machine. The attacker.py file will be for the attacker machine and the disk_controller.py file is to be copied to the week4 machine. For the attacker machine :`scp attacker.py ATTACKERNAME@ATTACKER_IP: PATH` For the week4 machine `scp disk_controller.py user@WEEK4_IP: PATH`
3) Once the files are on their respective machines you must escalate the week4 machine to root priveleges. This can be done with the command `sudo strace -o /dev/null /bin/sh -p`. To test this you can run `whoami` and the response should be `root`.
4) Once privleges have been escalted you must change the permissions of the .py file. `chmod 750 disk_controller.py`
5) For the attacker.py file you must configure the IP address to be the IP address of the target machine. 
6) Now you must make sure port `6000` is open and listening on the target machine. This can be done with the `firewall-cmd --add-port=6000/tcp` command.
7) Next on the week4 machine you must add the file to the crontab. To do this run the command `crontab -e` to open up the editor.
8) Then run `0 1 * * * PATH_TO_.py` this will add the file to the crontab which will execute it everyday at 0100. For the sake of grading
9) To persist across reboot you must reopen the crontab editor and add another entry with the command `@reboot PATH_TO_SCRIPT`
10) the file can just be executed with `python disk_controller.py`
11) Once that is executing you can move over to the attacker machine and execute the attacker.py file. This will establish the connection between the two machines.


#How the Backdoor Works

The backdoor works by setting up a TCP connection between the two virtual machines. We go through the firewall and open a specified TCP port on the target machine. We have a file that listens on the specified port for a connection. Once there is a connection, we authenticate the attacker with a password embedded into the source code that is immediately sent as the first communication. Once authenticated the attacker is able to send commands to the week4 machine's shell and those commands will be executed through a shell subproccess. We then take the the output of the command and send it back to the attacking machine. 


#Addressing the Five Requirements 

1) The backdoor opens up a TCP port on the target machine for the attacker machine to connect through. That port essentially emulates a shell where it sends requests for commands to the attacker machine and it then executes those commands through a subprocess. The target machine also sends back the output of the commands to represent a fully functioning remote shell.
2) The backdoor persists even after a reboot because we have added it to the crontab which will periodically execute the program. We also have the reboot tag which ensures that the script runs on startup even if the machine was rebooted during the middle of the day.
3) The attacker.py code has a field where the IP address of the targeting machine can be added.
4) We authenticate the attacker through the password that is initally sent once the connection is established. We do this by storing the password locally on both the attacker.py and disk_controller.py and once the connection is established, the first message from the attacker.py has to be the password. We do not ask for the password and instead assume that it will be the first message sent after a connection is established eliminating the potential of someone else attempting to use our backdoor.
5) We attempt to hide our file from a user by naming it disk_controller. This is a name that we believe the average computer user would not think twice about.


#Detecting the Backdoor

Our backdoor could be detected by a system administrator who is able to check the crontab and notices our file there. A trained individual would likely notice the file is not where it is supposed to be. 


#Other comments

We were able to get the conection and shell to successfully work on when we tested the two files on our local machines but when trying from either local machine to virtual machine or between two virtual machines we were not able to establish a connection. We debugged by trying to make sure the ports were open and listening and that the firewalls were down on those ports. 
