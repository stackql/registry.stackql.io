---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
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
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.language.documents</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `documents_analyzeEntities` | `EXEC` |  | Finds named entities (currently proper names and common nouns) in the text along with entity types, salience, mentions for each entity, and other properties. |
| `documents_analyzeEntitySentiment` | `EXEC` |  | Finds entities, similar to AnalyzeEntities in the text and analyzes sentiment associated with each entity and its mentions. |
| `documents_analyzeSentiment` | `EXEC` |  | Analyzes the sentiment of the provided text. |
| `documents_analyzeSyntax` | `EXEC` |  | Analyzes the syntax of the text and provides sentence boundaries and tokenization along with part of speech tags, dependency trees, and other properties. |
| `documents_annotateText` | `EXEC` |  | A convenience method that provides all the features that analyzeSentiment, analyzeEntities, and analyzeSyntax provide in one call. |
| `documents_classifyText` | `EXEC` |  | Classifies a document into categories. |
