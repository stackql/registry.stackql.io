---
title: publicDelegatedPrefixes
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
<tr><td><b>Name</b></td><td><code>publicDelegatedPrefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.publicDelegatedPrefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new PublicDelegatedPrefix. An up-to-date fingerprint must be provided in order to update the PublicDelegatedPrefix, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a PublicDelegatedPrefix. |
| `parentPrefix` | `string` | The URL of parent prefix. Either PublicAdvertisedPrefix or PublicDelegatedPrefix. |
| `status` | `string` | [Output Only] The status of the public delegated prefix. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#publicDelegatedPrefix for public delegated prefixes. |
| `ipCidrRange` | `string` | The IPv4 address range, in CIDR format, represented by this public delegated prefix. |
| `isLiveMigration` | `boolean` | If true, the prefix will be live migrated. |
| `region` | `string` | [Output Only] URL of the region where the public delegated prefix resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `publicDelegatedSubPrefixs` | `array` | The list of sub public delegated prefixes that exist for this public delegated prefix. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, publicDelegatedPrefix, region` | Returns the specified PublicDelegatedPrefix resource in the given region. |
| `list` | `SELECT` | `project, region` | Lists the PublicDelegatedPrefixes for a project in the given region. |
| `insert` | `INSERT` | `project, region` | Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request. |
| `delete` | `DELETE` | `project, publicDelegatedPrefix, region` | Deletes the specified PublicDelegatedPrefix in the given region. |
| `aggregatedList` | `EXEC` | `project` | Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes. |
| `patch` | `EXEC` | `project, publicDelegatedPrefix, region` | Patches the specified PublicDelegatedPrefix resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
