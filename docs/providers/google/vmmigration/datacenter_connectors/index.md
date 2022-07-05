---
title: datacenter_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - datacenter_connectors
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datacenter_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.datacenter_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The connector's name. |
| `state` | `string` | Output only. State of the DatacenterConnector, as determined by the health checks. |
| `stateTime` | `string` | Output only. The time the state was last set. |
| `availableVersions` | `object` | Holds informatiom about the available versions for upgrade. |
| `applianceSoftwareVersion` | `string` | Output only. Appliance last installed update bundle version. This is the version of the automatically updatable components on the appliance. |
| `bucket` | `string` | Output only. The communication channel between the datacenter connector and GCP. |
| `updateTime` | `string` | Output only. The last time the connector was updated with an API call. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `serviceAccount` | `string` | The service account to use in the connector when communicating with the cloud. |
| `applianceInfrastructureVersion` | `string` | Output only. Appliance OVA version. This is the OVA which is manually installed by the user and contains the infrastructure for the automatically updatable components on the appliance. |
| `createTime` | `string` | Output only. The time the connector was created (as an API call, not when it was actually installed). |
| `version` | `string` | The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified. |
| `upgradeStatus` | `object` | UpgradeStatus contains information about upgradeAppliance operation. |
| `registrationId` | `string` | Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sources_datacenterConnectors_get` | `SELECT` | `name` | Gets details of a single DatacenterConnector. |
| `projects_locations_sources_datacenterConnectors_list` | `SELECT` | `parent` | Lists DatacenterConnectors in a given Source. |
| `projects_locations_sources_datacenterConnectors_create` | `INSERT` | `parent` | Creates a new DatacenterConnector in a given Source. |
| `projects_locations_sources_datacenterConnectors_delete` | `DELETE` | `name` | Deletes a single DatacenterConnector. |
| `projects_locations_sources_datacenterConnectors_upgradeAppliance` | `EXEC` | `datacenterConnector` | Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version. |
