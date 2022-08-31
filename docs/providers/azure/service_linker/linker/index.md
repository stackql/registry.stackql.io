---
title: linker
hide_title: false
hide_table_of_contents: false
keywords:
  - linker
  - service_linker
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
<tr><td><b>Name</b></td><td><code>linker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_linker.linker</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | The provisioning state.  |
| `scope` | `string` | connection scope in source service. |
| `secretStore` | `object` | An option to store secret value in secure place |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `targetService` | `object` | The target service properties |
| `vNetSolution` | `object` | The VNet solution for linker |
| `authInfo` | `object` | The authentication info |
| `clientType` | `string` | The application client type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Linker_List` | `SELECT` | `resourceUri` | Returns list of Linkers which connects to the resource. |
| `Linker_CreateOrUpdate` | `INSERT` | `linkerName, resourceUri` | Create or update linker resource. |
| `Linker_Delete` | `DELETE` | `linkerName, resourceUri` | Delete a link. |
| `Linker_Get` | `EXEC` | `linkerName, resourceUri` | Returns Linker resource for a given name. |
| `Linker_ListConfigurations` | `EXEC` | `linkerName, resourceUri` | list source configurations for a linker. |
| `Linker_Update` | `EXEC` | `linkerName, resourceUri` | Operation to update an existing link. |
| `Linker_Validate` | `EXEC` | `linkerName, resourceUri` | Validate a link. |
