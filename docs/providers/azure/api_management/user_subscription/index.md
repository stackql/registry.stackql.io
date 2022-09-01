---
title: user_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - user_subscription
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
<tr><td><b>Name</b></td><td><code>user_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.user_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `startDate` | `string` | Subscription activation date. The setting is for audit purposes only and the subscription is not automatically activated. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `createdDate` | `string` | Subscription creation date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `primaryKey` | `string` | Subscription primary key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `endDate` | `string` | Date when subscription was cancelled or expired. The setting is for audit purposes only and the subscription is not automatically cancelled. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `state` | `string` | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. |
| `scope` | `string` | Scope like /products/&#123;productId&#125; or /apis or /apis/&#123;apiId&#125;. |
| `displayName` | `string` | The name of the subscription, or null if the subscription has no name. |
| `expirationDate` | `string` | Subscription expiration date. The setting is for audit purposes only and the subscription is not automatically expired. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `notificationDate` | `string` | Upcoming subscription expiration notification date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `allowTracing` | `boolean` | Determines whether tracing is enabled |
| `secondaryKey` | `string` | Subscription secondary key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `stateComment` | `string` | Optional subscription comment added by an administrator when the state is changed to the 'rejected'. |
| `ownerId` | `string` | The user resource identifier of the subscription owner. The value is a valid relative URL in the format of /users/&#123;userId&#125; where &#123;userId&#125; is a user identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `UserSubscription_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, userId` | Lists the collection of subscriptions of the specified user. |
| `UserSubscription_Get` | `EXEC` | `resourceGroupName, serviceName, sid, subscriptionId, userId` | Gets the specified Subscription entity associated with a particular user. |
