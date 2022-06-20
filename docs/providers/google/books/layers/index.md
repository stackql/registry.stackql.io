---
title: layers
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
<tr><td><b>Name</b></td><td><code>layers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.layers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique id of this layer summary. |
| `updated` | `string` | Timestamp for the last time an item in this layer was updated. (RFC 3339 UTC date-time format). |
| `annotationCount` | `integer` | The number of annotations for this layer. |
| `annotationTypes` | `array` | The list of annotation types contained for this layer. |
| `contentVersion` | `string` | The content version this resource is for. |
| `layerId` | `string` | The layer id for this summary. |
| `annotationsLink` | `string` | The link to get the annotations for this layer. |
| `volumeAnnotationsVersion` | `string` | The current version of this layer's volume annotations. Note that this version applies only to the data in the books.layers.volumeAnnotations.* responses. The actual annotation data is versioned separately. |
| `volumeId` | `string` | The volume id this resource is for. |
| `dataCount` | `integer` | The number of data items for this layer. |
| `annotationsDataLink` | `string` | Link to get data for this annotation. |
| `selfLink` | `string` | URL to this resource. |
| `kind` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `summaryId, volumeId` | Gets the layer summary for a volume. |
| `list` | `SELECT` | `volumeId` | List the layer summaries for a volume. |
