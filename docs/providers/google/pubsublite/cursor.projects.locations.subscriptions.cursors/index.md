---
title: cursor.projects.locations.subscriptions.cursors
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
<tr><td><b>Name</b></td><td><code>cursor.projects.locations.subscriptions.cursors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.cursor.projects.locations.subscriptions.cursors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `partitionCursors` | `array` | The partition cursors from this request. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationsId, projectsId, subscriptionsId` |
