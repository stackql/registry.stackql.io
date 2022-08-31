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
| `createdBy` | `object` | Details of the actor identity |
| `descriptionForAdmins` | `string` | The description provided by the access review creator and visible to admins. |
| `status` | `string` | This read-only field specifies the status of an accessReview. |
| `descriptionForReviewers` | `string` | The description provided by the access review creator to be shown to reviewers. |
| `reviewersType` | `string` | This field specifies the type of reviewers for a review. Usually for a review, reviewers are explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be chosen dynamically. For example managers review or self review. |
| `scope` | `object` | Descriptor for what needs to be reviewed |
| `instances` | `array` | This is the collection of instances returned when one does an expand on it. |
| `settings` | `object` | Settings of an Access Review. |
| `backupReviewers` | `array` | This is the collection of backup reviewers. |
| `displayName` | `string` | The display name for the schedule definition. |
| `type` | `string` | The resource type. |
| `reviewers` | `array` | This is the collection of reviewers. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AccessReviewScheduleDefinitionsAssignedForMyApproval_List` | `SELECT` |  |
