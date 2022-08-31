---
title: portal_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_settings
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
<tr><td><b>Name</b></td><td><code>portal_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.portal_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `subscriptions` | `object` | Subscriptions delegation settings properties. |
| `url` | `string` | A delegation Url. |
| `enabled` | `boolean` | Redirect Anonymous users to the Sign-In page. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `userRegistration` | `object` | User registration delegation settings properties. |
| `termsOfService` | `object` | Terms of service contract properties. |
| `validationKey` | `string` | A base64-encoded validation key to validate, that a request is coming from Azure API Management. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PortalSettings_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
