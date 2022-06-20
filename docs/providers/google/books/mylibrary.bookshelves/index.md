---
title: mylibrary.bookshelves
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
<tr><td><b>Name</b></td><td><code>mylibrary.bookshelves</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.mylibrary.bookshelves</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Id of this bookshelf, only unique by user. |
| `description` | `string` | Description of this bookshelf. |
| `selfLink` | `string` | URL to this resource. |
| `access` | `string` | Whether this bookshelf is PUBLIC or PRIVATE. |
| `volumeCount` | `integer` | Number of volumes in this bookshelf. |
| `kind` | `string` | Resource type for bookshelf metadata. |
| `updated` | `string` | Last modified time of this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `title` | `string` | Title of this bookshelf. |
| `volumesLastUpdated` | `string` | Last time a volume was added or removed from this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `created` | `string` | Created time for this bookshelf (formatted UTC timestamp with millisecond resolution). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `shelf` | Retrieves metadata for a specific bookshelf belonging to the authenticated user. |
| `list` | `SELECT` |  | Retrieves a list of bookshelves belonging to the authenticated user. |
| `addVolume` | `EXEC` | `shelf, volumeId` | Adds a volume to a bookshelf. |
| `clearVolumes` | `EXEC` | `shelf` | Clears all volumes from a bookshelf. |
| `moveVolume` | `EXEC` | `shelf, volumeId, volumePosition` | Moves a volume within a bookshelf. |
| `removeVolume` | `EXEC` | `shelf, volumeId` | Removes a volume from a bookshelf. |
