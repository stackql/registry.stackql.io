---
title: app_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - app_profiles
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
<tr><td><b>Name</b></td><td><code>app_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.app_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`. |
| `description` | `string` | Long form description of the use case for this AppProfile. |
| `multiClusterRoutingUseAny` | `object` | Read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes consistency to improve availability. |
| `singleClusterRouting` | `object` | Unconditionally routes all read/write requests to a specific cluster. This option preserves read-your-writes consistency but does not improve availability. |
| `etag` | `string` | Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instances_appProfiles_get` | `SELECT` | `name` | Gets information about an app profile. |
| `projects_instances_appProfiles_list` | `SELECT` | `parent` | Lists information about app profiles in an instance. |
| `projects_instances_appProfiles_create` | `INSERT` | `parent` | Creates an app profile within an instance. |
| `projects_instances_appProfiles_delete` | `DELETE` | `name` | Deletes an app profile from an instance. |
| `projects_instances_appProfiles_patch` | `EXEC` | `name` | Updates an app profile within an instance. |