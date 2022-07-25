# Day 1 _ Introduction to HTML

### Terminology

* `HTML` : HyperText Markup Language
* `Tag` : identifying portions of the document
* `<!DOCTYPE>` : indicating the document type which is often HTML5
* Head and body
* Element : kind of the same thing as a tag. an HTML element == an HTML tag
* Attribute : additional descriptions in a tag 
  * example _ `A tag` by itself does nothing. It needs `href` in order to go somewhere.

<br/>

#### `<ol>` `<li>`

* 하위에는 `<li>`태그를 사용한다. 이는 list item을 의미함

#### `<a>`

* `target=_blank`를 추가하면 링크 페이지가 새 탭으로 뜸

#### `index.html`

* `index.html`은 홈페이지를 의미한다. 메인 페이지! (convention X)
* A homepage is always called `index.html`

#### `<img>`

* `<image src="" alt="">`
  * alt는 screen reader나 search engine을 위한 것
  * the alt text is hidden. but when my link is broken, it appears.
* `title=""` 
  * this attribute let users see text when they hover on the image.
  * but it depends on web browsers.
* [MDN document about img tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)

* attribute에 width나 height가 있지만, 그걸 사용해서 줄이기보다는 그냥 리사이즈하는게 나음. 굳이 큰 파일을 업로드 할 이유X



#### Emphasize / `<strong>` & `<em>`





#### Reference

**HTML Elements Reference**

https://developer.mozilla.org/en-US/docs/Web/HTML/Element

**InternetingIsHard.com**

- Introduction https://internetingishard.com/html-and-css/introduction/
- Basic Web Pages https://internetingishard.com/html-and-css/basic-web-pages/
- Links and Images https://internetingishard.com/html-and-css/links-and-images/
- Semantic HTML https://internetingishard.com/html-and-css/semantic-html/

**Validating HTML**

http://validator.w3.org/

* limitations : can't check misspelling or bad paths 