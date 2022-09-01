---
title: access_review_history_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definitions
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
<tr><td><b>Name</b></td><td><code>access_review_history_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_history_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review history definition id. |
| `name` | `string` | The access review history definition unique id. |
| `reviewHistoryPeriodEndDateTime` | `string` | Date time used when selecting review data, all reviews included in data end on or before this date. For use only with one-time/non-recurring reports. |
| `createdDateTime` | `string` | Date time when history definition was created |
| `type` | `string` | The resource type. |
| `createdBy` | `object` | Details of the actor identity |
| `settings` | `object` | Recurrence settings of an Access Review History Definition. |
| `instances` | `array` | Set of access review history instances for this history definition. |
| `reviewHistoryPeriodStartDateTime` | `string` | Date time used when selecting review data, all reviews included in data start on or after this date. For use only with one-time/non-recurring reports. |
| `decisions` | `array` | Collection of review decisions which the history data should be filtered on. For example if Approve and Deny are supplied the data will only contain review results in which the decision maker approved or denied a review request. |
| `status` | `string` | This read-only field specifies the of the requested review history data. This is either requested, in-progress, done or error. |
| `displayName` | `string` | The display name for the history definition. |
| `scopes` | `array` | A collection of scopes used when selecting review history data |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessReviewHistoryDefinitions_List` | `SELECT` | `subscriptionId` | Lists the accessReviewHistoryDefinitions available from this provider, definition instances are only available for 30 days after creation. |
| `AccessReviewHistoryDefinitions_GetById` | `EXEC` | `historyDefinitionId, subscriptionId` | Get access review history definition by definition Id |
