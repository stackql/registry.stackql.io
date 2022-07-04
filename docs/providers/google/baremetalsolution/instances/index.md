---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier for the `Instance`, generated by the backend. |
| `name` | `string` | Output only. The resource name of this `Instance`. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. Format: `projects/{project}/locations/{location}/instances/{instance}` |
| `hyperthreadingEnabled` | `boolean` | True if you enable hyperthreading for the server, otherwise false. The default value is false. |
| `networks` | `array` | List of networks associated with this server. |
| `pod` | `string` | Immutable. Pod name. Pod is an independent part of infrastructure. Instance can be connected to the assets (networks, volumes) allocated in the same pod only. |
| `createTime` | `string` | Output only. Create a time stamp. |
| `networkTemplate` | `string` | Instance network template name. For eg, bondaa-bondaa, bondab-nic, etc. Generally, the template name follows the syntax of "bond" or "nic". |
| `interactiveSerialConsoleEnabled` | `boolean` | True if the interactive serial console feature is enabled for the instance, false otherwise. The default value is false. |
| `updateTime` | `string` | Output only. Update a time stamp. |
| `labels` | `object` | Labels as key value pairs. |
| `machineType` | `string` | The server type. [Available server types](https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations) |
| `osImage` | `string` | The OS image currently installed on the server. |
| `state` | `string` | The state of the server. |
| `luns` | `array` | List of LUNs associated with this server. |
| `logicalInterfaces` | `array` | List of logical interfaces for the instance. The number of logical interfaces will be the same as number of hardware bond/nic on the chosen network template. For the non-multivlan configurations (for eg, existing servers) that use existing default network template (bondaa-bondaa), both the Instance.networks field and the Instance.logical_interfaces fields will be filled to ensure backward compatibility. For the others, only Instance.logical_interfaces will be filled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `name` | Get details about a single server. |
| `projects_locations_instances_list` | `SELECT` | `parent` | List servers in a given project and location. |
| `projects_locations_instances_detachLun` | `EXEC` | `instance` | Detach LUN from Instance. |
| `projects_locations_instances_patch` | `EXEC` | `name` | Update details of a single server. |
| `projects_locations_instances_reset` | `EXEC` | `name` | Perform an ungraceful, hard reset on a server. Equivalent to shutting the power off and then turning it back on. |
| `projects_locations_instances_start` | `EXEC` | `name` | Starts a server that was shutdown. |
| `projects_locations_instances_stop` | `EXEC` | `name` | Stop a running server. |