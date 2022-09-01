---
title: blueprint
hide_title: false
hide_table_of_contents: false
keywords:
  - blueprint
  - blueprint
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
<tr><td><b>Name</b></td><td><code>blueprint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.blueprint</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `type` | `string` | Type of this resource. |
| `versions` | `object` | Published versions of this blueprint definition. |
| `layout` | `object` | Layout view of the blueprint definition for UI reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Blueprints_List` | `SELECT` | `resourceScope` | List blueprint definitions. |
| `Blueprints_CreateOrUpdate` | `INSERT` | `blueprintName, resourceScope` | Create or update a blueprint definition. |
| `Blueprints_Delete` | `DELETE` | `blueprintName, resourceScope` | Delete a blueprint definition. |
| `Blueprints_Get` | `EXEC` | `blueprintName, resourceScope` | Get a blueprint definition. |
