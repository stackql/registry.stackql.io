---
title: nat_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_addresses
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
<tr><td><b>Name</b></td><td><code>nat_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.nat_addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Resource ID of the NAT address. |
| `ipAddress` | `string` | Output only. The static IPV4 address. |
| `state` | `string` | Output only. State of the nat address. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_instances_natAddresses_get` | `SELECT` | `name` | Gets the details of a NAT address. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_natAddresses_list` | `SELECT` | `parent` | Lists the NAT addresses for an Apigee instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_natAddresses_create` | `INSERT` | `parent` | Creates a NAT address. The address is created in the RESERVED state and a static external IP address will be provisioned. At this time, the instance will not use this IP address for Internet egress traffic. The address can be activated for use once any required firewall IP whitelisting has been completed. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_natAddresses_delete` | `DELETE` | `name` | Deletes the NAT address. Connections that are actively using the address are drained before it is removed. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_natAddresses_activate` | `EXEC` | `name` | Activates the NAT address. The Apigee instance can now use this for Internet egress traffic. **Note:** Not supported for Apigee hybrid. |