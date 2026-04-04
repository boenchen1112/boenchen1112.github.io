---
title: 'Butterfly document - Get Started'
date: 2020-05-28 22:00:00
updated: 2025-12-10 00:00:00
tags:
  - Tutorial
  - Hexo
  - Theme
  - butterfly
  - EN
categories:
  - Docs
keywords: 'hexo,butterfly,theme,doc,tutorial,documentation,install,get started'
description: Butterfly Installation Guide - Get started with Hexo Butterfly theme
cover: https://oss.012700.xyz/butterfly/2024/09/butterfly-docs-01-cover.png
abbrlink: 21cfbf15
sticky: 100
series: docs
---

{% note blue 'fas fa-bullhorn' flat %}
This post is for Butterfly 4.0 and above. Some options may not be available in older versions.
If you are a new user, it is recommended to use the [latest release](https://github.com/jerryc127/hexo-theme-butterfly/releases).
{% endnote %}

# Install

## Git Installation

{% tabs install %}

<!-- tab Stable version (Recommended) -->

```bash
git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

<!-- endtab -->

<!-- tab Dev version (Testing) -->

> Dev version may contain bugs. It is not recommended unless you know what you are doing.

```bash
git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

<!-- endtab -->

{% endtabs %}

If you want to upgrade the theme, run the following command in the `themes/butterfly` directory:

```bash
git pull
```

## NPM Installation

> Requires Hexo 5.0.0 and above

```bash
npm install hexo-theme-butterfly
```

{% note warning flat %}
When installing via npm, the theme files will be placed in `node_modules/hexo-theme-butterfly` rather than the `themes/` folder.
{% endnote %}

If you want to upgrade the theme:

```bash
npm update hexo-theme-butterfly
```

# Apply Theme

Modify the Hexo root directory's `_config.yml`, change the theme setting to `butterfly`:

```yaml
theme: butterfly
```

# Install Required Plugins

{% tabs plugins %}

<!-- tab Renderer -->

If you have not yet installed the `pug` and `stylus` renderers, install them:

```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

<!-- endtab -->

{% endtabs %}

# Upgrade Recommendations

{% note info flat %}
To avoid losing custom configuration during theme upgrades, it is recommended to use [Hexo's Data Files](https://hexo.io/docs/data-files.html) feature.
{% endnote %}

Create a file `_config.butterfly.yml` in the Hexo root directory and copy the entire contents of the theme's `_config.yml` into it.

> Please note that the content in `_config.butterfly.yml` will override the settings in `themes/butterfly/_config.yml`.
> When updating the theme, check if the theme's `_config.yml` has any new settings added, and copy them to `_config.butterfly.yml`.

**Do NOT delete `themes/butterfly/_config.yml`**, it is still required by the theme even when using the override file.

```
.
├── _config.butterfly.yml   # Theme override config (your custom settings)
├── _config.yml             # Hexo root config
├── themes/
│   └── butterfly/
│       └── _config.yml     # Theme default config (do not delete)
```

Once `_config.butterfly.yml` exists, it takes priority over the theme's own `_config.yml`.

{% note success flat %}
You are ready to start! Run `hexo server` to preview your blog locally.
{% endnote %}
