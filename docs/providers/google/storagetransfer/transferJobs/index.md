---
title: transferJobs
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
<tr><td><b>Name</b></td><td><code>transferJobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storagetransfer.transferJobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The list next page token. |
| `transferJobs` | `array` | A list of transfer jobs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectId, transferJobsId` | Gets a transfer job. |
| `list` | `SELECT` | `filter` | Lists transfer jobs. |
| `create` | `INSERT` |  | Creates a transfer job that runs periodically. |
| `patch` | `EXEC` | `transferJobsId` | Updates a transfer job. Updating a job's transfer spec does not affect transfer operations that are running already. **Note:** The job's status field can be modified using this RPC (for example, to set a job's status to DELETED, DISABLED, or ENABLED). |
| `run` | `EXEC` | `transferJobsId` | Attempts to start a new TransferOperation for the current TransferJob. A TransferJob has a maximum of one active TransferOperation. If this method is called while a TransferOperation is active, an error wil be returned. |
