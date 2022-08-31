---
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
  - api_management
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
<tr><td><b>Name</b></td><td><code>subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `expirationDate` | `string` | Subscription expiration date. The setting is for audit purposes only and the subscription is not automatically expired. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `endDate` | `string` | Date when subscription was cancelled or expired. The setting is for audit purposes only and the subscription is not automatically cancelled. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `allowTracing` | `boolean` | Determines whether tracing is enabled |
| `startDate` | `string` | Subscription activation date. The setting is for audit purposes only and the subscription is not automatically activated. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `secondaryKey` | `string` | Subscription secondary key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `createdDate` | `string` | Subscription creation date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `primaryKey` | `string` | Subscription primary key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `scope` | `string` | Scope like /products/{productId} or /apis or /apis/{apiId}. |
| `ownerId` | `string` | The user resource identifier of the subscription owner. The value is a valid relative URL in the format of /users/{userId} where {userId} is a user identifier. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `notificationDate` | `string` | Upcoming subscription expiration notification date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `displayName` | `string` | The name of the subscription, or null if the subscription has no name. |
| `stateComment` | `string` | Optional subscription comment added by an administrator when the state is changed to the 'rejected'. |
| `state` | `string` | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subscription_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all subscriptions of the API Management service instance. |
| `Subscription_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, sid, subscriptionId` | Creates or updates the subscription of specified user to the specified product. |
| `Subscription_Delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, sid, subscriptionId` | Deletes the specified subscription. |
| `Subscription_Get` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Gets the specified Subscription entity. |
| `Subscription_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Gets the entity state (Etag) version of the apimanagement subscription specified by its identifier. |
| `Subscription_ListSecrets` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Gets the specified Subscription keys. |
| `Subscription_RegeneratePrimaryKey` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Regenerates primary key of existing subscription of the API Management service instance. |
| `Subscription_RegenerateSecondaryKey` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId` | Regenerates secondary key of existing subscription of the API Management service instance. |
| `Subscription_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, sid, subscriptionId` | Updates the details of a subscription specified by its identifier. |
