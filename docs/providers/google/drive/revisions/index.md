---
title: revisions
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
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `revisions` | `array` | The list of revisions. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#revisionList". |
| `nextPageToken` | `string` | The page token for the next page of revisions. This will be absent if the end of the revisions list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileId, revisionId` | Gets a revision's metadata or content by ID. |
| `list` | `SELECT` | `fileId` | Lists a file's revisions. |
| `delete` | `DELETE` | `fileId, revisionId` | Permanently deletes a file version. You can only delete revisions for files with binary content in Google Drive, like images or videos. Revisions for other files, like Google Docs or Sheets, and the last remaining file version can't be deleted. |
| `update` | `EXEC` | `fileId, revisionId` | Updates a revision with patch semantics. |