---
title: projects.locations.keyRings.cryptoKeys.cryptoKeyVersions
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
<tr><td><b>Name</b></td><td><code>projects.locations.keyRings.cryptoKeys.cryptoKeyVersions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.projects.locations.keyRings.cryptoKeys.cryptoKeyVersions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalSize` | `integer` | The total number of CryptoKeyVersions that matched the query. |
| `cryptoKeyVersions` | `array` | The list of CryptoKeyVersions. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCryptoKeyVersionsRequest.page_token to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns metadata for a given ImportJob. |
| `list` | `SELECT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Lists CryptoKeyVersions. |
| `create` | `INSERT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Create a new CryptoKeyVersion in a CryptoKey. The server will assign the next sequential id. If unset, state will be set to ENABLED. |
| `asymmetricDecrypt` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Decrypts data that was encrypted with a public key retrieved from GetPublicKey corresponding to a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_DECRYPT. |
| `asymmetricSign` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Signs data using a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from GetPublicKey. |
| `destroy` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Schedule a CryptoKeyVersion for destruction. Upon calling this method, CryptoKeyVersion.state will be set to DESTROY_SCHEDULED, and destroy_time will be set to the time destroy_scheduled_duration in the future. At that time, the state will automatically change to DESTROYED, and the key material will be irrevocably destroyed. Before the destroy_time is reached, RestoreCryptoKeyVersion may be called to reverse the process. |
| `getPublicKey` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns the public key for the given CryptoKeyVersion. The CryptoKey.purpose must be ASYMMETRIC_SIGN or ASYMMETRIC_DECRYPT. |
| `import` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Import wrapped key material into a CryptoKeyVersion. All requests must specify a CryptoKey. If a CryptoKeyVersion is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the CryptoKey. |
| `macSign` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Signs data using a CryptoKeyVersion with CryptoKey.purpose MAC, producing a tag that can be verified by another source with the same key. |
| `macVerify` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Verifies MAC tag using a CryptoKeyVersion with CryptoKey.purpose MAC, and returns a response that indicates whether or not the verification was successful. |
| `patch` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Update a CryptoKeyVersion's metadata. state may be changed between ENABLED and DISABLED using this method. See DestroyCryptoKeyVersion and RestoreCryptoKeyVersion to move between other states. |
| `restore` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Restore a CryptoKeyVersion in the DESTROY_SCHEDULED state. Upon restoration of the CryptoKeyVersion, state will be set to DISABLED, and destroy_time will be cleared. |
