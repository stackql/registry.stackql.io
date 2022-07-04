---
title: hot_tablets
hide_title: false
hide_table_of_contents: false
keywords:
  - hot_tablets
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
<tr><td><b>Name</b></td><td><code>hot_tablets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.hot_tablets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique name of the hot tablet. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/hotTablets/[a-zA-Z0-9_-]*`. |
| `endKey` | `string` | Tablet End Key (inclusive). |
| `endTime` | `string` | Output only. The end time of the hot tablet. |
| `nodeCpuUsagePercent` | `number` | Output only. The average CPU usage spent by a node on this tablet over the start_time to end_time time range. The percentage is the amount of CPU used by the node to serve the tablet, from 0% (tablet was not interacted with) to 100% (the node spent all cycles serving the hot tablet). |
| `startKey` | `string` | Tablet Start Key (inclusive). |
| `startTime` | `string` | Output only. The start time of the hot tablet. |
| `tableName` | `string` | Name of the table that contains the tablet. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_instances_clusters_hotTablets_list` | `SELECT` | `parent` |
