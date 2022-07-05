---
title: connection_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_profiles
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
<tr><td><b>Name</b></td><td><code>connection_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.connection_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource's name. |
| `displayName` | `string` | Required. Display name. |
| `labels` | `object` | Labels. |
| `gcsProfile` | `object` | Cloud Storage bucket profile. |
| `mysqlProfile` | `object` | MySQL database profile. |
| `oracleProfile` | `object` | Oracle database profile. |
| `updateTime` | `string` | Output only. The update time of the resource. |
| `forwardSshConnectivity` | `object` | Forward SSH Tunnel connectivity. |
| `privateConnectivity` | `object` | Private Connectivity |
| `staticServiceIpConnectivity` | `object` | Static IP address connectivity. |
| `createTime` | `string` | Output only. The create time of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_connectionProfiles_get` | `SELECT` | `name` | Use this method to get details about a connection profile. |
| `projects_locations_connectionProfiles_list` | `SELECT` | `parent` | Use this method to list connection profiles created in a project and location. |
| `projects_locations_connectionProfiles_create` | `INSERT` | `parent` | Use this method to create a connection profile in a project and location. |
| `projects_locations_connectionProfiles_delete` | `DELETE` | `name` | Use this method to delete a connection profile. |
| `projects_locations_connectionProfiles_discover` | `EXEC` | `parent` | Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request. |
| `projects_locations_connectionProfiles_patch` | `EXEC` | `name` | Use this method to update the parameters of a connection profile. |
