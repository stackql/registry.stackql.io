---
title: changes
hide_title: false
hide_table_of_contents: false
keywords:
  - changes
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
<tr><td><b>Name</b></td><td><code>changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.changes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the resource; defined by the server (output only). |
| `deletions` | `array` | Which ResourceRecordSets to remove? Must match existing data exactly. |
| `isServing` | `boolean` | If the DNS queries for the zone will be served. |
| `kind` | `string` |  |
| `startTime` | `string` | The time that this operation was started by the server (output only). This is in RFC3339 text format. |
| `status` | `string` | Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet. |
| `additions` | `array` | Which ResourceRecordSets to add? |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `changes_get` | `SELECT` | `changeId, managedZone, project` | Fetches the representation of an existing Change. |
| `changes_list` | `SELECT` | `managedZone, project` | Enumerates Changes to a ResourceRecordSet collection. |
| `changes_create` | `INSERT` | `managedZone, project` | Atomically updates the ResourceRecordSet collection. |
