---
title: delegated_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_providers
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>delegated_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.delegated_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier. |
| `routingResourceManagerType` | `string` | Resource manager type. |
| `tenantId` | `string` | Directory tenant identifier. |
| `offerId` | `string` | Identifier of the offer under the scope of a delegated provider. |
| `subscriptionId` | `string` | Subscription identifier. |
| `delegatedProviderSubscriptionId` | `string` | Parent DelegatedProvider subscription identifier. |
| `displayName` | `string` | Subscription name. |
| `externalReferenceId` | `string` | External reference identifier. |
| `owner` | `string` | Subscription owner. |
| `state` | `string` | Subscription notification state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DelegatedProviders_List` | `SELECT` | `subscriptionId` | Get the list of delegatedProviders. |
| `DelegatedProviders_Get` | `EXEC` | `delegatedProvider, subscriptionId` | Get the specified delegated provider. |
