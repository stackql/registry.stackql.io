---
title: diagnostic_settings_category
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings_category
  - monitor
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
<tr><td><b>Name</b></td><td><code>diagnostic_settings_category</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.diagnostic_settings_category</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `type` | `string` | Azure resource type |
| `categoryGroups` | `array` | the collection of what category groups are supported. |
| `categoryType` | `string` | The type of the diagnostic settings category. |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiagnosticSettingsCategory_List` | `SELECT` | `resourceUri` | Lists the diagnostic settings categories for the specified resource. |
| `DiagnosticSettingsCategory_Get` | `EXEC` | `name, resourceUri` | Gets the diagnostic settings category for the specified resource. |
