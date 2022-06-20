---
title: instanceGroupManagers
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
<tr><td><b>Name</b></td><td><code>instanceGroupManagers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instanceGroupManagers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this resource type. The server generates this identifier. |
| `name` | `string` | The name of the managed instance group. The name must be 1-63 characters long, and comply with RFC1035. |
| `description` | `string` | An optional description of this resource. |
| `currentActions` | `object` |  |
| `status` | `object` |  |
| `zone` | `string` | [Output Only] The URL of a zone where the managed instance group is located (for zonal resources). |
| `versions` | `array` | Specifies the instance templates used by this managed instance group to create instances. Each version is defined by an instanceTemplate and a name. Every version can appear at most once per instance group. This field overrides the top-level instanceTemplate field. Read more about the relationships between these fields. Exactly one version must leave the targetSize field unset. That version will be applied to all remaining instances. For more information, read about canary updates. |
| `instanceTemplate` | `string` | The URL of the instance template that is specified for this managed instance group. The group uses this template to create all new instances in the managed instance group. The templates for existing instances in the group do not change unless you run recreateInstances, run applyUpdatesToInstances, or set the group's updatePolicy.type to PROACTIVE. |
| `selfLink` | `string` | [Output Only] The URL for this managed instance group. The server defines this URL. |
| `creationTimestamp` | `string` | [Output Only] The creation timestamp for this managed instance group in RFC3339 text format. |
| `updatePolicy` | `object` |  |
| `autoHealingPolicies` | `array` | The autohealing policy for this managed instance group. You can specify only one value. |
| `fingerprint` | `string` | Fingerprint of this resource. This field may be used in optimistic locking. It will be ignored when inserting an InstanceGroupManager. An up-to-date fingerprint must be provided in order to update the InstanceGroupManager, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an InstanceGroupManager. |
| `namedPorts` | `array` | Named ports configured for the Instance Groups complementary to this Instance Group Manager. |
| `targetPools` | `array` | The URLs for all TargetPool resources to which instances in the instanceGroup field are added. The target pools automatically apply to all of the instances in the managed instance group. |
| `statefulPolicy` | `object` |  |
| `instanceGroup` | `string` | [Output Only] The URL of the Instance Group resource. |
| `distributionPolicy` | `object` |  |
| `baseInstanceName` | `string` | The base instance name to use for instances in this group. The value must be 1-58 characters long. Instances are named by appending a hyphen and a random four-character string to the base instance name. The base instance name must comply with RFC1035. |
| `region` | `string` | [Output Only] The URL of the region where the managed instance group resides (for regional resources). |
| `kind` | `string` | [Output Only] The resource type, which is always compute#instanceGroupManager for managed instance groups. |
| `targetSize` | `integer` | The target number of running instances for this managed instance group. You can reduce this number by using the instanceGroupManager deleteInstances or abandonInstances methods. Resizing the group also changes this number. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instanceGroupManager, project, zone` | Returns all of the details about the specified managed instance group. Gets a list of available managed instance groups by making a list() request. |
| `list` | `SELECT` | `project, zone` | Retrieves a list of managed instance groups that are contained within the specified project and zone. |
| `insert` | `INSERT` | `project, zone` | Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with the listmanagedinstances method. A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit. |
| `delete` | `DELETE` | `instanceGroupManager, project, zone` | Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information. |
| `abandonInstances` | `EXEC` | `instanceGroupManager, project, zone` | Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces the targetSize of the managed instance group by the number of instances that you abandon. This operation is marked as DONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| `aggregatedList` | `EXEC` | `project` | Retrieves the list of managed instance groups and groups them by zone. |
| `applyUpdatesToInstances` | `EXEC` | `instanceGroupManager, project, zone` | Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions. |
| `createInstances` | `EXEC` | `instanceGroupManager, project, zone` | Creates instances with per-instance configs in this managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of the creating or actions with the listmanagedinstances method. |
| `deleteInstances` | `EXEC` | `instanceGroupManager, project, zone` | Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces the targetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| `deletePerInstanceConfigs` | `EXEC` | `instanceGroupManager, project, zone` | Deletes selected per-instance configs for the managed instance group. |
| `listErrors` | `EXEC` | `instanceGroupManager, project, zone` | Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported. |
| `listManagedInstances` | `EXEC` | `instanceGroupManager, project, zone` | Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. |
| `listPerInstanceConfigs` | `EXEC` | `instanceGroupManager, project, zone` | Lists all of the per-instance configs defined for the managed instance group. The orderBy query parameter is not supported. |
| `patch` | `EXEC` | `instanceGroupManager, project, zone` | Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listManagedInstances method. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, see Updating instances in a MIG. |
| `patchPerInstanceConfigs` | `EXEC` | `instanceGroupManager, project, zone` | Inserts or patches per-instance configs for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
| `recreateInstances` | `EXEC` | `instanceGroupManager, project, zone` | Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking its currentAction field; for more information, see Checking the status of managed instances. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| `resize` | `EXEC` | `instanceGroupManager, project, size, zone` | Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is marked DONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with the listmanagedinstances method. When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including: + The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance. This list is subject to change. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. |
| `setInstanceTemplate` | `EXEC` | `instanceGroupManager, project, zone` | Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, run applyUpdatesToInstances, or set the group's updatePolicy.type to PROACTIVE. |
| `setTargetPools` | `EXEC` | `instanceGroupManager, project, zone` | Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is marked DONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group. |
| `updatePerInstanceConfigs` | `EXEC` | `instanceGroupManager, project, zone` | Inserts or updates per-instance configs for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
