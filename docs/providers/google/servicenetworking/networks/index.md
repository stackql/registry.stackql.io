---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
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
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `reservedRanges` | `array` | Output only. The reserved ranges associated with this private service access connection. |
| `producerExportCustomRoutes` | `boolean` | Export custom routes flag value for peering from producer to consumer. |
| `producerImportCustomRoutes` | `boolean` | Import custom routes flag value for peering from producer to consumer. |
| `vpcScReferenceArchitectureEnabled` | `boolean` | Output only. Indicates whether the VPC Service Controls reference architecture is configured for the producer VPC host network. |
| `producerImportSubnetRoutesWithPublicIp` | `boolean` | Import subnet routes with public ip flag value for peering from producer to consumer. |
| `consumerExportCustomRoutes` | `boolean` | Export custom routes flag value for peering from consumer to producer. |
| `producerExportSubnetRoutesWithPublicIp` | `boolean` | Export subnet routes with public ip flag value for peering from producer to consumer. |
| `producerNetwork` | `string` | Output only. The VPC host network that is used to host managed service instances. In the format, projects/{project}/global/networks/{network} where {project} is the project number e.g. '12345' and {network} is the network name. |
| `consumerImportCustomRoutes` | `boolean` | Import custom routes flag value for peering from consumer to producer. |
| `consumerImportSubnetRoutesWithPublicIp` | `boolean` | Import subnet routes with public ip flag value for peering from consumer to producer. |
| `usedIpRanges` | `array` | Output only. The IP ranges already in use by consumer or producer |
| `consumerExportSubnetRoutesWithPublicIp` | `boolean` | Export subnet routes with public ip flag value for peering from consumer to producer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_projects_global_networks_get` | `SELECT` | `name` | Service producers use this method to get the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP. |
| `services_projects_global_networks_updateConsumerConfig` | `EXEC` | `parent` | Service producers use this method to update the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP. |
