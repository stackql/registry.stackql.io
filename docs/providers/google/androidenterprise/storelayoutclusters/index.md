---
title: storelayoutclusters
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
<tr><td><b>Name</b></td><td><code>storelayoutclusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.storelayoutclusters</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `clusterId, enterpriseId, pageId` | Retrieves details of a cluster. |
| `list` | `SELECT` | `enterpriseId, pageId` | Retrieves the details of all clusters on the specified page. |
| `insert` | `INSERT` | `enterpriseId, pageId` | Inserts a new cluster in a page. |
| `delete` | `DELETE` | `clusterId, enterpriseId, pageId` | Deletes a cluster. |
| `update` | `EXEC` | `clusterId, enterpriseId, pageId` | Updates a cluster. |
