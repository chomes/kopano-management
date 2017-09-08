# kopano-management
Working on a tool to run backups of kopano via brick level backup
This will take a while so I'll slowly be working on this, the purpose of this script will serve several purposes:
* Create a config file that will allow for automated backup
* Email when the backup is done
* Rotate the backup and delete old versions
* Create both a brick level backup and mysql backup along with backing up attachments folder
* Down the line I also plan to expand on this and use this for general management for things like bulk user-add, moving etc that will work with accounts on ldap and allow you to send e-mails out to new users that have never used an account before things like a template can be sent out to the user explaining how to use kopano etc.  Again this is all a work in progress and will take a while it'll be one of my projects.
