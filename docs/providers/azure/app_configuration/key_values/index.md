---
title: key_values
hide_title: false
hide_table_of_contents: false
keywords:
  - key_values
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>key_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.key_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `contentType` | `string` | The content type of the key-value's value.<br />Providing a proper content-type can enable transformations of values when they are retrieved by applications. |
| `eTag` | `string` | An ETag indicating the state of a key-value within a configuration store. |
| `tags` | `object` | A dictionary of tags that can help identify what a key-value may be applicable for. |
| `label` | `string` | A value used to group key-values.<br />The label is used in unison with the key to uniquely identify a key-value. |
| `key` | `string` | The primary identifier of a key-value.<br />The key is used in unison with the label to uniquely identify a key-value. |
| `locked` | `boolean` | A value indicating whether the key-value is locked.<br />A locked key-value may not be modified until it is unlocked. |
| `lastModified` | `string` | The last time a modifying operation was performed on the given key-value. |
| `type` | `string` | The type of the resource. |
| `value` | `string` | The value of the key-value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `KeyValues_ListByConfigurationStore` | `SELECT` | `configStoreName, resourceGroupName, subscriptionId` | Lists the key-values for a given configuration store. |
| `KeyValues_CreateOrUpdate` | `INSERT` | `configStoreName, keyValueName, resourceGroupName, subscriptionId` | Creates a key-value. |
| `KeyValues_Delete` | `DELETE` | `configStoreName, keyValueName, resourceGroupName, subscriptionId` | Deletes a key-value. |
| `KeyValues_Get` | `EXEC` | `configStoreName, keyValueName, resourceGroupName, subscriptionId` | Gets the properties of the specified key-value. |
