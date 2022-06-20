---
title: layers.volumeAnnotations
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
<tr><td><b>Name</b></td><td><code>layers.volumeAnnotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.layers.volumeAnnotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique id of this volume annotation. |
| `updated` | `string` | Timestamp for the last time this anntoation was updated. (RFC 3339 UTC date-time format). |
| `contentRanges` | `object` | The content ranges to identify the selected text. |
| `selectedText` | `string` | Excerpt from the volume. |
| `volumeId` | `string` | The Volume this annotation is for. |
| `layerId` | `string` | The Layer this annotation is for. |
| `annotationDataId` | `string` | The annotation data id for this volume annotation. |
| `annotationType` | `string` | The type of annotation this is. |
| `pageIds` | `array` | Pages the annotation spans. |
| `data` | `string` | Data for this annotation. |
| `kind` | `string` | Resource Type |
| `deleted` | `boolean` | Indicates that this annotation is deleted. |
| `annotationDataLink` | `string` | Link to get data for this annotation. |
| `selfLink` | `string` | URL to this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `annotationId, layerId, volumeId` | Gets the volume annotation. |
| `list` | `SELECT` | `contentVersion, layerId, volumeId` | Gets the volume annotations for a volume and layer. |