---
title: projects.aggregated.usableSubnetworks
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
<tr><td><b>Name</b></td><td><code>projects.aggregated.usableSubnetworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.projects.aggregated.usableSubnetworks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `secondaryIpRanges` | `array` | Secondary IP ranges. |
| `statusMessage` | `string` | A human readable status message representing the reasons for cases where the caller cannot use the secondary ranges under the subnet. For example if the secondary_ip_ranges is empty due to a permission issue, an insufficient permission message will be given by status_message. |
| `subnetwork` | `string` | Subnetwork Name. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet |
| `ipCidrRange` | `string` | The range of internal addresses that are owned by this subnetwork. |
| `network` | `string` | Network Name. Example: projects/my-project/global/networks/my-network |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `projectsId` |
