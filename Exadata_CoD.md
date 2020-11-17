
## Exadata Core 갯수 변경 (Capacity On Demand) : 최소 16 코어
### eight rack 의 경우 증가단위 : 8,10,12,14,16,18

* 1. core 갯수 확인

```sql
DBMCLI> LIST DBSERVER attributes coreCount
```
* 2. core 수 변경

```sql
DBMCLI> ALTER DBSERVER pendingCoreCount = new_number_of_active_physical_cores
```
* 3. core 갯수 확인

```sql
DBMCLI> LIST DBSERVER attributes pendingCoreCount
```
* 4. 리부팅

* 5. active Core 확인

```sql
DBMCLI> LIST DBSERVER attributes coreCount
```
### 출처: https://pat98.tistory.com/848 [pat98's always & forever]
