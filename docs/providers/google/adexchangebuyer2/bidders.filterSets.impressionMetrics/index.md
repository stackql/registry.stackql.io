---
title: bidders.filterSets.impressionMetrics
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
<tr><td><b>Name</b></td><td><code>bidders.filterSets.impressionMetrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adexchangebuyer2.bidders.filterSets.impressionMetrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `impressionMetricsRows` | `array` | List of rows, each containing a set of impression metrics. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListImpressionMetricsRequest.pageToken field in the subsequent call to the impressionMetrics.list method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `biddersId, filterSetsId` |