---
title: projects.transferConfigs.runs
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
<tr><td><b>Name</b></td><td><code>projects.transferConfigs.runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.projects.transferConfigs.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `transferRuns` | `array` | Output only. The stored pipeline transfer runs. |
| `nextPageToken` | `string` | Output only. The next-pagination token. For multiple-page list results, this token can be used as the `ListTransferRunsRequest.page_token` to request the next page of list results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, runsId, transferConfigsId` | Returns information about the particular transfer run. |
| `list` | `SELECT` | `projectsId, transferConfigsId` | Returns information about running and completed jobs. |
| `delete` | `DELETE` | `projectsId, runsId, transferConfigsId` | Deletes the specified transfer run. |
