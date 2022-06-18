---
title: drives
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
<tr><td><b>Name</b></td><td><code>drives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.drives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `drives` | `array` | The list of shared drives. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#driveList". |
| `nextPageToken` | `string` | The page token for the next page of shared drives. This will be absent if the end of the list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `driveId` | Gets a shared drive's metadata by ID. |
| `list` | `SELECT` |  | Lists the user's shared drives. |
| `create` | `INSERT` | `requestId` | Creates a new shared drive. |
| `delete` | `DELETE` | `driveId` | Permanently deletes a shared drive for which the user is an organizer. The shared drive cannot contain any untrashed items. |
| `hide` | `EXEC` | `driveId` | Hides a shared drive from the default view. |
| `unhide` | `EXEC` | `driveId` | Restores a shared drive to the default view. |
| `update` | `EXEC` | `driveId` | Updates the metadate for a shared drive. |
