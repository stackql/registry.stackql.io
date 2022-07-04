---
title: findings
hide_title: false
hide_table_of_contents: false
keywords:
  - findings
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
<tr><td><b>Name</b></td><td><code>findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.websecurityscanner.findings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Finding. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{scanRunId}/findings/{findingId}'. The finding IDs are generated by the system. |
| `description` | `string` | Output only. The description of the vulnerability. |
| `trackingId` | `string` | Output only. The tracking ID uniquely identifies a vulnerability instance across multiple ScanRuns. |
| `outdatedLibrary` | `object` | Information reported for an outdated library. |
| `finalUrl` | `string` | Output only. The URL where the browser lands when the vulnerability is detected. |
| `xss` | `object` | Information reported for an XSS. |
| `reproductionUrl` | `string` | Output only. The URL containing human-readable payload that user can leverage to reproduce the vulnerability. |
| `violatingResource` | `object` | Information regarding any resource causing the vulnerability such as JavaScript sources, image, audio files, etc. |
| `body` | `string` | Output only. The body of the request that triggered the vulnerability. |
| `frameUrl` | `string` | Output only. If the vulnerability was originated from nested IFrame, the immediate parent IFrame is reported. |
| `vulnerableParameters` | `object` | Information about vulnerable request parameters. |
| `vulnerableHeaders` | `object` | Information about vulnerable or missing HTTP Headers. |
| `httpMethod` | `string` | Output only. The http method of the request that triggered the vulnerability, in uppercase. |
| `xxe` | `object` | Information reported for an XXE. |
| `fuzzedUrl` | `string` | Output only. The URL produced by the server-side fuzzer and used in the request that triggered the vulnerability. |
| `severity` | `string` | Output only. The severity level of the reported vulnerability. |
| `form` | `object` | ! Information about a vulnerability with an HTML. |
| `findingType` | `string` | Output only. The type of the Finding. Detailed and up-to-date information on findings can be found here: https://cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_scanConfigs_scanRuns_findings_get` | `SELECT` | `name` | Gets a Finding. |
| `projects_scanConfigs_scanRuns_findings_list` | `SELECT` | `parent` | List Findings under a given ScanRun. |