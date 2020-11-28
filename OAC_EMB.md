###  Embed Analytics Content into Web Pages 
* [Mike Durran: "Embedding with Oracle Analytics Cloud"](https://youtu.be/in75h40Jlko)
* [Oracle Analytics Cloud (OAC) Embedding— Public User Access — Part 1](https://medium.com/@insight2action/oracle-analytics-cloud-oac-embedding-public-user-access-part-1-5fb0f513508a)
* [Oracle Analytics Cloud (OAC) Embedding— Public User Access — Part 2](https://medium.com/@insight2action/oracle-analytics-cloud-oac-embedding-public-user-access-part-2-cb0c9cdb0d8)
* [Oracle Analytics Cloud Embedding — changing the IDCS token timeout](https://medium.com/@insight2action/oracle-analytics-cloud-embedding-changing-the-idcs-token-timeout-1da9323e1b94)
---
### Step By Step

#### Basic Test
##### Step 1 - Web Server 

```html
[opc@dbsec-lab oac]$ cat index.html
<!DOCTYPE html>

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>Spoon-Knife</title>
  <LINK href="styles.css" rel="stylesheet" type="text/css">
</head>

<body>

<img src="forkit.gif" id="octocat" alt="" />

<!-- Feel free to change this text here -->
<p>
  Fork me? Fork you, @octocat!
</p>
<p>
  Sean made a change
</p>

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
