---
title: projects.instances
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
<tr><td><b>Name</b></td><td><code>projects.instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.projects.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | The list of unreachable instances. It includes the names of instances whose metadata could not be retrieved within instance_deadline. |
| `instances` | `array` | The list of requested instances. |
| `nextPageToken` | `string` | `next_page_token` can be sent in a subsequent ListInstances call to fetch more of the matching instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, projectsId` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id. |
| `list` | `SELECT` | `projectsId` | Lists all instances in the given project. |
| `create` | `INSERT` | `projectsId` | Creates an instance and begins preparing it to begin serving. The returned long-running operation can be used to track the progress of preparing the new instance. The instance name is assigned by the caller. If the named instance already exists, `CreateInstance` returns `ALREADY_EXISTS`. Immediately upon completion of this request: * The instance is readable via the API, with all requested attributes but no allocated resources. Its state is `CREATING`. Until completion of the returned operation: * Cancelling the operation renders the instance immediately unreadable via the API. * The instance can be deleted. * All other attempts to modify the instance are rejected. Upon completion of the returned operation: * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels). * Databases can be created in the instance. * The instance's allocated resource levels are readable via the API. * The instance's state becomes `READY`. The returned long-running operation will have a name of the format `/operations/` and can be used to track creation of the instance. The metadata field type is CreateInstanceMetadata. The response field type is Instance, if successful. |
| `delete` | `DELETE` | `instancesId, projectsId` | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. |
| `getIamPolicy` | `EXEC` | `instancesId, projectsId` | Gets the access control policy for a database or backup resource. Returns an empty policy if a database or backup exists but does not have a policy set. Authorization requires `spanner.databases.getIamPolicy` permission on resource. For backups, authorization requires `spanner.backups.getIamPolicy` permission on resource. |
| `patch` | `EXEC` | `instancesId, projectsId` | Updates a pending or completed Backup. |
| `setIamPolicy` | `EXEC` | `instancesId, projectsId` | Sets the access control policy on a database or backup resource. Replaces any existing policy. Authorization requires `spanner.databases.setIamPolicy` permission on resource. For backups, authorization requires `spanner.backups.setIamPolicy` permission on resource. |
| `testIamPermissions` | `EXEC` | `instancesId, projectsId` | Returns permissions that the caller has on the specified database or backup resource. Attempting this RPC on a non-existent Cloud Spanner database will result in a NOT_FOUND error if the user has `spanner.databases.list` permission on the containing Cloud Spanner instance. Otherwise returns an empty set of permissions. Calling this method on a backup that does not exist will result in a NOT_FOUND error if the user has `spanner.backups.list` permission on the containing instance. |
