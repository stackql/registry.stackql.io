---
title: projects.locations.keyRings.cryptoKeys
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
<tr><td><b>Name</b></td><td><code>projects.locations.keyRings.cryptoKeys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.projects.locations.keyRings.cryptoKeys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalSize` | `integer` | The total number of CryptoKeys that matched the query. |
| `cryptoKeys` | `array` | The list of CryptoKeys. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCryptoKeysRequest.page_token to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns metadata for a given ImportJob. |
| `list` | `SELECT` | `keyRingsId, locationsId, projectsId` | Lists CryptoKeys. |
| `create` | `INSERT` | `keyRingsId, locationsId, projectsId` | Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required. |
| `decrypt` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Decrypts data that was protected by Encrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| `encrypt` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Encrypts data, so that it can only be recovered by a call to Decrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| `getIamPolicy` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `patch` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Update a CryptoKeyVersion's metadata. state may be changed between ENABLED and DISABLED using this method. See DestroyCryptoKeyVersion and RestoreCryptoKeyVersion to move between other states. |
| `setIamPolicy` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| `testIamPermissions` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
| `updatePrimaryVersion` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Update the version of a CryptoKey that will be used in Encrypt. Returns an error if called on a key whose purpose is not ENCRYPT_DECRYPT. |
