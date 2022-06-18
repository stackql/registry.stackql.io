---
title: snapshots
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.games.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | The ID of the snapshot. |
| `description` | `string` | The description of this snapshot. |
| `uniqueName` | `string` | The unique name provided when the snapshot was created. |
| `durationMillis` | `string` | The duration associated with this snapshot, in millis. |
| `lastModifiedMillis` | `string` | The timestamp (in millis since Unix epoch) of the last modification to this snapshot. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#snapshot`. |
| `title` | `string` | The title of this snapshot. |
| `progressValue` | `string` | The progress value (64-bit integer set by developer) associated with this snapshot. |
| `coverImage` | `object` | An image of a snapshot. |
| `driveId` | `string` | The ID of the file underlying this snapshot in the Drive API. Only present if the snapshot is a view on a Drive file and the file is owned by the caller. |
| `type` | `string` | The type of this snapshot. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `snapshotId` | Retrieves the metadata for a given snapshot ID. |
| `list` | `SELECT` | `playerId` | Retrieves a list of snapshots created by your application for the player corresponding to the player ID. |
