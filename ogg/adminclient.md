### OCI GG CMD LINE - adminclient

* [$OGG_HOME/bin/adminclient 사용](adminclient.md)

* connect 끝에 ! 가 있어야 함: The exclamation point (!) is very important. Without it, the command fails and returns an error.

```bash
 /u01/app/ogg/bin,
 ./adminclient
 connect <OCI-GoldenGate-deployment-url> as <OCI-GoldenGate-user> password <OCI-GoldenGate-password> !
 info all
 stats <extract-name>
 view messages
 purge exttrail <trail-file-name>
 ```
 
 ```
 cd $OGG_HOME/bin
 ./adminclient
OGG (not connected) 3> connect https://ggma.livelabs.oraclevcn.com:16000/ as oggadmin password Welcome1 !
Using default deployment 'Atlanta'

OGG (https://ggma.livelabs.oraclevcn.com:16000/ Atlanta) 4> info all
Program     Status      Group       Type             Lag at Chkpt  Time Since Chkpt

ADMINSRVR   RUNNING   
DISTSRVR    RUNNING   
PMSRVR      RUNNING   
RECVSRVR    RUNNING   

OGG (https://ggma.livelabs.oraclevcn.com:16000/ Atlanta) 5> help

Admin Client Command Summary:

  !                           - Executes the previous command without modifications.
  ADD CHECKPOINTTABLE         - Creates a checkpoint table in a database.
  ADD CREDENTIALS             - Create user credentials for use by the Administration Client.
  ADD CREDENTIALSTORE         - (Deprecated) Creates a credentials store (wallet) that stores encrypted database user credentials.
  ADD DISTPATH                - Creates a distribution path.
  ADD ENCRYPTIONPROFILE       - Create an encryption profile for trail encryption/decryption.
  ADD EXTRACT                 - Creates an Extract group.
  ADD EXTTRAIL                - Adds a local trail to the Oracle GoldenGate configuration.
  ADD HEARTBEATTABLE          - Add a heartbeat table to the database
  ADD MASTERKEY               - Adds a master key to a master-key wallet.
  ADD PROCEDURETRANDATA       - Enables procedure-level supplemental logging.
  ADD PROFILE                 - Create a profile for managed processes.
  ADD RECVPATH                - Creates a target-initiated distribution path in Receiver Server.
  ADD REPLICAT                - Adds a Replicat group.
  ADD RMTTRAIL                - Adds a remote trail to the Oracle GoldenGate configuration.
  ADD SCHEMATRANDATA          - Enables schema-level supplemental logging.
  ADD TRACETABLE              - Creates a trace table.
  ADD TRANDATA                - Enables table-level supplemental logging.
  ALLOWNESTED                 - Enables the use of nested OBEY files.
  ALTER CREDENTIALSTORE       - Changes the contents of a credentials store.
  ALTER DISTPATH              - Changes the attributes of a distribution path.
  ALTER ENCRYPTIONPROFILE     - Alter an encryption profile for trail encryption/decryption.
  ALTER EXTRACT               - Changes attributes of an Extract group.
  ALTER EXTTRAIL              - Changes attributes of a local trail.
  ALTER HEARTBEATTABLE        - Alter a heartbeat table in the database
  ALTER RECVPATH              - Changes the attributes of a target-initiated distribution path in Receiver Server.
  ALTER REPLICAT              - Changes attributes of a Replicat group.
  ALTER RMTTRAIL              - Changes attributes of a remote trail.
  CD                          - Change the Admin Client working directory
  CLEANUP CHECKPOINTTABLE     - Removes checkpoint records that are no longer needed.
  CLEANUP EXTRACT             - Deletes run history for an Extract group.
  CLEANUP REPLICAT            - Deletes run history of a Replicat group.
  CLEAR INSTANTIATION CSN FOR - Clear the instantiation CSN on a target table.
  CONNECT                     - Connect to an Oracle GoldenGate Service Manager
  CREATE WALLET               - (Deprecated) Creates a wallet that stores master encryption keys.
  DBLOGIN USERIDALIAS         - Logs the session into a database so that other commands that affect the database can be issued.
  DELETE CHECKPOINTTABLE      - Removes a checkpoint table from a database.
  DELETE CREDENTIALS          - Remove user credentials from the Administration Client.
  DELETE CREDENTIALSTORE      - Deletes the wallet that serves as a credentials store.
  DELETE DISTPATH             - Deletes a distribution path.
  DELETE ENCRYPTIONPROFILE    - Remove an encryption profile.
  DELETE EXTRACT              - Deletes an Extract group.
  DELETE EXTTRAIL             - Removes a local trail from the Oracle GoldenGate configuration.
  DELETE HEARTBEATENTRY       - Delete heartbeat table entries from the database
  DELETE HEARTBEATTABLE       - Delete a heartbeat table from the database
  DELETE MASTERKEY            - Marks a master key for deletion.
  DELETE PROCEDURETRANDATA    - Disables procedure-level supplemental logging.
  DELETE PROFILE              - Remove a managed process profile.
  DELETE RECVPATH             - Deletes a target-initiated distribution path in Receiver Server.
  DELETE REPLICAT             - Deletes a Replicat group.
  DELETE RMTTRAIL             - Removes a remote trail from the Oracle GoldenGate configuration.
  DELETE SCHEMATRANDATA       - Disables schema-level supplemental logging.
  DELETE TRACETABLE           - Removes a trace table.
  DELETE TRANDATA             - Disables table-level supplemental logging.
  DISABLE SERVICE             - Disable the specified Oracle GoldenGate services.
  DISCONNECT                  - Disconnect from the Oracle GoldenGate Service Manager
  EDIT ENCKEYS                - Opens the ENCKEYS file for editing in the default text editor.
  EDIT GLOBALS                - Opens the GLOBALS parameter file for editing in the default text editor.
  EDIT PARAMS                 - Opens a parameter file for editing in the default text editor.
  ENABLE SERVICE              - Enable the specified Oracle GoldenGate services.
  ENCRYPT PASSWORD            - Encrypt a password that is used in an Oracle GoldenGate parameter file or command.
  EXIT                        - Exit the Oracle GoldenGate Admin Client
  FLUSH SEQUENCE              - Updates an Oracle sequence so that initial redo records are available at the time that Extract starts capturing transaction data.
  HEALTH DEPLOYMENT           - Display the health of the specified Oracle GoldenGate deployments.
  HELP                        - Provides assistance with syntax and usage of commands.
  HISTORY                     - Shows a list of the most recently issued commands since the startup of the session.
  INFO ALL                    - Displays status and lag for all Oracle GoldenGate processes on a system.
  INFO CHECKPOINTTABLE        - Returns information about one or more checkpoint tables.
  INFO CREDENTIALS            - Display information about Administration Client user credentials.
  INFO CREDENTIALSTORE        - Returns information about a credentials store.
  INFO DISTPATH               - Returns information about distribution path(s).
  INFO ENCRYPTIONPROFILE      - Returns information about encryption profiles.
  INFO ER                     - Returns information about the specified wildcarded groups.
  INFO EXTRACT                - Returns information about an Extract group.
  INFO EXTTRAIL               - Returns information about a local trail.
  INFO HEARTBEATTABLE         - Describe a heartbeat table in the database
  INFO MASTERKEY              - Returns information about master keys.
  INFO PARAM                  - Displays parameter definition information.
  INFO PROCEDURETRANDATA      - Returns information about the state of procedure-level supplemental logging.
  INFO PROFILE                - Returns information about managed process profiles.
  INFO RECVPATH               - Returns information about target-initiated distribution path(s) in Receiver Server.
  INFO REPLICAT               - Returns information about a Replicat group.
  INFO RMTTRAIL               - Returns information about a remote trail.
  INFO SCHEMATRANDATA         - Returns information about the state of schema-level supplemental logging.
  INFO TRACETABLE             - Returns information about a trace table.
  INFO TRANDATA               - Returns information about the state of table-level supplemental logging.
  KILL ER                     - Forcibly terminates the specified wildcarded groups.
  KILL EXTRACT                - Forcibly terminates the run of an Extract group.
  KILL REPLICAT               - Forcibly terminates a Replicat group.
  LAG ER                      - Returns lag information about the specified wildcarded groups.
  LAG EXTRACT                 - Returns information about Extract lag.
  LAG REPLICAT                - Returns information about Replicat lag.
  LIST TABLES                 - Lists the tables in the database with names that match the input specification.
  MININGDBLOGIN USERIDALIAS   - Specifies the credentials of the user that an Oracle GoldenGate process uses to log into an Oracle mining database.
  NOALLOWNESTED               - Disables the use of nested OBEY files.
  OBEY                        - Processes a file that contains a list of Oracle GoldenGate commands.
  OPEN WALLET                 - (Deprecated) Opens a master-key wallet.
  PURGE EXTTRAIL              - Removes files related to a local trail from the file system.
  PURGE WALLET                - Permanently removes from a wallet the master keys that are marked as deleted.
  REGISTER EXTRACT            - Registers an Extract group with the database.
  REGISTER REPLICAT           - Registers a Replicat group with the database.
  RENEW MASTERKEY             - Adds a new version of a master key.
  RESTART DEPLOYMENT          - Restart the specified Oracle GoldenGate deployments.
  RESTART ER                  - Stops, then starts the specified wildcarded groups.
  RESTART EXTRACT             - Stops, then starts an Extract group.
  RESTART REPLICAT            - Stops, then starts a Replicat group.
  RESTART SERVICE             - Restart the specified Oracle GoldenGate services.
  SEND ER                     - Sends instructions to, or returns information about, the specified wildcarded groups.
  SEND EXTRACT                - Sends instructions to, or returns information about, a running Extract group.
  SEND REPLICAT               - Sends instructions to, or returns information about, a running Replicat group.
  SET COLOR                   - Enable or disable colored text in the Administration Client.
  SET DEBUG                   - Enable or disable debugging mode for the Administration Client.
  SET EDITOR                  - Sets the default text editor program for editing parameter files.
  SET INSTANTIATION CSN       - Set the instantiation CSN on a target table.
  SET PAGER                   - Sets the default text viewer program for viewing parameter and report files.
  SET VERBOSE                 - Enable or disable verbose command result output.
  SHELL                       - Executes shell commands on the local system.
  SHOW                        - Displays the attributes of the Oracle GoldenGate environment.
  START DEPLOYMENT            - Start the specified Oracle GoldenGate deployments.
  START DISTPATH              - Starts a distribution path.
  START ER                    - Starts the specified wildcarded groups.
  START EXTRACT               - Starts an Extract group.
  START RECVPATH              - Starts a target-initiated distribution path in Receiver Server.
  START REPLICAT              - Starts a Replicat group.
  START SERVICE               - Start the specified Oracle GoldenGate services.
  STATS DISTPATH              - Returns statistics for a distribution path.
  STATS ER                    - Returns processing statistics for the specified wildcarded groups.
  STATS EXTRACT               - Returns processing statistics for an Extract group.
  STATS RECVPATH              - Returns statistics for a target-initiated distribution path in Receiver Server.
  STATS REPLICAT              - Returns processing statistics for a Replicat group.
  STATUS DEPLOYMENT           - Display status of the specified Oracle GoldenGate deployments.
  STATUS ER                   - Returns the state of the specified wildcarded groups.
  STATUS EXTRACT              - Returns the state of an Extract group.
  STATUS REPLICAT             - Returns the state of a Replicat group.
  STATUS SERVICE              - Display status of the specified Oracle GoldenGate services.
  STOP DEPLOYMENT             - Stop the specified Oracle GoldenGate deployments.
  STOP DISTPATH               - Stops a distribution path.
  STOP ER                     - Stops the specified wildcarded groups.
  STOP EXTRACT                - Stops an Extract group.
  STOP RECVPATH               - Stops a target-initiated distribution path in Receiver Server.
  STOP REPLICAT               - Stops a Replicat group.
  STOP SERVICE                - Stop the specified Oracle GoldenGate services.
  SYNCHRONIZE REPLICAT        - Returns all threads of a coordinated Replicat to a uniform start point after an unclean shutdown of the Replicat process.
  UNDELETE MASTERKEY VERSION  - Changes the state of a master key from being marked as deleted to marked as available.
  UNREGISTER EXTRACT          - Unregisters an Extract group from the database.
  UNREGISTER REPLICAT         - Unregisters a Replicat group from the database.
  UPGRADE CHECKPOINTTABLE     - Adds a supplemental checkpoint table when upgrading Oracle GoldenGate from version 11.2.1.0.0 or earlier.
  UPGRADE HEARTBEATTABLE      - Alters heartbeat tables to track Extract restart position.
  VERSIONS                    - Displays information about the operating system and database.
  VIEW DISCARD                - Displays the discard file that is generated by Extract or Replicat.
  VIEW ENCKEYS                - Displays the contents of the ENCKEYS file in read-only mode on-screen.
  VIEW GLOBALS                - Displays the contents of the GLOBALS parameter file in read-only mode on-screen.
  VIEW MESSAGES               - Displays the Oracle GoldenGate message log (ggserr.log file).
  VIEW PARAMS                 - Displays the contents of a parameter file in read-only mode on-screen.
  VIEW REPORT                 - Displays the process report that is generated by Extract or Replicat.

OGG (https://ggma.livelabs.oraclevcn.com:16000/ Atlanta) 6> 

 ....
