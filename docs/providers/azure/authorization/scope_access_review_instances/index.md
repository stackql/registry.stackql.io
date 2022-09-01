---
title: scope_access_review_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instances
  - authorization
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
<tr><td><b>Name</b></td><td><code>scope_access_review_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.scope_access_review_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review instance id. |
| `name` | `string` | The access review instance name. |
| `reviewersType` | `string` | This field specifies the type of reviewers for a review. Usually for a review, reviewers are explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be chosen dynamically. For example managers review or self review. |
| `startDateTime` | `string` | The DateTime when the review instance is scheduled to be start. |
| `status` | `string` | This read-only field specifies the status of an access review instance. |
| `backupReviewers` | `array` | This is the collection of backup reviewers. |
| `type` | `string` | The resource type. |
| `reviewers` | `array` | This is the collection of reviewers. |
| `endDateTime` | `string` | The DateTime when the review instance is scheduled to end. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScopeAccessReviewInstances_List` | `SELECT` | `scheduleDefinitionId, scope` | Get access review instances |
| `ScopeAccessReviewInstances_Create` | `INSERT` | `id, scheduleDefinitionId, scope` | Update access review instance. |
| `ScopeAccessReviewInstances_GetById` | `EXEC` | `id, scheduleDefinitionId, scope` | Get access review instances |
