---
title: projects.instances.backupOperations
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
<tr><td><b>Name</b></td><td><code>projects.instances.backupOperations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.projects.instances.backupOperations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `operations` | `array` | The list of matching backup long-running operations. Each operation's name will be prefixed by the backup's name and the operation's metadata will be of type CreateBackupMetadata. Operations returned include those that are pending or have completed/failed/canceled within the last 7 days. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation. |
| `nextPageToken` | `string` | `next_page_token` can be sent in a subsequent ListBackupOperations call to fetch more of the matching metadata. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `instancesId, projectsId` |
