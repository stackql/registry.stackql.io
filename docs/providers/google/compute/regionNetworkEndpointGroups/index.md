---
title: regionNetworkEndpointGroups
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
<tr><td><b>Name</b></td><td><code>regionNetworkEndpointGroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.regionNetworkEndpointGroups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `networkEndpointType` | `string` | Type of network endpoints in this network endpoint group. Can be one of GCE_VM_IP_PORT, NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT, INTERNET_IP_PORT, SERVERLESS, PRIVATE_SERVICE_CONNECT. |
| `defaultPort` | `integer` | The default port used if the port number is not specified in the network endpoint. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `network` | `string` | The URL of the network to which all network endpoints in the NEG belong. Uses "default" project network if unspecified. |
| `subnetwork` | `string` | Optional URL of the subnetwork to which all network endpoints in the NEG belong. |
| `cloudFunction` | `object` | Configuration for a Cloud Function network endpoint group (NEG). The function must be provided explicitly or in the URL mask. Note: Cloud Function must be in the same project and located in the same region as the Serverless NEG. |
| `cloudRun` | `object` | Configuration for a Cloud Run network endpoint group (NEG). The service must be provided explicitly or in the URL mask. The tag is optional, may be provided explicitly or in the URL mask. Note: Cloud Run service must be in the same project and located in the same region as the Serverless NEG. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#networkEndpointGroup for network endpoint group. |
| `region` | `string` | [Output Only] The URL of the region where the network endpoint group is located. |
| `appEngine` | `object` | Configuration for an App Engine network endpoint group (NEG). The service is optional, may be provided explicitly or in the URL mask. The version is optional and can only be provided explicitly or in the URL mask when service is present. Note: App Engine service must be in the same project and located in the same region as the Serverless NEG. |
| `zone` | `string` | [Output Only] The URL of the zone where the network endpoint group is located. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `size` | `integer` | [Output only] Number of network endpoints in the network endpoint group. |
| `annotations` | `object` | Metadata defined as annotations on the network endpoint group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkEndpointGroup, project, region` | Returns the specified network endpoint group. Gets a list of available network endpoint groups by making a list() request. |
| `list` | `SELECT` | `project, region` | Retrieves the list of regional network endpoint groups available to the specified project in the given region. |
| `insert` | `INSERT` | `project, region` | Creates a network endpoint group in the specified project using the parameters that are included in the request. |
| `delete` | `DELETE` | `networkEndpointGroup, project, region` | Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service. |