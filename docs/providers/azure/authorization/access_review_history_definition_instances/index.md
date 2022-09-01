---
title: access_review_history_definition_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definition_instances
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
<tr><td><b>Name</b></td><td><code>access_review_history_definition_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_history_definition_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review history definition instance id. |
| `name` | `string` | The access review history definition instance unique id. |
| `runDateTime` | `string` | Date time when the history data report is scheduled to be generated. |
| `displayName` | `string` | The display name for the parent history definition. |
| `status` | `string` | Status of the requested review history instance data. This is either requested, in-progress, done or error. The state transitions are as follows - Requested -&gt; InProgress -&gt; Done -&gt; Expired |
| `fulfilledDateTime` | `string` | Date time when the history data report is scheduled to be generated. |
| `reviewHistoryPeriodEndDateTime` | `string` | Date time used when selecting review data, all reviews included in data end on or before this date. For use only with one-time/non-recurring reports. |
| `type` | `string` | The resource type. |
| `reviewHistoryPeriodStartDateTime` | `string` | Date time used when selecting review data, all reviews included in data start on or after this date. For use only with one-time/non-recurring reports. |
| `expiration` | `string` | Date time when history data report expires and the associated data is deleted. |
| `downloadUri` | `string` | Uri which can be used to retrieve review history data. To generate this Uri, generateDownloadUri() must be called for a specific accessReviewHistoryDefinitionInstance. The link expires after a 24 hour period. Callers can see the expiration date time by looking at the 'se' parameter in the generated uri. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AccessReviewHistoryDefinitionInstances_List` | `SELECT` | `historyDefinitionId, subscriptionId` |
