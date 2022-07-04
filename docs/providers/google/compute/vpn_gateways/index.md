---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.vpn_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#vpnGateway for VPN gateways. |
| `stackType` | `string` | The stack type for this VPN gateway to identify the IP protocols that are enabled. If not specified, IPV4_ONLY will be used. |
| `region` | `string` | [Output Only] URL of the region where the VPN gateway resides. |
| `vpnInterfaces` | `array` | The list of VPN interfaces associated with this VPN gateway. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `network` | `string` | URL of the network to which this VPN gateway is attached. Provided by the client when the VPN gateway is created. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `labelFingerprint` | `string` | A fingerprint for the labels being applied to this VpnGateway, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an VpnGateway. |
| `labels` | `object` | Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpnGateways_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of VPN gateways. |
| `vpnGateways_get` | `SELECT` | `project, region, vpnGateway` | Returns the specified VPN gateway. Gets a list of available VPN gateways by making a list() request. |
| `vpnGateways_list` | `SELECT` | `project, region` | Retrieves a list of VPN gateways available to the specified project and region. |
| `vpnGateways_insert` | `INSERT` | `project, region` | Creates a VPN gateway in the specified project and region using the data included in the request. |
| `vpnGateways_delete` | `DELETE` | `project, region, vpnGateway` | Deletes the specified VPN gateway. |
| `vpnGateways_setLabels` | `EXEC` | `project, region, resource` | Sets the labels on a VpnGateway. To learn more about labels, read the Labeling Resources documentation. |