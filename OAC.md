## OAC

* [excel upload limits : 250 MB and the data column limit for a single file is 250 columns.](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/add-spreadsheets-data-sets-acubi.html#GUID-7A93A9DD-17EE-4BE5-86CB-615095919314)

### Embed Analytics Content into Web Pages
* [Document](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/get-started-embedding-content-web-pages.html#GUID-0E129619-FE02-47F3-BB31-A31CC1D0AE9E)
* [Blog](https://medium.com/@insight2action/oracle-analytics-cloud-developer-experience-fe510b5507e9)
* syntax
```html
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Embeded Oracle Analytics Project Example</title>
        <script src="https://<instance>.analytics.ocp.oraclecloud.com/public/dv/v1/embedding/<embedding mode>/embedding.js" type="application/javascript">
        </script>

    </head>
    <body>
        <h1>Embeded Oracle Analytics Project</h1>
        <div style="border:1px solid black;position: absolute; width: calc(100% - 40px); height: calc(100% - 120px)" >
            <!--
            The following tag is the tag that will embed the specified project.
            Veryfy the project-path is the same as the server you are hosting this project on.
            -->
            <oracle-dv
               project-path="<project path>"
               active-page="canvas"
               active-tab-id="1">
            </oracle-dv>
        </div>
        <!--
        Apply Knockout bindings after DV project is fully loaded.  This should be executed in a body onload handler or in a <script> tag after the <oracle-dv> tag.
        -->
        <script>

        requirejs(['knockout', 'ojs/ojcore', 'ojs/ojknockout', 'ojs/ojcomposite', 'jet-composites/oracle-dv/loader'], function(ko) {
           function MyProject() {
              var idFilter = document.getElementsByName("P7_CUSTOMER")[0].value;
              var self = this;
              self.projectPath =  ko.observable("/users/youremail@yourdomain.com/Labour");
              self.filters = ko.observableArray([{
                 "sColFormula": "XSA('youremail@yourdomain.com'.'DEM_PROJECT_HOUR').\"Columns\".\"CUSTOMER\"",
                 "sColName": "Customer Label",
                 "sOperator": "in", /* One of in, notIn, between, less, lessOrEqual, greater, greaterOrequal */
                 "isNumericCol": false,
                 "bIsDoubleColumn": false,
                 "aCodeValues": [],
                 "aDisplayValues": [idFilter]
              }]);
           }
           ko.applyBindings(MyProject);
        });
        </script>
        <script> 
           function refreshProject()
           {
              $('oracle-dv').each(function() {
                 this.refreshData();
                 });
        }
        </script>      
    </body>
</html>
```
### Oracle Data Gateway
* [Oracle Data Gateway 5.4.0 Download](https://www.oracle.com/middleware/technologies/oac-downloads.html)
* [Oracle Data Gateway Document](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acabi/typical-workflow-connecting-premise-data-sources.html)
### OAC Data Sync
* [Download](https://www.oracle.com/middleware/technologies/oac-downloads.html)
* [Document](https://download.oracle.com/otn/java/cloud-service/OACDataSync_2_6_Documentation.pdf?AuthParam=1586435835_2b5176e367f254703d0651663f805410)
* [OBE-Loading Data Using Oracle Analytics Cloud Data Sync](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/oac_bi/loading_data_datasync/datasync_loading.html)
* install procudere
```
unzip OACDataSync_2_6_1.zip
cd OACDataSync_2_6_1

edit config.bat
set JAVA_HOME="C:\Program Files\Java\jdk1.8.0_231"

datasync.bat
```
* 사용자 롤 추가 : OAC console ->  users and roles -> Manage Application Roles : BI Advanced Content Author/  BI Dataload Author / DV Content Author 
