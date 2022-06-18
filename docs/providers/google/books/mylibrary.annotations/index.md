---
title: mylibrary.annotations
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
<tr><td><b>Name</b></td><td><code>mylibrary.annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.mylibrary.annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Id of this annotation, in the form of a GUID. |
| `kind` | `string` | Resource type. |
| `deleted` | `boolean` | Indicates that this annotation is deleted. |
| `afterSelectedText` | `string` | Anchor text after excerpt. For requests, if the user bookmarked a screen that has no flowing text on it, then this field should be empty. |
| `created` | `string` | Timestamp for the created time of this annotation. |
| `layerSummary` | `object` |  |
| `beforeSelectedText` | `string` | Anchor text before excerpt. For requests, if the user bookmarked a screen that has no flowing text on it, then this field should be empty. |
| `updated` | `string` | Timestamp for the last time this annotation was modified. |
| `selfLink` | `string` | URL to this resource. |
| `volumeId` | `string` | The volume that this annotation belongs to. |
| `currentVersionRanges` | `object` | Selection ranges for the most recent content version. |
| `clientVersionRanges` | `object` | Selection ranges sent from the client. |
| `data` | `string` | User-created data for this annotation. |
| `pageIds` | `array` | Pages that this annotation spans. |
| `highlightStyle` | `string` | The highlight style for this annotation. |
| `selectedText` | `string` | Excerpt from the volume. |
| `layerId` | `string` | The layer this annotation is for. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` |  | Retrieves a list of annotations, possibly filtered. |
| `insert` | `INSERT` |  | Inserts a new annotation. |
| `delete` | `DELETE` | `annotationId` | Deletes an annotation. |
| `summary` | `EXEC` | `layerIds, volumeId` | Gets the summary of specified layers. |
| `update` | `EXEC` | `annotationId` | Updates an existing annotation. |
