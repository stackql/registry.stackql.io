---
title: access_review_instances_assigned_for_my_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instances_assigned_for_my_approval
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
<tr><td><b>Name</b></td><td><code>access_review_instances_assigned_for_my_approval</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_instances_assigned_for_my_approval</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review instance id. |
| `name` | `string` | The access review instance name. |
| `reviewers` | `array` | This is the collection of reviewers. |
| `type` | `string` | The resource type. |
| `status` | `string` | This read-only field specifies the status of an access review instance. |
| `startDateTime` | `string` | The DateTime when the review instance is scheduled to be start. |
| `reviewersType` | `string` | This field specifies the type of reviewers for a review. Usually for a review, reviewers are explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be chosen dynamically. For example managers review or self review. |
| `endDateTime` | `string` | The DateTime when the review instance is scheduled to end. |
| `backupReviewers` | `array` | This is the collection of backup reviewers. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessReviewInstancesAssignedForMyApproval_List` | `SELECT` | `scheduleDefinitionId` | Get access review instances assigned for my approval. |
| `AccessReviewInstancesAssignedForMyApproval_GetById` | `EXEC` | `id, scheduleDefinitionId` | Get single access review instance assigned for my approval. |
