---
title: authorization_server
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server
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
<tr><td><b>Name</b></td><td><code>authorization_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.authorization_server</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `grantTypes` | `array` | Form of an authorization grant, which the client uses to request the access token. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `clientRegistrationEndpoint` | `string` | Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. |
| `displayName` | `string` | User-friendly authorization server name. |
| `authorizationEndpoint` | `string` | OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2. |
| `clientId` | `string` | Client or app id registered with this authorization server. |
| `clientSecret` | `string` | Client or app secret registered with this authorization server. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AuthorizationServer_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization servers defined within a service instance. |
| `AuthorizationServer_CreateOrUpdate` | `INSERT` | `authsid, resourceGroupName, serviceName, subscriptionId` | Creates new authorization server or updates an existing authorization server. |
| `AuthorizationServer_Delete` | `DELETE` | `If-Match, authsid, resourceGroupName, serviceName, subscriptionId` | Deletes specific authorization server instance. |
| `AuthorizationServer_Get` | `EXEC` | `authsid, resourceGroupName, serviceName, subscriptionId` | Gets the details of the authorization server specified by its identifier. |
| `AuthorizationServer_GetEntityTag` | `EXEC` | `authsid, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the authorizationServer specified by its identifier. |
| `AuthorizationServer_ListSecrets` | `EXEC` | `authsid, resourceGroupName, serviceName, subscriptionId` | Gets the client secret details of the authorization server. |
| `AuthorizationServer_Update` | `EXEC` | `If-Match, authsid, resourceGroupName, serviceName, subscriptionId` | Updates the details of the authorization server specified by its identifier. |
