---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - machine_learning_experimentation
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
<tr><td><b>Id</b></td><td><code>azure.machine_learning_experimentation.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `description` | `string` | The description of this workspace. |
| `type` | `string` | The type of the resource. |
| `keyVaultId` | `string` | The fully qualified arm id of the user key vault. |
| `tags` | `object` | The tags of the resource. |
| `discoveryUri` | `string` | The uri for this machine learning team account. |
| `provisioningState` | `string` | The current deployment state of team account resource. The provisioningState is to indicate states for resource provisioning. |
| `seats` | `string` | The no of users/seats who can access this team account. This property defines the charge on the team account. |
| `friendlyName` | `string` | The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created |
| `storageAccount` | `object` | The properties of a storage account for a machine learning team account. |
| `vsoAccountId` | `string` | The fully qualified arm id of the vso account to be used for this team account. |
| `creationDate` | `string` | The creation date of the machine learning team account in ISO8601 format. |
| `accountId` | `string` | The immutable id associated with this team account. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_List` | `SELECT` | `subscriptionId` | Lists all the available machine learning team accounts under the specified subscription. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available machine learning team accounts under the specified resource group. |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates a team account with the specified parameters. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes a machine learning team account. |
| `Accounts_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the properties of the specified machine learning team account. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates a machine learning team account with the specified parameters. |
