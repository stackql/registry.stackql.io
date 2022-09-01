---
title: data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores
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
<tr><td><b>Name</b></td><td><code>data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.data_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `extendedProperties` | `object` | A generic json used differently by each data source type. |
| `repositoryId` | `string` | Arm Id for the manager resource to which the data source is associated. This is optional. |
| `state` | `string` | State of the data source. |
| `type` | `string` | Type of the object. |
| `customerSecrets` | `array` | List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys. |
| `dataStoreTypeId` | `string` | The arm id of the data store type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataStores_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | Gets all the data stores/repositories in the given resource. |
| `DataStores_CreateOrUpdate` | `INSERT` | `dataManagerName, dataStoreName, resourceGroupName, subscriptionId` | Creates or updates the data store/repository in the data manager. |
| `DataStores_Delete` | `DELETE` | `dataManagerName, dataStoreName, resourceGroupName, subscriptionId` | This method deletes the given data store/repository. |
| `DataStores_Get` | `EXEC` | `dataManagerName, dataStoreName, resourceGroupName, subscriptionId` | This method gets the data store/repository by name. |
