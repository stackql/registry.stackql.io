---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
  - hybrid_data_manager
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
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.public_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `dataServiceLevel2Key` | `object` | Encryption Key. |
| `type` | `string` | Type of the object. |
| `dataServiceLevel1Key` | `object` | Encryption Key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PublicKeys_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | This method gets the list view of public keys, however it will only have one element. |
| `PublicKeys_Get` | `EXEC` | `dataManagerName, publicKeyName, resourceGroupName, subscriptionId` | This method gets the public keys. |