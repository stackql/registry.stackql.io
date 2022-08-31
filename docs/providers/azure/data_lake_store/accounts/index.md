---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_store.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `type` | `string` | The resource type. |
| `endpoint` | `string` | The full CName endpoint for this account. |
| `lastModifiedTime` | `string` | The account last modified time. |
| `location` | `string` | The resource location. |
| `tags` | `object` | The resource tags. |
| `creationTime` | `string` | The account creation time. |
| `provisioningState` | `string` | The provisioning status of the Data Lake Store account. |
| `accountId` | `string` | The unique identifier associated with this Data Lake Store account. |
| `state` | `string` | The state of the Data Lake Store account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_List` | `SELECT` | `subscriptionId` | Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any. |
| `Accounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location` | Creates the specified Data Lake Store account. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes the specified Data Lake Store account. |
| `Accounts_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks whether the specified account name is available or taken. |
| `Accounts_EnableKeyVault` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account. |
| `Accounts_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the specified Data Lake Store account. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the specified Data Lake Store account information. |
