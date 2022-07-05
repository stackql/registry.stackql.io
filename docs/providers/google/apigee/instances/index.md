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
<tr><td><b>Id</b></td><td><code>google.apigee.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Resource ID of the instance. Values must match the regular expression `^a-z{0,30}[a-z\d]$`. |
| `description` | `string` | Optional. Description of the instance. |
| `port` | `string` | Output only. Port number of the exposed Apigee endpoint. |
| `state` | `string` | Output only. State of the instance. Values other than `ACTIVE` means the resource is not ready to use. |
| `lastModifiedAt` | `string` | Output only. Time the instance was last modified in milliseconds since epoch. |
| `runtimeVersion` | `string` | Output only. Version of the runtime system running in the instance. The runtime system is the set of components that serve the API Proxy traffic in your Environments. |
| `ipRange` | `string` | Optional. IP range represents the customer-provided CIDR block of length 22 that will be used for the Apigee instance creation. This optional range, if provided, should be freely available as part of larger named range the customer has allocated to the Service Networking peering. If this is not provided, Apigee will automatically request for any available /22 CIDR block from Service Networking. The customer should use this CIDR block for configuring their firewall needs to allow traffic from Apigee. Input format: "a.b.c.d/22", Output format: a.b.c.d/22, e.f.g.h/28" |
| `diskEncryptionKeyName` | `string` | Customer Managed Encryption Key (CMEK) used for disk and volume encryption. Required for Apigee paid subscriptions only. Use the following format: `projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)` |
| `host` | `string` | Output only. Internal hostname or IP address of the Apigee endpoint used by clients to connect to the service. |
| `createdAt` | `string` | Output only. Time the instance was created in milliseconds since epoch. |
| `displayName` | `string` | Optional. Display name for the instance. |
| `serviceAttachment` | `string` | Output only. Resource name of the service attachment created for the instance in the format: `projects/*/regions/*/serviceAttachments/*` Apigee customers can privately forward traffic to this service attachment using the PSC endpoints. |
| `peeringCidrRange` | `string` | Optional. Size of the CIDR block range that will be reserved by the instance. PAID organizations support `SLASH_16` to `SLASH_20` and defaults to `SLASH_16`. Evaluation organizations support only `SLASH_23`. |
| `location` | `string` | Required. Compute Engine location where the instance resides. |
| `consumerAcceptList` | `array` | Optional. Customer accept list represents the list of projects (id/number) on customer side that can privately connect to the service attachment. It is an optional field which the customers can provide during the instance creation. By default, the customer project associated with the Apigee organization will be included to the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_instances_get` | `SELECT` | `name` | Gets the details for an Apigee runtime instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_list` | `SELECT` | `parent` | Lists all Apigee runtime instances for the organization. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_create` | `INSERT` | `parent` | Creates an Apigee runtime instance. The instance is accessible from the authorized network configured on the organization. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_delete` | `DELETE` | `name` | Deletes an Apigee runtime instance. The instance stops serving requests and the runtime data is deleted. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_patch` | `EXEC` | `name` | Updates an Apigee runtime instance. You can update the fields described in NodeConfig. No other fields will be updated. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_reportStatus` | `EXEC` | `instance` | Reports the latest status for a runtime instance. |
