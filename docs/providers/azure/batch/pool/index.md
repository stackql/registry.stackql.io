---
title: pool
hide_title: false
hide_table_of_contents: false
keywords:
  - pool
  - batch
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.pool</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `resizeOperationStatus` | `object` | Describes either the current operation (if the pool AllocationState is Resizing) or the previously completed operation (if the AllocationState is Steady). |
| `identity` | `object` | The identity of the Batch pool, if configured. If the pool identity is updated during update an existing pool, only the new vms which are created after the pool shrinks to 0 will have the updated identities |
| `scaleSettings` | `object` | Defines the desired size of the pool. This can either be 'fixedScale' where the requested targetDedicatedNodes is specified, or 'autoScale' which defines a formula which is periodically reevaluated. If this property is not specified, the pool will have a fixed scale with 0 targetDedicatedNodes. |
| `applicationPackages` | `array` | Changes to application package references affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged. There is a maximum of 10 application package references on any given pool. |
| `applicationLicenses` | `array` | The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail. |
| `taskSchedulingPolicy` | `object` |  |
| `userAccounts` | `array` |  |
| `interNodeCommunication` | `string` | This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to 'Disabled'. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
| `creationTime` | `string` |  |
| `taskSlotsPerNode` | `integer` | The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the pool or 256. |
| `lastModified` | `string` | This is the last time at which the pool level data, such as the targetDedicatedNodes or autoScaleSettings, changed. It does not factor in node-level changes such as a compute node changing state. |
| `deploymentConfiguration` | `object` |  |
| `currentLowPriorityNodes` | `integer` |  |
| `certificates` | `array` | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. |
| `allocationStateTransitionTime` | `string` |  |
| `metadata` | `array` | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. |
| `allocationState` | `string` |  |
| `mountConfiguration` | `array` | This supports Azure Files, NFS, CIFS/SMB, and Blobfuse. |
| `displayName` | `string` | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. |
| `provisioningState` | `string` |  |
| `type` | `string` | The type of the resource. |
| `autoScaleRun` | `object` |  |
| `startTask` | `object` | In some cases the start task may be re-run even though the node was not rebooted. Due to this, start tasks should be idempotent and exit gracefully if the setup they're performing has already been done. Special care should be taken to avoid start tasks which create breakaway process or install/launch services from the start task working directory, as this will block Batch from being able to re-run the start task. |
| `networkConfiguration` | `object` | The network configuration for a pool. |
| `vmSize` | `string` | For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (https://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). |
| `currentDedicatedNodes` | `integer` |  |
| `provisioningStateTransitionTime` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pool_ListByBatchAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all of the pools in the specified account. |
| `Pool_Create` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId` | Creates a new pool inside the specified account. |
| `Pool_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId` | Deletes the specified pool. |
| `Pool_DisableAutoScale` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Disables automatic scaling for a pool. |
| `Pool_Get` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Gets information about the specified pool. |
| `Pool_StopResize` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created. |
| `Pool_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Updates the properties of an existing pool. |
