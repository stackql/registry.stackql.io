---
title: management.segments
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>management.segments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.management.segments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Segment ID. |
| `name` | `string` | Segment name. |
| `created` | `string` | Time the segment was created. |
| `kind` | `string` | Resource type for Analytics segment. |
| `segmentId` | `string` | Segment ID. Can be used with the 'segment' parameter in Core Reporting API. |
| `selfLink` | `string` | Link for this segment. |
| `updated` | `string` | Time the segment was last modified. |
| `definition` | `string` | Segment definition. |
| `type` | `string` | Type for a segment. Possible values are "BUILT_IN" or "CUSTOM". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
