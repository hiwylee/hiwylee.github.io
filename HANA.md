## OAC(Oracle Analytics) Hana Interface 

* [hana jdbc driver](https://developers.sap.com/tutorials/hxe-connect-hxe-using-jdbc.html#ce721b2d-a0a6-4f23-972d-4d7301d5fd7a)
* [https://tools.hana.ondemand.com/#hanatools](https://tools.hana.ondemand.com/#hanatools]
* [Installing SAP HANA HDB Client](https://developers.sap.com/tutorials/hxe-ua-install-hdb-client-windows.html)
* [Connect to SAP HANA, express edition using JDBC](https://developers.sap.com/tutorials/hxe-connect-hxe-using-jdbc.html)
* [Installing SAP HANA, express edition with Docker](https://developers.sap.com/tutorials/hxe-ua-install-using-docker.html)
```bash
ls 
hanaclient-2.4.182-linux-x64.tar.gz
hanaclient-2.4.182-windows-x64.zip
HXEDownloadManager_linux.bin
HXEDownloadManager_linux.exe

cd C:\Users\hiwyl\Downloads\hanaclient-2.4.182-windows-x64
hdbinst.exe
cd C:\Program Files\sap\hdbclient
copy ngdbc.jar C:\Program Files\Oracle Analytics Desktop\war\obi-datasrc-server\WEB-INF\lib
```
