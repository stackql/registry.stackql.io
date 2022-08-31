---
title: private_links
hide_title: false
hide_table_of_contents: false
keywords:
  - private_links
  - iot_central
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
<tr><td><b>Name</b></td><td><code>private_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_central.private_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `requiredZoneNames` | `array` | The private link resource private link DNS zone name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `groupId` | `string` | The private link resource group id. |
| `requiredMembers` | `array` | The private link resource required member names. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinks_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get all private link resources of a IoT Central Application. |
| `PrivateLinks_Get` | `EXEC` | `api-version, groupId, resourceGroupName, resourceName, subscriptionId` | Get a private link resource of a IoT Central Application. |