---
title: storelayoutpages
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
<tr><td><b>Name</b></td><td><code>storelayoutpages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.storelayoutpages</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `enterpriseId, pageId` | Retrieves details of a store page. |
| `list` | `SELECT` | `enterpriseId` | Retrieves the details of all pages in the store. |
| `insert` | `INSERT` | `enterpriseId` | Inserts a new store page. |
| `delete` | `DELETE` | `enterpriseId, pageId` | Deletes a store page. |
| `update` | `EXEC` | `enterpriseId, pageId` | Updates the content of a store page. |
