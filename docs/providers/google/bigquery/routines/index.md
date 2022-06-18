---
title: routines
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
<tr><td><b>Name</b></td><td><code>routines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.routines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | A token to request the next page of results. |
| `routines` | `array` | Routines in the requested dataset. Unless read_mask is set in the request, only the following fields are populated: etag, project_id, dataset_id, routine_id, routine_type, creation_time, last_modified_time, and language. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `datasetsId, projectsId, routinesId` | Gets the specified routine resource by routine ID. |
| `list` | `SELECT` | `datasetsId, projectsId` | Lists all routines in the specified dataset. Requires the READER dataset role. |
| `insert` | `INSERT` | `datasetsId, projectsId` | Creates a new routine in the dataset. |
| `delete` | `DELETE` | `datasetsId, projectsId, routinesId` | Deletes the routine specified by routineId from the dataset. |
| `update` | `EXEC` | `datasetsId, projectsId, routinesId` | Updates information in an existing routine. The update method replaces the entire Routine resource. |
