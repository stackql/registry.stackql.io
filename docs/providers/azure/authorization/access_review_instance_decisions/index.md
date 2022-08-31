---
title: access_review_instance_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instance_decisions
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
<tr><td><b>Name</b></td><td><code>access_review_instance_decisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_instance_decisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review decision id. |
| `name` | `string` | The access review decision name. |
| `decision` | `string` | The decision on the approval step. This value is initially set to NotReviewed. Approvers can take action of Approve/Deny |
| `principal` | `object` | Target of the decision. |
| `principalResourceMembership` | `object` | Target of the decision. |
| `justification` | `string` | Justification provided by approvers for their action |
| `appliedDateTime` | `string` | The date and time when the review decision was applied. |
| `type` | `string` | The resource type. |
| `reviewedBy` | `object` | Details of the actor identity |
| `insights` | `array` | This is the collection of insights for this decision item. |
| `appliedBy` | `object` | Details of the actor identity |
| `resource` | `object` | Target of the decision. |
| `recommendation` | `string` | The feature- generated recommendation shown to the reviewer. |
| `reviewedDateTime` | `string` | Date Time when a decision was taken. |
| `applyResult` | `string` | The outcome of applying the decision. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AccessReviewInstanceDecisions_List` | `SELECT` | `id, scheduleDefinitionId, subscriptionId` |