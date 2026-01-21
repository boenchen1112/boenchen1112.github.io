# Hexo Butterfly Theme Setup Notes

## Overview
Recreating the site structure from `luketsengtw.github.io` using Hexo + Butterfly theme.

## Source Analysis
- **Original site**: https://luketsengtw.github.io/
- **Generator**: Hexo 7.3.0
- **Theme**: Butterfly 5.4.3
- **Downloaded repo**: Contains only compiled HTML (not source markdown files)

## Setup Steps Completed

### 1. Create Hexo Project
```bash
npm install -g hexo-cli
hexo init my-blog
cd my-blog
```

### 2. Install Butterfly Theme
```bash
git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

### 3. Install Required Renderers
```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

### 4. Configure `_config.yml`
- Changed `theme: landscape` to `theme: butterfly`
- Updated site info (title, subtitle, description, author)
- Set language to `zh-TW`
- Set permalink format to `posts/:abbrlink/`

### 5. Create `_config.butterfly.yml`
Copied from `themes/butterfly/_config.yml` and customized:
- Navigation menu (首頁, 文章, 分類, 標籤, 關於)
- Social links (GitHub, Email)
- Avatar: `/img/avatar.jpg`
- Background images for index, archive, tags, categories pages

### 6. Copy Images
Copied all images from downloaded repo to `source/img/`:
- avatar.jpg
- favicon.ico
- main_background.jpg
- archive_background_smaller.jpg
- tags_background_smaller.jpg
- category_background_smaller.jpg
- Various cover images (cpp_cover.png, css_cover.png, etc.)

### 7. Create Required Pages
```
source/categories/index.md  (type: "categories")
source/tags/index.md        (type: "tags")
source/about/index.md       (type: "about")
```

### 8. Run Development Server
```bash
npx hexo server --port 4000
# Open http://localhost:4000/
```

## Useful Commands

```bash
# Create new post
npx hexo new "Post Title"

# Generate static files
npx hexo generate

# Clean cache
npx hexo clean

# Deploy (after configuring deploy settings)
npx hexo deploy
```

## What's NOT Included
- Original markdown post content (only HTML was available)
- To add posts, create `.md` files in `source/_posts/`

## File Structure
```
my-blog/
├── _config.yml              # Main Hexo config
├── _config.butterfly.yml    # Theme config
├── source/
│   ├── _posts/              # Blog posts (markdown)
│   ├── about/index.md
│   ├── categories/index.md
│   ├── tags/index.md
│   └── img/                 # Images
├── themes/
│   └── butterfly/           # Theme files
└── package.json
```

## Resources
- Butterfly docs: https://butterfly.js.org/
- Hexo docs: https://hexo.io/docs/
- Theme repo: https://github.com/jerryc127/hexo-theme-butterfly
