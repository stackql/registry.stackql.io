---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute_admin.quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `ddagpuCount` | `integer` | Maximum number of dda gpus allowed. |
| `location` | `string` | Location of the resource. |
| `coresLimit` | `integer` | Maximum number of cores allowed. |
| `maxAllocationPremiumManagedDisksAndSnapshots` | `integer` | Maximum number of managed disks and snapshots of type premium allowed. |
| `maxAllocationStandardManagedDisksAndSnapshots` | `integer` | Maximum number of managed disks and snapshots of type standard allowed. |
| `type` | `string` | Type of Resource. |
| `vmScaleSetCount` | `integer` | Maximum number of scale sets allowed. |
| `partitionedGpuCount` | `integer` | Maximum number of partitioned gpus allowed. |
| `virtualMachineCount` | `integer` | Maximum number of virtual machines allowed. |
| `availabilitySetCount` | `integer` | Maximum number of availability sets allowed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Quotas_List` | `SELECT` | `location, subscriptionId` | Get a list of existing Compute quotas. |
| `Quotas_CreateOrUpdate` | `INSERT` | `location, quotaName, subscriptionId` | Creates or Updates a Compute Quota with the provided quota parameters. |
| `Quotas_Delete` | `DELETE` | `location, quotaName, subscriptionId` | Delete an existing Compute quota. |
| `Quotas_Get` | `EXEC` | `location, quotaName, subscriptionId` | Get an existing Compute Quota. |
