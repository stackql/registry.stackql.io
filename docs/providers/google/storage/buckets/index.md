---
title: buckets
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
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.buckets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the bucket. For buckets, the id and name properties are the same. |
| `name` | `string` | The name of the bucket. |
| `autoclass` | `object` | The bucket's Autoclass configuration. |
| `etag` | `string` | HTTP 1.1 Entity tag for the bucket. |
| `satisfiesPZS` | `boolean` | Reserved for future use. |
| `labels` | `object` | User-provided labels, in key/value pairs. |
| `projectNumber` | `string` | The project number of the project the bucket belongs to. |
| `timeCreated` | `string` | The creation time of the bucket in RFC 3339 format. |
| `customPlacementConfig` | `object` | The bucket's custom placement configuration for Custom Dual Regions. |
| `location` | `string` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Defaults to US. See the developer's guide for the authoritative list. |
| `kind` | `string` | The kind of item this is. For buckets, this is always storage#bucket. |
| `lifecycle` | `object` | The bucket's lifecycle configuration. See lifecycle management for more information. |
| `updated` | `string` | The modification time of the bucket in RFC 3339 format. |
| `metageneration` | `string` | The metadata generation of this bucket. |
| `defaultObjectAcl` | `array` | Default access controls to apply to new objects when no ACL is provided. |
| `locationType` | `string` | The type of the bucket location. |
| `storageClass` | `string` | The bucket's default storage class, used whenever no storageClass is specified for a newly-created object. This defines how objects in the bucket are stored and determines the SLA and the cost of storage. Values include MULTI_REGIONAL, REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY. If this value is not specified when the bucket is created, it will default to STANDARD. For more information, see storage classes. |
| `website` | `object` | The bucket's website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the Static Website Examples for more information. |
| `retentionPolicy` | `object` | The bucket's retention policy. The retention policy enforces a minimum retention time for all objects contained in the bucket, based on their creation time. Any attempt to overwrite or delete objects younger than the retention period will result in a PERMISSION_DENIED error. An unlocked retention policy can be modified or removed from the bucket via a storage.buckets.update operation. A locked retention policy cannot be removed or shortened in duration for the lifetime of the bucket. Attempting to remove or decrease period of a locked retention policy will result in a PERMISSION_DENIED error. |
| `rpo` | `string` | The Recovery Point Objective (RPO) of this bucket. Set to ASYNC_TURBO to turn on Turbo Replication on a bucket. |
| `versioning` | `object` | The bucket's versioning configuration. |
| `acl` | `array` | Access controls on the bucket. |
| `encryption` | `object` | Encryption configuration for a bucket. |
| `owner` | `object` | The owner of the bucket. This is always the project team's owner group. |
| `cors` | `array` | The bucket's Cross-Origin Resource Sharing (CORS) configuration. |
| `defaultEventBasedHold` | `boolean` | The default value for event-based hold on newly created objects in this bucket. Event-based hold is a way to retain objects indefinitely until an event occurs, signified by the hold's release. After being released, such objects will be subject to bucket-level retention (if any). One sample use case of this flag is for banks to hold loan documents for at least 3 years after loan is paid in full. Here, bucket-level retention is 3 years and the event is loan being paid in full. In this example, these objects will be held intact for any number of years until the event has occurred (event-based hold on the object is released) and then 3 more years after that. That means retention duration of the objects begins from the moment event-based hold transitioned from true to false. Objects under event-based hold cannot be deleted, overwritten or archived until the hold is removed. |
| `logging` | `object` | The bucket's logging configuration, which defines the destination bucket and optional name prefix for the current bucket's logs. |
| `selfLink` | `string` | The URI of this bucket. |
| `billing` | `object` | The bucket's billing configuration. |
| `iamConfiguration` | `object` | The bucket's IAM configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bucket` | Returns metadata for the specified bucket. |
| `list` | `SELECT` | `project` | Retrieves a list of buckets for a given project. |
| `insert` | `INSERT` | `project, data__name` | Creates a new bucket. |
| `delete` | `DELETE` | `bucket` | Permanently deletes an empty bucket. |
| `getIamPolicy` | `EXEC` | `bucket` | Returns an IAM policy for the specified bucket. |
| `lockRetentionPolicy` | `EXEC` | `bucket, ifMetagenerationMatch` | Locks retention policy on a bucket. |
| `patch` | `EXEC` | `bucket` | Patches a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. |
| `setIamPolicy` | `EXEC` | `bucket, data__bindings` | Updates an IAM policy for the specified bucket. |
| `testIamPermissions` | `EXEC` | `bucket, permissions` | Tests a set of permissions on the given bucket to see which, if any, are held by the caller. |
| `update` | `EXEC` | `bucket, data__acl` | Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. |