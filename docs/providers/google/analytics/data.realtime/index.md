---
title: data.realtime
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
<tr><td><b>Name</b></td><td><code>data.realtime</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.data.realtime</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID for this data response. |
| `columnHeaders` | `array` | Column headers that list dimension names followed by the metric names. The order of dimensions and metrics is same as specified in the request. |
| `totalResults` | `integer` | The total number of rows for the query, regardless of the number of rows in the response. |
| `query` | `object` | Real time data request query parameters. |
| `profileInfo` | `object` | Information for the view (profile), for which the real time data was requested. |
| `kind` | `string` | Resource type. |
| `rows` | `array` | Real time data rows, where each row contains a list of dimension values followed by the metric values. The order of dimensions and metrics is same as specified in the request. |
| `totalsForAllResults` | `object` | Total values for the requested metrics over all the results, not just the results returned in this response. The order of the metric totals is same as the metric order specified in the request. |
| `selfLink` | `string` | Link to this page. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `ids, metrics` |
