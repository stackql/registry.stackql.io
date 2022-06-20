---
title: projects.transferConfigs
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
<tr><td><b>Name</b></td><td><code>projects.transferConfigs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.projects.transferConfigs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `transferConfigs` | `array` | Output only. The stored pipeline transfer configurations. |
| `nextPageToken` | `string` | Output only. The next-pagination token. For multiple-page list results, this token can be used as the `ListTransferConfigsRequest.page_token` to request the next page of list results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, transferConfigsId` | Returns information about the particular transfer run. |
| `list` | `SELECT` | `projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `create` | `INSERT` | `projectsId` | Creates a new data transfer configuration. |
| `delete` | `DELETE` | `projectsId, transferConfigsId` | Deletes the specified transfer run. |
| `patch` | `EXEC` | `projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `scheduleRuns` | `EXEC` | `projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `startManualRuns` | `EXEC` | `projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
