---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - notification_hubs
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.notification_hubs.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `updatedAt` | `string` | The time the namespace was updated. |
| `region` | `string` | Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe |
| `critical` | `boolean` | Whether or not the namespace is set as Critical. |
| `location` | `string` | Resource location |
| `provisioningState` | `string` | Provisioning state of the Namespace. |
| `serviceBusEndpoint` | `string` | Endpoint you can use to perform NotificationHub operations. |
| `createdAt` | `string` | The time the namespace was created. |
| `enabled` | `boolean` | Whether or not the namespace is currently enabled. |
| `type` | `string` | Resource type |
| `metricId` | `string` | Identifier for Azure Insights metrics |
| `namespaceType` | `string` | The namespace type. |
| `scaleUnit` | `string` | ScaleUnit where the namespace gets created |
| `subscriptionId` | `string` | The Id of the Azure subscription associated with the namespace. |
| `sku` | `object` | The Sku description for a namespace |
| `status` | `string` | Status of the namespace. It can be any of these values:1 = Created/Active2 = Creating3 = Suspended4 = Deleting |
| `dataCenter` | `string` | Data center for the namespace |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Namespaces_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the available namespaces within a resourceGroup. |
| `Namespaces_ListAll` | `SELECT` | `subscriptionId` | Lists all the available namespaces within the subscription irrespective of the resourceGroups. |
| `Namespaces_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId, data__location` | Creates/Updates a service namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| `Namespaces_Delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId` | Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace. |
| `Namespaces_CheckAvailability` | `EXEC` | `subscriptionId, data__name` | Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name. |
| `Namespaces_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__properties` | Creates an authorization rule for a namespace |
| `Namespaces_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Deletes a namespace authorization rule |
| `Namespaces_Get` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Returns the description for the specified namespace. |
| `Namespaces_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets an authorization rule for a namespace by name. |
| `Namespaces_ListAuthorizationRules` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets the authorization rules for a namespace. |
| `Namespaces_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets the Primary and Secondary ConnectionStrings to the namespace  |
| `Namespaces_Patch` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Patches the existing namespace |
| `Namespaces_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule |