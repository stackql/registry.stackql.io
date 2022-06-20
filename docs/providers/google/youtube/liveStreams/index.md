---
title: liveStreams
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
<tr><td><b>Name</b></td><td><code>liveStreams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.youtube.liveStreams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube assigns to uniquely identify the stream. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#liveStream". |
| `snippet` | `object` |  |
| `status` | `object` | Brief description of the live stream status. |
| `cdn` | `object` | Brief description of the live stream cdn settings. |
| `contentDetails` | `object` | Detailed settings of a stream. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `part` | Retrieve the list of streams associated with the given channel. -- |
| `insert` | `INSERT` | `part` | Inserts a new stream for the authenticated user. |
| `delete` | `DELETE` | `id` | Deletes an existing stream for the authenticated user. |
| `update` | `EXEC` | `part` | Updates an existing stream for the authenticated user. |
