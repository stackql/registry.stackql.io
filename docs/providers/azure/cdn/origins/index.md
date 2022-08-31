---
title: origins
hide_title: false
hide_table_of_contents: false
keywords:
  - origins
  - cdn
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
<tr><td><b>Name</b></td><td><code>origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.origins</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `privateEndpointStatus` | `string` | The approval status for the connection to the Private Link |
| `provisioningState` | `string` | Provisioning status of the origin. |
| `resourceState` | `string` | Resource status of the origin. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Origins_ListByEndpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origins within an endpoint. |
| `Origins_Create` | `INSERT` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Creates a new origin within the specified endpoint. |
| `Origins_Delete` | `DELETE` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Deletes an existing origin within an endpoint. |
| `Origins_Get` | `EXEC` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Gets an existing origin within an endpoint. |
| `Origins_Update` | `EXEC` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Updates an existing origin within an endpoint. |