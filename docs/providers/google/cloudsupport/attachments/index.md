---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - attachments
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
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsupport.attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the attachment. |
| `creator` | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
| `filename` | `string` | The filename of the attachment (e.g. `"graph.jpg"`). |
| `mimeType` | `string` | Output only. The MIME type of the attachment (e.g. text/plain). |
| `sizeBytes` | `string` | Output only. The size of the attachment in bytes. |
| `createTime` | `string` | Output only. The time at which the attachment was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `cases_attachments_list` | `SELECT` | `parent` | Retrieve all attachments associated with a support case. |
| `attachments_create` | `INSERT` | `parent` | Create a file attachment on a case or Cloud resource. |
