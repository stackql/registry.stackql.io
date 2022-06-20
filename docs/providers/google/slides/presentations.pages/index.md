---
title: presentations.pages
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
<tr><td><b>Name</b></td><td><code>presentations.pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.slides.presentations.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `masterProperties` | `object` | The properties of Page that are only relevant for pages with page_type MASTER. |
| `pageProperties` | `object` | The properties of the Page. The page will inherit properties from the parent page. Depending on the page type the hierarchy is defined in either SlideProperties or LayoutProperties. |
| `layoutProperties` | `object` | The properties of Page are only relevant for pages with page_type LAYOUT. |
| `pageElements` | `array` | The page elements rendered on the page. |
| `notesProperties` | `object` | The properties of Page that are only relevant for pages with page_type NOTES. |
| `objectId` | `string` | The object ID for this page. Object IDs used by Page and PageElement share the same namespace. |
| `pageType` | `string` | The type of the page. |
| `revisionId` | `string` | The revision ID of the presentation containing this page. Can be used in update requests to assert that the presentation revision hasn't changed since the last read operation. Only populated if the user has edit access to the presentation. The format of the revision ID may change over time, so it should be treated opaquely. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the presentation has not changed. Conversely, a changed ID (for the same presentation and user) usually means the presentation has been updated; however, a changed ID can also be due to internal factors such as ID format changes. |
| `slideProperties` | `object` | The properties of Page that are only relevant for pages with page_type SLIDE. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `pageObjectId, presentationId` | Gets the latest version of the specified page in the presentation. |
| `getThumbnail` | `EXEC` | `pageObjectId, presentationId` | Generates a thumbnail of the latest version of the specified page in the presentation and returns a URL to the thumbnail image. This request counts as an [expensive read request](/slides/limits) for quota purposes. |
