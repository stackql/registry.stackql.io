---
title: ddos_protection_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - ddos_protection_plans
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
<tr><td><b>Name</b></td><td><code>ddos_protection_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.ddos_protection_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `provisioningState` | `string` | The current provisioning state. |
| `location` | `string` | Resource location. |
| `tags` | `object` | Resource tags. |
| `virtualNetworks` | `array` | The list of virtual networks associated with the DDoS protection plan resource. This list is read-only. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `resourceGuid` | `string` | The resource GUID property of the DDoS protection plan resource. It uniquely identifies the resource, even if the user changes its name or migrate the resource across subscriptions or resource groups. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DdosProtectionPlans_List` | `SELECT` | `subscriptionId` | Gets all DDoS protection plans in a subscription. |
| `DdosProtectionPlans_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the DDoS protection plans in a resource group. |
| `DdosProtectionPlans_CreateOrUpdate` | `INSERT` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Creates or updates a DDoS protection plan. |
| `DdosProtectionPlans_Delete` | `DELETE` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Deletes the specified DDoS protection plan. |
| `DdosProtectionPlans_Get` | `EXEC` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Gets information about the specified DDoS protection plan. |
| `DdosProtectionPlans_UpdateTags` | `EXEC` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Update a DDoS protection plan tags. |
