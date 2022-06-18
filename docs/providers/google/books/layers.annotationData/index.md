---
title: layers.annotationData
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
<tr><td><b>Name</b></td><td><code>layers.annotationData</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.layers.annotationData</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Unique id for this annotation data. |
| `kind` | `string` | Resource Type |
| `updated` | `string` | Timestamp for the last time this data was updated. (RFC 3339 UTC date-time format). |
| `annotationType` | `string` | The type of annotation this data is for. |
| `encodedData` | `string` | Base64 encoded data for this annotation data. |
| `selfLink` | `string` | URL for this resource. * |
| `data` | `object` |  |
| `layerId` | `string` | The Layer id for this data. * |
| `volumeId` | `string` | The volume id for this data. * |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `annotationDataId, contentVersion, layerId, volumeId` | Gets the annotation data. |
| `list` | `SELECT` | `contentVersion, layerId, volumeId` | Gets the annotation data for a volume and layer. |
