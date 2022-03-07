## Network Data Model Graph
### User Guide
* [User Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/network-data-model-graph-overview.html#GUID-E088F1BF-6F15-495F-9732-C8A62649607B)

### Network Data Model Graph
#### Contraction Hierarchies (21c)
* [REST API for Spatial Network Data Model Contraction Hierarchies](https://docs.oracle.com/en/database/oracle/oracle-database/21/ndmcr/QuickStart.html)
* [``Contraction Hierarchies Web Demo``](https://132.226.169.232:4040/chrest/)
  * ![image](https://user-images.githubusercontent.com/7068088/157004103-8ec74b92-cc12-4385-98a8-56ac782ec044.png)
* [Network Management and Analysis Using Contraction Hierarchies](https://docs.oracle.com/en/database/oracle/oracle-database/21/topol/network-data-model-graph-overview.html#GUID-A95D054C-68FE-4132-8D1A-114A35314D04)

#### Contraction Hierarchies REST API Examples
* Start / Stop

```
sudo systemctl start ndm
sudo systemctl stop ndm
sudo systemctl restart ndm
```
* [Oracle Spatial Network Data Model - README](https://cloud.oracle.com/marketplace/application/115683709/usageInformation?region=ap-chuncheon-1)
* [``Example 5-3 Simple Spatial (SDO) Network Example (PL/SQL``)](https://docs.oracle.com/en/database/oracle/oracle-database/21/topol/network-data-model-graph-overview.html#GUID-BE3DED28-F97F-4AB5-9F2D-60C9CEE66E91)
* Contraction Hierarchies REST API Examples
  *  creating a contraction hierarchies network model under a preconfigured directory:

```
{"createNetworkRequest":
    {
        "chName":"my_example",
        "networkName":"MY_NETWORK_NAME",
        "dbUrl":"jdbc:oracle:thin:@<host>:<port>:<sid>",
        "dbUser":"my_username",
        "dbPassword":"my_password",
        "processGeometry":true,
        "processTurnRestrictions":false,
        "primaryLinkCostColumn":"LENGTH",
        "primaryCostUnit":"meter",
        "primaryCostScaleFactor":10,
        "secondaryLinkCostColumns":["LENGTH/S"],
        "secondaryCostUnits":["second"],
        "secondaryCostScaleFactors":[10]
    }
}
```

* loading a contraction hierarchies network model into memory:

```
{"loadNetworkRequest":
    {
        "chName":"my_example",
        "networkName":"MY_NETWORK_NAME",
        "considerTurnRestrictions":false
    }
}
```
* request for a shortest path analysis

```
{
    "chName":"my_example",
    "shortestPathRequest":{
        "startPoints" : { "pointOnNet" : [ 
            { "linkId" : 238135, "percentage" : 0.28 } 
        ] }, 
        "endPoints" : { "pointOnNet" : [ 
            { "linkId" : 261315, "percentage" : 0.93 }
        ] },         
        "geometry":true
    }
}
```

* response for a shortest path analysis
```
{
  "shortestPathResponse" : {
    "cost" : 2906.6,
    "geometry" : "{\"type\":\"LineString\",\"coordinates\":[[-74.00501,40.70583],[-74.00457,40.70549],[-74.00447,40.70541],[-74.00418,40.70559],[-74.00386,40.70579],[-74.00361,40.70595],[-74.00346,40.70605],[-74.00335,40.70611],[-74.00318,40.70621],[-74.00231,40.7067],[-74.00274,40.70722],[-74.00311,40.70767],[-74.00336,40.708],[-74.00345,40.70808],[-74.00407,40.70745],[-74.00412,40.70757],[-74.00433,40.70783],[-74.00477,40.70841],[-74.00505,40.70876],[-74.00513,40.70885],[-74.00524,40.70893],[-74.00532,40.70899],[-74.00547,40.70909],[-74.00643,40.70956],[-74.00705,40.70987],[-74.00774,40.71022],[-74.00906,40.71089],[-74.01046,40.71153],[-74.01013,40.71209],[-74.00967,40.71274],[-74.00927,40.71326],[-74.00902,40.71359],[-74.00885,40.71381],[-74.0084,40.71437],[-74.00795,40.71494],[-74.00755,40.71544],[-74.00882,40.71602],[-74.0092,40.71619],[-74.00911,40.71692],[-74.00906,40.71726],[-74.009,40.7176],[-74.00894,40.71793],[-74.00888,40.71827],[-74.00882,40.71864],[-74.00875,40.71903],[-74.0087,40.7193],[-74.00858,40.71996],[-74.00847,40.72065],[-74.00842,40.72089],[-74.00837,40.7212],[-74.00834,40.72133],[-74.00823,40.72198],[-74.00812,40.72264],[-74.00801,40.72328],[-74.00795,40.72365],[-74.00793,40.72376],[-74.00786,40.72382],[-74.00777,40.72388],[-74.00773,40.72392],[-74.00771,40.72393],[-74.00745,40.72412],[-74.00736,40.72417],[-74.00728,40.72424],[-74.00723,40.72429],[-74.0071,40.72441],[-74.00703,40.7245]]}",
    "linkIds" : [ 238135, 69834, 69856, 187992, 39327, 39328, 18867, 189084, 189085, 189086, 189087, 142716, 142717, 142718, 142719, 142720, 193362, 193363, 54588, 54589, 54657, 153376, 68912, 61331, 61332, 177603, 177604, 177605, 177606, 177607, 106801, 96723, 96724, 96725, 96726, 65028, 176816, 176817, 65012, 65013, 65014, 65015, 261314, 261315 ],
    "nodeIds" : [ 42427254, 42427256, 42440356, 3350498747, 42452620, 42457292, 42444271, 42440270, 42440271, 673008453, 42440278, 42440280, 42440282, 42440284, 42440287, 42428385, 42440290, 42453943, 42453952, 42430004, 42429562, 42449597, 42431611, 42445356, 42445357, 42436322, 42430571, 42430529, 42429833, 42436326, 42436327, 42436330, 42436333, 42436335, 42436336, 42424610, 1104165608, 42436308, 42424408, 42436340, 42436014, 4142105822, 42424619, 42424630, 42423514 ],
    "startIndex" : 0,
    "startPercentage" : 0.28,
    "endIndex" : 43,
    "endPercentage" : 0.93
  },
  "unit" : "meter"
}
```

#### Key Terms
* Node
* Link
* Network Element
* Path / Subpath
* Lgical Network
* Spatial  Network
* Feature : [Features and Feature Layers](Features and Feature Layers)
* Cost 
* Duration 
* State 
* Type 
* 
#### Main Step
  * Create the network using a procedure
    * [SDO_NET.CREATE_SDO_NETWORK](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/SDO_NET-reference.html#GUID-AA9BB0EB-AF18-4765-A6BF-E6FD2E247AE0) for a spatial network with non-LRS SDO_GEOMETRY objects
    * [SDO_NET.CREATE_LRS_NETWORK](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/SDO_NET-reference.html#GUID-E27DEE9F-7704-4860-8FD2-6E0BE1D1A883) for a spatial network with LRS SDO_GEOMETRY objects
    * [SDO_NET.CREATE_TOPO_NETWORK](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/SDO_NET-reference.html#GUID-DC364605-B313-46D7-BDA4-56EF00F3D2D9) for a spatial network with topology geometry (SDO_TOPO_GEOMETRY) objects
    * [SDO_NET.CREATE_LOGICAL_NETWORK](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/SDO_NET-reference.html#GUID-D828A58B-4DFD-4B28-B502-8080B342AC0E) for a logical network that does not contain spatial information
* Insert data into the node and link tables,( path and path-link tables) : [ Network Data Model Graph Tables]( Network Data Model Graph Tables)
* Validate the network, using the [SDO_NET.VALIDATE_NETWORK](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/SDO_NET-reference.html#GUID-51950D89-3315-4F81-B0AC-6E20C9F35760) function.
* For a spatial (SDO or LRS) network, insert the appropriate information into the [USER_SDO_GEOM_METADATA]() view, and create spatial indexes on the geometry columns.
*
