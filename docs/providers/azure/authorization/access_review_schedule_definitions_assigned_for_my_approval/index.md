---
title: access_review_schedule_definitions_assigned_for_my_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions_assigned_for_my_approval
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
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions_assigned_for_my_approval</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_schedule_definitions_assigned_for_my_approval</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review schedule definition id. |
| `name` | `string` | The access review schedule definition unique id. |
| `status` | `string` | This read-only field specifies the status of an accessReview. |
| `scope` | `object` | Descriptor for what needs to be reviewed |
| `descriptionForAdmins` | `string` | The description provided by the access review creator and visible to admins. |
| `displayName` | `string` | The display name for the schedule definition. |
| `instances` | `array` | This is the collection of instances returned when one does an expand on it. |
| `backupReviewers` | `array` | This is the collection of backup reviewers. |
| `createdBy` | `object` | Details of the actor identity |
| `settings` | `object` | Settings of an Access Review. |
| `reviewersType` | `string` | This field specifies the type of reviewers for a review. Usually for a review, reviewers are explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be chosen dynamically. For example managers review or self review. |
| `reviewers` | `array` | This is the collection of reviewers. |
| `type` | `string` | The resource type. |
| `descriptionForReviewers` | `string` | The description provided by the access review creator to be shown to reviewers. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AccessReviewScheduleDefinitionsAssignedForMyApproval_List` | `SELECT` |  |
