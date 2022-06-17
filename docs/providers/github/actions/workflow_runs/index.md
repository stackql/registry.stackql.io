---
title: workflow_runs
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.workflow_runs</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | The ID of the workflow run. |
| `name` | `string` | The name of the workflow run. |
| `run_attempt` | `integer` | Attempt number of the run, 1 for first attempt and higher if the workflow was re-run. |
| `html_url` | `string` |  |
| `check_suite_node_id` | `string` | The node ID of the associated check suite. |
| `workflow_url` | `string` | The URL to the workflow. |
| `head_commit` | `object` | Simple Commit |
| `check_suite_url` | `string` | The URL to the associated check suite. |
| `cancel_url` | `string` | The URL to cancel the workflow run. |
| `head_branch` | `string` |  |
| `url` | `string` | The URL to the workflow run. |
| `workflow_id` | `integer` | The ID of the parent workflow. |
| `event` | `string` |  |
| `node_id` | `string` |  |
| `pull_requests` | `array` |  |
| `rerun_url` | `string` | The URL to rerun the workflow run. |
| `logs_url` | `string` | The URL to download the logs for the workflow run. |
| `status` | `string` |  |
| `updated_at` | `string` |  |
| `head_repository` | `object` | Minimal Repository |
| `jobs_url` | `string` | The URL to the jobs for the workflow run. |
| `head_sha` | `string` | The SHA of the head commit that points to the version of the worflow being run. |
| `previous_attempt_url` | `string` | The URL to the previous attempted run of this workflow, if one exists. |
| `check_suite_id` | `integer` | The ID of the associated check suite. |
| `head_repository_id` | `integer` |  |
| `artifacts_url` | `string` | The URL to the artifacts for the workflow run. |
| `repository` | `object` | Minimal Repository |
| `run_number` | `integer` | The auto incrementing run number for the workflow run. |
| `conclusion` | `string` |  |
| `run_started_at` | `string` | The start time of the latest run. Resets on re-run. |
| `created_at` | `string` |  |
## Methods
