---
title: edits
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
<tr><td><b>Name</b></td><td><code>edits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.edits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Output only. Identifier of the edit. Can be used in subsequent API calls. |
| `expiryTimeSeconds` | `string` | Output only. The time (as seconds since Epoch) at which the edit will expire and will be no longer valid for use. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `editId, packageName` | Gets an app edit. |
| `insert` | `INSERT` | `packageName` | Creates a new edit for an app. |
| `delete` | `DELETE` | `editId, packageName` | Deletes an app edit. |
| `commit` | `EXEC` | `editId, packageName` | Commits an app edit. |
| `validate` | `EXEC` | `editId, packageName` | Validates an app edit. |
