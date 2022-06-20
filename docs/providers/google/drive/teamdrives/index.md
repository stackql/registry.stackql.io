---
title: teamdrives
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
<tr><td><b>Name</b></td><td><code>teamdrives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.teamdrives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `teamDrives` | `array` | The list of Team Drives. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#teamDriveList". |
| `nextPageToken` | `string` | The page token for the next page of Team Drives. This will be absent if the end of the Team Drives list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `teamDriveId` | Deprecated use drives.get instead. |
| `list` | `SELECT` |  | Deprecated use drives.list instead. |
| `create` | `INSERT` | `requestId` | Deprecated use drives.create instead. |
| `delete` | `DELETE` | `teamDriveId` | Deprecated use drives.delete instead. |
| `update` | `EXEC` | `teamDriveId` | Deprecated use drives.update instead |
