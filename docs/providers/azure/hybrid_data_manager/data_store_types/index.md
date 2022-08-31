---
title: data_store_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_store_types
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
<tr><td><b>Name</b></td><td><code>data_store_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_data_manager.data_store_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the object. |
| `name` | `string` | Name of the object. |
| `supportedDataServicesAsSink` | `array` | Supported data services where it can be used as a sink. |
| `supportedDataServicesAsSource` | `array` | Supported data services where it can be used as a source. |
| `type` | `string` | Type of the object. |
| `repositoryType` | `string` | Arm type for the manager resource to which the data source type is associated. This is optional. |
| `state` | `string` | State of the data store type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataStoreTypes_ListByDataManager` | `SELECT` | `dataManagerName, resourceGroupName, subscriptionId` | Gets all the data store/repository types that the resource supports. |
| `DataStoreTypes_Get` | `EXEC` | `dataManagerName, dataStoreTypeName, resourceGroupName, subscriptionId` | Gets the data store/repository type given its name. |
