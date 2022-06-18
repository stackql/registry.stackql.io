---
title: projects.versions
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
<tr><td><b>Name</b></td><td><code>projects.versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.script.projects.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `versions` | `array` | The list of versions. |
| `nextPageToken` | `string` | The token use to fetch the next page of records. if not exist in the response, that means no more versions to list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `scriptId, versionNumber` | Gets a version of a script project. |
| `list` | `SELECT` | `scriptId` | List the versions of a script project. |
| `create` | `INSERT` | `scriptId` | Creates a new immutable version using the current code, with a unique version number. |
