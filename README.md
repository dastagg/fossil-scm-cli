# Fossil-SCM command line scripts

This is my collection of cli scripts for working with Fossil-SCM.

They are a little crude, but they work. 

I symbolically link the Ticket scripts to the "$HOME/bin" directory. The files
and the server scripts in the server directory are used for other things.

## Short Descriptions:

### Files

``ticket-config``: This is copied to the "$HOME/dev/FOSSIL/fossil-files" directory.
``scmenu`` uses it when it creates a new Fossil repository.


``makelocalrepo.sh``: This is the same as the "f" option in scmenu. 
	I use it for testing sometimes.


### Ticket scripts

``fta``: Fossil Ticket Add:  
	This will display a prompt for all the fields of a new ticket.

``ftc``: Fossil Ticket Close:   
	I do a ``ftso`` first, select the id of the ticket that will be closed,
type ``ftc ``, paste the id and hit enter. 

``ftqa``: Fossil Ticket Quick Add:  
	I use this when I am working through a tutorial of some kind (book,
video, website etc.). It will just prompt for the Description and the Chapter
and fill in all the other fields with defaults. 

``ftsa``: Fossil Ticket Show All:  
	Show All Tickets.

``ftso``: Fossil Ticket Show Open:  
	Show only Open Tickets.


### Server scripts

I have a server that runs Fossil as well.
All the files located in the "\server" directory are used on that server.
See the "rpi-rack" repo for an Ansible install of Fossil.

``copyrepo.sh``: There is an "upload" directory on the server. I move the repo from
the FOSSIL directory to that directory, ssh into the server, run the copyrepo.sh (as sudo), then run scmenu on the
local computer to re-connect it to the repo in the working project directory.

``fossil.cgi``: This is the cgi script I use on the server

``rebuildall.sh``: When Fossil-SCM has a new release, I will run this in the
/var/www/fossils directory to update all the repos to the latest version.

