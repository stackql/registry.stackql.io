---
title: trusted_id_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - trusted_id_providers
  - data_lake_store
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
<tr><td><b>Name</b></td><td><code>trusted_id_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_store.trusted_id_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `idProvider` | `string` | The URL of this trusted identity provider. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TrustedIdProviders_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account. |
| `TrustedIdProviders_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, trustedIdProviderName` | Creates or updates the specified trusted identity provider. During update, the trusted identity provider with the specified name will be replaced with this new provider |
| `TrustedIdProviders_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, trustedIdProviderName` | Deletes the specified trusted identity provider from the specified Data Lake Store account |
| `TrustedIdProviders_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId, trustedIdProviderName` | Gets the specified Data Lake Store trusted identity provider. |
| `TrustedIdProviders_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId, trustedIdProviderName` | Updates the specified trusted identity provider. |
