---
title: "Single Post with YAML front matter"
date: 2017-07-20
tags: ["single", "yaml", "cross-link"]
categories: ["cat1", "cat2"]
draft: false
menu:
  foo:
    parent: "main"
    weight: 10
    identifier: "single-yaml"
---

<div class="ox-hugo-toc toc has-section-numbers">

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [First heading in this post](#first-heading)
- <span class="section-num">2</span> [Second heading in this post](#second-heading-in-this-post)

</div>
<!--endtoc-->

This is a single post. You do not need to set the `EXPORT_FILE_NAME` property in here. But then you also lose the tag and property inheritance, TODO state, etc. Org awesomeness.

This file will export the front-matter in YAML (because `#+hugo_front_matter_format: yaml`). See [{{< relref "post-toml" >}}]({{< relref "post-toml" >}}) that exports that in TOML.

Here's the same link with description: [Post exported with TOML front-matter]({{< relref "post-toml" >}}).

Here's an example with relative link to an Org file: [{{< relref "post4" >}}]({{< relref "post4" >}}).

---

All of the above linked Org files **have to** export posts using _per-file_ flow, and they **cannot be** page bundles or have slugs --- See `ox-hugo` Issue #[131](https://github.com/kaushalmodi/ox-hugo/issues/131) for requirements for this basic cross-linking to work as expected.

---


## <span class="section-num">1</span> First heading in this post {#first-heading}

This is a under first heading.


## <span class="section-num">2</span> Second heading in this post {#second-heading-in-this-post}

This is a under second heading.


This text is auto inserted at the end of the exported Markdown.
