---
title: transfer_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer_logs
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
<tr><td><b>Name</b></td><td><code>transfer_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.transfer_logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `messageText` | `string` | Message text. |
| `messageTime` | `string` | Time when message was logged. |
| `severity` | `string` | Message severity. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_transferConfigs_runs_transferLogs_list` | `SELECT` | `parent` |
| `projects_transferConfigs_runs_transferLogs_list` | `SELECT` | `parent` |