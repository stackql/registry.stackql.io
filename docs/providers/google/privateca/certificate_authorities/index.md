---
title: certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authorities
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
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificate_authorities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`. |
| `type` | `string` | Required. Immutable. The Type of this CertificateAuthority. |
| `state` | `string` | Output only. The State for this CertificateAuthority. |
| `config` | `object` | A CertificateConfig describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1. |
| `tier` | `string` | Output only. The CaPool.Tier of the CaPool that includes this CertificateAuthority. |
| `deleteTime` | `string` | Output only. The time at which this CertificateAuthority was soft deleted, if it is in the DELETED state. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `subordinateConfig` | `object` | Describes a subordinate CA's issuers. This is either a resource name to a known issuing CertificateAuthority, or a PEM issuer certificate chain. |
| `lifetime` | `string` | Required. Immutable. The desired lifetime of the CA certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate. |
| `accessUrls` | `object` | URLs where a CertificateAuthority will publish content. |
| `createTime` | `string` | Output only. The time at which this CertificateAuthority was created. |
| `expireTime` | `string` | Output only. The time at which this CertificateAuthority will be permanently purged, if it is in the DELETED state. |
| `gcsBucket` | `string` | Immutable. The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs. This must be a bucket name, without any prefixes (such as `gs://`) or suffixes (such as `.googleapis.com`). For example, to use a bucket named `my-bucket`, you would simply specify `my-bucket`. If not specified, a managed bucket will be created. |
| `caCertificateDescriptions` | `array` | Output only. A structured description of this CertificateAuthority's CA certificate and its issuers. Ordered as self-to-root. |
| `updateTime` | `string` | Output only. The time at which this CertificateAuthority was last updated. |
| `keySpec` | `object` | A Cloud KMS key configuration that a CertificateAuthority will use. |
| `pemCaCertificates` | `array` | Output only. This CertificateAuthority's certificate chain, including the current CertificateAuthority's certificate. Ordered such that the root issuer is the final element (consistent with RFC 5246). For a self-signed CA, this will only list the current CertificateAuthority's certificate. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_caPools_certificateAuthorities_get` | `SELECT` | `name` | Returns a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_list` | `SELECT` | `parent` | Lists CertificateAuthorities. |
| `projects_locations_caPools_certificateAuthorities_create` | `INSERT` | `parent` | Create a new CertificateAuthority in a given Project and Location. |
| `projects_locations_caPools_certificateAuthorities_delete` | `DELETE` | `name` | Delete a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_activate` | `EXEC` | `name` | Activate a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. After the parent Certificate Authority signs a certificate signing request from FetchCertificateAuthorityCsr, this method can complete the activation process. |
| `projects_locations_caPools_certificateAuthorities_disable` | `EXEC` | `name` | Disable a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_enable` | `EXEC` | `name` | Enable a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_patch` | `EXEC` | `name` | Update a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_undelete` | `EXEC` | `name` | Undelete a CertificateAuthority that has been deleted. |
