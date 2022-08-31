---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `location` | `string` | Specifies the location of the resource. |
| `groupId` | `string` | The private link resource group id. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `requiredZoneNames` | `array` | The private link resource Private link DNS zone name. |
| `requiredMembers` | `array` | The private link resource required member names. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkResources_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |