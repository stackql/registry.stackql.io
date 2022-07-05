---
title: provisioning_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_quotas
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
<tr><td><b>Name</b></td><td><code>provisioning_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.provisioning_quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the provisioning quota. |
| `gcpService` | `string` | The gcp service of the provisioning quota. |
| `instanceQuota` | `object` | A resource budget. |
| `storageGib` | `string` | Storage size (GB). |
| `availableCount` | `integer` | The available count of the provisioning quota. |
| `assetType` | `string` | The asset type of this provisioning quota. |
| `location` | `string` | The specific location of the provisioining quota. |
| `serverCount` | `string` | Server count. |
| `networkBandwidth` | `string` | Network bandwidth, Gbps |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_provisioningQuotas_list` | `SELECT` | `parent` |
