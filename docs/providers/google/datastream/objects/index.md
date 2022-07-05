---
title: objects
hide_title: false
hide_table_of_contents: false
keywords:
  - objects
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
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.objects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The object resource's name. |
| `displayName` | `string` | Required. Display name. |
| `errors` | `array` | Output only. Active errors on the object. |
| `sourceObject` | `object` | Represents an identifier of an object in the data source. |
| `updateTime` | `string` | Output only. The last update time of the object. |
| `backfillJob` | `object` | Represents a backfill job on a specific stream object. |
| `createTime` | `string` | Output only. The creation time of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_streams_objects_get` | `SELECT` | `name` | Use this method to get details about a stream object. |
| `projects_locations_streams_objects_list` | `SELECT` | `parent` | Use this method to list the objects of a specific stream. |
| `projects_locations_streams_objects_lookup` | `EXEC` | `parent` | Use this method to look up a stream object by its source object identifier. |
| `projects_locations_streams_objects_startBackfillJob` | `EXEC` | `object` | Use this method to start a backfill job for the specified stream object. |
| `projects_locations_streams_objects_stopBackfillJob` | `EXEC` | `object` | Use this method to stop a backfill job for the specified stream object. |
