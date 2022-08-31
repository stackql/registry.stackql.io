---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Service_List` | `SELECT` | `api-version, applicationResourceName, resourceGroupName, subscriptionId` | Gets the information about all services of an application resource. The information include the description and other properties of the Service. |
| `Service_Get` | `EXEC` | `api-version, applicationResourceName, resourceGroupName, serviceResourceName, subscriptionId` | Gets the information about the service resource with the given name. The information include the description and other properties of the service. |