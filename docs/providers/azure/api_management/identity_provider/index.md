---
title: identity_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider
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
<tr><td><b>Name</b></td><td><code>identity_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.identity_provider</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `clientId` | `string` | Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft. |
| `clientSecret` | `string` | Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IdentityProvider_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of Identity Provider configured in the specified service instance. |
| `IdentityProvider_CreateOrUpdate` | `INSERT` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Creates or Updates the IdentityProvider configuration. |
| `IdentityProvider_Delete` | `DELETE` | `If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId` | Deletes the specified identity provider configuration. |
| `IdentityProvider_Get` | `EXEC` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the configuration details of the identity Provider configured in specified service instance. |
| `IdentityProvider_GetEntityTag` | `EXEC` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the identityProvider specified by its identifier. |
| `IdentityProvider_ListSecrets` | `EXEC` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the client secret details of the Identity Provider. |
| `IdentityProvider_Update` | `EXEC` | `If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId` | Updates an existing IdentityProvider configuration. |
