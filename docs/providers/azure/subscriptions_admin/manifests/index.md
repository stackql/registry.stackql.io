---
title: manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - manifests
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
<tr><td><b>Name</b></td><td><code>manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.manifests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the registration. |
| `extensionCollection` | `object` | The manifest extension collection definition. |
| `resourceTypes` | `object` | List of the resource types. |
| `resourceLocation` | `string` | The location of the resource. |
| `providerAuthorization` | `object` | The resource provider authorization information. |
| `routingResourceManagerType` | `string` | Resource manager type. |
| `alwaysRoutable` | `boolean` | A value indicating whether the manifest is always routable by all subscriptions. |
| `providerType` | `string` | The resource provider type. |
| `resourceTags` | `object` | The resource tags. |
| `providerLocation` | `string` | The location of the provider. |
| `displayName` | `string` | The display name. |
| `namespace` | `string` | The namespace. |
| `provisioningState` | `string` | The provisioning state. |
| `linkedNotificationRules` | `object` | List of the linked notification rules. |
| `resourceHydrationAccounts` | `object` | List of the resource hydration accounts. |
| `enabled` | `boolean` | A value indicating whether this resource provider is enabled. |
| `subscriptionId` | `string` | The subscription ID under which RP is registered. |
| `metadata` | `object` | The metadata. |
| `resourceGroupName` | `string` | The name of the resource group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Manifests_List` | `SELECT` | `subscriptionId` | Get a list of all manifests. |
| `Manifests_Get` | `EXEC` | `manifestName, subscriptionId` | Get the specified manifest. |
