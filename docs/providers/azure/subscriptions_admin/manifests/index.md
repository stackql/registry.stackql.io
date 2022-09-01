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
| `routingResourceManagerType` | `string` | Resource manager type. |
| `resourceTypes` | `object` | List of the resource types. |
| `enabled` | `boolean` | A value indicating whether this resource provider is enabled. |
| `provisioningState` | `string` | The provisioning state. |
| `providerAuthorization` | `object` | The resource provider authorization information. |
| `resourceTags` | `object` | The resource tags. |
| `subscriptionId` | `string` | The subscription ID under which RP is registered. |
| `resourceLocation` | `string` | The location of the resource. |
| `metadata` | `object` | The metadata. |
| `extensionCollection` | `object` | The manifest extension collection definition. |
| `displayName` | `string` | The display name. |
| `namespace` | `string` | The namespace. |
| `resourceGroupName` | `string` | The name of the resource group. |
| `resourceHydrationAccounts` | `object` | List of the resource hydration accounts. |
| `providerLocation` | `string` | The location of the provider. |
| `providerType` | `string` | The resource provider type. |
| `linkedNotificationRules` | `object` | List of the linked notification rules. |
| `alwaysRoutable` | `boolean` | A value indicating whether the manifest is always routable by all subscriptions. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Manifests_List` | `SELECT` | `subscriptionId` | Get a list of all manifests. |
| `Manifests_Get` | `EXEC` | `manifestName, subscriptionId` | Get the specified manifest. |
