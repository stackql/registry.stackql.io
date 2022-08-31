---
title: access_review_schedule_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions
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
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_schedule_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review schedule definition id. |
| `name` | `string` | The access review schedule definition unique id. |
| `createdBy` | `object` | Details of the actor identity |
| `descriptionForAdmins` | `string` | The description provided by the access review creator and visible to admins. |
| `instances` | `array` | This is the collection of instances returned when one does an expand on it. |
| `status` | `string` | This read-only field specifies the status of an accessReview. |
| `displayName` | `string` | The display name for the schedule definition. |
| `scope` | `object` | Descriptor for what needs to be reviewed |
| `reviewersType` | `string` | This field specifies the type of reviewers for a review. Usually for a review, reviewers are explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be chosen dynamically. For example managers review or self review. |
| `type` | `string` | The resource type. |
| `settings` | `object` | Settings of an Access Review. |
| `backupReviewers` | `array` | This is the collection of backup reviewers. |
| `reviewers` | `array` | This is the collection of reviewers. |
| `descriptionForReviewers` | `string` | The description provided by the access review creator to be shown to reviewers. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessReviewScheduleDefinitions_List` | `SELECT` | `subscriptionId` | Get access review schedule definitions |
| `AccessReviewScheduleDefinitions_DeleteById` | `DELETE` | `scheduleDefinitionId, subscriptionId` | Delete access review schedule definition |
| `AccessReviewScheduleDefinitions_CreateOrUpdateById` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Create or Update access review schedule definition. |
| `AccessReviewScheduleDefinitions_GetById` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Get single access review definition |
| `AccessReviewScheduleDefinitions_Stop` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Stop access review definition |
