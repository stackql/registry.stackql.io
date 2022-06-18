---
title: edits.listings
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
<tr><td><b>Name</b></td><td><code>edits.listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.edits.listings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | The kind of this response ("androidpublisher#listingsListResponse"). |
| `listings` | `array` | All localized listings. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `editId, language, packageName` | Gets a localized store listing. |
| `list` | `SELECT` | `editId, packageName` | Lists all localized store listings. |
| `delete` | `DELETE` | `editId, language, packageName` | Deletes a localized store listing. |
| `deleteall` | `EXEC` | `editId, packageName` | Deletes all store listings. |
| `patch` | `EXEC` | `editId, language, packageName` | Patches a localized store listing. |
| `update` | `EXEC` | `editId, language, packageName` | Creates or updates a localized store listing. |
