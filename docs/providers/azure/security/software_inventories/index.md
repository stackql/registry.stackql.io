---
title: software_inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - software_inventories
  - security
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
<tr><td><b>Name</b></td><td><code>software_inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.software_inventories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `endOfSupportDate` | `string` | The end of support date in case the product is upcoming end of support. |
| `osPlatform` | `string` | Platform of the operating system running on the device. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `vendor` | `string` | Name of the software vendor. |
| `endOfSupportStatus` | `string` | End of support status. |
| `softwareName` | `string` | Name of the software product. |
| `firstSeenAt` | `string` | First time that the software was seen in the device. |
| `numberOfKnownVulnerabilities` | `integer` | Number of weaknesses. |
| `version` | `string` | Version number of the software product. |
| `deviceId` | `string` | Unique identifier for the virtual machine in the service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SoftwareInventories_ListByExtendedResource` | `SELECT` | `api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId` | Gets the software inventory of the virtual machine. |
| `SoftwareInventories_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets the software inventory of all virtual machines in the subscriptions. |
| `SoftwareInventories_Get` | `EXEC` | `api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, softwareName, subscriptionId` | Gets a single software data of the virtual machine. |
