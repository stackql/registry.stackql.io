---
title: files
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `files` | `array` | The list of files. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
| `incompleteSearch` | `boolean` | Whether the search process was incomplete. If true, then some search results may be missing, since all documents were not searched. This may occur when searching multiple drives with the "allDrives" corpora, but all corpora could not be searched. When this happens, it is suggested that clients narrow their query by choosing a different corpus such as "user" or "drive". |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#fileList". |
| `nextPageToken` | `string` | The page token for the next page of files. This will be absent if the end of the files list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `fileId` | Gets a file's metadata or content by ID. |
| `list` | `SELECT` |  | Lists or searches files. |
| `create` | `INSERT` |  | Creates a new file. |
| `delete` | `DELETE` | `fileId` | Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive the user must be an organizer on the parent. If the target is a folder, all descendants owned by the user are also deleted. |
| `copy` | `EXEC` | `fileId` | Creates a copy of a file and applies any requested updates with patch semantics. Folders cannot be copied. |
| `emptyTrash` | `EXEC` |  | Permanently deletes all of the user's trashed files. |
| `export` | `EXEC` | `fileId, mimeType` | Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB. |
| `generateIds` | `EXEC` |  | Generates a set of file IDs which can be provided in create or copy requests. |
| `update` | `EXEC` | `fileId` | Updates a file's metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics. |
| `watch` | `EXEC` | `fileId` | Subscribes to changes to a file |
