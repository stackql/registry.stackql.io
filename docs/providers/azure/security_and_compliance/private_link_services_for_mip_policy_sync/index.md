---
title: private_link_services_for_mip_policy_sync
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_mip_policy_sync
  - security_and_compliance
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
<tr><td><b>Name</b></td><td><code>private_link_services_for_mip_policy_sync</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_and_compliance.private_link_services_for_mip_policy_sync</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The properties of a service instance. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The resource tags. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `location` | `string` | The resource location. |
| `type` | `string` | The resource type. |
| `kind` | `string` | The kind of the service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `privateLinkServicesForMIPPolicySync_List` | `SELECT` | `subscriptionId` | Get all the privateLinkServicesForMIPPolicySync instances in a subscription. |
| `privateLinkServicesForMIPPolicySync_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `privateLinkServicesForMIPPolicySync_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a privateLinkServicesForMIPPolicySync instance. |
| `privateLinkServicesForMIPPolicySync_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a service instance. |
| `privateLinkServicesForMIPPolicySync_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a privateLinkServicesForMIPPolicySync resource. |
| `privateLinkServicesForMIPPolicySync_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a privateLinkServicesForMIPPolicySync instance. |
