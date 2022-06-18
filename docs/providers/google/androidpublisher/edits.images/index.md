---
title: edits.images
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
<tr><td><b>Name</b></td><td><code>edits.images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.edits.images</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `editId, imageType, language, packageName` | Lists all images. The response may be empty. |
| `delete` | `DELETE` | `editId, imageId, imageType, language, packageName` | Deletes the image (specified by id) from the edit. |
| `deleteall` | `EXEC` | `editId, imageType, language, packageName` | Deletes all images for the specified language and image type. Returns an empty response if no images are found. |
| `upload` | `EXEC` | `editId, imageType, language, packageName` | Uploads an image of the specified language and image type, and adds to the edit. |
