---
title: allowed_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - allowed_connections
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
<tr><td><b>Name</b></td><td><code>allowed_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.allowed_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `calculatedDateTime` | `string` | The UTC time on which the allowed connections resource was calculated |
| `connectableResources` | `array` | List of connectable resources |
| `location` | `string` | Location where the resource is stored |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AllowedConnections_List` | `SELECT` | `api-version, subscriptionId` | Gets the list of all possible traffic between resources for the subscription |
| `AllowedConnections_ListByHomeRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Gets the list of all possible traffic between resources for the subscription and location. |
| `AllowedConnections_Get` | `EXEC` | `api-version, ascLocation, connectionType, resourceGroupName, subscriptionId` | Gets the list of all possible traffic between resources for the subscription and location, based on connection type. |