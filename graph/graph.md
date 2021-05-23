## Graphs Stdio
 * [Getting Started with Graph Studio](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=758&p210_type=3&session=6871376584532)
### User Setup

* DB user 생성시 REST/GRAPH 선택
* 
```sql
GRANT GRAPH_DEVELOPER TO ATOMY02 ;
ALTER USER ATOMY02 GRANT CONNECT THROUGH "GRAPH$PROXY_USER";

select * from dba_role_privs where grantee in ('ATOMY01','ATOMY02');
GRANTEE GRANTED_ROLE    ADMIN_OPTION DELEGATE_OPTION DEFAULT_ROLE COMMON INHERITED 
------- --------------- ------------ --------------- ------------ ------ --------- 
ATOMY01 DWROLE          NO           NO              YES          NO     NO        
ATOMY01 OML_DEVELOPER   NO           NO              NO           NO     NO        
ATOMY01 GRAPH_DEVELOPER NO           NO              YES          NO     NO        
ATOMY02 OML_DEVELOPER   NO           NO              YES          NO     NO        
ATOMY02 CONNECT         NO           NO              YES          NO     NO        
ATOMY02 GRAPH_DEVELOPER NO           NO              YES          NO     NO        
ATOMY02 DWROLE          NO           NO              YES          NO     NO        

```

* Graph Studio
*
```
DROP PROPERTY GRAPH my_first_graph ;

CREATE PROPERTY GRAPH my_first_graph ;

INSERT INTO my_first_graph
    VERTEX austin LABELS (City) PROPERTIES (austin.name = 'Austin', austin.population = 964254),
    VERTEX tokyo LABELS (City) PROPERTIES (tokyo.name = 'Tokyo', tokyo.population = 9273672),
    VERTEX zurich LABELS (City) PROPERTIES (zurich.name = 'Zurich', zurich.population = 402762),
    VERTEX europe LABELS (Continent) PROPERTIES (europe.name = 'Europe'),
    VERTEX US LABELS (Country) PROPERTIES (US.name = 'United States of America'),
    VERTEX texas LABELS (State) PROPERTIES (texas.name = 'Texas', texas.area_size_km2 = 695662),
    VERTEX japan LABELS (Country) PROPERTIES (japan.name = 'Japan', japan.area_size_km2 = 377975),
    EDGE austinCapital BETWEEN austin AND texas LABELS (capital_of),
    EDGE austinCountry BETWEEN austin AND US LABELS (located_in),
    EDGE texasCountry BETWEEN texas AND US LABELS (located_in),
    EDGE zurichContinent BETWEEN zurich AND europe LABELS (located_in),
    EDGE tokyoCapital BETWEEN tokyo AND japan LABELS (capital_of),
    EDGE tokyoCountry BETWEEN tokyo AND japan LABELS (located_in),
    EDGE zurichTokyo BETWEEN zurich AND tokyo LABELS (connecting_flight) PROPERTIES (zurichTokyo.distance_km = 9576),
    EDGE zurichAustin BETWEEN zurich AND austin LABELS (connecting_flight) PROPERTIES (zurichAustin.distance_km = 8674)
``    

