---
title: shelves
hide_title: false
hide_table_of_contents: false
keywords:
  - shelves
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
<tr><td><b>Name</b></td><td><code>shelves</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.libraryagent.shelves</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the shelf. Shelf names have the form `shelves/{shelf_id}`. The name is ignored when creating a shelf. |
| `theme` | `string` | The theme of the shelf |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `shelves_get` | `SELECT` | `name` | Gets a shelf. Returns NOT_FOUND if the shelf does not exist. |
| `shelves_list` | `SELECT` |  | Lists shelves. The order is unspecified but deterministic. Newly created shelves will not necessarily be added to the end of this list. |
