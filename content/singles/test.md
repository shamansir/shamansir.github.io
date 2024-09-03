---
title: "Another Post with TOML front matter"
description: "Some description for this post."
date: 2024-07-20
tags: ["single", "toml", "cross-link"]
categories: ["cat1", "cat2"]
draft: false
menu:
  foo:
    parent: "main"
    weight: 10
    identifier: "single-toml"
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [First heading in this post](#first-heading-in-this-post)
- <span class="section-num">2</span> [Second heading in this post](#second-heading-in-this-post)
- <span class="section-num">3</span> [Cross-linking](#cross-linking)
    - <span class="section-num">3.1</span> [Link to file in the same directory](#link-to-file-in-the-same-directory)
    - <span class="section-num">3.2</span> [Link + Description](#link-plus-description)
    - <span class="section-num">3.3</span> [Link to file in a different directory](#link-to-file-in-a-different-directory)
    - <span class="section-num">3.4</span> [Link to file that has a Hugo slug set](#link-to-file-that-has-a-hugo-slug-set)
    - <span class="section-num">3.5</span> [Link to the CUSTOM_ID of a different file](#link-to-the-custom-id-of-a-different-file)

</div>
<!--endtoc-->

This is a single post. You do not need to set the `EXPORT_FILE_NAME` property in here. But then you also lose the tag and property inheritance Org awesomeness.


## <span class="section-num">1</span> First heading in this post {#first-heading-in-this-post}

This is a under first heading.


## <span class="section-num">2</span> Second heading in this post {#second-heading-in-this-post}

This is a under second heading.


## <span class="section-num">3</span> Cross-linking {#cross-linking}

All of the below linked Org files **have to have** exported posts using the _per-file_ flow, and they **cannot be** page bundles or have set a different `#+export_file_name` --- See `ox-hugo` Issue #[131](https://github.com/kaushalmodi/ox-hugo/issues/131) for requirements for this basic cross-linking to work as expected.


### <span class="section-num">3.1</span> Link to file in the same directory {#link-to-file-in-the-same-directory}

This file will export the front-matter in TOML (default). See [{{< relref "post-yaml" >}}]({{< relref "post-yaml" >}}) that exports that in YAML.


### <span class="section-num">3.2</span> Link + Description {#link-plus-description}

Here's the same link with description: [Post exported with YAML front-matter]({{< relref "post-yaml" >}}).


### <span class="section-num">3.3</span> Link to file in a different directory {#link-to-file-in-a-different-directory}

[{{< relref "post3" >}}]({{< relref "post3" >}}).


### <span class="section-num">3.4</span> Link to file that has a Hugo slug set {#link-to-file-that-has-a-hugo-slug-set}

This one is magic! You can link to the Org file, no matter what slug is set in the exported file.. Hugo will do the job of translating from the Markdown file name to the actual link/slug.

[{{< relref "post-with-slug" >}}]({{< relref "post-with-slug" >}})


### <span class="section-num">3.5</span> Link to the CUSTOM_ID of a different file {#link-to-the-custom-id-of-a-different-file}

[{{< relref "post-yaml#first-heading" >}}]({{< relref "post-yaml#first-heading" >}})


This text is auto inserted at the end of the exported Markdown.
