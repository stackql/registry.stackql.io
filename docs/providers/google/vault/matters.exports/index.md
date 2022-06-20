---
title: matters.exports
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
<tr><td><b>Name</b></td><td><code>matters.exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vault.matters.exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `exports` | `array` | The list of exports. |
| `nextPageToken` | `string` | Page token to retrieve the next page of results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `exportId, matterId` | Gets an export. |
| `list` | `SELECT` | `matterId` | Lists details about the exports in the specified matter. |
| `create` | `INSERT` | `matterId` | Creates an export. |
| `delete` | `DELETE` | `exportId, matterId` | Deletes an export. |
