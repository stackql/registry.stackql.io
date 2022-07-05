---
title: canaryevaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - canaryevaluations
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canaryevaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.canaryevaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the canary evalution. |
| `verdict` | `string` | Output only. The resulting verdict of the canary evaluations: NONE, PASS, or FAIL. |
| `startTime` | `string` | Required. Start time for the canary evaluation's analysis. |
| `createTime` | `string` | Output only. Create time of the canary evaluation. |
| `treatment` | `string` | Required. The newer version that is serving requests. |
| `metricLabels` | `object` | Labels that can be used to filter Apigee metrics. |
| `state` | `string` | Output only. The current state of the canary evaluation. |
| `control` | `string` | Required. The stable version that is serving requests. |
| `endTime` | `string` | Required. End time for the evaluation's analysis. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_instances_canaryevaluations_get` | `SELECT` | `name` | Gets a CanaryEvaluation for an organization. |
| `organizations_instances_canaryevaluations_create` | `INSERT` | `parent` | Creates a new canary evaluation for an organization. |
