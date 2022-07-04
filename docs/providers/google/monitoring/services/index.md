---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]  |
| `gkeWorkload` | `object` | A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, k8s_container or k8s_pod). |
| `appEngine` | `object` | App Engine service. Learn more at https://cloud.google.com/appengine. |
| `meshIstio` | `object` | Istio service scoped to an Istio mesh. Anthos clusters running ASM &lt; 1.6.8 will have their services ingested as this type. |
| `custom` | `object` | Custom view of service telemetry. Currently a place-holder pending final design. |
| `displayName` | `string` | Name used for UI elements listing this Service. |
| `telemetry` | `object` | Configuration for how to query telemetry on a Service. |
| `clusterIstio` | `object` | Istio service scoped to a single Kubernetes cluster. Learn more at https://istio.io. Clusters running OSS Istio will have their services ingested as this type. |
| `cloudEndpoints` | `object` | Cloud Endpoints service. Learn more at https://cloud.google.com/endpoints. |
| `userLabels` | `object` | Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. |
| `istioCanonicalService` | `object` | Canonical service scoped to an Istio mesh. Anthos clusters running ASM &gt;= 1.6.8 will have their services ingested as this type. |
| `gkeNamespace` | `object` | GKE Namespace. The field names correspond to the resource metadata labels on monitored resources that fall under a namespace (for example, k8s_container or k8s_pod). |
| `gkeService` | `object` | GKE Service. The "service" here represents a Kubernetes service object (https://kubernetes.io/docs/concepts/services-networking/service). The field names correspond to the resource labels on k8s_service monitored resources (https://cloud.google.com/monitoring/api/resources#tag_k8s_service). |
| `cloudRun` | `object` | Cloud Run service. Learn more at https://cloud.google.com/run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_get` | `SELECT` | `name` | Get the named Service. |
| `services_list` | `SELECT` | `parent` | List Services for this Metrics Scope. |
| `services_create` | `INSERT` | `parent` | Create a Service. |
| `services_delete` | `DELETE` | `name` | Soft delete this Service. |
| `services_patch` | `EXEC` | `name` | Update this Service. |
