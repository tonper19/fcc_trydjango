# Markdown cheatsheet

## This is an h2 tag

###### This is an h6 tag

## EMPHASIS

_This text will be italic_

**This text will be bold**

_You **can** combine them_

## LISTS

- Item 1
- Item 2
  - Item 2a
  - Item 2b

1. Item 1
2. Item 2
3. Item 3
   - Item 3a
   - Item 3b

## LINKS

http://github.com - automatic! [GitHub](http://github.com)

## BLOCKQUOTES

As Grace Hopper said:

> I’ve always been more interested
> in the future than in the past.

## FENCED CODE BLOCKS

- Markdown coverts text with four leading spaces into a code block; with GFM you can wrap your code with ``` to create a code block without the leading spaces. Add an optional language identifier and your code will get syntax highlighting.

```python
def product_detail_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

```

```javascript function test() {
console.log("look ma’, no spaces"); }
```

## TASK LISTS

- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)

## TABLES

| First Header     | Second Header    |
| ---------------- | ---------------- |
| Content cell 1   | Content cell 2   |
| Content column 1 | Content column 2 |
