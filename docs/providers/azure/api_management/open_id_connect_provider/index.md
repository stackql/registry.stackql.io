---
title: open_id_connect_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - open_id_connect_provider
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
<tr><td><b>Name</b></td><td><code>open_id_connect_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.open_id_connect_provider</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | User-friendly description of OpenID Connect Provider. |
| `displayName` | `string` | User-friendly OpenID Connect Provider name. |
| `metadataEndpoint` | `string` | Metadata endpoint URI. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `clientId` | `string` | Client ID of developer console which is the client application. |
| `clientSecret` | `string` | Client Secret of developer console which is the client application. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OpenIdConnectProvider_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists of all the OpenId Connect Providers. |
| `OpenIdConnectProvider_CreateOrUpdate` | `INSERT` | `opid, resourceGroupName, serviceName, subscriptionId` | Creates or updates the OpenID Connect Provider. |
| `OpenIdConnectProvider_Delete` | `DELETE` | `If-Match, opid, resourceGroupName, serviceName, subscriptionId` | Deletes specific OpenID Connect Provider of the API Management service instance. |
| `OpenIdConnectProvider_Get` | `EXEC` | `opid, resourceGroupName, serviceName, subscriptionId` | Gets specific OpenID Connect Provider without secrets. |
| `OpenIdConnectProvider_GetEntityTag` | `EXEC` | `opid, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the openIdConnectProvider specified by its identifier. |
| `OpenIdConnectProvider_ListSecrets` | `EXEC` | `opid, resourceGroupName, serviceName, subscriptionId` | Gets the client secret details of the OpenID Connect Provider. |
| `OpenIdConnectProvider_Update` | `EXEC` | `If-Match, opid, resourceGroupName, serviceName, subscriptionId` | Updates the specific OpenID Connect Provider. |
