---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
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
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed identity generic object. |
| `parameters` | `object` | Blueprint assignment parameter values. |
| `tags` | `object` | Resource tags. |
| `resourceGroups` | `object` | Names and locations of resource group placeholders. |
| `location` | `string` | The geo-location where the resource lives |
| `blueprintId` | `string` | ID of the published version of a blueprint definition. |
| `locks` | `object` | Defines how resources deployed by a blueprint assignment are locked. |
| `status` | `object` | The status of a blueprint assignment. This field is readonly. |
| `scope` | `string` | The target subscription scope of the blueprint assignment (format: '/subscriptions/{subscriptionId}'). For management group level assignments, the property is required. |
| `provisioningState` | `string` | State of the blueprint assignment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Assignments_List` | `SELECT` | `resourceScope` | List blueprint assignments within a subscription or a management group. |
| `Assignments_CreateOrUpdate` | `INSERT` | `assignmentName, resourceScope, data__identity` | Create or update a blueprint assignment. |
| `Assignments_Delete` | `DELETE` | `assignmentName, resourceScope` | Delete a blueprint assignment. |
| `Assignments_Get` | `EXEC` | `assignmentName, resourceScope` | Get a blueprint assignment. |
| `Assignments_WhoIsBlueprint` | `EXEC` | `assignmentName, resourceScope` | Get Blueprints service SPN objectId |
