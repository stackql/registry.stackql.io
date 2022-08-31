---
title: security_admin_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - security_admin_configurations
  - network
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
<tr><td><b>Name</b></td><td><code>security_admin_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_admin_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `description` | `string` | A description of the security configuration. |
| `provisioningState` | `string` | The current provisioning state. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type. |
| `applyOnNetworkIntentPolicyBasedServices` | `array` | Enum list of network intent policy based services. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityAdminConfigurations_List` | `SELECT` | `networkManagerName, resourceGroupName, subscriptionId` | Lists all the network manager security admin configurations in a network manager, in a paginated format. |
| `SecurityAdminConfigurations_CreateOrUpdate` | `INSERT` |  | Creates or updates a network manager security admin configuration. |
| `SecurityAdminConfigurations_Delete` | `DELETE` |  | Deletes a network manager security admin configuration. |
| `SecurityAdminConfigurations_Get` | `EXEC` |  | Retrieves a network manager security admin configuration. |