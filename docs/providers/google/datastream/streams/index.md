---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.streams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The stream's name. |
| `updateTime` | `string` | Output only. The last update time of the stream. |
| `backfillNone` | `object` | Backfill strategy to disable automatic backfill for the Stream's objects. |
| `displayName` | `string` | Required. Display name. |
| `customerManagedEncryptionKey` | `string` | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. |
| `labels` | `object` | Labels. |
| `state` | `string` | The state of the stream. |
| `createTime` | `string` | Output only. The creation time of the stream. |
| `errors` | `array` | Output only. Errors on the Stream. |
| `sourceConfig` | `object` | The configuration of the stream source. |
| `backfillAll` | `object` | Backfill strategy to automatically backfill the Stream's objects. Specific objects can be excluded. |
| `destinationConfig` | `object` | The configuration of the stream destination. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_streams_get` | `SELECT` | `name` | Use this method to get details about a stream. |
| `projects_locations_streams_list` | `SELECT` | `parent` | Use this method to list streams in a project and location. |
| `projects_locations_streams_create` | `INSERT` | `parent` | Use this method to create a stream. |
| `projects_locations_streams_delete` | `DELETE` | `name` | Use this method to delete a stream. |
| `projects_locations_streams_patch` | `EXEC` | `name` | Use this method to update the configuration of a stream. |
