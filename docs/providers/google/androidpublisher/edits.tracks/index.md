---
title: edits.tracks
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
<tr><td><b>Name</b></td><td><code>edits.tracks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.edits.tracks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | The kind of this response ("androidpublisher#tracksListResponse"). |
| `tracks` | `array` | All tracks. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `editId, packageName, track` | Gets a track. |
| `list` | `SELECT` | `editId, packageName` | Lists all tracks. |
| `patch` | `EXEC` | `editId, packageName, track` | Patches a track. |
| `update` | `EXEC` | `editId, packageName, track` | Updates a track. |
