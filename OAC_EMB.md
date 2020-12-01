###  Embed Analytics Content into Web Pages 
* [Mike Durran: "Embedding with Oracle Analytics Cloud"](https://youtu.be/in75h40Jlko)
* [Oracle Analytics Cloud (OAC) Embedding— Public User Access — Part 1](https://medium.com/@insight2action/oracle-analytics-cloud-oac-embedding-public-user-access-part-1-5fb0f513508a)
* [Oracle Analytics Cloud (OAC) Embedding— Public User Access — Part 2](https://medium.com/@insight2action/oracle-analytics-cloud-oac-embedding-public-user-access-part-2-cb0c9cdb0d8)
* [Oracle Analytics Cloud Embedding — changing the IDCS token timeout](https://medium.com/@insight2action/oracle-analytics-cloud-embedding-changing-the-idcs-token-timeout-1da9323e1b94)
---
### Step By Step
#### 사전 준비
* IDCS Confidential application 생성
* Web Tier Policy -> Allow CORS

* firewall open
```bash
[opc@www ~]$ sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
success
[opc@www ~]$ sudo firewall-cmd --reload
success
[opc@www ~]$ sudo iptables-save | grep 80
-A IN_public_allow -p tcp -m tcp --dport 80 -m conntrack --ctstate NEW,UNTRACKED -j ACCEPT
```
* auth token generation

```bash
#
# id@oracle.com / pass
# Client ID: d905f61c475647d49cebeabd2445e5a9
# Client Secret: 59130cf0-df87-4607-a7c3-cb3d16b2b465
# echo Client ID:59130cf0-df87-4607-a7c3-cb3d16b2b465 | base64
# scope: 
$ echo d905f61c475647d49cebeabd2445e5a9:Client Secret | base64
ZDkwNWY2MWM0NzU2NDdkNDljZWJlYWJkMjQ0NWU1YTk6NTkxMzBjZjAtZGY4Ny00NjA3LWE3YzMtY2IzZDE2YjJiNDY1

$ curl --request POST --url  https://idcs-98312ec13f5048bf99adf9033c2ef380.identity.oraclecloud.com/oauth2/v1/token --header 'Authorization: Basic ZDkwNWY2MWM0NzU2NDdkNDljZWJlYWJkMjQ0NWU1YTk6NTkxMzBjZjAtZGY4Ny00NjA3LWE3YzMtY2IzZDE2YjJiNDY1' --header 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' -d 'grant_type=password&username=my@oracle.com&password=pass&scope=https://ikoym3emnrueruof63p7yyhiq3hoja2q.analytics.ocp.oraclecloud.comurn:opc:resource:consumer::all'
```
* security list ingress 80 open;
* oac safe domain 등록

#### Basic Test
##### Step 1 - Web Server 

* python web server

```bash
sudo python3 -m http.server 80
```
* index.html
```html
[opc@dbsec-lab oac]$ cat index.html
<html>
  <head>
   <meta http-equiv=”Content-Type” content=”text/html; charset=utf-8">
   <title>Standalone DV Embed Demo Using Token</title>
        <script src="https://bkoac-frr7lzpgn4zg-fr.analytics.ocp.oraclecloud.com/public/dv/v1/embedding/standalone/embedding.js" type="application/javascript">
        </script>
  </head>
 <body>

   <B>Standalone embedded project test</B>
   <div style=”width: calc(100% — 40px); height: (100% — 40px); border: 1px solid black; padding: 10px;” >
     <oracle-dv project-path="/@Catalog/shared/BK/BKTEST">
     </oracle-dv>
   </div>

 <script>
  var token = "eyJ4NXQjUzI1NiI6Ilh0b1dIem9lN1R1Wk9IbUgwcEhfVEQ4UnpYOE1GTE9Bak1SaXhTQ1YwQWciLCJ4NXQiOiJubnBxaXRBQjRvdU43d1NYNXUtendqemdkZFkiLCJraWQiOiJTSUdOSU5HX0tFWSIsImFsZyI6IlJTMjU2In0.eyJ1c2VyX3R6IjoiQW1lcmljYVwvQ2hpY2FnbyIsInN1YiI6ImJvbmdraS5qZW9uZ0BvcmFjbGUuY29tIiwidXNlcl9sb2NhbGUiOiJlbiIsInVzZXIudGVuYW50Lm5hbWUiOiJpZGNzLTk4MzEyZWMxM2Y1MDQ4YmY5OWFkZjkwMzNjMmVmMzgwIiwiaXNzIjoiaHR0cHM6XC9cL2lkZW50aXR5Lm9yYWNsZWNsb3VkLmNvbVwvIiwidXNlcl90ZW5hbnRuYW1lIjoiaWRjcy05ODMxMmVjMTNmNTA0OGJmOTlhZGY5MDMzYzJlZjM4MCIsImNsaWVudF9pZCI6ImQ5MDVmNjFjNDc1NjQ3ZDQ5Y2ViZWFiZDI0NDVlNWE5Iiwic3ViX3R5cGUiOiJ1c2VyIiwic2NvcGUiOiJ1cm46b3BjOnJlc291cmNlOmNvbnN1bWVyOjphbGwiLCJjbGllbnRfdGVuYW50bmFtZSI6ImlkY3MtOTgzMTJlYzEzZjUwNDhiZjk5YWRmOTAzM2MyZWYzODAiLCJ1c2VyX2xhbmciOiJlbiIsImV4cCI6MTYwNjc4OTYwMCwiaWF0IjoxNjA2Nzg5NTAwLCJjbGllbnRfZ3VpZCI6IjdlODQ3NzgyZDI5MTQ2NjNiN2Y1ZTEwMDM2NTE3Nzk4IiwiY2xpZW50X25hbWUiOiJDbGllbnQgQXBwbGljYXRpb24iLCJ0ZW5hbnQiOiJpZGNzLTk4MzEyZWMxM2Y1MDQ4YmY5OWFkZjkwMzNjMmVmMzgwIiwianRpIjoiMTFlYjMzN2M2OTk4MWRhMjhlZWM4NTk5NGMwZjQ2YTAiLCJndHAiOiJybyIsInVzZXJfZGlzcGxheW5hbWUiOiJCb25na2kgSmVvbmciLCJzdWJfbWFwcGluZ2F0dHIiOiJ1c2VyTmFtZSIsInByaW1UZW5hbnQiOnRydWUsInRva190eXBlIjoiQVQiLCJjYV9ndWlkIjoiY2FjY3QtMTEzZGUzYTU3Yzk4NDg0OWJlYTNjMDA5MWZjNWUyM2YiLCJhdWQiOlsiaHR0cHM6XC9cL2Jrb2FjLWZycjdsenBnbjR6Zy1mci5hbmFseXRpY3Mub2NwLm9yYWNsZWNsb3VkLmNvbSIsImh0dHBzOlwvXC9pa295bTNlbW5ydWVydW9mNjNwN3l5aGlxM2hvamEycS5hbmFseXRpY3Mub2NwLm9yYWNsZWNsb3VkLmNvbSJdLCJ1c2VyX2lkIjoiYmU4ZmQ1NzU0NGJmNGQ5OGIyNDBmZjdkMWY4OTQ5MGMiLCJ0ZW5hbnRfaXNzIjoiaHR0cHM6XC9cL2lkY3MtOTgzMTJlYzEzZjUwNDhiZjk5YWRmOTAzM2MyZWYzODAuaWRlbnRpdHkub3JhY2xlY2xvdWQuY29tOjQ0MyIsInJlc291cmNlX2FwcF9pZCI6Ijk1YTU0OThjMTE3NTRlNTU4OGUxM2NjZGMzODI5YjYzIn0.aPOvlWl0qjXu6fWbO23pNx56kyJmdukHenikla3Wqma2aq1lksSCqAoghCtnCExxLsuqGrSSAmd-1iXGVQoZC2xR99JZ43M4Phv3SYHHn6z582Aoi-UDpz11zduJJyybqOFuvqyFo5QlIDcnE4qZlCSyC6YTWMhWM1OYMGInoeOyQWZ2Bzu8iQtg3yrlhLvcHYOptq9R5MjVlRljTsCMh33-2kW-EJ-i9pFNCxQzxOqM5UqMFxF9wmEpeGeuZP59i4xPCKPe5ARZ5DP0O0OwnWTfQoj57wIYBekJryjs4_K2ncFk1liFjR5Fz7ZTDPriZmKdcJjUnR0Kidg5DRD30g";
   requirejs(['jquery', 'knockout', 'obitech-application/application'],
//  requirejs(['jquery', 'knockout', 'obitech-application/application', 'ojs/ojcore', 'ojs/ojknockout', 'ojs/ojcomposite', 'jet-composites/oracle-dv/loader'],
  function($, ko, application) {
  application.setSecurityConfig("token", {tokenAuthFunction:
  function(){
  return token;
  }
  });
  ko.applyBindings();
  }
  );
  </script>
 </body>
</html>
[opc@dbsec-lab oac]$

```


```bash
[opc@dbsec-lab oac]$ sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
121.134.70.44 - - [28/Nov/2020 10:38:24] "GET / HTTP/1.1" 200 -

121.134.70.44 - - [28/Nov/2020 10:38:24] code 404, message File not found
121.134.70.44 - - [28/Nov/2020 10:38:24] "GET /forkit.gif HTTP/1.1" 404 -

```

##### Step 2 - OAC Instance & Dashboard
* OAC Instance
* Dashboard
* Register ‘Safe Domain’ in OAC
##### Step 3 - IDCS - Confidence Application
* Required role : Identity Domain Administrator, Security Administrator, or Application Administrator
##### Step 4 - Generating Token Manual  

##### Step 5 - Embeding OAC Dashboard
---
#### Advanced  Test

##### Step 1 - Function to Generate Auth 
##### Step 2 - API Gateway to invoke function
##### Step 3 - Embeding OAC Dashboard
