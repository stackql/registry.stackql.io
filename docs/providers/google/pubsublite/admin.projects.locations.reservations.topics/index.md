---
title: admin.projects.locations.reservations.topics
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
<tr><td><b>Name</b></td><td><code>admin.projects.locations.reservations.topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.admin.projects.locations.reservations.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `topics` | `array` | The names of topics attached to the reservation. The order of the topics is unspecified. |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationsId, projectsId, reservationsId` |
