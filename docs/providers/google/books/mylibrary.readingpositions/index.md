---
title: mylibrary.readingpositions
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
<tr><td><b>Name</b></td><td><code>mylibrary.readingpositions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.mylibrary.readingpositions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updated` | `string` | Timestamp when this reading position was last updated (formatted UTC timestamp with millisecond resolution). |
| `volumeId` | `string` | Volume id associated with this reading position. |
| `epubCfiPosition` | `string` | Position in an EPUB as a CFI. |
| `gbImagePosition` | `string` | Position in a volume for image-based content. |
| `gbTextPosition` | `string` | Position in a volume for text-based content. |
| `kind` | `string` | Resource type for a reading position. |
| `pdfPosition` | `string` | Position in a PDF file. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `volumeId` | Retrieves my reading position information for a volume. |
| `setPosition` | `EXEC` | `position, timestamp, volumeId` | Sets my reading position information for a volume. |
