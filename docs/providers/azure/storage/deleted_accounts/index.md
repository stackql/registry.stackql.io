---
title: deleted_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_accounts
  - storage
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
<tr><td><b>Name</b></td><td><code>deleted_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.deleted_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deletionTime` | `string` | Deletion time of the deleted account. |
| `location` | `string` | Location of the deleted account. |
| `restoreReference` | `string` | Can be used to attempt recovering this deleted account via PutStorageAccount API. |
| `storageAccountResourceId` | `string` | Full resource id of the original storage account. |
| `creationTime` | `string` | Creation time of the deleted account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedAccounts_List` | `SELECT` | `subscriptionId` | Lists deleted accounts under the subscription. |
| `DeletedAccounts_Get` | `EXEC` | `deletedAccountName, location, subscriptionId` | Get properties of specified deleted account resource. |
