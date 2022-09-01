---
title: product_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - product_subscriptions
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
<tr><td><b>Name</b></td><td><code>product_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `displayName` | `string` | The name of the subscription, or null if the subscription has no name. |
| `endDate` | `string` | Date when subscription was cancelled or expired. The setting is for audit purposes only and the subscription is not automatically cancelled. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `state` | `string` | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. |
| `notificationDate` | `string` | Upcoming subscription expiration notification date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `secondaryKey` | `string` | Subscription secondary key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `scope` | `string` | Scope like /products/&#123;productId&#125; or /apis or /apis/&#123;apiId&#125;. |
| `stateComment` | `string` | Optional subscription comment added by an administrator when the state is changed to the 'rejected'. |
| `expirationDate` | `string` | Subscription expiration date. The setting is for audit purposes only and the subscription is not automatically expired. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `createdDate` | `string` | Subscription creation date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `startDate` | `string` | Subscription activation date. The setting is for audit purposes only and the subscription is not automatically activated. The subscription lifecycle can be managed by using the `state` property. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `primaryKey` | `string` | Subscription primary key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `ownerId` | `string` | The user resource identifier of the subscription owner. The value is a valid relative URL in the format of /users/&#123;userId&#125; where &#123;userId&#125; is a user identifier. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `allowTracing` | `boolean` | Determines whether tracing is enabled |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ProductSubscriptions_List` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` |
