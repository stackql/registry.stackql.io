---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.certificate</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `subject` | `string` | Subject attribute of the certificate. |
| `thumbprint` | `string` | Thumbprint of the certificate. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `expirationDate` | `string` | Expiration date of the certificate. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `keyVault` | `object` | KeyVault contract details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificate_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of all certificates in the specified service instance. |
| `Certificate_CreateOrUpdate` | `INSERT` | `certificateId, resourceGroupName, serviceName, subscriptionId` | Creates or updates the certificate being used for authentication with the backend. |
| `Certificate_Delete` | `DELETE` | `If-Match, certificateId, resourceGroupName, serviceName, subscriptionId` | Deletes specific certificate. |
| `Certificate_Get` | `EXEC` | `certificateId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the certificate specified by its identifier. |
| `Certificate_GetEntityTag` | `EXEC` | `certificateId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the certificate specified by its identifier. |
| `Certificate_RefreshSecret` | `EXEC` | `certificateId, resourceGroupName, serviceName, subscriptionId` | From KeyVault, Refresh the certificate being used for authentication with the backend. |