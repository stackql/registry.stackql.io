---
title: certificate_revocation_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_revocation_lists
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
<tr><td><b>Name</b></td><td><code>certificate_revocation_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificate_revocation_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`. |
| `pemCrl` | `string` | Output only. The PEM-encoded X.509 CRL. |
| `updateTime` | `string` | Output only. The time at which this CertificateRevocationList was updated. |
| `createTime` | `string` | Output only. The time at which this CertificateRevocationList was created. |
| `state` | `string` | Output only. The State for this CertificateRevocationList. |
| `revisionId` | `string` | Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string. |
| `revokedCertificates` | `array` | Output only. The revoked serial numbers that appear in pem_crl. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `accessUrl` | `string` | Output only. The location where 'pem_crl' can be accessed. |
| `sequenceNumber` | `string` | Output only. The CRL sequence number that appears in pem_crl. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_caPools_certificateAuthorities_certificateRevocationLists_get` | `SELECT` | `name` | Returns a CertificateRevocationList. |
| `projects_locations_caPools_certificateAuthorities_certificateRevocationLists_list` | `SELECT` | `parent` | Lists CertificateRevocationLists. |
| `projects_locations_caPools_certificateAuthorities_certificateRevocationLists_patch` | `EXEC` | `name` | Update a CertificateRevocationList. |
