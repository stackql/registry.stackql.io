---
title: admin.projects.locations.topics
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
<tr><td><b>Name</b></td><td><code>admin.projects.locations.topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.admin.projects.locations.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results. |
| `topics` | `array` | The list of topic in the requested parent. The order of the topics is unspecified. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `locationsId, projectsId, topicsId` | Returns the topic configuration. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns the list of topics for the given project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new topic. |
| `delete` | `DELETE` | `locationsId, projectsId, topicsId` | Deletes the specified topic. |
| `getPartitions` | `EXEC` | `locationsId, projectsId, topicsId` | Returns the partition information for the requested topic. |
| `patch` | `EXEC` | `locationsId, projectsId, topicsId` | Updates properties of the specified topic. |
