---
title: admin.projects.locations.reservations
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
<tr><td><b>Name</b></td><td><code>admin.projects.locations.reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.admin.projects.locations.reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results. |
| `reservations` | `array` | The list of reservation in the requested parent. The order of the reservations is unspecified. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `locationsId, projectsId, reservationsId` | Returns the topic configuration. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns the list of reservations for the given project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new reservation. |
| `delete` | `DELETE` | `locationsId, projectsId, reservationsId` | Deletes the specified topic. |
| `patch` | `EXEC` | `locationsId, projectsId, reservationsId` | Updates properties of the specified topic. |
