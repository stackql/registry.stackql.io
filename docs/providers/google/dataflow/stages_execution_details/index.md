---
title: stages_execution_details
hide_title: false
hide_table_of_contents: false
keywords:
  - stages_execution_details
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
<tr><td><b>Name</b></td><td><code>stages_execution_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.stages_execution_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If present, this response does not contain all requested tasks. To obtain the next page of results, repeat the request with page_token set to this value. |
| `workers` | `array` | Workers that have done work on the stage. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_jobs_stages_getExecutionDetails` | `SELECT` | `jobId, location, projectId, stageId` |