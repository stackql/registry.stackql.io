---
title: data.mcf
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
<tr><td><b>Name</b></td><td><code>data.mcf</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analytics.data.mcf</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID for this data response. |
| `rows` | `array` | Analytics data rows, where each row contains a list of dimension values followed by the metric values. The order of dimensions and metrics is same as specified in the request. |
| `profileInfo` | `object` | Information for the view (profile), for which the Analytics data was requested. |
| `itemsPerPage` | `integer` | The maximum number of rows the response can contain, regardless of the actual number of rows returned. Its value ranges from 1 to 10,000 with a value of 1000 by default, or otherwise specified by the max-results query parameter. |
| `nextLink` | `string` | Link to next page for this Analytics data query. |
| `totalResults` | `integer` | The total number of rows for the query, regardless of the number of rows in the response. |
| `query` | `object` | Analytics data request query parameters. |
| `totalsForAllResults` | `object` | Total values for the requested metrics over all the results, not just the results returned in this response. The order of the metric totals is same as the metric order specified in the request. |
| `previousLink` | `string` | Link to previous page for this Analytics data query. |
| `kind` | `string` | Resource type. |
| `selfLink` | `string` | Link to this page. |
| `columnHeaders` | `array` | Column headers that list dimension names followed by the metric names. The order of dimensions and metrics is same as specified in the request. |
| `containsSampledData` | `boolean` | Determines if the Analytics data contains sampled data. |
| `sampleSize` | `string` | The number of samples used to calculate the result. |
| `sampleSpace` | `string` | Total size of the sample space from which the samples were selected. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `end-date, ids, metrics, start-date` |
