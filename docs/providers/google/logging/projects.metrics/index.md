---
title: projects.metrics
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
<tr><td><b>Name</b></td><td><code>projects.metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.projects.metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `metrics` | `array` | A list of logs-based metrics. |
| `nextPageToken` | `string` | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call this method again using the value of nextPageToken as pageToken. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `metricsId, projectsId` | Gets a logs-based metric. |
| `list` | `SELECT` | `projectsId` | Lists logs-based metrics. |
| `create` | `INSERT` | `projectsId` | Creates a logs-based metric. |
| `delete` | `DELETE` | `metricsId, projectsId` | Deletes a logs-based metric. |
| `update` | `EXEC` | `metricsId, projectsId` | Creates or updates a logs-based metric. |
