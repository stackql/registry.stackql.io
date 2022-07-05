---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the job, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/ tasks/{task_id}/jobs/{job_id}. |
| `state` | `string` | Output only. Execution state for the job. |
| `startTime` | `string` | Output only. The time when the job was started. |
| `endTime` | `string` | Output only. The time when the job ended. |
| `service` | `string` | Output only. The underlying service running a job. |
| `retryCount` | `integer` | Output only. . The number of times the job has been retried (excluding the initial attempt). |
| `serviceJob` | `string` | Output only. The full resource name for the job run under a particular service. |
| `message` | `string` | Output only. Additional information about the current state. |
| `uid` | `string` | Output only. System generated globally unique ID for the job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_tasks_jobs_get` | `SELECT` | `name` | Get job resource. |
| `projects_locations_lakes_tasks_jobs_list` | `SELECT` | `parent` | Lists Jobs under the given task. |
| `projects_locations_lakes_tasks_jobs_cancel` | `EXEC` | `name` | Cancel jobs running for the task resource. |
