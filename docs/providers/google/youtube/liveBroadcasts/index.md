---
title: liveBroadcasts
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
<tr><td><b>Name</b></td><td><code>liveBroadcasts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.youtube.liveBroadcasts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | The ID that YouTube assigns to uniquely identify the broadcast. |
| `status` | `object` | Live broadcast state. |
| `contentDetails` | `object` | Detailed settings of a broadcast. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#liveBroadcast". |
| `snippet` | `object` | Basic broadcast information. |
| `statistics` | `object` | Statistics about the live broadcast. These represent a snapshot of the values at the time of the request. Statistics are only returned for live broadcasts. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `part` | Retrieve the list of broadcasts associated with the given channel. |
| `insert` | `INSERT` | `part` | Inserts a new stream for the authenticated user. |
| `delete` | `DELETE` | `id` | Delete a given broadcast. |
| `bind` | `EXEC` | `id, part` | Bind a broadcast to a stream. |
| `transition` | `EXEC` | `broadcastStatus, id, part` | Transition a broadcast to a given status. |
| `update` | `EXEC` | `part` | Updates an existing broadcast for the authenticated user. |
