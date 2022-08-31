---
title: scope_access_review_instance_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instance_decisions
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
<tr><td><b>Name</b></td><td><code>scope_access_review_instance_decisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.scope_access_review_instance_decisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review decision id. |
| `name` | `string` | The access review decision name. |
| `appliedDateTime` | `string` | The date and time when the review decision was applied. |
| `reviewedBy` | `object` | Details of the actor identity |
| `reviewedDateTime` | `string` | Date Time when a decision was taken. |
| `recommendation` | `string` | The feature- generated recommendation shown to the reviewer. |
| `resource` | `object` | Target of the decision. |
| `applyResult` | `string` | The outcome of applying the decision. |
| `insights` | `array` | This is the collection of insights for this decision item. |
| `appliedBy` | `object` | Details of the actor identity |
| `justification` | `string` | Justification provided by approvers for their action |
| `decision` | `string` | The decision on the approval step. This value is initially set to NotReviewed. Approvers can take action of Approve/Deny |
| `type` | `string` | The resource type. |
| `principal` | `object` | Target of the decision. |
| `principalResourceMembership` | `object` | Target of the decision. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ScopeAccessReviewInstanceDecisions_List` | `SELECT` | `id, scheduleDefinitionId, scope` |
