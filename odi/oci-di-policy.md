## Policy

### Root  Compartment Policy

```
allow group <group-name> to inspect compartments in tenancy
```

### Compartment Policy

* Service policy:

```
allow service dataintegration to use virtual-network-family in compartment <your_compartment>
```

* For Non-admin users:

```
allow group <group-name> to manage dis-workspaces in compartment <compartment-name>
allow group <group-name> to manage dis-work-requests in compartment <compartment-name>
allow group <group-name> to use virtual-network-family in compartment <compartment-name>
allow group <group-name> to manage tag-namespaces in compartment <compartment-name>
```

* To use Object Storage service - 방법 1: 

```
allow group <group_name> to use object-family in compartment <compartment-name>
allow any-user to use buckets in compartment <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace_ocid>'}
allow any-user to manage objects in compartment <compartment-name> where ALL {request.principal.type='disworkspace',request.principal.id='<workspace_ocid>'}
To use Autonomous Data Warehouse (ADW) or Autonomous Transaction Processing (ATP) as Target:
allow any-user {PAR_MANAGE} in compartment <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace_ocid>'}
```

* To use Object Storage service - 방법 2: 
```
allow any-user to read buckets in compartment orcl where ALL {request.principal.type = 'disworkspace', request.principal.id = 'ocid1.disworkspace.oc1.ap-seoul-1.amaaaaaaaiz7opyaznh47cc65m4px5wqdsdl6hx6jcdxrfv36sfnjap4pmoq', request.operation = 'GetBucket'}
allow any-user to manage objects in compartment orcl where ALL {request.principal.type = 'disworkspace', request.principal.id = 'ocid1.disworkspace.oc1.ap-seoul-1.amaaaaaaaiz7opyaznh47cc65m4px5wqdsdl6hx6jcdxrfv36sfnjap4pmoq'}
allow any-user to manage buckets in compartment orcl where ALL {request.principal.type='disworkspace', request.principal.id='ocid1.disworkspace.oc1.ap-seoul-1.amaaaaaaaiz7opyaznh47cc65m4px5wqdsdl6hx6jcdxrfv36sfnjap4pmoq', request.permission = 'PAR_MANAGE'}
```
