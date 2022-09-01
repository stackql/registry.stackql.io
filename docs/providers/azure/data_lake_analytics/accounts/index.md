---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_lake_analytics
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
<tr><td><b>Id</b></td><td><code>azure.data_lake_analytics.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `accountId` | `string` | The unique identifier associated with this Data Lake Analytics account. |
| `lastModifiedTime` | `string` | The account last modified time. |
| `provisioningState` | `string` | The provisioning status of the Data Lake Analytics account. |
| `creationTime` | `string` | The account creation time. |
| `state` | `string` | The state of the Data Lake Analytics account. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `endpoint` | `string` | The full CName endpoint for this account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_List` | `SELECT` | `subscriptionId` | Gets the first page of Data Lake Analytics accounts, if any, within the current subscription. This includes a link to the next page, if any. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the first page of Data Lake Analytics accounts, if any, within a specific resource group. This includes a link to the next page, if any. |
| `Accounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location` | Creates the specified Data Lake Analytics account. This supplies the user with computation services for Data Lake Analytics workloads. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Begins the delete process for the Data Lake Analytics account object specified by the account name. |
| `Accounts_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks whether the specified account name is available or taken. |
| `Accounts_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets details of the specified Data Lake Analytics account. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the Data Lake Analytics account object specified by the accountName with the contents of the account object. |
