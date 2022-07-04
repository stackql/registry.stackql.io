---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
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
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.policysimulator.results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `replayResults` | `array` | The results of running a Replay. |
| `nextPageToken` | `string` | A token that you can use to retrieve the next page of ReplayResult objects. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_locations_replays_results_list` | `SELECT` | `parent` |
| `organizations_locations_replays_results_list` | `SELECT` | `parent` |
| `projects_locations_replays_results_list` | `SELECT` | `parent` |