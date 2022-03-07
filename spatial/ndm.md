## Network Data Model Graph
### User Guide
* [User Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/topol/network-data-model-graph-overview.html#GUID-E088F1BF-6F15-495F-9732-C8A62649607B)

### Network Data Model Graph
#### Contraction Hierarchies (21c)
* [REST API for Spatial Network Data Model Contraction Hierarchies](https://docs.oracle.com/en/database/oracle/oracle-database/21/ndmcr/QuickStart.html)
* [``Contraction Hierarchies Web Demo``](https://132.226.169.232:4040/chrest/)
* [Network Management and Analysis Using Contraction Hierarchies](https://docs.oracle.com/en/database/oracle/oracle-database/21/topol/network-data-model-graph-overview.html#GUID-A95D054C-68FE-4132-8D1A-114A35314D04)
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
