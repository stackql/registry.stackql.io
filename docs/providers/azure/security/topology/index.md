---
title: topology
hide_title: false
hide_table_of_contents: false
keywords:
  - topology
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
<tr><td><b>Name</b></td><td><code>topology</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.topology</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `location` | `string` | Location where the resource is stored |
| `topologyResources` | `array` | Azure resources which are part of this topology resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `calculatedDateTime` | `string` | The UTC time on which the topology was calculated |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Topology_List` | `SELECT` | `api-version, subscriptionId` | Gets a list that allows to build a topology view of a subscription. |
| `Topology_ListByHomeRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Gets a list that allows to build a topology view of a subscription and location. |
| `Topology_Get` | `EXEC` | `api-version, ascLocation, resourceGroupName, subscriptionId, topologyResourceName` | Gets a specific topology component. |
