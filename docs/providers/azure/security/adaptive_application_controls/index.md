---
title: adaptive_application_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_application_controls
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
<tr><td><b>Name</b></td><td><code>adaptive_application_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.adaptive_application_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `sourceSystem` | `string` | The source type of the machine group |
| `recommendationStatus` | `string` | The initial recommendation status of the machine group or machine |
| `vmRecommendations` | `array` |  |
| `location` | `string` | Location where the resource is stored |
| `pathRecommendations` | `array` |  |
| `protectionMode` | `object` | The protection mode of the collection/file types. Exe/Msi/Script are used for Windows, Executable is used for Linux. |
| `configurationStatus` | `string` | The configuration status of the machines group or machine or rule |
| `issues` | `array` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `enforcementMode` | `string` | The application control policy enforcement/protection mode of the machine group |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AdaptiveApplicationControls_List` | `SELECT` | `api-version, subscriptionId` | Gets a list of application control machine groups for the subscription. |
| `AdaptiveApplicationControls_Delete` | `DELETE` | `api-version, ascLocation, groupName, subscriptionId` | Delete an application control machine group |
| `AdaptiveApplicationControls_Get` | `EXEC` | `api-version, ascLocation, groupName, subscriptionId` | Gets an application control VM/server group. |
| `AdaptiveApplicationControls_Put` | `EXEC` | `api-version, ascLocation, groupName, subscriptionId` | Update an application control machine group |
