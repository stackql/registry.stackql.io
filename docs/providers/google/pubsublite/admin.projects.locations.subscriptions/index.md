---
title: admin.projects.locations.subscriptions
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
<tr><td><b>Name</b></td><td><code>admin.projects.locations.subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.admin.projects.locations.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results. |
| `subscriptions` | `array` | The list of subscriptions in the requested parent. The order of the subscriptions is unspecified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, subscriptionsId` | Returns the topic configuration. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns the list of subscriptions for the given project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new subscription. |
| `delete` | `DELETE` | `locationsId, projectsId, subscriptionsId` | Deletes the specified topic. |
| `patch` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Updates properties of the specified topic. |
| `seek` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Performs an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog. Seek translates these targets to cursors for each partition and orchestrates subscribers to start consuming messages from these seek cursors. If an operation is returned, the seek has been registered and subscribers will eventually receive messages from the seek cursors (i.e. eventual consistency), as long as they are using a minimum supported client library version and not a system that tracks cursors independently of Pub/Sub Lite (e.g. Apache Beam, Dataflow, Spark). The seek operation will fail for unsupported clients. If clients would like to know when subscribers react to the seek (or not), they can poll the operation. The seek operation will succeed and complete once subscribers are ready to receive messages from the seek cursors for all partitions of the topic. This means that the seek operation will not complete until all subscribers come online. If the previous seek operation has not yet completed, it will be aborted and the new invocation of seek will supersede it. |
